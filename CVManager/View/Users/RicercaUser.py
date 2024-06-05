from PyQt5.QtWidgets import QLineEdit, QPushButton, QDialog, QMessageBox
from PyQt5.uic import loadUi

from Gestori.GestoreUsers import GestoreUsers
from View.Users.UserForm import UserForm


class RicercaUser(QDialog):

    def __init__(self, parent=None):
        super(RicercaUser, self).__init__(parent)

        self.edit_user = None
        loadUi("./GUILayout/find_user.ui", self)
        self.gestore_users = GestoreUsers()

        self.line_username = self.findChild(QLineEdit, "username_to_find")
        self.button_ricerca_user = self.findChild(QPushButton, "button_ricerca_user")

        self.button_ricerca_user.clicked.connect(self.handle_ricerca_user_click)

    def handle_ricerca_user_click(self):
        user = self.gestore_users.ricerca_user(self.line_username.text())
        if user is None:
            QMessageBox.critical(self, 'Errore', "Nessun user trovato con questo username. Riprova", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.edit_user = UserForm(user=user)
            self.edit_user.show()
            self.close()




