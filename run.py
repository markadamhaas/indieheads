from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import forms
# from flask_wtf import FlaskForm
# from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
# from wtforms.validators import DataRequired

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

@app.route('/shows')
def shows():
    # placeholder
    return render_template('shows.html')

@app.route('/venues')
def venues():
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Venue_Name')  # Default sorting is by name
    cursor.execute(f"SELECT * FROM VENUE ORDER BY {sort_option};")
    venues = cursor.fetchall()
    cursor.close()
    return render_template('venues.html', venues=venues, sort=sort_option)

@app.route('/equipment')
def equipment():
    # placeholder
    return render_template('equipment.html')

@app.route('/merch')
def merch():
    # placeholder
    return render_template('merch.html')

###########################################################################################################################################################################

@app.route('/create-show', methods=['GET', 'POST'])
def createshow():
    form = forms.CreateShowForm()

    # Retrieve data from the MySQL table For SelectField
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
    return render_template('create-show.html', form=form)

@app.route("/create-band", methods=['GET', 'POST'])
def createband():
    form = forms.CreateBandForm()

    # Get data and create Band
    cursor = mydb.cursor()
    if form.validate_on_submit():
        name = form.name.data
        genre = form.genre.data
        instagram = form.instagram.data
        contact = form.contact.data
        contactphone = form.contactphone.data
        cursor.execute("INSERT INTO BANDS (Band_Name, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number) VALUES (%s, %s, %s, %s, %s);", 
                        (name, genre, instagram, contact, contactphone))
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('bands'))
    return render_template('create-band.html', form=form)

@app.route("/create-venue", methods=['GET', 'POST'])
def createvenue():
    form = forms.CreateVenueForm()

    # Get data and create Venue
    cursor = mydb.cursor()
    if form.validate_on_submit():
        name = form.name.data
        street = form.street.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        price = form.price.data
        type = form.type.data
        contact = form.contact.data
        contactphone = form.contactphone.data
        contactemail = form.contactemail.data
        cursor.execute("INSERT INTO VENUE (Venue_Name, Venue_Street, Venue_City, Venue_State, Venue_Zip, Venue_Price, Venue_Type, Venue_Contact, Venue_Phone, Venue_Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                        (name, street, city, state, zip, price, type, contact, contactphone, contactemail))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('venues'))
    return render_template('create-band.html', form=form)

@app.route("/create-equipment", methods=['GET', 'POST'])
def createequipment():
    form = forms.CreateEquipmentForm()

    # Retrieve data from the MySQL table For SelectField
    cursor = mydb.cursor()
    cursor.execute('SELECT Volunteer_ID, Volunteer_FName, Volunteer_LName FROM VOLUNTEER') #volunteer select
    volunteeroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.volunteer.choices = [(row[0], row[1]+row[2]) for row in volunteeroptions]

    # Get data and create Equipment
    cursor = mydb.cursor()
    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        volunteer = form.volunteer.data
        cursor.execute("INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID) VALUES (%s, %s, %s);", 
                        (type, cost, volunteer))
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('equipment'))
    return render_template('create-equipment.html', form=form)

@app.route("/create-merch", methods=['GET', 'POST'])
def createmerch():
    form = forms.CreateMerchForm()

    # Get data and create Merch
    cursor = mydb.cursor()
    if form.validate_on_submit():
        type = form.type.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        cursor.execute("INSERT INTO MERCH (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable) VALUES (%s, %s, %s, %s);", 
                        (type, description, price, quantity))
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('merch'))
    return render_template('create-merch.html', form=form)

@app.route("/create-vendor", methods=['GET', 'POST'])
def createvendor():
    form = forms.CreateVendorForm()

    # Get data and create Vendor
    cursor = mydb.cursor()
    if form.validate_on_submit():
        name = form.name.data
        street = form.street.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        phone = form.phone.data
        email = form.email.data
        cursor.execute("INSERT INTO VENDOR (Vendor_Name, Vendor_Street, Vendor_City, Vendor_State, Vendor_Zip, Vendor_Phone, Vendor_Email) VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                        (name, street, city, state, zip, phone, email))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('vendors'))
    return render_template('create-vendor.html', form=form)

@app.route("/create-volunteer", methods=['GET', 'POST'])
def createvolunteer():
    form = forms.CreateVolunteerForm()

    # Get data and create Volunteer
    cursor = mydb.cursor()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        phone = form.phone.data
        email = form.email.data
        avail1 = form.avail1.data
        avail2 = form.avail2.data
        avail3 = form.avail3.data
        avail4 = form.avail4.data
        availlist = [avail1, avail2, avail3, avail4]
        for i in availlist:
            if i == True:
                i = 1
            else: i = 0
        cursor.execute("INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4);", 
                        (fname, lname, phone, email, avail1, avail2, avail3, avail4))
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('volunteers'))
    return render_template('create-volunteer.html', form=form)

###########################################################################################################################################################################

@app.route("/delete_band/<int:id>", methods=['POST'])
def delete_band(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM BANDS WHERE Band_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('bands'))

@app.route("/delete_venue/<int:id>", methods=['POST'])
def delete_venue(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM VENUE WHERE Venue_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('venues'))

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

if __name__ == '__main__':
    app.run(debug=True)
