#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:27:23 2022

@author: pstepniewski
"""

import pandas as pd
import itertools
import sqlite3

def sql_help_example():
    """
    Fonction démo de connexion et requête sur sqllite
    si jamais vous êtes perdus
    
    Returns
    -------
    None.

    """    
    conn = sqlite3.connect('data/db/tootvdb.db')
    dbcur = conn.cursor()
    dbcur.execute("""SELECT * 
                      FROM too_spots_infos""")
    res = dbcur.fetchall()
    print(res)
    #renvoie le contenu de la table too_spots_infos

def compute_date_spike(df_visites):
    """
    Cette fonction prend en entrée les visites pour un spot données à +ou- 20 minutes
    autour de sa date de diffusion annoncée et retourne la minute précédent le pic de visites

    voir le test test_impact_analysis.test_compute_date_spike_is_highest_minus_one
    Parameters
    ----------
    df_visites : pandas.DataFrame
        Les visites extraites de la base sql à - et + 20 minutes autour du spot

    Returns
    -------
    str
        la date précédent de le pic de visites

    """
    #fake_date_spike juste pour passer les test unitaire. Remplacez le par votre code
    fake_date_spike = "2022-05-06 16:26"
    return fake_date_spike


def compute_increment(df_visites,date_spike,effect_duration):
    """
    Cette fonction prend en entrée les visites, une date de pic, une durée 
    d'effet (5 ou 10 min) et retourne un entier représentant le nombre de visites 
    supplémentaires générée par le spot sur cette durée d'effet après le pic du spot

    Parameters
    ----------
    df_visites : pandas.DataFrame
        Les visites extraites de la base sql à - et + 20 minutes autour du spot
    duree_effet : int
        durée de l'effet en minutes après le pic du spot

    Returns
    -------
    int
    l'estimation de l'incrément de visiteurs    

    """
    #fake_increment juste pour passer les test unitaire. Remplacez le par votre code
    fake_increment = 120
    return fake_increment


def compute_increment_for_all_spots(date_spots_list):
    """
    Cette fonction prend en entrée la liste des dates de tous les 14 spots dispo
    dans la table too_spots_infos.
    
    Pour chaque spots elle effectue les étapes suviantes:
        - récupère en SQL pour chaque spot, son tarif_net_fo dans la table too_spots_info
        - récupère en SQL pour chaque spot, les visites à +- 20 min autour (df_visites)
        - calcule la date du pic avec compute_date_spike
        - calcule de l'incrément d'audience avec compute_increment et la date_spike 
        trouvée plus haut
        - calcule le cout par visite supplémentaire à partir du tarif_net_fo
    
    Elle retourne un dataFrame ayant pour colonnes:
        [date_diffusion,date_spike,increment_5_min,increment_10_min,tarif_net_fo,cout_par_visite]
    Parameters
    ----------
    spot_dates_list : list
        liste de date de diffusion des spots (récupérée dans too_spots_info)

    Returns
    -------
    pandas.Dataframe

    """
    #fakedf juste pour passer les test unitaire. Remplacez le par votre code
    fake_df = pd.DataFrame({"date_diffusion":itertools.repeat("2022-04-26 19:44:00",14),
                            "date_spike":itertools.repeat("2022-04-26 19:44:00",14),
                            "increment_5_min": itertools.repeat(50,14),
                            "increment_10_min":itertools.repeat(56,14),
                            "tarif_net_fo":itertools.repeat(3000,14),
                            "cout_par_visite":itertools.repeat(50,14)})
    
    return fake_df


def compute_campaign_stats(increment_price_df):
    """
    Cette fonction prend en entrée le dataframe renvoyé par compute_increment_for_all_spots
    et calcule le total d'incrément d'audience à 5 et 10 min pour la campagne pub
    ,le cout total et le cout par visite supplémentaire calculé sur tous les spots

    Parameters
    ----------
    increment_price_df : pandas.DataFrame
        le information d'incrément au spot, rénvoyés par la fonction précédente

    Returns
    -------
    pandas.DataFrame
    les statistiques résumant la campagne (une ligne) avec les colonnes suivantes
    [nombre de spots,increment_5_min_total,increment_10_min_total
     ,cout_campagne_total,cout_par_visite_supplementaire]

    """
    
    #fakedf juste pour passer les test unitaire. Remplacez le par votre code
    fake_df = pd.DataFrame({"nombre de spots":[1],
                        "increment_5_min_total":[0],
                        "increment_10_min_total":[0],
                        "cout_campagne_total":[0],
                        "cout_par_visite_supplementaire":[0]})
    
    return fake_df


