def show_all(items):
    """Выводит все элементы списка."""
    if not items:
        print("Список пуст.")
        return
    print("\n--- Все элементы ---")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

def filter_by_text(items):
    """Фильтрует список по введённому тексту."""
    if not items:
        print("Список пуст.")
        return
    text = input("Введите текст для поиска: ").lower()
    filtered = [item for item in items if text in item.lower()]
    if not filtered:
        print("Ничего не найдено.")
        return
    print(f"\n--- Элементы, содержащие '{text}' ---")
    for i, item in enumerate(filtered, 1):
        print(f"{i}. {item}")

def get_user_list():
    """Запрашивает у пользователя список."""
    print("Введите элементы списка через запятую:")
    raw = input(">>> ")
    items = [s.strip() for s in raw.split(",") if s.strip()]
    return items

def main():
    print("=== Фильтр списка ===")
    items = get_user_list()
    while True:
        print("\n1. Показать все элементы")
        print("2. Фильтр по тексту")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_all(items)
        elif choice == "2":
            filter_by_text(items)
        elif choice == "0":
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()