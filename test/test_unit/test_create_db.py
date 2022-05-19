#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce script teste les fonctions de création de la base sqlite à partir
des fichiers csv contenur dans ./data
La base est créée dans data/db/tootvdb.db

@author: pstepniewski
"""

import pytest
import src.utils as ut
import os
import sqlite3
import shutil
import pytest

@pytest.fixture
def dbcon(tmp_path):
    conn = sqlite3.connect(os.path.join(tmp_path,'tootvdb.db'))
    return conn

def test_create_db_dest_folder_exists(tmp_path):
    ut.create_db(tmp_path)
    assert(os.path.exists(tmp_path))

def test_create_db_created_file_db(tmp_path):
    ut.create_db(tmp_path)
    assert(os.path.isfile(os.path.join(tmp_path,"tootvdb.db")))
    
def test_create_table_visits_from_csv_file_table_created(dbcon):
    table_name = "too_visites_minute"
    csv_file_path = "data/visites_minutes.csv"
    ut.create_table_visits_from_csv_file(dbcon,table_name,csv_file_path)
    
    dbcur = dbcon.cursor()
    dbcur.execute("""SELECT name from sqlite_master 
                  WHERE type = "table" AND name = "too_visites_minute" """)
    assert(dbcur.fetchone() is not None)
    dbcur.close()
    
def test_create_table_spots_from_csv_file_table_created(dbcon):
    table_name = "too_spots_infos"
    csv_file_path = "data/too_spots_infos.csv"
    ut.create_table_spots_from_csv_file(dbcon,table_name,csv_file_path)
    
    dbcur = dbcon.cursor()
    dbcur.execute("""SELECT name from sqlite_master 
                  WHERE type = "table" AND name = "too_spots_infos" """)
    assert(dbcur.fetchone() is not None)
    dbcur.close()
  
    

