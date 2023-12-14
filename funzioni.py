def registrati(username: str, password: str, nome: str, cognome: str, redis_conn: redis.Redis):
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti altre istanze
    # fatto senza hash per la password perchè non richiesto dal professore
    chiave_utente = f'UTENTE:{username}'
    
    if redis_conn.exists(chiave_utente):
        print(f"L'utente {username} esiste già")
        return False

    redis_conn.hset(chiave_utente, 'DnD', 'False') #impostato su False di default
    redis_conn.hset(chiave_utente, 'Password', password)
    redis_conn.hset(chiave_utente, 'Nome', nome)
    redis_conn.hset(chiave_utente, 'Cognome', cognome)

    print(f"Utente {username} registrato con successo.")
    return True

def login(username: str, password: str) -> str or bool:  # BASE
    return False
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti
    # in caso siano presenti restituisce l'id (chiave)
    # restituisce l'id_utente se ha corrispondenza, altrimenti restituisce false


def trova_utenti(username: str) -> list:  # GABRIEL
    # l'utente passe un username, anche parziale, e verranno restituiti tutti gli username
    # anche parzialmente compatibili
    # restutuisce una lista di username
    ...


def aggiungi_utenti(username_contatto: str, id_utente: str) -> bool:  # CARLOATTA
    # viene passato un username e viene aggiunto alla lista dei contatti.
    # restituisce vero se tutto va a buon fine
    ...


def cambia_stato(username: str) -> bool:  # GABRIEL
    # tramite hset, si modifica lo stato del non disturbare
    # retituisce True se va tutto a buon fine
    ...


def ottieni_stato(username_destinatario: str) -> bool:  # GABRIEL
    # dato un username, restituire lo stato, False se è occupato
    ...


def messaggi(mittente: str, destinatario: str, testo: str) -> bool:  # BASE
    # l'untente inserisce il destinatario, ed il testo.
    # restituisce True se va tutto bene
    ...


def leggi_messaggi(mittente: str, destinatario: str) -> list:  # CARLOTTA
    # restituisce tutti i valori da tra due utenti
    ...
