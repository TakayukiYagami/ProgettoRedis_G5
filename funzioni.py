# STRUTTURE DATI
#     UTENTE:
#         id_utente(num):username{(hash)
#             DnD:bool
#             Password:Hash
#             Nome:str
#             Cnome:str
#         }
#     CONTATTI_UTENTI:
#         {id_utenti(num)_contatti:[contatto1-->username, contatto2, contattoN]}
#     MESSAGGI:
#         {}


def registrati(username: str, password: str) -> bool:  # CARLOTTA
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti
    # altre istanze
    # in caso non sono presenti altre istanze utilizzare l'hash per salvare la password
    ...


def login(username: str, password: str) -> str:  # BASE
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti
    # in caso siano presenti restituisce l'id (chiave)
    # restituisce l'id_utente
    ...


def trova_utenti(username: str) -> list:  # GABRIEL
    # l'utente passe un username, anche parziale, e verranno restituiti tutti gli username
    # anche parzialmente compatibili
    # restutuisce una lista di username
    ...


def aggiungi_utenti(username_contatto: str, id_utente) -> bool:  # CARLOATTA
    # viene passato un username e viene aggiunto alla lista dei contatti.
    # restituisce vero se tutto va a buon fine
    ...


def cambia_stato(id_utente: str) -> bool:  # GABRIEL
    # tramite hset, si modifica lo stato del non disturbare
    # retituisce True se va tutto a buon fine
    ...


def messaggi(mittente: str, destinatario: str, testo: str) -> bool:
    # l'untente inserisce il destinatario, ed il testo.
    # restituisce True se va tutto bene
    ...
