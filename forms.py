from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField, DecimalField, TextAreaField, BooleanField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, Length

class CreateShowForm(FlaskForm):
    # Event Record
    venue = SelectField('Venue', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    time = StringField('Time')
    ticketprice = DecimalField('Ticket Price', validators=[DataRequired()])

    # Equipment Select
    equipment = SelectMultipleField('Equipment', validators=[DataRequired()])

    # Merch Select
    merch = SelectMultipleField('Merch', validators=[DataRequired()])

    # Set List
    band1 = SelectField("Band 1", validators=[DataRequired()])
    band2 = SelectField("Band 2", validators=[DataRequired()])
    band3 = SelectField("Band 3", validators=[DataRequired()])
    band4 = SelectField("Band 4", validators=[DataRequired()])

    # Volunteer Schedule
    volunteer1 = SelectField("Volunteer 1", validators=[DataRequired()])
    volunteer2 = SelectField("Volunteer 2", validators=[DataRequired()])
    volunteer3 = SelectField("Volunteer 3", validators=[DataRequired()])
    volunteer4 = SelectField("Volunteer 4", validators=[DataRequired()])

    # Submit
    submit = SubmitField('Save')

class UpdateShowForm(FlaskForm):
    # Event Record
    venue = SelectField('Venue', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    time = StringField('Time')
    ticketprice = DecimalField('Ticket Price', validators=[DataRequired()])
    ticketssold = IntegerField('Tickets Sold', validators=[DataRequired()])
    miscexpenses = DecimalField('Miscellaneous Expenses', validators=[DataRequired()])
 
    # Equipment Select
    equipment = SelectMultipleField('Equipment', validators=[DataRequired()])

    # Merch Select
    merch = SelectMultipleField('Merch', validators=[DataRequired()])

    # Set List
    band1 = SelectField("Band 1", validators=[DataRequired()])
    band2 = SelectField("Band 2", validators=[DataRequired()])
    band3 = SelectField("Band 3", validators=[DataRequired()])
    band4 = SelectField("Band 4", validators=[DataRequired()])

    # Volunteer Schedule
    volunteer1 = SelectField("Volunteer 1", validators=[DataRequired()])
    volunteer2 = SelectField("Volunteer 2", validators=[DataRequired()])
    volunteer3 = SelectField("Volunteer 3", validators=[DataRequired()])
    volunteer4 = SelectField("Volunteer 4", validators=[DataRequired()])

    # Submit
    submit = SubmitField('Save')

class EventMerchForm(FlaskForm):
    merchid = HiddenField('Hidden Field')
    quantity = IntegerField('')
    submit = SubmitField('Save')

class CreateBandForm(FlaskForm):
    # Band Record
    name = StringField('Band', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    genre = StringField('Genre',validators=[DataRequired()])
    instagram = StringField('Instagram')
    contact = StringField('Contact Name',validators=[DataRequired()])
    contactphone = StringField('Contact Phone Number',validators=[DataRequired()])
    
    # Submit
    submit = SubmitField('Save')

class CreateVenueForm(FlaskForm):
    # Venue Record
    name = StringField('Name', validators=[DataRequired()])
    street = StringField('Street')
    city = StringField('City')
    state = StringField('State Code', validators=[Length(max=2)])
    zip = StringField('Zip')
    price = DecimalField('Price')
    type = StringField('Type')
    contact = StringField('Contact Name')
    contactphone = StringField('Contact Phone Number')
    contactemail = StringField('Contact Email')
    
    # Submit
    submit = SubmitField('Save')

class CreateEquipmentForm(FlaskForm):
    # Equipment Record
    type = StringField('Type', validators=[DataRequired()])
    cost = DecimalField('Cost')
    volunteer = SelectField('Pickup Volunteer')

    # Vendor Select
    vendor = SelectField('Vendor', validators=[DataRequired()])
    
    # Submit
    submit = SubmitField('Save')

class CreateMerchForm(FlaskForm):
    # Merch Record
    type = StringField('Type', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = DecimalField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

    # Vendor Select
    vendor = SelectField('Vendor', validators=[DataRequired()])
    cost = DecimalField('Cost', validators=[DataRequired()])

    # Submit
    submit = SubmitField('Save')

class CreateVendorForm(FlaskForm):
    # Vendor Record
    name = StringField('Name', validators=[DataRequired()])
    street = StringField('Street')
    city = StringField('City')
    state = StringField('State Code',validators=[Length(max=2)])
    zip = StringField('Zip')
    phone = StringField('Phone Number')
    email = StringField('Email')
    
    # Submit
    submit = SubmitField('Save')

class CreateVolunteerForm(FlaskForm):
    # Volunteer Record
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone Number')
    email = StringField('Email')
    avail1 = BooleanField('Time Slot 1')
    avail2 = BooleanField('Time Slot 2')
    avail3 = BooleanField('Time Slot 3')
    avail4 = BooleanField('Time Slot 4')
    
    # Submit
    submit = SubmitField('Save')