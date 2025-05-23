from app.extensions import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'Courses'


    course_id = db.Column(db.String(255), nullable = False, primary_key = True, unique = True)
    course_name = db.Column(db.String(255), nullable = False)
    course_instructor = db.Column(db.String(255), nullable = False)
    program_id = db.Column(db.String(255), nullable = False, foreign_key = True)
    created_at = db.Column(db.DateTime, default = datetime.now())   # This is a time stamp
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def __init__(self, course_name,course_instructor,program_id):
        self.course_name = course_name
        self.course_instructor = course_instructor
        self.program_id = program_id
       