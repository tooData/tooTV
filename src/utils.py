#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:27:11 2022

@author: pstepniewski
"""

import sqlite3
from sqlite3 import Error
import os
import shutil
import pandas as pd


def create_db(dir_file_db):
    """ create a database connection to a SQLite database """
    
    if(os.path.isdir(dir_file_db)):        
        shutil.rmtree(dir_file_db)
    os.mkdir(dir_file_db)   
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(dir_file_db,"tootvdb.db"))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
def create_table_visits_from_csv_file(dbcon,table_name,csv_file_path):
    data = pd.read_csv(csv_file_path)
    data.to_sql(table_name,dbcon,if_exists="replace",index = False)
    
def create_table_spots_from_csv_file(dbcon,table_name,csv_file_path):
    data = pd.read_csv(csv_file_path)
    data.to_sql(table_name,dbcon,if_exists="replace",index = False)
    
def create_work_db():
    create_db('data/db')
    conn = sqlite3.connect('data/db/tootvdb.db')
    create_table_visits_from_csv_file(conn,"too_visites_minute","data/visites_minutes.csv")
    create_table_spots_from_csv_file(conn,"too_spots_infos","data/too_spots_infos.csv")