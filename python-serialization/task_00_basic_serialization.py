import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.

    :param data: Dictionnaire Python à sérialiser.
    :param filename: Nom du fichier de sortie JSON. Si le fichier existe déjà, il sera remplacé.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Charge un fichier JSON et désérialise son contenu en un dictionnaire Python.

    :param filename: Nom du fichier JSON d'entrée.
    :return: Dictionnaire Python désérialisé à partir du fichier JSON.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    print(f"Data loaded and deserialized from '{filename}'.")
    return data
