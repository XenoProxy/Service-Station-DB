from app import app, db
from database.models import Auto, Clients


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Auto": Auto, "Clients": Clients}

