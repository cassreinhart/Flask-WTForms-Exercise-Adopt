from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import URL, InputRequired, Optional

class PetForm(FlaskForm):
    """Form for adding a pet"""
    
    name = StringField("Pet's Name", validators=[InputRequired()])
    species = SelectField("Species", 
                choices=[('cat','Cat'), ('dog','Dog'), ('porcupine','Porcupine')], 
                validators=[InputRequired()])
    photo_url = StringField("URL to Photo", validators=[URL(), Optional()])
    age = IntegerField("Age in Years", 
                validators=[Optional(, NumberRange(min=0, max=30, message='Enter Age in Years from 0-30'))])
    notes = TextAreaField("Extra Notes", validators=[Optional()])
    #available = BooleanField("Available for adoption?", validators=[Optional()], default="checked")