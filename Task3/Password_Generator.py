import secrets
import string
import sys

def create_secure_key(length, include_special=True):
    """
    Constructs a unique password using cryptographically secure randomization.
    """
    # Define our character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|"
    
    # Base pool
    pool = letters + digits
    if include_special:
        pool += symbols

    # Generate the password using 'secrets' for actual security
    password = "".join(secrets.choice(pool) for _ in range(length))
    return password

def run_vault():
    print("🔐 Welcome to VaultGen | Secure Password Architect")
    print("—" * 45)
    
    try:
        # 1. Get Length with a 'human' validation check
        raw_length = input("🤔 How long should this password be? (Recommended 12+): ").strip()
        
        if not raw_length.isdigit():
            print("❌ I need a whole number to work with. Let's try again.")
            return

        length = int(raw_length)
        
        if length < 6:
            print("⚠️ That's a bit short! Security experts recommend at least 8-12 characters.")
        
        # 2. Get Complexity Preference
        complexity = input("✨ Include special symbols? (yes/no): ").lower().strip()
        use_symbols = complexity in ['yes', 'y', 'sure', 'yeah']

        # 3. Processing
        print("\n⏳ Mixing characters and salting the vault...")
        final_password = create_secure_key(length, use_symbols)

        # 4. Result Display with a 'Strength' estimate
        print("—" * 45)
        print(f"✅ Your New Password: {final_password}")
        
        # Human touch: simple logic to rate the password
        if length >= 14 and use_symbols:
            print("💪 Strength: Iron-clad. That's a great password.")
        elif length >= 10:
            print("👍 Strength: Decent. Good for everyday accounts.")
        else:
            print("😟 Strength: Weak. Consider a longer length for better security.")
        print("—" * 45)

    except KeyboardInterrupt:
        print("\n\nExiting securely. Goodbye!")
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    run_vault()
