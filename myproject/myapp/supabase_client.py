from supabase import create_client, Client


url = "https://aiwspgoyllinmfpruoii.supabase.co"  # Replace with your actual project URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFpd3NwZ295bGxpbm1mcHJ1b2lpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNTgzNDY4MCwiZXhwIjoyMDIxNDEwNjgwfQ.O_Wi1qkpU0U8-KnyFuF5i14zZcPFF7gUSoWmbRDUOw0"   # Replace with your actual secret key

supabase: Client = create_client(url, key)



