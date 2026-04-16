import Stripe from 'stripe';

let stripeClient: Stripe | null = null;

export function getStripeServer() {
  const secretKey = process.env.STRIPE_SECRET_KEY;

  if (!secretKey) {
    return null;
  }

  if (!stripeClient) {
    stripeClient = new Stripe(secretKey, {
      apiVersion: '2025-02-24.acacia',
      appInfo: {
        name: 'Little Lab Coats Member App MVP',
      },
    });
  }

  return stripeClient;
}
