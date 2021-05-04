import pandas as pd 
import numpy as np 
import Algo_recherche_1motif as algo_first # importation du fichier des fonctions qui cherchent la 1ere occuerence
# import Algo_recherche_occ_motif as algo_occ # importation du fichier des fonctions qui cherchent plusieurs occurences
import time 

t1 = time.perf_counter()
# create excel writer object
writer = pd.ExcelWriter('first_motif.xlsx')

                                                      # TABLES DU NOMBRE DE COMAPRAISONS

# CREATION DES TABLES DU NOMBRE DE COMPARAISONS QUAND LA TAILLE DU TEXTE EST FIXE
columns = ['ALGO_NAIF', 'ALGO_MP', 'ALGO_KMP', 'ALGO_RK']
indexes = ['2', '4', '8', '20', '30', '50', '100']
liste_taille_texte = [100, 500, 1000, 2000, 5000, 10000, 1000000]
df1 = pd.DataFrame(0, index=indexes, columns=columns)
name = 'COMPARAISONS_TEXTE'
liste=[]
for i in liste_taille_texte:
    df = pd.DataFrame(0, index=indexes, columns=columns)
    for idx in indexes:
        moyenne_naif=0
        moyenne_MP=0
        moyenne_KMP=0
        moyenne_RK=0
        for nbr in range(0, 100):
            # Generation du texte et du motif
            T = algo_first.generer_texte(i)
            M = algo_first.generer_motif(int(idx))
            # resultat pour algo naif
            res = algo_first.rech_naive(T, M)
            moyenne_naif += res[1]
            # resultat pour algo MP
            res = algo_first.rech_MP_2(T, M)
            moyenne_MP += res[1]
            # resultat pour algo KMP
            res = algo_first.rech_KMP(T, M)
            moyenne_KMP += res[1]
            # resultat pour algo RK
            res = algo_first.rech_RK(T, M)
            moyenne_RK += res[1]
        # remplissage de chaque colonne avec la moyenne obtenue par son algorithme
        df.at[idx, 'ALGO_NAIF'] = moyenne_naif/100
        df.at[idx, 'ALGO_MP'] = moyenne_MP/100
        df.at[idx, 'ALGO_KMP'] = moyenne_KMP/100
        df.at[idx, 'ALGO_RK'] = moyenne_RK/100
    liste.append(df)
df1 = pd.concat(liste, keys=[100, 500, 1000, 2000, 5000, 10000, 1000000])
# write dataframe to excel
df1.to_excel(writer, name)
# save the excel
writer.save()
#----------------------------------------------------------------------------------------------------------------------------------------
# CREATION DES TABLES DU NOMBRE DE COMPARAISONS QUAND LA TAILLE DU MOTIF EST FIXE
columns = ['ALGO_NAIF', 'ALGO_MP', 'ALGO_KMP', 'ALGO_RK']
indexes = ['100', '500', '1000', '2000', '5000', '10000', '1000000']
liste_taille_motif = [2, 4, 8, 20, 30, 50, 100]
df1 = pd.DataFrame(0, index=indexes, columns=columns)
name = 'COMPARAISONS_MOTIF'
liste=[]
for i in liste_taille_motif:
    df = pd.DataFrame(0, index=indexes, columns=columns)
    for idx in indexes:
        moyenne_naif=0
        moyenne_MP=0
        moyenne_KMP=0
        moyenne_RK=0
        for nbr in range(0, 100):
            # Generation du texte et du motif
            T = algo_first.generer_texte(int(idx))
            M = algo_first.generer_motif(i)
            # resultat pour algo naif
            res = algo_first.rech_naive(T, M)
            moyenne_naif += res[1]
            # resultat pour algo MP
            res = algo_first.rech_MP_2(T, M)
            moyenne_MP += res[1]
            # resultat pour algo KMP
            res = algo_first.rech_KMP(T, M)
            moyenne_KMP += res[1]
            # resultat pour algo RK
            res = algo_first.rech_RK(T, M)
            moyenne_RK += res[1]
        # remplissage de chaque colonne avec la moyenne obtenue par son algorithme
        df.at[idx, 'ALGO_NAIF'] = moyenne_naif/100
        df.at[idx, 'ALGO_MP'] = moyenne_MP/100
        df.at[idx, 'ALGO_KMP'] = moyenne_KMP/100
        df.at[idx, 'ALGO_RK'] = moyenne_RK/100
    liste.append(df)
df1 = pd.concat(liste, keys=[2, 4, 8, 20, 30, 50, 100])
# write dataframe to excel
df1.to_excel(writer, name)
# save the excel
writer.save()

#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
                                                    # TABLES DU TEMPS D'EXECUTION

# CREATION DES TABLES DU TEMPS D'EXECUTION QUAND LA TAILLE DU TEXTE EST FIXE
columns = ['ALGO_NAIF', 'ALGO_MP', 'ALGO_KMP', 'ALGO_RK']
indexes = ['2', '4', '8', '20', '30', '50', '100']
liste_taille_texte = [100, 500, 1000, 2000, 5000, 10000, 1000000]
df1 = pd.DataFrame(0.00, index=indexes, columns=columns)
name = 'TEMPS_TEXTE'
liste=[]
for i in liste_taille_texte:
    df = pd.DataFrame(0.00, index=indexes, columns=columns)
    for idx in indexes:
        moyenne_naif=0
        moyenne_MP=0
        moyenne_KMP=0
        moyenne_RK=0
        for nbr in range(0, 100):
            # Generation du texte et du motif
            T = algo_first.generer_texte(i)
            M = algo_first.generer_motif(int(idx))
            # resultat pour algo naif
            res = algo_first.rech_naive(T, M)
            moyenne_naif += res[2]
            # resultat pour algo MP
            res = algo_first.rech_MP_2(T, M)
            moyenne_MP += res[2]
            # resultat pour algo KMP
            res = algo_first.rech_KMP(T, M)
            moyenne_KMP += res[2]
            # resultat pour algo RK
            res = algo_first.rech_RK(T, M)
            moyenne_RK += res[2]
        # remplissage de chaque colonne avec la moyenne obtenue par son algorithme
        df.at[idx, 'ALGO_NAIF'] = round(moyenne_naif/100, 8)
        df.at[idx, 'ALGO_MP'] = round(moyenne_MP/100, 8)
        df.at[idx, 'ALGO_KMP'] = round(moyenne_KMP/100, 8)
        df.at[idx, 'ALGO_RK'] = round(moyenne_RK/100, 8)
    liste.append(df)
df1 = pd.concat(liste, keys=[100, 500, 1000, 2000, 5000, 10000, 1000000])
# write dataframe to excel
df1.to_excel(writer, name)
# save the excel
writer.save()
#----------------------------------------------------------------------------------------------------------------------------------------
# CREATION DES TABLES DU TEMPS D'EXECUTION QUAND LA TAILLE DU MOTIF EST FIXE
columns = ['ALGO_NAIF', 'ALGO_MP', 'ALGO_KMP', 'ALGO_RK']
indexes = ['100', '500', '1000', '2000', '5000', '10000', '1000000']
liste_taille_motif = [2, 4, 8, 20, 30, 50, 100]
df1 = pd.DataFrame(0.00, index=indexes, columns=columns)
name = 'TEMPS_MOTIF'
liste=[]
for i in liste_taille_motif:
    df = pd.DataFrame(0.00, index=indexes, columns=columns)
    for idx in indexes:
        moyenne_naif=0
        moyenne_MP=0
        moyenne_KMP=0
        moyenne_RK=0
        for nbr in range(0, 100):
            # Generation du texte et du motif
            T = algo_first.generer_texte(int(idx))
            M = algo_first.generer_motif(i)
            # resultat pour algo naif
            res = algo_first.rech_naive(T, M)
            moyenne_naif += res[2]
            # resultat pour algo MP
            res = algo_first.rech_MP_2(T, M)
            moyenne_MP += res[2]
            # resultat pour algo KMP
            res = algo_first.rech_KMP(T, M)
            moyenne_KMP += res[2]
            # resultat pour algo RK
            res = algo_first.rech_RK(T, M)
            moyenne_RK += res[2]
        # remplissage de chaque colonne avec la moyenne obtenue par son algorithme
        df.at[idx, 'ALGO_NAIF'] = round(moyenne_naif/100, 8)
        df.at[idx, 'ALGO_MP'] = round(moyenne_MP/100, 8)
        df.at[idx, 'ALGO_KMP'] = round(moyenne_KMP/100, 8)
        df.at[idx, 'ALGO_RK'] = round(moyenne_RK/100, 8)
    liste.append(df)
df1 = pd.concat(liste, keys=[2, 4, 8, 20, 30, 50, 100])
# write dataframe to excel
df1.to_excel(writer, name)
# save the excel
writer.save()



#----------------------------------------TEMPS D'EXECUTION DE CE PROGRAMME--------------------------------------------------
t2 = time.perf_counter()
print('EXECUTION TIME : ', t2-t1)