import { NextResponse } from 'next/server';
import { createSupabaseServerClient } from '@/lib/supabase/server';
import { getAppUrl, hasSupabasePublicEnv } from '@/lib/env';

export async function GET(request: Request) {
  const requestUrl = new URL(request.url);
  const code = requestUrl.searchParams.get('code');
  const nextPath = requestUrl.searchParams.get('next') ?? '/account?auth=signed-in';

  if (!code) {
    return NextResponse.redirect(new URL('/auth?error=Missing%20auth%20code', getAppUrl()));
  }

  if (!hasSupabasePublicEnv()) {
    return NextResponse.redirect(new URL('/auth?status=callback-success', getAppUrl()));
  }

  try {
    const supabase = await createSupabaseServerClient();

    if (!supabase) {
      throw new Error('Supabase server client is not configured.');
    }

    const { error } = await supabase.auth.exchangeCodeForSession(code);

    if (error) {
      throw error;
    }

    return NextResponse.redirect(new URL(nextPath, getAppUrl()));
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Auth callback failed.';
    return NextResponse.redirect(new URL(`/auth?error=${encodeURIComponent(message)}`, getAppUrl()));
  }
}
