-- Donau-Ries Haustechnik — Supabase setup
-- Run this once in the Supabase SQL Editor (project: kcioqwkrklwpgtmwoanu).

-- Table for contact form submissions
create table if not exists public.kontakt_anfragen (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text,
  email text,
  message text,
  source_page text
);

-- Row Level Security: visitors may only INSERT, never read.
-- You read submissions in the Supabase dashboard (Table Editor).
alter table public.kontakt_anfragen enable row level security;

drop policy if exists "Public can submit contact form" on public.kontakt_anfragen;
create policy "Public can submit contact form"
  on public.kontakt_anfragen
  for insert
  to anon
  with check (true);
