#!/bin/bash

# Cílová složka pro .py soubory
TARGET_DIR="../QtFiles"

# Vytvoří složku, pokud ještě neexistuje
mkdir -p "$TARGET_DIR"

# Smyčka přes všechny .ui soubory ve složce
for file in *.ui; do
    [ -e "$file" ] || continue  # pokud neexistuje, přeskočí
    echo "Překládám $file …"
    # Přeloží .ui do .py v cílové složce
    pyside6-uic "$file" -o "$TARGET_DIR/${file%.ui}.py"
done

echo "Hotovo! Všechny .ui soubory jsou přeloženy do $TARGET_DIR"
