import { NextResponse } from 'next/server';

export async function POST() {
  return NextResponse.json({
    ok: true,
    placeholder: true,
    nextStep: 'Look up the signed-in user, load their Stripe customer ID, and create a billing portal session.',
  });
}
