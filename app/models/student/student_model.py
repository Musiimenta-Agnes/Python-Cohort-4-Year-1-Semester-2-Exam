from app.extensions import db
from datetime import datetime


class Student(db.Model):
    __tablename__ = 'Students'

    student_id = db.Column(db.String(255), nullable = False, primary_key = True, unique = True)
    student_contact = db.Column(db.String(255), nullable = False)
    student_name = db.Column(db.String(255), nullable = False)
    student_email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    program_id = db.Column(db.String(255),db.ForeignKey('programs.program_id'))
    program = db.relationship('Program',backref = 'students')
    created_at = db.Column(db.DateTime, default = datetime.now())   # This is a time stamp
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def __init__(self, student_name,student_contact,student_email, password,program_id):
        self.student_name = student_name
        self.student_contact = student_contact
        self.student_email = student_email
        self.password = password
        self.program_id = program_id


       