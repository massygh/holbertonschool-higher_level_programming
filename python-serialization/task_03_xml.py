#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize the dictionary into XML and save it to the given filename.
    
    :param dictionary: Python dictionary to serialize.
    :param filename: Filename to save the XML data.
    """
    root = ET.Element("data")  # Create root element
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)  # Create child element
        element.text = str(value)  # Convert value to string and set as text content
    
    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename and return a Python dictionary.
    
    :param filename: Filename to read the XML data.
    :return: Deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)  # Parse XML file
        root = tree.getroot()  # Get root element
        
        # Reconstruct dictionary
        dictionary = {}
        for element in root:
            dictionary[element.tag] = element.text
        
        return dictionary
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Example dictionary
    data = {
        "name": "John",
        "age": 30,
        "is_student": True
    }

    # Serialize to XML
    serialize_to_xml(data, "data.xml")

    # Deserialize from XML
    deserialized_data = deserialize_from_xml("data.xml")
    print("Deserialized data:", deserialized_data)
