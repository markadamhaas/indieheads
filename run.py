from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'supersecretkey'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="password",  
    database="indieheads" 
)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/bands", methods=['GET', 'POST'])
def bands():
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Band_Name')  # Default sorting is by name
    cursor.execute(f"SELECT * FROM BANDS ORDER BY {sort_option};")
    bands = cursor.fetchall()
    cursor.close()
    return render_template('bands.html', bands=bands, sort=sort_option)

@app.route("/add_band", methods=['POST'])
def add_band():
    cursor = mydb.cursor()
    newBandName = request.form.get('Band_Name')
    newBandGenre = request.form.get('Band_Genre')
    newBandLocation = request.form.get('Band_Location')
    newBandInstagram = request.form.get('Band_Instagram')
    newBandContactPerson = request.form.get('B_Contact_Person')
    newBandContactPhone = request.form.get('B_Contact_Number')
    cursor.execute("INSERT INTO BANDS (Band_Name, Band_Genre, Band_Location, Band_Instagram, B_Contact_Person, B_Contact_Number) VALUES (%s, %s, %s, %s, %s, %s);", 
                    (newBandName, newBandGenre, newBandLocation, newBandInstagram, newBandContactPerson, newBandContactPhone))
    mydb.commit()
    cursor.close()
    return redirect(url_for('bands'))

@app.route("/delete_band/<int:id>", methods=['POST'])
def delete_band(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM BANDS WHERE Band_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('bands'))

@app.route("/edit_band/<int:id>", methods=['GET', 'POST'])
def edit_band(id):
    cursor = mydb.cursor(dictionary=True)
    if request.method == 'POST':
        bandName = request.form.get('Band_Name')
        bandGenre = request.form.get('Band_Genre')
        bandLocation = request.form.get('Band_Location')
        bandInstagram = request.form.get('Band_Instagram')
        bandContactPerson = request.form.get('B_Contact_Person')
        bandContactPhone = request.form.get('B_Contact_Number')
        cursor.execute("UPDATE BANDS SET Band_Name = %s, Band_Genre = %s, Band_Location = %s, Band_Instagram = %s, B_Contact_Person = %s, B_Contact_Number = %s WHERE Band_ID = %s;", 
                        (bandName, bandGenre, bandLocation, bandInstagram, bandContactPerson, bandContactPhone, id,))
        mydb.commit()
        cursor.close()
        return redirect(url_for('bands'))
    else:
        cursor.execute("SELECT * FROM BANDS WHERE Band_ID = %s;", (id,))
        band = cursor.fetchone()
        cursor.close()
        return render_template('edit-band.html', band=band)


@app.route('/shows')
def shows():
    # placeholder
    return render_template('shows.html')

class CreateShowForm(FlaskForm):
    # Event Record
    venue = SelectField('Venue', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    ticketprice = IntegerField('Ticket Price', validators=[DataRequired()])

    # Equipment Select

    # Merch Select

    # Set List

    # Volunteer Schedule

    # Submit
    submit = SubmitField('Create')

@app.route('/create_show', methods=['GET', 'POST'])
def createshow():
    form = CreateShowForm()
    # Retrieve data from the MySQL table
    cursor = mydb.cursor()
    cursor.execute('SELECT Venue_ID, Venue_Name FROM VENUE') #venue select
    venueoptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.venue.choices = [(row[0], row[1]) for row in venueoptions]

    # Get data and create Event
    cursor = mydb.cursor()
    if form.validate_on_submit():
        venue = form.venue.data
        date = form.date.data
        time = form.time.data
        ticketprice = form.ticketprice.data
        cursor.execute("INSERT INTO EVENT (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price, Total_Expenses, Revenue) VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                    (venue, date, time, 0, ticketprice, 0, 0))
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('shows'))
    return render_template('create_show.html', form=form)

@app.route('/venues')
def venues():
    # placeholder
    return render_template('venues.html')

@app.route('/equipment')
def equipment():
    # placeholder
    return render_template('equipment.html')

@app.route('/merch')
def merch():
    # placeholder
    return render_template('merch.html')

if __name__ == '__main__':
    app.run(debug=True)
