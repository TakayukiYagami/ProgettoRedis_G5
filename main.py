import threading

import funzioni
import redis

id_utente = 'lucabarbetta'
if __name__ == '__main__':

    r = redis.Redis(
        host="redis-10797.c55.eu-central-1-1.ec2.cloud.redislabs.com",
        port=10797,
        password="yGoGfZmUmeAy90OLyd27DoVDyXgeq95L",
        decode_responses=True
    )

    while True:
        print('Benvenuti nel sistema di messaggistica di redis')
        print('Seleziona una delle seguenti opzioni:')
        if id_utente:
            thread_notifiche = threading.Thread(target=funzioni.hai_una_nuova_notifica, args=(id_utente, r))
            thread_notifiche.start()
            while 1:
                print('1. Esci')
                print('2. Cambia stato')
                print('3. Cerca un nuovo contatto')
                print('4. Aggiungi nuovo contatto')
                print('5. Manda messaggio')
                print('6. Vedi cronologia')
                sel = input('')
                try:
                    sel = int(sel)
                except:
                    print('Non hai inserito un valore valido')
                if sel == 1:
                    print('Arrivederci')
                    id_utente = None
                    r.close()
                    break
                if sel == 2:
                    stato = funzioni.cambia_stato(id_utente, r)
                    if stato:
                        print(f'Stato cambiato con successo, stato attuale: {stato}')
                if sel == 3:
                    username_contatto = input('Inserisci username da cercare (anche parziale)')
                    utenti = funzioni.trova_utenti(username=username_contatto, redis_conn=r)
                    if utenti:
                        for elem in utenti:
                            print(elem)
                    else:
                        print('Nessun utente trovato')
                if sel == 4:
                    username_contatto = input('Inserisci username: ')
                    if funzioni.aggiungi_utente(username_utente=id_utente, username_contatto=username_contatto,
                                                redis_conn=r):
                        print(f'{username_contatto} aggiunto con successo')
                    else:
                        print('Username non trovato')
                if sel == 5:
                    contatti = funzioni.ottieni_contatti(id_utente, r)
                    id_destinatario = ''
                    if contatti:
                        for i, elem in enumerate(contatti):
                            print(f'{i + 1}) {elem}')
                        while 1:
                            id_destinatario = input('Seleziona contatto')
                            try:
                                id_destinatario = int(id_destinatario)
                                break
                            except:
                                print('Non hai inserito un valore valido')
                    id_destinatario = contatti[id_destinatario - 1]
                    messaggio = input('inserisci il messaggio:')
                    stato = funzioni.messaggi(mittente=id_utente, destinatario=id_destinatario, testo=messaggio,
                                              redis_conn=r)
                    if stato == 1:
                        print('Messaggio non recapitato, utente in DnD')
                    elif stato == 2:
                        print('Messaggio recapitato con successo')
                if sel == 6:
                    contatti = funzioni.ottieni_contatti(id_utente, r)
                    id_destinatario = ''
                    if contatti:
                        for i, elem in enumerate(contatti):
                            print(f'{i + 1}) {elem}')
                        while 1:
                            id_destinatario = input('Seleziona contatto')
                            try:
                                id_destinatario = int(id_destinatario)
                                break
                            except:
                                print('Non hai inserito un valore valido')
                    id_destinatario = contatti[id_destinatario - 1]
                    print('Caricamento messaggi...')
                    chat = funzioni.leggi_messaggi(mittente=id_utente, destinatario=id_destinatario, redis_conn=r)
                    for elem in chat:
                        print(elem)
        else:
            while 1:
                print('1. Esci')
                print('2. Registrati')
                print('3. Accedi')
                sel = input('')
                try:
                    sel = int(sel)
                    break
                except:
                    print('Non hai inserito un valore valido')
            if sel == 1:
                print('Arrivederci')
                r.close()
                break
            if sel == 2:
                while 1:
                    user = input('Inserisci username: ')
                    pw = input('Inserisci password: ')
                    nome = input('Inserisci nome: ')
                    cognome = input('Inserisci cognome: ')
                    out = funzioni.registrati(username=user, password=pw, nome=nome, cognome=cognome, redis_conn=r)
                    if out:
                        print('Registrazione avvenuta con successo')
                        break
                    print('Username già preso')
                    break
            if sel == 3:
                while 1:
                    user = input('Inserisci username: ')
                    pw = input('Inserisci password: ')
                    out = funzioni.login(username=user, password=pw, redis_conn=r)
                    if out:
                        id_utente = out
                        break
                    print('Username o Password sbagliati')
                    break
