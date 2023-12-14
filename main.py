import funzioni

# Assuming id_utente is initially set to None or some default value
id_utente = 1

if __name__ == '__main__':
    while True:
        print('Benvenuti nel sistema di messaggistica di redis')
        print('Seleziona una delle seguenti opzioni:')
        if id_utente:
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
                    id_utente = None
                    break
        else:
            while 1:
                print('1. Registrati')
                print('2. Accedi')
                sel = input('')
                try:
                    sel = int(sel)
                    break
                except:
                    print('Non hai inserito un valore valido')
            if sel == 1:
                while 1:
                    user = input('Inserisci username: ')
                    pw = input('Inserisci password: ')
                    out = funzioni.registrati(username=user, password=pw)
                    if out:
                        print('Registrazione avvenuta con successo')
                        break
                    print('Username già preso')
                    break
            if sel == 2:
                while 1:
                    user = input('Inserisci username: ')
                    pw = input('Inserisci password: ')
                    out = funzioni.login(username=user, password=pw)
                    if out:
                        id_utente = out
                        break
                    print('Username o Password sbagliati')
                    break
