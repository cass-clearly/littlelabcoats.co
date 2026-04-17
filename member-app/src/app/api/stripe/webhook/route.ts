import { NextResponse } from 'next/server';
import { getStripeServer } from '@/lib/stripe';

const supportedEvents = [
  'checkout.session.completed',
  'customer.subscription.updated',
  'customer.subscription.deleted',
  'invoice.payment_failed',
] as const;

export async function POST(request: Request) {
  const body = await request.text();
  const signature = request.headers.get('stripe-signature');
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  const stripe = getStripeServer();

  if (!webhookSecret || !signature || !stripe) {
    return NextResponse.json({
      ok: true,
      mode: 'mock',
      receivedBytes: body.length,
      supportedEvents,
      nextStep: 'Add STRIPE_WEBHOOK_SECRET and database writes to turn webhook verification into real entitlement sync.',
    });
  }

  try {
    const event = stripe.webhooks.constructEvent(body, signature, webhookSecret);

    return NextResponse.json({
      ok: true,
      mode: 'verified',
      eventId: event.id,
      eventType: event.type,
      supported: supportedEvents.includes(event.type as (typeof supportedEvents)[number]),
      nextStep: 'Persist the event in webhook_events and upsert entitlements based on the verified event type.',
    });
  } catch (error) {
    return NextResponse.json(
      {
        ok: false,
        message: error instanceof Error ? error.message : 'Stripe signature verification failed.',
      },
      { status: 400 },
    );
  }
}
