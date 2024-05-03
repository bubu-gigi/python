from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class IndexView(QWidget):

    def __init__(self, parent=None):
        super(IndexView, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Gestisci Servizi", self.navigate_to_servizi), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Abbonamenti", self.navigate_to_abbonamenti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Dipendenti", self.navigate_to_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Clienti", self.navigate_to_clienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Sistema", self.navigate_to_sistema), 2, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestione Dipendenti")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def navigate_to_servizi(self):
        pass

    def navigate_to_clienti(self):
        pass

    def navigate_to_dipendenti(self):
        pass

    def navigate_to_abbonamenti(self):
        pass

    def navigate_to_sistema(self):
        pass