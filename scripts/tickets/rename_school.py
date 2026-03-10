"""
Example Admin Script: Rename a School

Usage from GitHub Actions:
Script Path: scripts/tickets/example/rename_school.py
Arguments: --schoolId=123 --newName="New School Name"
"""

import os
import sys

def main():
    print("=========================================")
    print("🚀 Starting rename_school.py admin script")
    print("=========================================")

    # 1. Read Database Credentials from Environment
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

    if not supabase_url or not supabase_key:
        print("❌ Error: Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY environment variables.", file=sys.stderr)
        sys.exit(1)

    # 2. Parse basic arguments
    args = sys.argv[1:]
    school_id_arg = next((a for a in args if a.startswith("--schoolId=")), None)
    new_name_arg = next((a for a in args if a.startswith("--newName=")), None)

    if not school_id_arg or not new_name_arg:
        print("❌ Error: Missing required arguments. Please provide --schoolId=... and --newName=...", file=sys.stderr)
        sys.exit(1)

    school_id = school_id_arg.split("=", 1)[1]
    new_name = new_name_arg.split("=", 1)[1]

    print(f"ℹ️ Parsed arguments - School ID: {school_id}, New Name: {new_name}")

    # 3. Initialize Supabase Client (Service Role for Admin Access)
    print("⏳ Initializing Supabase client...")
    # from supabase import create_client, Client
    # supabase: Client = create_client(supabase_url, supabase_key) # Uncomment when implementing real DB logic

    # 4. Perform the operation
    try:
        print(f"⏳ Updating school ID {school_id} to name: \"{new_name}\"...")
        
        # Example:
        # response = supabase.table("schools").update({"name": new_name}).eq("id", school_id).execute()
        
        print(f"✅ Progress: Successfully updated Database for school ID: {school_id}")
    except Exception as e:
        print(f"❌ Error executing update: {str(e)}", file=sys.stderr)
        sys.exit(1)

    print("=========================================")
    print("🎉 Script rename_school.py completed successfully.")
    print("=========================================")

if __name__ == "__main__":
    main()
