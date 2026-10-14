import { createClient, type SupabaseClient } from '@supabase/supabase-js'

let browserClient: SupabaseClient | undefined

export function useSupabase() {
  const config = useRuntimeConfig()

  if (import.meta.client && browserClient) return browserClient

  const client = createClient(
    config.public.supabaseUrl,
    config.public.supabasePublishableKey,
  )

  if (import.meta.client) browserClient = client

  return client
}
