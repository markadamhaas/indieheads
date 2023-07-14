from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DateTimeField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateShowForm(FlaskForm):
    # Event Record
    venue = SelectField('Venue', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = DateTimeField('Time', format='%H:%M:')
    ticketprice = IntegerField('Ticket Price', validators=[DataRequired()])

    # Equipment Select

    # Merch Select

    # Set List

    # Volunteer Schedule

    # Submit
    submit = SubmitField('Create')

class CreateBandForm(FlaskForm):
    # Event Record
    name = StringField('Band', validators=[DataRequired()])
    genre = StringField('Genre')
    Instagram = StringField('Instagram')
    contact = StringField('Contact Name')
    contactphone = StringField('Contact Phone Number')
    
    # Submit
    submit = SubmitField('Create')