# coding: utf-8
# Gioco della Battaglia navale a un giocatore
# W. Vannini 2017

from random import randint

#
# 1. INIZIALIZZAZIONE
#     0. creare due tavole di gioco 5x5
#         1. una tavola "NAVI" dove posiziona le sue navi (che noi non vediamo)
#         2. una tavola "TIRI" dove annota i notri tiri (che vediamo)
#     1. schermata di benvenuto e visualizzazione della tavola TIRI dove compaiono i nostri tiri (inizialmente vuota)
#     2. posiziona a caso 5 navi da 1 sulla tavola NAVI (che noi non vediamo mai)
#     3. porta il numero di navi rimaste da colpire a 5 e porta il numero di colpi sparati a 0

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
    rigaNave = randint(1,5)
    colonnaNave = randint(1,5)
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

#stampiamo la tavola dei colpi
stampaTavola(navi)
