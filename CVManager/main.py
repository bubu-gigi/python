import json
import os.path
import sys

from PyQt5.QtWidgets import QApplication
from View.IndexView import IndexView

if __name__ == '__main__':
    data = {
        "nome": "guglielmo",
        "cognome": "borgognoni",
        "email": "bubugigigmail.com"
    }
    if os.path.isfile("Dati/Utente.json"):
        with open("Dati/Utente.json", "a") as f:
            tmp = json.dumps(data)
            json.dump(tmp,  f)
    else:
        with open("Dati/Utente.json", "w+") as f:
            tmp = json.dumps(data)
            json.dump(tmp, f)

    #app = QApplication(sys.argv)
    #view_index = IndexView()
    #view_index.show()
    #sys.exit(app.exec())