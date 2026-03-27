import sqlite3
import os

def fetch_lxc_parameters():
    db_path = os.path.join(os.getcwd(), 'lxc_deploy.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT memory, network, disks, containername FROM `lxc to deploy`')
    rows = cursor.fetchall()
    conn.close()
    return [{'memory': row[0], 'network': row[1], 'disks': row[2], 'containername': row[3]} for row in rows]