import hashlib
import re
import json
import  random
import string


def is_password_secure(password):
    # Vérifie si le mot de passe respecte les exigences de sécurité
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in '!@#$%^&*' for c in password)
    )

def get_secure_password():
    while True:
        password = input("Choisissez un mot de passe : ")

        if is_password_secure(password):
            return password
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

def hash_password(password):
    # Crypte le mot de passe avec l'algorithme SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

if __name__ == "__main__":
    # Demande à l'utilisateur de choisir un mot de passe sécurisé
    secure_password = get_secure_password()

    # Crypte le mot de passe
    hashed_password = hash_password(secure_password)

    # Affiche le mot de passe crypté
    print(f"Mot de passe crypté avec SHA-256 : {hashed_password}")
