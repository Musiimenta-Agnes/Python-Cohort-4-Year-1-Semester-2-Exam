from app.extensions import db
from app.models.program.program_model import Program
from app.models.course.course_model import Course
from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_409_CONFLICT

# (c) Create new course
# Define the bluerints
course = Blueprint('course',__name__,url_prefix='/api/v1/course')

# Define the route
@course.route('/create_course', methods = ['POST'])
def create_course():
    data = request.json
    course_name = data.get('student_name ')
    course_instructor = data.get('course_instructor ')
    program_id = data.get('program_id')
    program = Program.query.get(program_id)

    # Verification of the details
    if not course_name  or not course_instructor or not program_id:
        return jsonify({
            'error':'All fields are required!'
        }),HTTP_400_BAD_REQUEST
    

    
        # Registering the new student
    try:
         new_data = Course(course_name=course_name,course_instructor=course_instructor,program_id=program_id,program=program)

         # Adding the new data to the database
         db.session.add(new_data)
         db.session.commit()

         # The return message
         return jsonify({
              'message': new_data.course_name + 'has successifully been created as a course',
              'course_name': new_data.course_name,
              'course_instructor': new_data.course_instructor,
              'program_id': new_data.program_id
         }),HTTP_200_OK

    except Exception as e:
         return jsonify({
              'error': str(e)
         }),HTTP_500_INTERNAL_SERVER_ERROR
    
