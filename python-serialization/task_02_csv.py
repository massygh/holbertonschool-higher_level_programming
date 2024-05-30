import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en un fichier JSON.
    
    :param csv_filename: Nom du fichier CSV à convertir.
    :return: True si la conversion est réussie, False sinon.
    """
    try:
        # Lire les données du fichier CSV
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]
        
        # Sérialiser les données en JSON et les écrire dans un fichier
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        print("Conversion successful. Data written to 'data.json'.")
        return True
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    csv_filename = 'example.csv'  # Remplacez par le nom de votre fichier CSV
    convert_csv_to_json(csv_filename)
