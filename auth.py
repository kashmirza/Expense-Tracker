import hashlib
from file_handler import load_data, save_data
from validation import is_valid_password

USERS_FILE = "users.json"


def hash_password(password):
    """
    Convert password into SHA-256 hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    users = load_data(USERS_FILE)

    print("\n========== REGISTER ==========")

    username = input("Enter Username: ").strip().lower()

    if not username:
        print("❌ Username cannot be empty.")
        return

    if username in users:
        print("❌ Username already exists.")
        return

    password = input("Enter Password: ")

    valid, message = is_valid_password(password)

    if not valid:
        print(f"❌ {message}")
        return

    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("❌ Passwords do not match.")
        return

    users[username] = {
        "password": hash_password(password)
    }

    save_data(USERS_FILE, users)

    print("✅ Registration Successful!")


def login():
    users = load_data(USERS_FILE)

    print("\n========== LOGIN ==========")

    for attempt in range(3):

        username = input("Username: ").strip().lower()
        password = input("Password: ")

        if username not in users:
            print("❌ Username not found.")
        else:
            hashed = hash_password(password)

            if hashed == users[username]["password"]:
                print(f"\n✅ Welcome {username}!")
                return username

            else:
                print("❌ Incorrect Password.")

        remaining = 2 - attempt

        if remaining > 0:
            print(f"Attempts Remaining: {remaining}")

    print("\n❌ Too many failed attempts.")
    return None


def logout():
    print("\n✅ Logged Out Successfully.")