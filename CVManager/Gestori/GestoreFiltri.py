from Gestori.Helper import Helper
from Models.Filters.FiltriDipendenti import FiltriDipendenti
from Models.Filters.FiltriProgetti import FiltriProgetti

class GestoreFiltri:


    @staticmethod
    def handle_filtri_list_view_dipendenti(filtri: FiltriDipendenti):
        all_dipendenti_as_dict = Helper.get_all_dipendenti()
        all_dipendenti = []
        if all_dipendenti_as_dict is not None:
            all_dipendenti.extend(all_dipendenti_as_dict.values())
        dipendenti_filtered = []

        if all_dipendenti == "ko" or all_dipendenti is None or len(all_dipendenti) == 0:
            return {}

        for dipendente in all_dipendenti:
            if (dipendente.get_nome().lower().startswith(filtri.get_search()) or
                    dipendente.get_cognome().lower().startswith(filtri.get_search()) or
                    dipendente.get_codice_fiscale().lower().startswith(filtri.get_search())):
                if filtri.get_ruolo() != "tutti":
                    if dipendente.get_ruolo().lower() == str(filtri.get_ruolo()):
                        if filtri.get_stato() != "tutti":
                            if dipendente.get_stato().lower() == filtri.get_stato():
                                dipendenti_filtered.append(dipendente)
                        else:
                            dipendenti_filtered.append(dipendente)
                else:
                    if filtri.get_stato() != "tutti":
                        if dipendente.get_stato().lower() == filtri.get_stato():
                            dipendenti_filtered.append(dipendente)
                    else:
                        dipendenti_filtered.append(dipendente)
        if len(dipendenti_filtered) > 1:
            if filtri.get_ordinamento() == "alfabetico ascendente":
                dipendenti_filtered = sorted(dipendenti_filtered, key=lambda x: x.get_cognome(), reverse=False)
                return dipendenti_filtered
            elif filtri.get_ordinamento() == "alfabetico discendente":
                dipendenti_filtered = sorted(dipendenti_filtered, key=lambda x: x.get_cognome(), reverse=True)
                return dipendenti_filtered
            elif filtri.get_ordinamento() == "matricola ascendente":
                dipendenti_filtered = sorted(dipendenti_filtered, key=lambda x: int(x.get_matricola()), reverse=False)
                return dipendenti_filtered
            elif filtri.get_ordinamento() == "matricola discendente":
                dipendenti_filtered = sorted(dipendenti_filtered, key=lambda x: int(x.get_matricola()), reverse=True)
                return dipendenti_filtered
            else:
                return dipendenti_filtered
        else:
            return dipendenti_filtered

    @staticmethod
    def handle_filtri_list_view_progetti(filtri: FiltriProgetti):
        all_progetti_as_dict = Helper.get_all_progetti()
        all_progetti = []
        if all_progetti_as_dict is not None:
            all_progetti.extend(all_progetti_as_dict.values())
        progetti_filtered = []

        if all_progetti == "ko" or all_progetti is None or len(all_progetti) == 0:
            return {}

        for progetto in all_progetti:
            if progetto.get_titolo().lower().startswith(filtri.get_search()):
                if filtri.get_tipologia() == "tutti":
                    if filtri.get_stato() == "tutti":
                        progetti_filtered.append(progetto)
                    else:
                        if filtri.get_stato() == progetto.get_stato():
                            progetti_filtered.append(progetto)
                else:
                    if filtri.get_tipologia() == progetto.get_tipologia():
                        if filtri.get_stato() == "tutti":
                            progetti_filtered.append(progetto)
                        else:
                            if filtri.get_stato() == progetto.get_stato():
                                progetti_filtered.append(progetto)
        if len(progetti_filtered) > 1:
            if filtri.get_ordinamento() == "alfabetico ascendente":
                progetti_filtered = sorted(progetti_filtered, key=lambda x: x.get_titolo(), reverse=False)
                return progetti_filtered
            elif filtri.get_ordinamento() == "alfabetico discendente":
                progetti_filtered = sorted(progetti_filtered, key=lambda x: x.get_titolo(), reverse=True)
                return progetti_filtered
            else:
                return progetti_filtered
        else:
            return progetti_filtered