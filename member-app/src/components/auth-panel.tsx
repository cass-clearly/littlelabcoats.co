'use client';

import { type FormEvent, useMemo, useState } from 'react';
import { createSupabaseBrowserClient } from '@/lib/supabase/browser';

type AuthMode = 'magic-link' | 'sign-in' | 'sign-up';

type AuthPanelProps = {
  redirectUrl: string;
  supabaseReady: boolean;
};

export function AuthPanel({ redirectUrl, supabaseReady }: AuthPanelProps) {
  const supabase = useMemo(() => createSupabaseBrowserClient(), []);
  const [mode, setMode] = useState<AuthMode>('magic-link');
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setMessage(null);

    try {
      if (!supabaseReady || !supabase) {
        if (mode === 'magic-link') {
          setMessage(`Supabase is not configured yet, so this stays in demo mode. Once credentials are added, a real magic link will be sent to ${email || 'your email'}.`);
        } else if (mode === 'sign-up') {
          setMessage('Supabase credentials are still pending, but this screen is wired for email/password sign-up once the project is connected.');
        } else {
          setMessage('Supabase credentials are still pending, so password sign-in is intentionally blocked in local review.');
        }

        return;
      }

      if (mode === 'magic-link') {
        const { error } = await supabase.auth.signInWithOtp({
          email,
          options: {
            emailRedirectTo: redirectUrl,
          },
        });

        if (error) {
          throw error;
        }

        setMessage(`Magic link sent to ${email}.`);
        return;
      }

      if (mode === 'sign-in') {
        const { error } = await supabase.auth.signInWithPassword({
          email,
          password,
        });

        if (error) {
          throw error;
        }

        window.location.href = '/account?auth=signed-in';
        return;
      }

      const { error } = await supabase.auth.signUp({
        email,
        password,
        options: {
          emailRedirectTo: redirectUrl,
          data: {
            full_name: fullName,
          },
        },
      });

      if (error) {
        throw error;
      }

      setMessage('Account created. Check your email to confirm the address and complete sign-in.');
    } catch (error) {
      setMessage(error instanceof Error ? error.message : 'Something went wrong.');
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="stack-md">
      <div className="segmented-control" role="tablist" aria-label="Authentication mode">
        <button type="button" className={`segment${mode === 'magic-link' ? ' segment-active' : ''}`} onClick={() => setMode('magic-link')}>
          Magic link
        </button>
        <button type="button" className={`segment${mode === 'sign-in' ? ' segment-active' : ''}`} onClick={() => setMode('sign-in')}>
          Sign in
        </button>
        <button type="button" className={`segment${mode === 'sign-up' ? ' segment-active' : ''}`} onClick={() => setMode('sign-up')}>
          Create account
        </button>
      </div>

      <form className="auth-form" onSubmit={handleSubmit}>
        {mode === 'sign-up' ? (
          <label className="form-field">
            <span className="form-label">Family or parent name</span>
            <input className="form-input" type="text" value={fullName} onChange={(event) => setFullName(event.target.value)} placeholder="The Rivera Family" />
          </label>
        ) : null}

        <label className="form-field">
          <span className="form-label">Email address</span>
          <input className="form-input" type="email" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="family@example.com" required />
        </label>

        {mode !== 'magic-link' ? (
          <label className="form-field">
            <span className="form-label">Password</span>
            <input className="form-input" type="password" value={password} onChange={(event) => setPassword(event.target.value)} placeholder="Create a password" required />
          </label>
        ) : null}

        <button type="submit" className="button button-primary" disabled={busy}>
          {busy ? 'Working…' : mode === 'magic-link' ? 'Email me a magic link' : mode === 'sign-in' ? 'Sign in to my account' : 'Create my member account'}
        </button>
      </form>

      {message ? <p className="inline-note">{message}</p> : null}
    </div>
  );
}
