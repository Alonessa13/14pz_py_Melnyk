import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_contact():
    name = input("Введи ім’я контакту: ")
    phone = input("Введи номер телефону: ")
    contacts = load_contacts()
    contacts[name] = phone
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)
    print("Контакт збережено.")

def show_contacts():
    contacts = load_contacts()
    print("Список контактів:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# --- Основна програма ---
while True:
    print("\n1 — Додати контакт\n2 — Показати всі\n0 — Вийти")
    choice = input("Вибери дію: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "0":
        break
