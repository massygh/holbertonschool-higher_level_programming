import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de l'objet et l'enregistre
        :param filename: Nom du fichier où l'objet sera sérialisé.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Failed to serialize object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Charge et retourne une instance de CustomObject à partir du fichier
        :param filename: Nom du fichier où l'objet est sérialisé.
        :return: Instance de CustomObject ou None en cas d'erreur.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from '{filename}'.")
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Failed to deserialize object: {e}")
            return None

# Exemple d'utilisation


if __name__ == "__main__":
    # Crée une instance de CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Sérialise l'objet
    obj.serialize("object.pkl")

    # Désérialise l'objet dans une nouvelle instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    if new_obj:
        new_obj.display()
