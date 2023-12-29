import redis
import time


def registrati(username: str, password: str, nome: str, cognome: str, redis_conn: redis.Redis):
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti altre istanze
    # fatto senza hash per la password perchè non richiesto dal professore
    chiave_utente = f'UTENTE:{username}'

    if redis_conn.exists(chiave_utente):
        print(f"L'utente {username} esiste già")
        return False

    redis_conn.hset(chiave_utente, 'DnD', 'False')  # impostato su False di default
    redis_conn.hset(chiave_utente, 'Password', password)
    redis_conn.hset(chiave_utente, 'Nome', nome)
    redis_conn.hset(chiave_utente, 'Cognome', cognome)

    print(f"Utente {username} registrato con successo.")
    return True


def login(username: str, password: str, redis_conn: redis.Redis) -> str or bool:  # BASE
    # l'utente passa username e password, il database viene interrogato per vedere se sono presenti
    # in caso siano presenti restituisce l'id (chiave)
    # restituisce l'id_utente se ha corrispondenza, altrimenti restituisce false
    chiave_utente = f'UTENTE:{username}'
    password_redis = redis_conn.hget(chiave_utente, 'Password')
    if password_redis == password:
        return username
    return False


def trova_utenti(username: str, redis_conn: redis.Redis) -> list:  # GABRIEL
    # l'utente passe un username, anche parziale, e verranno restituiti tutti gli username
    # anche parzialmente compatibili
    # restutuisce una lista di username o una lista vuota se non trova nulla
    ...


def aggiungi_utente(username_utente: str, username_contatto: str, redis_conn: redis.Redis) -> bool:
    # viene passato un username e viene aggiunto alla lista dei contatti.
    # restituisce vero se tutto va a buon fine
    chiave_contatti = f'CONTATTI_UTENTE:{username_utente}'
    chiave_contatto = f'UTENTE:{username_contatto}'  # utente da aggiungere esiste?
    if not redis_conn.exists(chiave_contatto):
        return False
    redis_conn.sadd(chiave_contatti, username_contatto)  # sadd gestisce già caso in cui siano già amic*
    return True


def cambia_stato(username: str, redis_conn: redis.Redis) -> bool:
    # tramite hset, si modifica lo stato del non disturbare
    # restituisce True se va tutto a buon fine
    chiave_utente = f'UTENTE:{username}'

    if not redis_conn.exists(chiave_utente):
        return False

    stato_corrente = redis_conn.hget(chiave_utente, 'DnD')
    if stato_corrente == b'True':
        nuovo_stato = 'False'
    else:
        nuovo_stato = 'True'
    redis_conn.hset(chiave_utente, 'DnD', nuovo_stato)
    return nuovo_stato


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


def ottieni_contatti(username: str, redis_conn: redis.Redis) -> list:
    # funzione che dato un userame trova i suoi contati
    # restituisce una lista
    chiave = f'CONTATTI_UTENTE:{username}'
    if redis_conn.exists(chiave):
        valori = redis_conn.smembers(chiave)
        return list(valori)
    else:
        return []


def messaggi(mittente: str, destinatario: str, testo: str, redis_conn: redis.Redis) -> int:  # BASE
    # l'untente inserisce il destinatario, ed il testo.
    # restituisce 2 se va tutto bene, restituisce 1 se l'utente è occupato
    # controllo sullo stato del destinatario
    if not ottieni_stato(destinatario, redis_conn):
        return 1
    chiave = sorted([mittente, destinatario])
    # creazione del testo composto da: 26 caratteri relativi al timestamp, 1 carattere relativo alla posizione sulla lista
    # del mittente e N caratteri desitinati al testo
    testo_metadati = str(int(time.time())) + str(chiave.index(mittente)) + testo
    chiave_esiste = redis_conn.exists(f'{chiave[0]}{chiave[1]}')
    if not chiave_esiste:
        redis_conn.rpush(f'{mittente}{destinatario}', testo_metadati)
    redis_conn.rpush(f'{mittente}{destinatario}', testo_metadati)
    return 2


def leggi_messaggi(mittente: str, destinatario: str, redis_conn: redis.Redis) -> list or bool:  # CARLOTTA
    # restituisce tutti i valori da tra due utenti
    # ogni elemento della lista è un testo mandato da un utente
    # restituisce False se non trova la chat tra i due utenti
<<<<<<< HEAD

    chiave = f'{mittente}{destinatario}'
    chiave_esiste = redis_conn.exists(chiave)

    if not chiave_esiste:
        print("La chat tra i due utenti non esiste.")
        return False

    messaggi = redis_conn.lrange(chiave, 0, -1)

    result = []
    for messaggio in messaggi:
        timestamp = messaggio[:11]
        testo = messaggio[11:]
        if messaggio[11] == 0: #io ho supposto che l'indice per il mittente sia sempre 0 però forse è un errore?
            prefisso = ">" #messaggio inviato
        else:
            prefisso = "<" #messaggio ricevuto
        messaggio_formattato = f"{prefisso} {testo}"
        result.append(messaggio_formattato)

    return result

=======
    ...
>>>>>>> 95b61bf99b5c35b93a860801ea6d0f1953cf3bb4
