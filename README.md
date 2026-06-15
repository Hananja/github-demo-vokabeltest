# Vokabeltrainer für Pull-Request-Übungen

Dies ist eine kleine Python-Terminalanwendung für den Unterricht. Die Grundversion ist bewusst einfach gehalten, damit Schülerinnen und Schüler sie verstehen, ausführen und anschließend über kleine Erweiterungen per Pull Request verbessern können.

## Lernziele

- Python-Code lesen und erweitern
- Arbeit mit Funktionen, Modulen und JSON-Dateien
- erste Unit-Tests verstehen und ergänzen
- Branches, Commits, Pull Requests und Code-Reviews üben

## Start

```bash
python3 main.py
```

## Tests

```bash
python3 -m unittest discover -s tests
```

## Projektstruktur

- `main.py`: Startpunkt und Menü
- `trainer.py`: Quiz- und Auswertungslogik
- `storage.py`: Laden und Speichern der Vokabeln
- `data/vocabulary.json`: Beispieldaten
- `tests/`: einfache Unit-Tests

## Vorgehensweise für den Unterricht

1. Repository klonen
2. Basisprogramm testen und analysieren
3. Kleine Erweiterungsaufgabe implementieren (s. u.)
4. Änderungen werden per Pull Request eingereicht.

Entwickeln Sie jeweils die Anpassungen in einem eigenen Branch.

## Pull-Request-Aufgaben

jeweils mit passendem Test:

1. Eingaben ohne Beachtung der Groß- und Kleinschreibung vergleichen.
2. Menüpunkt zum Hinzufügen neuer Vokabeln ergänzen.
3. Kategorien wie `IT`, `Englisch`, `Biologie` einführen.
4. Nur fünf zufällige Fragen pro Runde abfragen.
5. Punktestand nach jeder Frage anzeigen.
6. Fehlerliste am Ende der Runde ausgeben.
7. Statistikdatei mit Anzahl richtiger und falscher Antworten speichern.
8. CSV-Import für neue Vokabeln ergänzen.
9. Zusätzliche Tests für Randfälle schreiben.
10. Hilfe-Menü mit Bedienhinweisen ergänzen.
