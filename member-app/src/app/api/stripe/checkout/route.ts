import { NextResponse } from 'next/server';
import { getAppUrl, hasRequiredServerEnv } from '@/lib/env';
import { getStripeServer } from '@/lib/stripe';

export async function POST() {
  if (!hasRequiredServerEnv()) {
    return NextResponse.json(
      {
        ok: false,
        message: 'Missing environment configuration for Stripe checkout.',
      },
      { status: 500 },
    );
  }

  const stripe = getStripeServer();

  if (!stripe) {
    return NextResponse.json({ ok: false, message: 'Stripe client is not configured.' }, { status: 500 });
  }

  return NextResponse.json({
    ok: true,
    placeholder: true,
    nextStep: 'Create a Checkout Session for the signed-in user and annual all-access price.',
    successUrl: `${getAppUrl()}/account?checkout=success`,
    cancelUrl: `${getAppUrl()}/billing?checkout=cancelled`,
  });
}
