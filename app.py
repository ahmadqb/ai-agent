from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    machine_id: str

def get_db_connection():
    return sqlite3.connect('factory_data.db')

@app.get("/api/machine_status")
def get_machine_status(machine_id: str):
    """Fetches recent assembly logs for a specific machine."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assembly_logs WHERE machine_id = ? ORDER BY timestamp DESC LIMIT 5", (machine_id,))
    rows = cursor.fetchall()
    conn.close()


@app.get("/api/all_machines")
def get_all_machines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT machine_id FROM assembly_logs")
    machines = [row[0] for row in cursor.fetchall()]
    conn.close()
    return machines

@app.get("/api/errors")
def get_errors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assembly_logs WHERE status = 'ERROR'")
    rows = cursor.fetchall()
    conn.close()
    return [{"machine": r[1], "torque": r[3], "time": r[5]} for r in rows]
    
    # Format as list of dicts for the LLM to read easily
    return [{"id": r[0], "machine": r[1], "process": r[2], "torque": r[3], "status": r[4], "time": r[5]} for r in rows]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)