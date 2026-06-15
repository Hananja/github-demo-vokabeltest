from trainer import run_quiz, ask_yes_no
from storage import load_vocabulary, save_vocabulary

extra_vocabulary = []

def show_menu():
    print("\nVokabeltrainer")
    print("-" * 20)
    print("1) Quiz starten")
    print("2) Vokabeln anzeigen")
    print("3) Vokabeln hinzufügen")
    print("4) Beenden")


def show_vocabulary(entries):
    print("\nVorhandene Vokabeln:")
    for index, item in enumerate(entries, start=1):
        print(f"{index:>2}. {item['question']} -> {item['answer']}")


def main():
    entries = load_vocabulary("data/vocabulary.json")

    while True:
        show_menu()
        choice = input("Auswahl: ").strip()

        if choice == "1":
            run_quiz(entries)
        elif choice == "2":
            show_vocabulary(entries)
        elif choice == "3":
            entries = add_vocabulary(entries)
        elif choice == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

        if choice in {"1", "2"}:
            ask_yes_no("Weiter mit Enter bestätigen")


def add_vocabulary(entries):
    global extra_vocabulary
    extra_vocabulary += [{"question": input("Frage: "), "answer": input("Antwort: ")}]
    save_vocabulary("data/vocabulary.json", extra_vocabulary + entries)
    return extra_vocabulary + entries
    

if __name__ == "__main__":
    main()
