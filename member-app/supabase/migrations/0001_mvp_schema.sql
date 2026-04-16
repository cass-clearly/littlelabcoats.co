-- Little Lab Coats member-app MVP schema scaffold
-- Grounded in docs/subscription-site-mvp-plan-2026-04-16.md

create extension if not exists pgcrypto;

create table if not exists public.users (
  id uuid primary key default gen_random_uuid(),
  auth_user_id uuid unique,
  email text unique not null,
  full_name text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.products (
  id uuid primary key default gen_random_uuid(),
  stripe_product_id text unique not null,
  slug text unique not null,
  name text not null,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.prices (
  id uuid primary key default gen_random_uuid(),
  product_id uuid not null references public.products(id) on delete cascade,
  stripe_price_id text unique not null,
  nickname text,
  interval text,
  unit_amount integer,
  currency text default 'usd',
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.content_items (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  grade text not null,
  domain text not null,
  unit_name text not null,
  preview_url text not null,
  member_asset_path text not null,
  launch_included boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.stripe_customers (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null unique references public.users(id) on delete cascade,
  stripe_customer_id text not null unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.entitlements (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.users(id) on delete cascade,
  product_id uuid not null references public.products(id) on delete cascade,
  source text not null default 'stripe',
  status text not null default 'active',
  starts_at timestamptz,
  ends_at timestamptz,
  stripe_subscription_id text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (user_id, product_id)
);

create table if not exists public.webhook_events (
  id uuid primary key default gen_random_uuid(),
  provider text not null default 'stripe',
  external_event_id text not null unique,
  event_type text not null,
  payload jsonb not null,
  processed_at timestamptz,
  created_at timestamptz not null default now()
);

comment on table public.entitlements is 'Stripe webhook is the source of truth for subscription-derived access.';
comment on table public.content_items is 'Hybrid MVP: static preview URLs plus protected member asset paths.';
