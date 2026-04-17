import { NextResponse } from 'next/server';
import { getAppUrl, hasStripeServerEnv } from '@/lib/env';
import { getStripeServer } from '@/lib/stripe';

type CheckoutRequest = {
  plan?: string;
  email?: string;
  successPath?: string;
  cancelPath?: string;
  mock?: boolean;
};

export async function POST(request: Request) {
  const body = (await request.json().catch(() => ({}))) as CheckoutRequest;
  const plan = body.plan ?? 'annual-all-access';
  const successPath = body.successPath ?? '/checkout/success';
  const cancelPath = body.cancelPath ?? '/checkout/cancel';

  if (body.mock || !hasStripeServerEnv()) {
    return NextResponse.json({
      ok: true,
      mode: 'mock',
      message: 'Stripe is not configured in this environment yet, so the checkout button is using a local success route.',
      url: `${getAppUrl()}${successPath}?mock=1&plan=${encodeURIComponent(plan)}`,
    });
  }

  const stripe = getStripeServer();

  if (!stripe) {
    return NextResponse.json({ ok: false, message: 'Stripe client is not configured.' }, { status: 500 });
  }

  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'subscription',
      line_items: [
        {
          price: process.env.STRIPE_PRICE_ID_ANNUAL,
          quantity: 1,
        },
      ],
      allow_promotion_codes: true,
      billing_address_collection: 'auto',
      customer_email: body.email,
      success_url: `${getAppUrl()}${successPath}?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${getAppUrl()}${cancelPath}`,
      metadata: {
        source: 'little-lab-coats-member-app',
        plan,
      },
    });

    if (!session.url) {
      throw new Error('Stripe checkout session did not return a URL.');
    }

    return NextResponse.json({
      ok: true,
      mode: 'live',
      message: 'Redirecting to Stripe Checkout.',
      url: session.url,
      sessionId: session.id,
    });
  } catch (error) {
    return NextResponse.json(
      {
        ok: false,
        message: error instanceof Error ? error.message : 'Unable to create Stripe Checkout session.',
      },
      { status: 500 },
    );
  }
}
