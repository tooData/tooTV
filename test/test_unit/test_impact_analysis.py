#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce fichier teste les fonctions de test_impact_analysis sur des cas fictifs
Cela vous permet de voir les résultats attendus, surtout au niveau du format
Les chiffres utilisées ici sont fictifs. 
Pour les fonctions sur l'incrément, il s'agit de tranche d'incrément éspéré pour 
le cas de spot fictif de la fixture visites()

@author: pstepniewski
"""
import pytest
import pandas as pd
import src.impact_analysis as ia
import numpy as np

@pytest.fixture
def visites():
    visites = pd.read_csv("test/test_unit/data/test_visites_spikes.csv")
    return visites
    

@pytest.fixture
def date_spots_list():
    date_spots_list = ["2022-05-06 16:24:00",
                        "2022-05-05 19:44:00",
                        "2022-05-05 16:56:00",
                        "2022-05-05 12:25:00",
                        "2022-05-04 20:07:00",
                        "2022-05-04 19:21:00",
                        "2022-05-04 16:24:00",
                        "2022-05-03 16:23:00",
                        "2022-05-03 15:47:00",
                        "2022-05-02 19:41:00",
                        "2022-05-02 19:12:00",
                        "2022-05-02 14:39:00",
                        "2022-04-26 19:44:00",
                        "2022-04-20 21:31:00"] 
    return date_spots_list
    

def test_compute_date_spike_is_highest_minus_one(visites):
    date_spike = ia.compute_date_spike(visites)
    assert(date_spike == "2022-05-06 16:26")
    
    
def test_compute_increment_5_is_between_100_and_200(visites):
    increment = ia.compute_increment(visites,"2022-05-06 16:26",5)
    assert(100 <= increment <= 200)
    
    
def test_compute_increment_10_is_between_100_and_200(visites):
    increment = ia.compute_increment(visites,"2022-05-06 16:26",10)
    assert(100 <= increment <= 200)
    
    
def test_compute_increment_for_all_spots_returns_df_14_rows(date_spots_list):
    res = ia.compute_increment_for_all_spots(date_spots_list)
    expected_columns =  ["date_diffusion","date_spike","increment_5_min",
                         "increment_10_min","tarif_net_fo","cout_par_visite"]
    assert(isinstance(res, pd.DataFrame))
    assert len(res.columns) == len(expected_columns)
    assert all([a == b for a, b in zip(res.columns, expected_columns)])
    assert(len(res) == 14)
    #vérifie que le dataframe contient les bonnes colonnes

def test_compute_campaign_stats_returns_df_1_row():
    expected_columns = ["nombre de spots",
                        "increment_5_min_total",
                        "increment_10_min_total",
                        "cout_campagne_total",
                        "cout_par_visite_supplementaire"]
    
    test_df = pd.DataFrame({"date_diffusion":"2022-04-26 19:44:00","date_spike":"2022-04-26 19:44:00",
               "increment_5_min": [50], "increment_10_min":[56],
               "tarif_net_fo":[3000],"cout_par_visite":[50]})
    
    res = ia.compute_campaign_stats(test_df)
    assert(isinstance(res, pd.DataFrame))
    assert(len(res) == 1)
    assert len(res.columns) == len(expected_columns)
    assert all([a == b for a, b in zip(res.columns, expected_columns)])
