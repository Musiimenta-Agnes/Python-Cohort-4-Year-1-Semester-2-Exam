from app.extensions import db
from app.models.program.program_model import Program
from app.models.student.student_model import Student
from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_409_CONFLICT
import validators

#(b) Create a new student

# Define the bluerints
student = Blueprint('student',__name__,url_prefix='/api/v1/student')

# Define the route
@student.route('/create_student', methods = ['POST'])
def create_student():
    data = request.json
    student_name = data.get('student_name ')
    student_email = data.get('student_email ')
    password = data.get('password ')
    student_contact = data.get('student_contact ')
    program_id = data.get('program_id')
    program = Program.query.get(program_id)

    # Verification of the details
    if not student_name or not student_email or not password or not student_contact:
        return jsonify({
            'error':'All fields are required!'
        }),HTTP_400_BAD_REQUEST
    
    # Validating the email
    if not validators.email(student_email):
         return jsonify({
            'error':'Invalid email!'
        }),HTTP_400_BAD_REQUEST
    
    # Checking for data consistency
    if Student.query.filter_by(student_email = student_email) is not None:
         return jsonify({
            'error':'The email is already in use!'
        }),HTTP_409_CONFLICT
    
    if Student.query.filter_by(student_contact = student_contact) is not None:
         return jsonify({
            'error':'The phone number is already in use!'
        }),HTTP_409_CONFLICT
    
    # Checking for the password length
    if len(password) < 5:
          return jsonify({
            'error':'Password is too short!'
        }),HTTP_409_CONFLICT
         

    # Registering the new student
    try:
         new_data = Student(student_name=student_name, student_email=student_email, password=password,student_contact=student_contact,program_id=program_id,program=program)

         # Adding the new data to the database
         db.session.add(new_data)
         db.session.commit()

         # The return message
         return jsonify({
              'message': new_data.student_name + 'has successifully been created as student',
              'student_name': new_data.student_name,
              'student_email': new_data.student_email,
              'password': new_data.password,
              'student_contact': new_data.student_contact,
              'program_id': new_data.program_id
         }),HTTP_200_OK

    except Exception as e:
         return jsonify({
              'error': str(e)
         }),HTTP_500_INTERNAL_SERVER_ERROR






# (d) Getting all stdents
@student.route('/get', methods = ['GET'])
def get_all_student():
     all_studetnts = Student.query.all()
     student_data = []

     for student in all_studetnts:
          student_information = {
              'student_name': student.student_name,
              'student_email':student.student_email,
              'password': student.password,
              'student_contact': student.student_contact,
            #   'program_id': student.program_id
          }

          student_data.append(student_information)

          # The return message

     return jsonify({
              'message': 'All students have successifully been retrieved',
              'Total': len(student_data),
              'Students': student_data
             
         }),HTTP_200_OK





# (e) Delete a student
@student.route('/delete/<int:student_id>', methods = ['DELETE'])
def delete_student(student_id):
     try:
          student = Student.query.filter_by(student_id = student_id).first()
          if not student:
            return jsonify({
                'error': 'This student does not exist!'
            }),HTTP_404_NOT_FOUND
          
          else:
               db.session.delete(student)
          
          # The return message
               return jsonify({
                    'message': 'The student has been successifully deleted',    
                }),HTTP_200_OK

          

     except Exception as e:
          return jsonify({
               'error': str(e)
          }),HTTP_500_INTERNAL_SERVER_ERROR



