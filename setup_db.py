import sqlite3
import os

# Optional: Delete the old database file if it was created in a broken state
if os.path.exists('factory_data.db'):
    os.remove('factory_data.db')

conn = sqlite3.connect('factory_data.db')
cursor = conn.cursor()

# Create a table for manufacturing assembly data
cursor.execute('''
CREATE TABLE IF NOT EXISTS assembly_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id TEXT,
    process_type TEXT,
    torque_value REAL,
    status TEXT,
    timestamp TEXT
)
''')

# Insert some dummy data (Notice we only provide 5 values now)
dummy_data = [
    ('MCH-01', 'fastening', 45.2, 'OK', '2026-10-05 08:00:00'),
    ('MCH-01', 'fastening', 32.1, 'ERROR', '2026-10-05 08:15:00'), # Anomaly!
    ('MCH-02', 'assembly', 46.0, 'OK', '2026-10-05 09:00:00'),
]

# FIX: Explicitly state which columns we are inserting into. 
# SQLite will automatically handle the 'id' column.
cursor.executemany('''
    INSERT INTO assembly_logs (machine_id, process_type, torque_value, status, timestamp) 
    VALUES (?,?,?,?,?)
''', dummy_data)

conn.commit()
conn.close()
print("Database created successfully!")