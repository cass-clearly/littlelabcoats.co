import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const url = new URL(request.url);
  const code = url.searchParams.get('code');

  return NextResponse.json({
    ok: Boolean(code),
    message:
      'Supabase auth callback placeholder. Exchange the code for a session here once the Supabase project is configured.',
  });
}
