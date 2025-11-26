import sqlite3
from typing import List, Tuple
from models.athlete import  Athlete

def create_database():
    return sqlite3.connect("training.db")

def create_athlete_table():
    conn=create_database()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS athlete(
            id_number INTEGER PRIMARY KEY,
            profile BLOB,
            name TEXT NOT NULL,
            martial_arts TEXT,
            current_weight REAL,
            category TEXT,
            competition_per_month INTEGER,
            private_coaching_hours INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_athlete(athlete):
    conn = sqlite3.connect("training.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO athlete(
                            id_number, 
                            profile, 
                            name, 
                            martial_arts, 
                            current_weight, 
                            category, 
                            competition_per_month, 
                            private_coaching_hours
                            ) 
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
            athlete.id_number,
            athlete.profile,
            athlete.name,
            athlete.martial_arts,
            athlete.current_weight, 
            athlete.category,
            athlete.competition_per_month,
            athlete.private_coaching_hours
            )
    
    )
    conn.commit()
    conn.close()

def get_all_athletes():
    conn = sqlite3.connect("training.db")
    c = conn.cursor()
    c.execute("SELECT * FROM athlete")
    data = c.fetchall()
    conn.close()
    return data