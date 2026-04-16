import { NextResponse } from 'next/server';

const supportedEvents = [
  'checkout.session.completed',
  'customer.subscription.updated',
  'customer.subscription.deleted',
  'invoice.payment_failed',
] as const;

export async function POST(request: Request) {
  const body = await request.text();

  return NextResponse.json({
    ok: true,
    placeholder: true,
    receivedBytes: body.length,
    supportedEvents,
    nextStep:
      'Verify Stripe signature, enforce idempotency via webhook_events, and upsert entitlements based on subscription lifecycle.',
  });
}
