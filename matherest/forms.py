from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from matherest.models import User

class FormLogin(FlaskForm):
    email =             StringField("Email", validators=[DataRequired(), Email()])
    password =             PasswordField("Senha", validators=[DataRequired()])
    button_confirm = SubmitField("Fazer Login")

class FormCreateAccount(FlaskForm):
    username=           StringField("Nome de Usuário", validators=[DataRequired()])
    email =             StringField("Email", validators=[DataRequired(), Email()])
    password =          PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    password_confirm =  PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    button_confirm =    SubmitField("Criar Usuário")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("Email já cadastrado, faça login para continuar")
        
