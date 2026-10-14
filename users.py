import getpass

USERS = {
    "admin": "admin123",
    "student": "student123",
}


def login():
    print("=" * 40)
    print("              MiniOS Login")
    print("=" * 40)
    for _ in range(3):
        username = input("Username: ").strip()
        try:
            password = getpass.getpass("Password: ")
        except Exception:
            password = input("Password: ")
        if USERS.get(username) == password:
            print("\nLogin successful.")
            print(f"Welcome, {username}!\n")
            return username
        print("Error: Wrong username or password.\n")
    print("Too many failed attempts.")
    return None
