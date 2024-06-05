
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox, QDialog
from PyQt5.uic import loadUi

from Gestori.GestoreUsers import GestoreUsers

class UserForm(QDialog):
    def __init__(self, parent=None, user=None):
        super(UserForm, self).__init__(parent)

        loadUi("./GUILayout/crea_user.ui", self)
        self.gestore_users = GestoreUsers()
        self.user = user

        self.line_username = self.findChild(QLineEdit, "username")
        self.line_password = self.findChild(QLineEdit, "password")
        self.line_role = self.findChild(QLineEdit, "role")

        self.button_cancel = self.findChild(QPushButton, "button_cancel_user")
        self.button_delete = self.findChild(QPushButton, "button_delete_user")
        self.button_save = self.findChild(QPushButton, "button_save_user")

        if user is None:
            self.button_delete.hide()

        if user is not None:
            self.line_username.setText(user.get_username())
            self.line_password.setText(user.get_password())
            self.line_role.setText(user.get_role())

        self.button_cancel.clicked.connect(self.handle_cancel_click)
        self.button_delete.clicked.connect(self.handle_delete_click)
        self.button_save.clicked.connect(self.handle_save_click)

    def handle_cancel_click(self):
        self.close()

    def handle_delete_click(self):
        self.gestore_users.rimuovi_user(self.line_username.text())
        self.close()

    def handle_save_click(self):
        children = self.findChildren(QLineEdit)
        for c in children:
            if (c.text() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return
        if len(self.line_password.text()) < 8:
            QMessageBox.critical(self, 'Errore', "La password deve avere almeno 8 caratteri", QMessageBox.Ok, QMessageBox.Ok)
            return
        if self.user is not None:
            self.gestore_users.modifica_user(self.line_username.text(), self.line_password.text(),
                                             self.line_role.text())
        else:
            self.gestore_users.salva_user(self.line_username.text(), self.line_password.text(),
                                         self.line_role.text())
        self.close()

