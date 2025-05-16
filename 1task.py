import json

FILE_NAME = "game_stats.json"

def load_stats():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"wins": 0, "losses": 0}

def update_stats(win):
    stats = load_stats()
    if win:
        stats["wins"] += 1
    else:
        stats["losses"] += 1
    with open(FILE_NAME, "w") as file:
        json.dump(stats, file)
    print("Оновлена статистика:", stats)

# --- Основна програма ---
answer = input("Ти виграв гру? (так/ні): ").strip().lower()
update_stats(win=(answer == "так"))
