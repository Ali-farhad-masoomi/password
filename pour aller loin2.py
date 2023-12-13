import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_password_duplicate(password, password_list):
    return password in password_list

# Exemple d'utilisation
password_file = ["password123", "securePass", "random@456"]

# Générer un nouveau mot de passe
new_password = generate_password()

# Vérifier s'il est déjà dans la liste
if is_password_duplicate(new_password, password_file):
    print("Le mot de passe existe déjà dans le fichier.")
else:
    print(f"Ajouter le nouveau mot de passe : {new_password}")
    password_file.append(new_password)

# Afficher la liste mise à jour
print("Liste des mots de passe :")
for password in password_file:
    print(password)
