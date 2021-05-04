from random import randint
import time


# GENERER UN TEXTE ALEATOIRE DE TAILLE 200
def generer_texte(taille):
    T=''
    for i in range(0, taille):
        T += 'AGCT'[randint(0, 3)]
    return T

# GENERER UN MOTIF ALEATOIRE DE TAILLE 4
def generer_motif(taille):
    M=''
    for i in range(0, taille):
        M += 'AGCT'[randint(0,3)]
    return M

#----------------------------------------------------------------------------------------------------------------------------------------
# FONCTION DE RECHERCHE NAIVE 
def rech_naive(T,M):
    n = len(T) # affecter la taille du texte T a la variable n
    m = len(M) # affecter la taille du motif M a la variable m
    if n>=m : # verification si la taille du texte T est bien grande que celle du motif M
        t1 = time.perf_counter() # initialisation du compteur de temps d'execution
        i = 0 # initialisation du compteur de parcours du texte a 0
        nbr_comparaison = 0 # initialisation du compteur de nombre de comparaison a 0
        while i<n-m+1: # Parcours du texte 
            j=0 # initialisation du compteur de parcours du motif a 0
            nbr_comparaison +=1 # incrementation du compteur de comparaison par 1
            while(j<m) and (T[i+j]==M[j]): # Parcours du motif tout en verifiant si T[i+j] est egale a M[j]
                nbr_comparaison +=1 # incrementation du compteur de comparaison par 1
                j+=1 # incrementation du compteur de parcours du motif pour passer au prochain caractere
            if j==m: # verifier si le compteur j a atteint la taille du motif (motif trouve dans le texte a la position i)
                t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
                return (i, nbr_comparaison-1, t2-t1) # retourner le resultat dans la forme suivante (position, nombre de comparaison, temps d'execution)
            i+=1 # incrementation du compteur de parcours du Texte pour passer au prochain caractere ( dans le cas ou le motif n'a pas encore ete trouve)
        t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
        return (-1, nbr_comparaison-1, t2-t1) # motif introuvable, on retourne -1 a la place de la position 
    else: # Dans le cas ou la taille de T est supp de celle de M
        return (-2, 0, 0)  # ERREUR, impossible de rechercher M dans T, on retourne -2 a la place de la position


#----------------------------------------------------------------------------------------------------------------------------------------
# FONCTION QUI CALCULE LE TABLEAU DES BORDS
def tab_bords(M): 
    m = len(M) 
    bord = [] 
    bord.append(-1) 
    i = -1 
    for j in range(0, m):
        while (i>=0) and (M[i]!=M[j]): 
            i = bord[i]
        i += 1 
        bord.append(i) 
    return bord 


# FONCTION DE Morris-Pratt (MP) -- VERSION 2 --
def rech_MP_2(T, M):
    n = len(T) # affecter la taille du texte T a la variable n
    m = len(M) # affecter la taille du motif M a la variable m
    if n >= m : # verification si la taille du texte T est bien grande que celle du motif M
        t1 = time.perf_counter() # initialisation du compteur de temps d'execution 
        i = 0 # initialisation du compteur de parcours du texte a 0
        j = 0 # initialisation du compteur de parcours du motif a 0
        bord = tab_bords(M) # creation du tableau des bords du motif M en entree en utilisant la fonction definis auparavant
        nbr_comparaison = 0 # initialisation du compteur de nombre de comparaison a 0
        while i<n-m+1 : # Parcours du texte 
            while (j<m) and (T[i+j]==M[j]):  # Parcours du motif tout en verifiant si T[i+j] est egale a M[j]
                j += 1 # incrementation de j pour passer au prochain caractere
                nbr_comparaison += 1 # incrementation du compteur de comparaison par 1
            if j==m: # verifier si le compteur j a atteint la taille du motif (motif trouve dans le texte a la position i)
                t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
                return(i,nbr_comparaison, t2-t1) # retourner le resultat dans la forme suivante (position, nombre de comparaison, temps d'execution)
            i = i+j-bord[j] # decalage de la fenetre dans le texte
            nbr_comparaison += 1 # incrementation du compteur de comparaison par 1
            if bord[j] > 0: # pour ne pas tester les cararcteres de M deja testes, on verifie si le bord est supperieur a 0 (cas VRAI)
                j = bord[j]  # on memorise le bord dans la variable j afin d'eviter la repitition non necessaires de comparaisons deja effectuees
            else: # dans le cas ou le bord est -1 ou 0
                j = 0 # on remet la variable j a 0 
        t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
        return (-1, nbr_comparaison, t2-t1)  # motif introuvable, on retourne -1 a la place de la position 
    else: # Dans le cas ou la taille de T est supp de celle de M
        return (-2, 0, 0) # ERREUR, impossible de rechercher M dans T, on retourne -2 a la place de la position



#----------------------------------------------------------------------------------------------------------------------------------------
# FONCTION DES MEILLEURS BORDS
def best_bord(M):
    bestbord = []
    bestbord.append(-1)
    i = -1
    m = len(M)
    for j in range(0, m):
        while (i>=0) and (M[i] != M[j]):
            i = bestbord[i]
        i += 1
        try:
            if(i == m-1) or (M[j+1] != M[i]):
                bestbord.append(i)
            else:
                bestbord.append(bestbord[i])
        except:
            if(i == m-1) or ('' != M[i]):
                bestbord.append(i)
            else:
                bestbord.append(bestbord[i])

    return bestbord

# FONCTION DE KNUTH-MORRIS-PRATT (KMP)
def rech_KMP(T, M):
    n = len(T) # affecter la taille du texte T a la variable n
    m = len(M) # affecter la taille du motif M a la variable m
    if n >= m : # verification si la taille du texte T est bien grande que celle du motif M
        t1 = time.perf_counter() # initialisation du compteur de temps d'execution 
        i = 0 # initialisation du compteur de parcours du texte a 0
        j = 0 # initialisation du compteur de parcours du motif a 0
        bestbord = best_bord(M) # creation du tableau des bords du motif M en entree en utilisant la fonction definis auparavant
        nbr_comparaison = 0 # initialisation du compteur de nombre de comparaison a 0
        while i<n-m+1 : # Parcours du texte 
            nbr_comparaison += 1 # incrementation du compteur de comparaison par 1
            while (j<m) and (T[i+j]==M[j]):  # Parcours du motif tout en verifiant si T[i+j] est egale a M[j]
                j += 1 # incrementation de j pour passer au prochain caractere
                nbr_comparaison += 1 # incrementation du compteur de comparaison par 1
            if j==m: # verifier si le compteur j a atteint la taille du motif (motif trouve dans le texte a la position i)
                t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
                return(i,nbr_comparaison-1, t2-t1) # retourner le resultat dans la forme suivante (position, nombre de comparaison, temps d'execution)
            i = i+j-bestbord[j] # decalage de la fenetre 
            if bestbord[j] > 0: # pour ne pas tester les cararcteres de M deja testes, on verifie si le bord est supperieur a 0 (cas VRAI)
                j = bestbord[j]  # on memorise le bord dans la variable j afin d'eviter la repitition non necessaires de comparaisons deja effectuees
            else: # dans le cas ou le bord est -1 ou 0
                j = 0 # on remet la variable j a 0 
        t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
        return (-1, nbr_comparaison-1, t2-t1)  # motif introuvable, on retourne -1 a la place de la position 
    else: # Dans le cas ou la taille de T est supp de celle de M
        return (-2, 0, 0) # ERREUR, impossible de rechercher M dans T, on retourne -2 a la place de la position

#----------------------------------------------------------------------------------------------------------------------------------------
# FONCTION DE COMPARAISONS ENTRE 2 CHAINES DE MEMES TAILLES
def equal_str(t1, t2):
    i = 0 # intialisation du compteur de parcours des 2 chaines a 0
    while (i<len(t1)) and (t1[i]==t2[i]): # parcourir les 2 chaines tout en verifiant si les 2 chaines contiennent le meme caractere a la position i
        i +=1 # dans le cas ou les 2 conditions sont vraies, on passe au prochain caractere (on incremente i par 1)
    if i==len(t1): # a la sortie de la boucle, on verifie si on a atteint la fin de la chaine
        return True # dans le cas ou i egale la taille des chaines en entree, on retourne VRAI
    else:
        return False # dans le cas ou i n'est pas egale a la taille des chaines en entree, on retourne FAUX

# FONCTION DE RABIN-KARP (RK)
def rech_RK(T, M):
    n = len(T) # affecter la taille du texte T a la variable n
    m = len(M) # affecter la taille du motif M a la variable m
    if n>=m : # verification si la taille du texte T est bien grande que celle du motif M
        t1 = time.perf_counter()  # initialisation du compteur de temps d'execution
        # creation du dictionnaire 'alphabet' contenant les alphabets du texte et leur poids
        alphabet = {
            'A': 1, # l'alphabet A aura le poids 1
            'C': 2, # l'alphabet C aura le poids 2
            'G': 3, # l'alphabet G aura le poids 3
            'T': 4  # l'alphabet T aura le poids 4
        }
        prem = 273977793409 # affectation d'un nombre premier tres grand a la variable prem afin de l'utiliser au hashage de notre chaine
        hash_T = 0 # initialisation de la variable de hashage des chaines extraites du texte a 0
        hash_M = 0 # initialisation de la variable de hashage du motif M a 0
        nbr_comparaison = 0 # initialisation du compteur de nombre de comparaison a 0
        for i in range(0, m): # Boucle pour effectuer le hashage du motif M et une chaine (meme taille que M) extraites du texte T
            hash_M = (4*hash_M + alphabet[M[i]]) % prem # hashage du i eme caractere et sommer le resulatat a la variable hash_M
            hash_T = (4*hash_T + alphabet[T[i]]) % prem # hashage du i eme caractere et sommer le resulatat a la variable hash_T
        for i in range(n-m+1): # parcours du texte
            if hash_T == hash_M: # verifier si le hash code de la chaine extraites du texte qui commence a la position i est egale au hash code du motif (cas TRUE)
                if equal_str(M, T[i:i+m]): # verifier si la chaine est egale au motif ( car les erreurs au calcul du hash code sont possibles) en utilisant la fonction equal_str defini un peu plus haut dans le code
                    nbr_comparaison = nbr_comparaison + m # on increment le nombre de comparaison par le nombre de caracatere du motif M
                    t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
                    return (i, nbr_comparaison, t2-t1) # retourner le resultat dans la forme suivante (position, nombre de comparaison, temps d'execution)
            # Dans le cas ou les hash code ne sont pas egaux, on continue le traitement
            # avant de remonter en haut de boucle on :
            if i < n-m: # verifie si le nombre de caracteres restants est egale a la taille du motif M
                hash_T = (( hash_T -(alphabet[T[i]]* 4**(m-1)))*4 + alphabet[T[i+m]]) % prem # on calcule le hash code de la prochaine chaine dans le texte (on avance par 1 caractere)
                nbr_comparaison += 1 # on incremente le nombre de comparaison par 1 car on vient de lire un nouveau caractere
            else: # dans le cas ou le nombre de caracteres restants n'est pas suffisant
                t2 = time.perf_counter() # affecter le temps de fin du calcul a la variable t2
                return(-1, nbr_comparaison, t2-t1) # motif introuvable, on retourne -1 a la place de la position 
    else:  # Dans le cas ou la taille de T est supp de celle de M
        return (-2, 0, 0) # ERREUR, impossible de rechercher M dans T, on retourne -2 a la place de la position

