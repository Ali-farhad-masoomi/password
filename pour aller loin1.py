import hashlib
import json
import os

def hash_password(password):
    # Hache le mot de passe avec l'algorithme SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def load_passwords(filename):
    # Charge les mots de passe depuis le fichier JSON
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
    else:
        passwords = {}
    return passwords

def save_passwords(filename, passwords):
    # Enregistre les mots de passe dans le fichier JSON
    with open(filename, 'w') as file:
        json.dump(passwords, file, indent=2)

def add_password(passwords):
    # Ajoute un nouveau mot de passe
    service = input("Nom du service ou du compte : ")
    user = input("Nom d'utilisateur : ")
    pwd = input("Mot de passe : ")
    
    hashed_pwd = hash_password(pwd)
    passwords[service] = {"user": user, "password": hashed_pwd}
    save_passwords("passwords.json", passwords)
    print("Mot de passe ajouté avec succès.")

def display_passwords(passwords):
    # Affiche les mots de passe enregistrés
    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        print("Mots de passe enregistrés :")
        for service, details in passwords.items():
            print(f"Service/Compte : {service}")
            print(f"Nom d'utilisateur : {details['user']}")
            print("Mot de passe : ********")
            print()

if __name__ == "__main__":
    password_file = "passwords.json"
    stored_passwords = load_passwords(password_file)

    while True:
        print("\n1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe enregistrés")
        print("3. Quitter")
        
        choice = input("Choisissez une option (1/2/3) : ")

        if choice == "1":
            add_password(stored_passwords)
        elif choice == "2":
            display_passwords(stored_passwords)
        elif choice == "3":
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")
