import { NextResponse } from 'next/server';
import { getAppUrl, getBillingPortalReturnUrl, hasStripeServerEnv } from '@/lib/env';
import { getStripeServer } from '@/lib/stripe';

type PortalRequest = {
  customerId?: string;
  returnPath?: string;
  mock?: boolean;
};

export async function POST(request: Request) {
  const body = (await request.json().catch(() => ({}))) as PortalRequest;
  const returnUrl = body.returnPath ? `${getAppUrl()}${body.returnPath}` : getBillingPortalReturnUrl();

  if (body.mock || !hasStripeServerEnv() || !body.customerId) {
    return NextResponse.json({
      ok: true,
      mode: 'mock',
      message: 'Billing portal is using the mock account return path until a real Stripe customer is available.',
      url: `${getAppUrl()}/account?portal=mock`,
    });
  }

  const stripe = getStripeServer();

  if (!stripe) {
    return NextResponse.json({ ok: false, message: 'Stripe client is not configured.' }, { status: 500 });
  }

  try {
    const session = await stripe.billingPortal.sessions.create({
      customer: body.customerId,
      return_url: returnUrl,
    });

    return NextResponse.json({
      ok: true,
      mode: 'live',
      message: 'Redirecting to Stripe billing portal.',
      url: session.url,
    });
  } catch (error) {
    return NextResponse.json(
      {
        ok: false,
        message: error instanceof Error ? error.message : 'Unable to create a billing portal session.',
      },
      { status: 500 },
    );
  }
}
