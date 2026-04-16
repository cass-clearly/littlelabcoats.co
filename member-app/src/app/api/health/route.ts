import { NextResponse } from 'next/server';
import { getMissingServerEnv } from '@/lib/env';

export async function GET() {
  const missingEnv = getMissingServerEnv();

  return NextResponse.json({
    ok: missingEnv.length === 0,
    missingEnv,
  });
}
