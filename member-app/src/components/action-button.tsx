'use client';

import { useState } from 'react';

type ActionButtonProps = {
  endpoint: string;
  label: string;
  pendingLabel: string;
  body?: Record<string, unknown>;
  variant?: 'primary' | 'secondary';
};

export function ActionButton({ endpoint, label, pendingLabel, body, variant = 'primary' }: ActionButtonProps) {
  const [pending, setPending] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  async function handleClick() {
    setPending(true);
    setMessage(null);

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body ?? {}),
      });

      const data = (await response.json()) as { ok?: boolean; message?: string; url?: string };

      if (!response.ok) {
        throw new Error(data.message ?? 'The action failed.');
      }

      if (data.url) {
        window.location.href = data.url;
        return;
      }

      setMessage(data.message ?? 'Action completed.');
    } catch (error) {
      setMessage(error instanceof Error ? error.message : 'Something went wrong.');
    } finally {
      setPending(false);
    }
  }

  return (
    <div className="stack-sm">
      <button type="button" className={`button ${variant === 'secondary' ? 'button-secondary' : 'button-primary'}`} onClick={handleClick} disabled={pending}>
        {pending ? pendingLabel : label}
      </button>
      {message ? <p className="inline-note">{message}</p> : null}
    </div>
  );
}
