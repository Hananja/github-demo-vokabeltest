import json
from pathlib import Path
from unittest import case

IT_VOCABULARY = [
    {"question": "database", "answer": "datenbank"},
    {"question": "file", "answer": "datei"},
    {"question": "username", "answer": "nutzername"},
    {"question": "network", "answer": "Netzwerk"},
    {"question": "server", "answer": "Server"},
]

DEFAULT_VOCABULARY = [
    {"question": "house", "answer": "Haus"},
    {"question": "tree", "answer": "Baum"},
    {"question": "school", "answer": "Schule"},
    {"question": "car", "answer": "Auto"},
    {"question": "street", "answer": "Straße"},
]

BIO_VOCABULARY = [
    {"question": "cell", "answer": "Zelle"},
    {"question": "gene", "answer": "Gen"},
    {"question": "nucleus", "answer": "Zellkern"},
    {"question": "fungus", "answer": "Pilz"},
    {"question": "adaption", "answer": "Anpassung"},
]


def load_vocabulary(file_path, index):
    print("index: ", index)
    match index:
        case 1:
            save_vocabulary(file_path, IT_VOCABULARY)
            return IT_VOCABULARY.copy()
        case 2:
            save_vocabulary(file_path, DEFAULT_VOCABULARY)
            return DEFAULT_VOCABULARY.copy()
        case 3:
            save_vocabulary(file_path, BIO_VOCABULARY)
            return BIO_VOCABULARY.copy()


def save_vocabulary(file_path, entries):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(entries, file, ensure_ascii=False, indent=2)
