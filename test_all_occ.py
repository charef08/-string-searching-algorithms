import Algo_recherche_occ_motif as algo_occ # importation du fichier des fonctions qui cherchent plusieurs occurences

T = algo_occ.generer_texte(1000)
M = algo_occ.generer_motif(4)
# T='ATCATATGATATATAGATC'
# M='AT'

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
print('RESULTATS DE RECHERCHE DES OCCURENCES D\'UN MOTIF M DANS UN TEXTE T AVEC LES ALGOS NAIF, MP, KMP ET RK : \n ')

# test de la fonction de l'algorithme naif et affichage des resultats
print("RECHERCHE AVEC L'ALGORITHME NAIF (Toutes les occurences de M en T )  :  \n") 
res_NV2 = algo_occ.rech_naive2(T, M)
if res_NV2[0][0] > -1:
    print('Le nombre de comparaison est :'+str(res_NV2[1])+'\n\
La position de la chaine M dans T est : '+str(res_NV2[0])+'\n\
le temps d\'execution est de : '+str(res_NV2[2]))
else:
    if res_RK[0][0] == -1 :
        print('La chaine M est introuvable dans T\n\
et le nombre de comparaison est de : ', str(res_NV2[1])+' \n\
Avec un temps d\'execution de : '+ str(res_NV2[2]))
    else:
        print("LA TAILLE DE LA SOUS-CHAINE M DOIT ETRE INFERIEUR A LA TAILLE DU TEXTE T")

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Morris-Pratt et affichage des resultats
print("RECHERCHE AVEC L'ALGORITHME MORRIS-PRATT (VERSION 2) :  \n") 
res_MP_2 = algo_occ.rech_MP_2(T,M)
if res_MP_2[0][0] > -1:
    print('Le nombre de comparaison est :'+str(res_MP_2[1])+'\n\
La position de la chaine M dans T est : '+str(res_MP_2[0])+'\n\
le temps d\'execution est de : '+str(res_MP_2[2]))
else:
    if res_RK[0][0] == -1 :
        print('La chaine M est introuvable dans T\n\
et le nombre de comparaison est de : ', str(res_MP_2[1])+' \n\
Avec un temps d\'execution de : '+ str(res_MP_2[2]))
    else:
        print("LA TAILLE DE LA SOUS-CHAINE M DOIT ETRE INFERIEUR A LA TAILLE DU TEXTE T")

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Knuth-Morris-Pratt et affichage des resultats
print("RECHERCHE AVEC L'ALGORITHME KNUTH-MORRIS-PRATT")      
res_kmp = algo_occ.rech_KMP(T, M)
if res_kmp[0][0] > -1:
    print('Le nombre de comparaison est :'+str(res_kmp[1])+'\n\
La position de la chaine M dans T est : '+str(res_kmp[0])+'\n\
le temps d\'execution est de : '+str(res_kmp[2]))
else:
    if res_RK[0][0] == -1 :
        print('La chaine M est introuvable dans T\n\
et le nombre de comparaison est de : ', str(res_kmp[1])+' \n\
Avec un temps d\'execution de : '+ str(res_kmp[2]))
    else:
        print("LA TAILLE DE LA SOUS-CHAINE M DOIT ETRE INFERIEUR A LA TAILLE DU TEXTE T")

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Robin-Karp et affichage des resultats
print("RECHERCHE AVEC L'ALGORITHME DE ROBIN-KARP : \n")
res_RK = algo_occ.rech_RK(T, M)
if res_RK[0][0] > -1 :
    print('Le Nombre de comparaison est : '+str(res_RK[1])+'\n\
La position de la chaine M dans le texte T est : '+ str(res_RK[0])+' \n\
Avec un temps d\'execution de : '+ str(res_RK[2])) 
else:
    if res_RK[0][0] == -1 :
        print('La chaine M est introuvable dans T\n \
et le nombre de comparaison est de : ', str(res_RK[1])+' \n\
Avec un temps d\'execution de : '+ str(res_RK[2]))
    else:
        print("LA TAILLE DE LA SOUS-CHAINE M DOIT ETRE INFERIEUR A LA TAILLE DU TEXTE T")


print('\n \n')