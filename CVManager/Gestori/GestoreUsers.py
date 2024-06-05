import pickle

from Gestori.Helper import Helper

class GestoreUsers:

    def __init__(self):
        self.users = Helper.get_all_users()

    def ricerca_user(self, username: str):
        self.users = Helper.get_all_users()
        if self.users is not None and len(self.users) is not 0:
            for u in self.users.values():
                if u.get_username() == username:
                    return u
        else:
            return None

    def salva_user(self, username: str, password: str, role: str):
        from Models.User import User
        self.users = Helper.get_all_users()
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_role(role)
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is None:
            if self.users is None:
                self.users = {}
            self.users[user.get_username()] = user
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def modifica_user(self, username: str, password: str, role: str):
        from Models.User import User
        self.users = Helper.get_all_users()
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_role(role)
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is not None:
            self.users[user.get_username()] = user
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_user(self, username: str):
        self.users = Helper.get_all_users()
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is not None:
            del self.users[username]
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def reimposta_password(self, username, vecchia_password, nuova_password, conferma_password):
        user = self.ricerca_user(username)
        if user is None:
            return "user not found"
        if user.get_password() != vecchia_password:
            return "old password wrong"
        if len(nuova_password) < 8:
            return "password not validated"
        if nuova_password != conferma_password:
            return "new password not the same"
        user.set_password(nuova_password)
        self.modifica_user(user.get_username(), user.get_password(), user.get_role())
        return "ok"


