import json
import csv
import sys
import os

def json_to_csv(json_path):
    # Verificar que el archivo existe
    if not os.path.isfile(json_path):
        print(f"❌ No se encontró el archivo: {json_path}")
        return

    # Determinar nombre de salida
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    csv_path = f"{base_name}.csv"

    # Leer el JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Si es un único objeto, lo convertimos en lista
    if isinstance(data, dict):
        data = [data]

    # Crear el CSV usando tabulador como delimitador
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar='\\')

        for item in data:
            # Construir etiquetas
            etiquetas_parts = []
            if item.get("level"):
                etiquetas_parts.append(item["level"])
            if item.get("part_of_speech"):
                etiquetas_parts.append(item["part_of_speech"])
            if item.get("semantic_category"):
                etiquetas_parts.append(item["semantic_category"])
            etiquetas = " ".join(etiquetas_parts)

            writer.writerow([
                item.get("id", ""),              # 1 - ID
                item.get("term", ""),            # 2 - Term EN
                "",                              # 3 - Vacía
                item.get("pronunciation", ""),   # 4 - IPA EN
                item.get("definition", ""),      # 5 - Definition
                item.get("example", ""),         # 6 - Example EN
                item.get("term_es", ""),         # 7 - Term ES
                item.get("example_es", ""),      # 8 - Example ES
                etiquetas                        # 9 - Tags (level + POS)
            ])

    print(f"✅ CSV generado para Anki: {csv_path} (UTF-8 con BOM, delimitado por tabulador)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Arrastra un archivo JSON encima de este script para convertirlo a CSV.")
    else:
        json_to_csv(sys.argv[1])