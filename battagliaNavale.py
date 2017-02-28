# coding: utf-8
# Gioco della Battaglia navale a un giocatore
# W. Vannini 2017

from random import randint



###########################################
# INIZIALIZZAZIONE
###########################################

# creo una matrice 5x5 per le navi
# inizialmente piena di 0
# le celle potranno contenere:
# 0: acqua
# X: nave

navi = {}

for i in ['A','B','C','D','E']:
    navi[i] = ['0'] * 5

# creo una seconda matrice 5x5 per registrare i tiri
# le celle potranno contenere:
# 0: acqua
# +: colpo a vuoto
# X: colpo a segno

tiri = {}

for i in ['A', 'B', 'C', 'D', 'E']:
    tiri[i] = ['0'] * 5

# stampaTavola: fa pretty print del dizionario che viene passato
# il dizionario deve avere chiavi alfabetiche e i valori devono tutti essere
# liste dello stesso numero di elementi.

# metto 5 navi da 1 a caso nella tabella navi
for i in range(5):
    #la tavola è un dizionario 5x5, le chiavi sono le prime 5 lettere dell'alfabeto
    rigaNave = 'ABCDE'[randint(0,4)]
    #print("rigaNave=" + str(rigaNave))
    colonnaNave = randint(0,4)
    #print("colonnaNave="+ str(colonnaNave))
    navi[rigaNave][colonnaNave] = 'X'




def stampaTavola(tav):
    chiavi = sorted(tav.keys())

    # stampare qui le intestazioni di colonna!!!
    intColonne = '    '
    j = 1
    for i in tav[chiavi[0]]:
        intColonne += str(j) + '   '
        j += 1
    print(intColonne)


    for i in chiavi:
        #stampa la riga i-esima
        corpoRiga = ''
        for j in tav[i]:
            corpoRiga += ' | ' + j
        # aggiungo l'ultimo bordo
        corpoRiga += ' | '
        print(i + corpoRiga)



############################################
# Schermata di benvenuto
############################################

print("***********************************************")
print("************* BATTAGLIA NAVALE 1.0 ************")
print("***********************************************")
print("***********************************************")
print("Indica la tua mossa con una lettera e un numero")
print("in quest'ordine, e senza spazio in mezzo.")
print("Ad esempio: B2")
print("***********************************************")
print("***********************************************")
print() #riga vuota per separare visivamente

###########################################
# CICLO PRINCIPALE
###########################################

while True:
    #stampiamo la tavola dei colpi
    stampaTavola(navi)
    
    colpo = input("coordinate di tiro (scrivi esci per uscire):")
    print() #riga vuota per spaziare
    if colpo == "esci":
        print("***********************************************")
        print("partita terminata\n\n")
        break
    else:
        print("tiro alla riga " + colpo[0].upper() + " colonna " + str(colpo[1]))
        print()
