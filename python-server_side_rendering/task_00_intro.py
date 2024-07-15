def generate_invitations(template, attendees):
    # Vérifier si le modèle est une chaîne de caractères
    if not isinstance(template, str):
        print("Erreur : Le modèle doit être une chaîne de caractères.")
        return

    # Vérifier si les participants sont une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : Les participants doivent être une liste de dictionnaires.")
        return

    # Vérifier si le modèle est vide
    if not template.strip():
        print("Le modèle est vide, aucun fichier de sortie généré.")
        return

    # Vérifier si la liste des participants est vide
    if not attendees:
        print("Aucune donnée fournie, aucun fichier de sortie généré.")
        return

    # Traiter chaque participant
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") if attendee.get(key) is not None else "N/A"
            output = output.replace(f"{{{key}}}", value)
        
        # Écrire dans le fichier de sortie
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as f:
            f.write(output)
        print(f"Généré {output_filename}")
