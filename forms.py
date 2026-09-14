from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , ValidationError
from wtforms.validators import DataRequired, Email , Length , EqualTo
from models import user

# EXTRA VALIDATORS

def validate_email(self , email_field):
    user_verifier = user.query.filter_by(email=email_field.data).first()
    if user_verifier:
        raise ValidationError('já existe um email ligado a um usuário.')
# REGISTER FORM 

class userR_form(FlaskForm):

    name = StringField('Digite seu nome:' , validators=[DataRequired()])

    email = StringField('Digite seu email:' , validators=[DataRequired() , Email() ])

    password = PasswordField('Digite sua senha:' , validators=[DataRequired(message='É obrigatório o uso de uma senha.') , Length(min=8 , max=20 , message='A senha deve possuir no mínimo de 8 a 20 caracteres.')])

    re_password = PasswordField('Digite sua senha novamente:' , validators=[DataRequired(message='É obrigatório o uso de uma senha.') , Length(min=8 , max=20 , message='A senha deve possuir no mínimo de 8 a 20 caracteres.' ) , EqualTo('password' , message=' as duas senhas precisam ser iguais. ')])

    submit = SubmitField('Cadastrar')

# EXTRA VALIDATORS

def email_valid(self , email_field):
    user_verifier = user.query.filter_by(email=email_field.data).first()
    if user_verifier:
        raise ValidationError('já existe um email ligado a um usuário.')