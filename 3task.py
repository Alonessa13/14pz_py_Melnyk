import json

DB_FILE = "clients.json"

def load_clients():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_clients(clients):
    with open(DB_FILE, "w") as file:
        json.dump(clients, file)

def add_client():
    name = input("Ім’я клієнта: ")
    email = input("Email клієнта: ")
    clients = load_clients()
    clients.append({"name": name, "email": email})
    save_clients(clients)
    print("Клієнт доданий.")

def find_client():
    name = input("Введи ім’я для пошуку: ")
    clients = load_clients()
    for c in clients:
        if c["name"].lower() == name.lower():
            print("Знайдено:", c)
            return
    print("Клієнта не знайдено.")

def delete_client():
    name = input("Введи ім’я для видалення: ")
    clients = load_clients()
    clients = [c for c in clients if c["name"].lower() != name.lower()]
    save_clients(clients)
    print("Клієнт видалений (якщо існував).")

# --- Основна програма ---
while True:
    print("\n1 — Додати клієнта\n2 — Знайти клієнта\n3 — Видалити клієнта\n0 — Вийти")
    choice = input("Вибери дію: ")
    if choice == "1":
        add_client()
    elif choice == "2":
        find_client()
    elif choice == "3":
        delete_client()
    elif choice == "0":
        break
