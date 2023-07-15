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

    # Retrieve data from the MySQL table For Venue
    cursor = mydb.cursor()
    cursor.execute('SELECT Venue_ID, Venue_Name FROM VENUE')
    venueoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Equipment
    cursor = mydb.cursor()
    cursor.execute('SELECT Equipment_ID, Equipment_Type FROM EQUIPMENT')
    equipmentoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Merch
    cursor = mydb.cursor()
    cursor.execute('SELECT Merch_ID, Merch_Type FROM MERCH')
    merchoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Band
    cursor = mydb.cursor()
    cursor.execute('SELECT Band_ID, Band_Name FROM BANDS')
    bandoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Volunteer
    cursor = mydb.cursor()
    cursor.execute('SELECT Volunteer_ID, Volunteer_Name FROM VOLUNTEER')
    volunteeroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.venue.choices = [(row[0], row[1]) for row in venueoptions]
    form.equipment.choices = [(row[0], row[1]) for row in equipmentoptions]
    form.merch.choices = [(row[0], row[1]) for row in merchoptions]
    form.band1.choices = [(row[0], row[1]) for row in bandoptions]
    form.band2.choices = [(row[0], row[1]) for row in bandoptions]
    form.band3.choices = [(row[0], row[1]) for row in bandoptions]
    form.band4.choices = [(row[0], row[1]) for row in bandoptions]
    form.volunteer1.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer2.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer3.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer4.choices = [(row[0], row[1]) for row in volunteeroptions]
    

    # Get data and create Event
    cursor = mydb.cursor()
    if form.validate_on_submit():
        venue = form.venue.data
        date = form.date.data
        time = form.time.data
        ticketprice = form.ticketprice.data

        equipment = form.equipment.data
        
        merch = form.merch.data

        band1 = form.band1.data
        band2 = form.band2.data
        band3 = form.band3.data
        band4 = form.band4.data

        volunteer1 = form.volunteer1.data
        volunteer2 = form.volunteer2.data
        volunteer3 = form.volunteer3.data
        volunteer4 = form.volunteer4.data

        cursor.execute("INSERT INTO EVENT (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price, Total_Expenses, Revenue) VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                    (venue, date, time, 0, ticketprice, 0, 0))
        
        mydb.commit()

        event_ID = ("SELECT last_insert_id();")
        
        for i in equipment:
            cursor.execute("INSERT INTO EVENTEQUIPMENT (Event_ID, Equipment_ID) VALUES (%s, %s);",
                           (event_ID, equipment[i]))
        
        for i in merch:
            cursor.execute("INSERT INTO EVENTMERCH (Event_ID, Merch_ID, QuantitySold) VALUES (%s, %s, %s);",
                           (event_ID, merch[i], 0))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, band1, 1))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, band2, 2))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, band3, 3))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, band4, 4))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, volunteer1, 1))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, volunteer2, 2))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, volunteer3, 3))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID, volunteer4, 4))

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
    cursor.execute('SELECT Vendor_ID, Vendor_Name FROM VENDOR') #vendor select
    vendoroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.volunteer.choices = [(row[0], row[1]+row[2]) for row in volunteeroptions]
    form.vendor.choices = [(row[0], row[1]) for row in vendoroptions]

    # Get data and create Equipment
    cursor = mydb.cursor()
    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        volunteer = form.volunteer.data
        vendor = form.vendor.data

        cursor.execute("INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID) VALUES (%s, %s, %s);", 
                        (type, cost, volunteer))
        mydb.commit()

        equipment_ID = ("SELECT last_insert_id();")

        cursor.execute("INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID) VALUES (%s, %s);", 
                        (equipment_ID, vendor))

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
    cursor.execute('SELECT Vendor_ID, Vendor_Name FROM VENDOR') #vendor select
    vendoroptions = cursor.fetchall()
    form.vendor.choices = [(row[0], row[1]) for row in vendoroptions]

    if form.validate_on_submit():
        type = form.type.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        vendor = form.vendor.data
        cursor.execute("INSERT INTO MERCH (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable) VALUES (%s, %s, %s, %s);", 
                        (type, description, price, quantity))
        
        mydb.commit()
        
        merch_ID = ("SELECT last_insert_id();")

        cursor.execute("INSERT INTO EQUIPMENTVENDOR (Merch_ID, Vendor_ID, QuantitySupplied) VALUES (%s, %s, %s);", 
                        (merch_ID, vendor, quantity))
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

@app.route("/edit-show/<int:id>", methods=['GET', 'POST'])
def editshow(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM EVENT WHERE EVENT_ID = %s', (id,))
    record = cursor.fetchone()
    # cursor.execute('SELECT * FROM your_table WHERE id = %s', (id))
    # record = cursor.fetchone()

    form = forms.CreateShowForm()
    # form.name.data
    # form.genre.data
    # form.instagram.data
    # form.contact.data
    # form.contactphone.data

    form = forms.CreateShowForm()

    # Retrieve data from the MySQL table For Venue
    cursor = mydb.cursor()
    cursor.execute('SELECT Venue_ID, Venue_Name FROM VENUE')
    venueoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Equipment
    cursor = mydb.cursor()
    cursor.execute('SELECT Equipment_ID, Equipment_Type FROM EQUIPMENT')
    equipmentoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Merch
    cursor = mydb.cursor()
    cursor.execute('SELECT Merch_ID, Merch_Type FROM MERCH')
    merchoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Band
    cursor = mydb.cursor()
    cursor.execute('SELECT Band_ID, Band_Name FROM BANDS')
    bandoptions = cursor.fetchall()
    cursor.close()

    # Retrieve data from the MySQL table For Volunteer
    cursor = mydb.cursor()
    cursor.execute('SELECT Volunteer_ID, Volunteer_Name FROM VOLUNTEER')
    volunteeroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.venue.choices = [(row[0], row[1]) for row in venueoptions]
    form.equipment.choices = [(row[0], row[1]) for row in equipmentoptions]
    form.merch.choices = [(row[0], row[1]) for row in merchoptions]
    form.band1.choices = [(row[0], row[1]) for row in bandoptions]
    form.band2.choices = [(row[0], row[1]) for row in bandoptions]
    form.band3.choices = [(row[0], row[1]) for row in bandoptions]
    form.band4.choices = [(row[0], row[1]) for row in bandoptions]
    form.volunteer1.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer2.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer3.choices = [(row[0], row[1]) for row in volunteeroptions]
    form.volunteer4.choices = [(row[0], row[1]) for row in volunteeroptions]
    
    # Get data and create Event
    cursor = mydb.cursor()
    record = cursor.fetchone()
    if form.validate_on_submit():
        venue = form.venue.data
        date = form.date.data
        time = form.time.data
        ticketprice = form.ticketprice.data

        equipment = form.equipment.data
        
        merch = form.merch.data

        band1 = form.band1.data
        band2 = form.band2.data
        band3 = form.band3.data
        band4 = form.band4.data

        volunteer1 = form.volunteer1.data
        volunteer2 = form.volunteer2.data
        volunteer3 = form.volunteer3.data
        volunteer4 = form.volunteer4.data

        cursor.execute("UPDATE EVENT SET (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price, Total_Expenses, Revenue) VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE Event_ID = %s;", 
                    (venue, date, time, 0, ticketprice, 0, 0, id))
        
        mydb.commit()
        
        for i in equipment:
            cursor.execute("UPDATE EVENTEQUIPMENT SET (Equipment_ID) VALUES (%s) WHERE Event_ID = %s;",
                           (equipment[i], id))
        
        for i in merch:
            cursor.execute("UPDATE EVENTMERCH SET (Merch_ID, QuantitySold) VALUES (%s, %s) WHERE Event_ID = %s;",
                           (merch[i], 0, id))
        
        cursor.execute("UPDATE SETLIST SET (Band_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (band1, 1, id))
        
        cursor.execute("UPDATE SETLIST SET (Band_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (band2, 2, id))
        
        cursor.execute("UPDATE SETLIST SET (Band_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (band3, 3, id))
        
        cursor.execute("UPDATE SETLIST SET (Band_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (band4, 4, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET (Volunteer_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (volunteer1, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET (Volunteer_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (volunteer2, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET (Volunteer_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (volunteer3, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET (Volunteer_ID, Timeslot) VALUES (%s, %s) WHERE Event_ID = %s;",
                       (volunteer4, id))
        
        
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('shows'))
    return render_template('edit-show.html', form=form, record=record)


@app.route("/edit-band/<int:id>", methods=['GET', 'POST'])
def editband(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM BANDS WHERE Band_ID = %s', (id,))
    record = cursor.fetchone()

    form = forms.CreateBandForm()
    # form.name.data
    # form.genre.data
    # form.instagram.data
    # form.contact.data
    # form.contactphone.data

    if form.validate_on_submit():
        name = form.name.data
        genre = form.genre.data
        instagram = form.instagram.data
        contact = form.contact.data
        contactphone = form.contactphone.data
        cursor.execute("UPDATE BANDS SET (Band_Name, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number) VALUES (%s, %s, %s, %s, %s) WHERE Band_ID = %s;", 
                        (name, genre, instagram, contact, contactphone, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('bands'))
    return render_template('edit-band.html', form=form, record=record)

@app.route("/edit-venue/<int:id>", methods=['GET', 'POST'])
def editvenue(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM VENUE WHERE VENUE_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateVenueForm()

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
        cursor.execute("UPDATE VENUE SET (Venue_Name, Venue_Street, Venue_City, Venue_State, Venue_Zip, Venue_Price, Venue_Type, Venue_Contact, Venue_Phone, Venue_Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE Venue_ID = %s;", 
                        (name, street, city, state, zip, price, type, contact, contactphone, contactemail, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('venues'))
    return render_template('edit-venue.html', form=form, record=record)

@app.route("/edit-equipment/<int:id>", methods=['GET', 'POST'])
def editequipment(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM EQUIPMENT WHERE Equipment_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateEquipmentForm()

    cursor.execute('SELECT Volunteer_ID, Volunteer_FName, Volunteer_LName FROM VOLUNTEER') #volunteer select
    volunteeroptions = cursor.fetchall()
    cursor.execute('SELECT Vendor_ID, Vendor_Name FROM VENDOR') #vendor select
    vendoroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    form.volunteer.choices = [(row[0], row[1]+row[2]) for row in volunteeroptions]
    form.vendor.choices = [(row[0], row[1]) for row in vendoroptions]

    # Get data and create Equipment
    cursor = mydb.cursor()
    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        volunteer = form.volunteer.data
        vendor = form.vendor.data

        cursor.execute("UPDATE EQUIPMENT SET (Equipment_Type, Equipment_Cost, Volunteer_ID) VALUES (%s, %s, %s) WHERE Equipment_ID = %s;", 
                        (type, cost, volunteer, id))

        cursor.execute("UPDATE EQUIPMENTVENDOR SET (Vendor_ID) VALUES (%s, %s) WHERE Equipment_ID = %s;", 
                        (vendor, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('equipment'))
    return render_template('edit-equipment.html', form=form, record=record)

@app.route("/edit-merch/<int:id>", methods=['GET', 'POST'])
def editmerch(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM MERCH WHERE Merch_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateMerchForm()

    # Get data and create Merch
    cursor = mydb.cursor()
    cursor.execute('SELECT Vendor_ID, Vendor_Name FROM VENDOR') #vendor select
    vendoroptions = cursor.fetchall()
    form.vendor.choices = [(row[0], row[1]) for row in vendoroptions]

    # Get data and create Equipment
    if form.validate_on_submit():
        type = form.type.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        vendor = form.vendor.data
        cursor.execute("UPDATE MERCH SET (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable) VALUES (%s, %s, %s, %s) WHERE Merch_ID = %s;", 
                        (type, description, price, quantity, id))

        cursor.execute("UPDATE MERCHVENDOR SET (Vendor_ID) VALUES (%s, %s) WHERE Equipment_ID = %s;", 
                        (vendor, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('merch'))
    return render_template('edit-merch.html', form=form, record=record)

@app.route("/edit-vendor/<int:id>", methods=['GET', 'POST'])
def editvendor(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM VENDOR WHERE Vendor_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateVendorForm()

    if form.validate_on_submit():
        name = form.name.data
        street = form.street.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        phone = form.phone.data
        email = form.email.data
        cursor.execute("UPDATE VENDOR (Vendor_Name, Vendor_Street, Vendor_City, Vendor_State, Vendor_Zip, Vendor_Phone, Vendor_Email) VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE Vendor_ID = %s;", 
                        (name, street, city, state, zip, phone, email, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('vendor'))
    return render_template('edit-vendor.html', form=form, record=record)

@app.route("/edit-volunteer/<int:id>", methods=['GET', 'POST'])
def editvolunteer(id):
    # Get record
    cursor = mydb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM VOLUNTEER WHERE Volunteer_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateVolunteerForm()

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
        cursor.execute("INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4) WHERE Volunteer_ID = %s;", 
                        (fname, lname, phone, email, avail1, avail2, avail3, avail4, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('vendor'))
    return render_template('edit-vendor.html', form=form, record=record)

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

if __name__ == '__main__':
    app.run(debug=True)
