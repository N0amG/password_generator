import json
import random
import string

class PasswordManager:
    
    def __init__(self):
        pass
    
    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def load_existing_passwords(self):
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def save_to_json(self, data):
        with open('passwords.json', 'w') as file:  # Utiliser 'w' pour réécrire le fichier
            json.dump(data, file, indent=4)

    def generate_passwords(self, website, username, password_length):
        passwords = self.load_existing_passwords()
        
        password = self.generate_password(password_length)
        
        passwords.append({"website": website, "username": username, "password": password})

        self.save_to_json(passwords)
        print("Mots de passe enregistrés dans passwords.json")
        return password

    def sort_passwords(self):
        passwords = self.load_existing_passwords()

        sorted_passwords = sorted(passwords, key=lambda x: (x['website'], x['username']))
        self.save_to_json(sorted_passwords)
        
if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.sort_passwords()