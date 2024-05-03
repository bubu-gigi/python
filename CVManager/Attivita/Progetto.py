import datetime


class Progetto:

    def __init__(self):
        self.id = -1
        self.titolo = ""
        self.descrizione = ""
        # self.pm_id = {}
        self.tipologia = ""
        self.data_inizio = datetime.datetime(1970, 1, 1)
        self.data_fine = datetime.datetime(9999, 12, 31)
        self.budget = 0.0
        self.stato = ""