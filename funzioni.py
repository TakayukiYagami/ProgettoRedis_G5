import redis

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


def aggiungi_utente(username_utente: str, username_contatto: str, redis_conn: redis.Redis) -> bool:  
    # viene passato un username e viene aggiunto alla lista dei contatti.
    # restituisce vero se tutto va a buon fine
    chiave_contatti = f'CONTATTI_UTENTE:{username_utente}'

    chiave_utente = f'UTENTE:{username_utente}' 
    if not redis_conn.exists(chiave_utente): #utente  principale esiste? 
        print(f"L'utente {username_utente} non esiste.")
        return False

    chiave_contatto = f'UTENTE:{username_contatto}' #utente da aggiungere esiste?
    if not redis_conn.exists(chiave_contatto):
        print(f"L'utente {username_contatto} non esiste.")
        return False

    redis_conn.sadd(chiave_contatti, username_contatto) #sadd gestisce già caso in cui siano già amici

    print(f"{username_contatto} è stato aggiunto alla lista dei contatti di {username_utente}.")
    return True



def cambia_stato(username: str, redis_conn: redis.Redis) -> bool: 
    # tramite hset, si modifica lo stato del non disturbare
    # restituisce True se va tutto a buon fine
    chiave_utente = f'UTENTE:{username}'

    if not redis_conn.exists(chiave_utente):
        print(f"L'utente {username} non esiste.")
        return False

    stato_corrente = redis_conn.hget(chiave_utente, 'DnD')
    if stato_corrente == b'True':
        nuovo_stato = 'False'
    else:
        nuovo_stato = 'True'
    redis_conn.hset(chiave_utente, 'DnD', nuovo_stato)

    print(f"Lo stato di non disturbare per l'utente {username} è stato cambiato a {nuovo_stato}.")
    return True



def ottieni_stato(username: str, redis_conn: redis.Redis) -> bool: 
    # dato un username, restituire lo stato, False se è occupato
    chiave_utente = f'UTENTE:{username}'

    if not redis_conn.exists(chiave_utente):
        print(f"L'utente {username} non esiste.")
        return False

    stato = redis_conn.hget(chiave_utente, 'DnD')

    if stato == 'True':
        print(f"Lo stato dell'utente {username} è: Occupato")
        return False
    
    else:
        print(f"Lo stato dell'utente {username} è: Disponibile")
        return True


def messaggi(mittente: str, destinatario: str, testo: str) -> bool:  # BASE
    # l'untente inserisce il destinatario, ed il testo.
    # restituisce True se va tutto bene
    ...


def leggi_messaggi(mittente: str, destinatario: str) -> list:  # CARLOTTA
    # restituisce tutti i valori da tra due utenti
    ...
