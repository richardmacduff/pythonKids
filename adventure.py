# -*- coding: iso-8859-15 -*-

"""
Lo scheletro di un gioco adventure --richiede Python 2.7.

La variabile mondo una struttura dati che descrive il mondo che vogliamo  esplorare. Questa struttura è costituita da coppie chiave/valore che descrivono i luoghi e le uscite che li collegano. Ogni luogo ha una descrizione e una o più uscite che lo collegano ad altri luoghi.

Dal punto di vista implementativo, vengono usati dei dizionari.

Il codice alla fine del file crea un ciclo che permette di attraversare i diversi luoghi del gioco.
Ad ogni iterazione:
- viene visualizzato il luogo in cui ci si trova,
- vengono elencate le uscite disponibili
- si chiede un input all'utente (deve corrispondere al nome di un'uscita)
- il programma risponde spostandosi da un luogo all'altro o dicendo che non capisce l'input.

"""

mondo = {
    'caverna': {
        'descrizione': 'Sei in una caverna misteriosa.',
        'uscite': {
            'sù': 'cortile',
        },
    },
    'torre': {
        'descrizione': "Sei in cima a un'alta torre.",
        'uscite': {
            'giù': 'ingresso',
        },
    },
    'cortile': {
        'descrizione': 'Sei nel cortile del castello.',
        'uscite': {
            'sud': 'ingresso',
            'giù': 'caverna'
        },
    },
    'ingresso': {
        'descrizione': "Sei all'ingresso del castello",
        'uscite': {
            'sud': 'foresta',
            'sù': 'torre',
            'nord': 'cortile',
        },
    },
    'foresta': {
        'descrizione': 'Sei nella radura di una foresta.',
        'uscite': {
            'nord': 'ingresso',
        },
    },
}


# Partiamo dalla caverna.
tappa = 'caverna'
# Avvia il ciclo che ci porta di tappa in tappa.
while True:
    # Prendiamo i dettagli del posto nel mondo in cui stiamo facendo tappa.
    posto = mondo[tappa]
    # Stampa descrizione e uscite del posto.
    print(posto['descrizione'])
    print('uscite disponibili:')
    print(', '.join(posto['uscite'].keys()))
    # chiediamo l'input dell'utente
    direzione = raw_input('Che uscita prendo? [stop per uscire]: ').strip().lower()
    # Comportiamoci secondo l'input dell'utente
    if direzione == 'stop':
        print('Ciao ciao!')
        break  # interrompi il ciclo e esci
    elif direzione in posto['uscite']:
        # raggiungi una nuova tappa
        tappa = posto['uscite'][direzione]
    else:
        # l'input dell'utente non corrisponde a nessuna uscita
        print("Non capisco!")
