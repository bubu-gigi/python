from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.uic import loadUi

from Gestori.Helper import Helper
from View.Dipendenti.DipendenteForm import DipendenteForm
from View.Dipendenti.DipendentiTable import DipendentiTable
from View.Users.ReimpostaPassword import ReimpostaPassword

class Login(QWidget):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.reimposta_password = None
        self.dipendente_form = None
        self.dipendenti_table = None
        loadUi("./GUILayout/login.ui", self)

        self.setFixedSize(750, 500)



        self.line_username = self.findChild(QLineEdit, "line_username")
        self.line_password = self.findChild(QLineEdit, "line_password")
        self.button_login = self.findChild(QPushButton, "button_login")
        self.button_login.clicked.connect(self.handle_login_click)
        self.button_reimposta_password = self.findChild(QPushButton, "button_reimposta_password")
        self.button_reimposta_password.clicked.connect(self.handle_reimposta_password_click)


    #R01mkWgY
    def handle_login_click(self):
        users = Helper.get_all_users()
        dipendenti = Helper.get_all_dipendenti()

        if self.line_username.text() == "admin" and self.line_password.text() == "admin":
            self.dipendenti_table = DipendentiTable()
            self.dipendenti_table.show()
            return self.close()
        if users is None or len(users) <= 0 or len(dipendenti) <= 0 or dipendenti is None:
            QMessageBox.critical(self, 'Errore', "Nessun user salvato. Solo un amministratore può loggare.",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            for user in users.values():
                username = user.get_username()
                password = user.get_password()
                if username == self.line_username.text() and password == self.line_password.text():
                    if user.get_role() == "admin":
                        self.dipendenti_table = DipendentiTable()
                        self.dipendenti_table.show()
                        return self.close()
                    else:
                        matricola = username[-3:]
                        while matricola.startswith("0"):
                            matricola = matricola[1:]
                        if username == password:
                            self.reimposta_password = ReimpostaPassword()
                            self.reimposta_password.show()
                            return self.close()
                        for dipendente in dipendenti.values():
                            if int(dipendente.get_matricola()) == int(matricola):
                                self.dipendente_form = DipendenteForm(dipendente=dipendente)
                                self.dipendente_form.show()
                                return self.close()
                        self.dipendente_form = DipendenteForm()
                        self.dipendente_form.show()
                        return self.close()
            QMessageBox.critical(self, 'Errore', "Credenziali Errate. Riprovare.",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return


    def handle_reimposta_password_click(self):
        self.reimposta_password = ReimpostaPassword()
        self.reimposta_password.show()
        self.close()



