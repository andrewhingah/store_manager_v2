import re

def verify_name_details(name):
    """check that user details are valid"""
    if len(name.strip()) == 0:
        return {"message":"Name/category cannot be empty"}, 400
    if len(name) < 3:
        return {"message":"Too short, please add more characters"}, 400
    if len(name) > 15:
        return 'Too long, please remove some characters', 400
    if name.isdigit():
        return {"message":"Name cannot be digits only"}, 400
    if re.search('[a-z]',name) is None:
        return {"message": "please include a letter"}, 400

def validate_email(email):
    
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    if not re.match(email_regex, email):
        return {
                'Status': 'Error',
                'message': 'Ooops! {} is not a valid email address'.format(email) }, 400

def validate_password(password):
    '''
    password should be at least 8 characters
    password should contain a digit
    password should contain a capital letter
    '''
    if len(password) < 8:
        return {"message":"Make sure your password is at lest 8 characters"}, 400
    elif re.search('[0-9]',password) is None:
        return{"message":"Make sure your password has a number in it"}, 400
    elif re.search('[A-Z]',password) is None: 
        return{"message":"Make sure your password has a capital letter in it"}, 400


def validate_all(username, email, password):
    if verify_name_details(username):
        return verify_name_details(username)
    if validate_email(email):
        return validate_email(email)
    if validate_password(password):
        return validate_password(password)

def validate_quantity_id(num):
    if not num.isdigit():
        return {"message": "Only integers are allowed for the field"}