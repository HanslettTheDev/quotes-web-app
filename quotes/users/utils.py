import os
import secrets
from flask import url_for, current_app
# from PIL import Image
from quotes import mail
from flask_mail import Message

def save_pic(form_pic):
    random_hex_name = secrets.token_hex(8) #create a random hex 8 digit name which will be used as a file name to avoid conflicts in the database
    _, file_ext = os.path.splitext(form_pic.filename) #create a variable using the os path split text function split the file name from the extension
    picture_name = random_hex_name + file_ext #now concactinate the random_hex_name with the file extension
    picture_path = os.path.join(current_app.root_path, 'static/profile_images', picture_name) #using the os module join the path of the directory of the saved file with the new concactinated variable
    # resize picture 
    final_size = (125, 125)
    # # i = Image.open(form_pic)
    # i.thumbnail(final_size)
    
    # i.save(picture_path) #use the save function to store the picture name finally
    
    return picture_name

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@ToxicQuotes.com', recipients=[user.email])
    msg.body = f'''To reset your password for your Toxic Quotes Account, click the following link:   
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request simply ignore this email! and no changes will occur
'''
    mail.send(msg)