import json

class AuthService:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        with open("auth/users.json") as f:
            return json.load(f)

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

    def register(self, username, password):
        if username not in self.users:
            self.users[username] = password
            with open('auth/users.json', 'w') as f:
                json.dump(self.users, f)
            return True
        return False