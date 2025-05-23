from app.extensions import db
from app.models.program.program_model import Program
from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_500_INTERNAL_SERVER_ERROR


# (a) Question 1
 #Define the Blue Print
program = Blueprint('program',__name__,url_prefix='/api/v1/program')

# Define the route
@program.route('/create', methods = ['POST'])

# Function to create program
def create_program():
    data = request.json
    program_name= data.get('program_name')
    program_address = data.get('program_address')
    created_at = data.get('created_at')
    updated_at = data.get('updated _at')


    # verifying the details
    if not program_name or not program_address:
        return jsonify({
            'error': 'All fields are required!'
        }),HTTP_400_BAD_REQUEST
    
    # Creating the  new program 
    new_program = Program(program_name=program_name,program_address=program_address)

    # Adding thenew program to the database
    db.session.add(new_program)
    db.session.commit()

    # The return message
    return jsonify({
        'message': new_program.program_name + 'has successufully been created',
        'program_name': new_program.program_name,
        'program_address': new_program.program_address,
        'created_at': new_program.created_at,
        'updated_at': new_program.updated_at
        

    }),HTTP_200_OK



# (b) Update programs by id

# Define the route
@program.route('/edit/<int:program_id>', methods = ['PUT'])
def update_program(program_id):
    program = Program.query.filter_by(program_id = program_id).first()

    try:
        # Checking whether the program exists
        if not program:
            return jsonify({
                'error': 'This program does not exist!'
            }),HTTP_404_NOT_FOUND
        
        else:
            program_name = request.get_json().get('program_name', program.program_name)
            program_address = request.get_json().get('program_address', program.program_address)
            created_at = request.get_json().get('created_at', program.created_at)
            updated_at= request.get_json().get('updated_at', program.updated_at)

            # Updating the data
            program.program_name = program_name
            program.program_address = program_address
            program.created_at = created_at
            program.updated_at = updated_at

            # Commiting the updated data
            db.session.commit()

            # The return message
            return jsonify({
                'message': 'The program data has successifully been updated',
                'program_name': program.program_name,
                'program_address': program.program_address,
                'craeted_at': program.created_at
            })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR



    




