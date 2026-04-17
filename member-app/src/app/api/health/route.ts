import { NextResponse } from 'next/server';
import { getAppMode, getReadinessChecks } from '@/lib/env';

export async function GET() {
  const checks = getReadinessChecks();

  return NextResponse.json({
    ok: checks.every((check) => check.ready),
    mode: getAppMode(),
    checks,
    routes: ['/', '/auth', '/account', '/library', '/billing', '/checkout/success', '/checkout/cancel'],
  });
}
