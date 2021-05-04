import Algo_recherche_1motif as algo_first # importation du fichier des fonctions qui cherchent la 1ere occuerence

T = algo_first.generer_texte(1000)
M = algo_first.generer_motif(4)
# T='ATCATATGATATATAGATC'
# M='AT'

print('----------------------------------------------------------------------------------------------------------------------------- \n')
print('RESULTATS DE RECHERCHE DE LA 1ERE APPARITION D\'UN MOTIF M DANS UN TEXTE T AVEC LES ALGOS NAIF, MP, KMP ET RK : \n ')

# test de la fonction de l'algorithme naif et affichage des resultats
res_NV = algo_first.rech_naive(T,M)
print("RECHERCHE AVEC L'ALGORITHME NAIF :  \n") 
if res_NV[0] > -1 :
    print('Le Nombre de comparaison est : '+str(res_NV[1])+'\n\
La position de la chaine M dans le texte T est : '+ str(res_NV[0])+' \n\
Avec un temps d\'execution de : '+ str(res_NV[2])) 
else:
    print('La chaine M est introuvable dans T\n \
et le nombre de comparaison est de : ', str(res_NV[1])+' \n\
Avec un temps d\'execution de : '+ str(res_NV[2])) 

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Morris-Pratt et affichage des resultats
res_MP_2 = algo_first.rech_MP_2(T,M)
print("RECHERCHE AVEC L'ALGORITHME MORRIS-PRATT (VERSION 2) :  \n") 
if res_MP_2[0] > -1 :
    print('Le Nombre de comparaison est : '+str(res_MP_2[1])+'\n\
La position de la chaine M dans le texte T est : '+ str(res_MP_2[0])+' \n\
Avec un temps d\'execution de : '+ str(res_MP_2[2])) 
else:
    print('La chaine M est introuvable dans T\n \
et le nombre de comparaison est de : ', str(res_MP_2[1])+' \n\
Avec un temps d\'execution de : '+ str(res_MP_2[2]))

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Knuth-Morris-Pratt et affichage des resultats
res_kmp = algo_first.rech_KMP(T, M)
print("RECHERCHE AVEC L'ALGORITHME KNUTH-MORRIS-PRATT : \n")
if res_kmp[0] > -1 :
    print('Le Nombre de comparaison est : '+str(res_kmp[1])+'\n\
La position de la chaine M dans le texte T est : '+ str(res_kmp[0])+' \n\
Avec un temps d\'execution de : '+ str(res_kmp[2])) 
else:
    print('La chaine M est introuvable dans T\n \
et le nombre de comparaison est de : ', str(res_kmp[1])+' \n\
Avec un temps d\'execution de : '+ str(res_kmp[2]))

print('\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# test de la fonction de l'algorithme Robin-Karp et affichage des resultats
res_RK = algo_first.rech_RK(T, M)
print("RECHERCHE AVEC L'ALGORITHME DE ROBIN-KARP : \n")
if res_RK[0] > -1 :
    print('Le Nombre de comparaison est : '+str(res_RK[1])+'\n\
La position de la chaine M dans le texte T est : '+ str(res_RK[0])+' \n\
Avec un temps d\'execution de : '+ str(res_RK[2])) 
else:
    print('La chaine M est introuvable dans T\n \
et le nombre de comparaison est de : ', str(res_RK[1])+' \n\
Avec un temps d\'execution de : '+ str(res_RK[2]))

print('\n \n')