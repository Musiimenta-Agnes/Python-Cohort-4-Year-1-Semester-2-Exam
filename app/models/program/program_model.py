from datetime import datetime
from app.extensions import db

class Program(db.Model):
    __tablename__ = 'Programs'

    program_id = db.Column(db.String(255), nullable = False, primary_key = True, unique = True)
    program_name = db.Column(db.String(255), nullable = False)
    program_address = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now())   # This is a time stamp
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def __init__(self, program_name, program_address):
        self.name = program_name
        self.program_address = program_address
      
     
        