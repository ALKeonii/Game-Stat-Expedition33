import sqlite3
from models import GameStat

DB_NAME = "game_stats.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            party_name TEXT NOT NULL,
            favorite_character TEXT,
            achievements INTEGER,
            time_played TEXT,
            levels_reached INTEGER
        )
    """)
    conn.commit()
    conn.close()

def create_game_stat(stat: GameStat):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO game_stats (party_name, favorite_character, achievements, time_played, levels_reached)
        VALUES (?, ?, ?, ?, ?)
    """, (stat.party_name, stat.favorite_character, stat.achievements, stat.time_played, stat.levels_reached))
    conn.commit()
    conn.close()

def read_all_game_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_stats")
    rows = cursor.fetchall()
    conn.close()
    return [GameStat(*row) for row in rows]

def update_game_stat(stat: GameStat):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE game_stats
        SET party_name=?, favorite_character=?, achievements=?, time_played=?, levels_reached=?
        WHERE id=?
    """, (stat.party_name, stat.favorite_character, stat.achievements, stat.time_played, stat.levels_reached, stat.id))
    conn.commit()
    conn.close()

def delete_game_stat(stat_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM game_stats WHERE id=?", (stat_id,))
    conn.commit()
    conn.close()