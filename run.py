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
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM EVENT")
    events = cursor.fetchall()
    for event in events:
        #misc cost
        misc = event[6]
        
        #equipment cost
        equipmentcost = 0
        cursor.execute("SELECT Equipment_Cost FROM EQUIPMENT JOIN EVENTEQUIPMENT ON EQUIPMENT.Equipment_ID=EVENTEQUIPMENT.Equipment_ID WHERE EVENTEQUIPMENT.Event_ID=%s;",
                       (event[0],))
        equipmentcosts = cursor.fetchall()
        for equipment in equipmentcosts:
            equipmentcost+=equipment[0]

        #merch cost
        merchcost = 0
        cursor.execute("SELECT Cost FROM MERCHVENDOR JOIN EVENTMERCH ON MERCHVENDOR.Merch_ID=EVENTMERCH.Merch_ID WHERE EVENTMERCH.Event_ID=%s;",
                       (event[0],))
        merchcosts = cursor.fetchall()
        for merch in merchcosts:
            merchcost+=merch[0]

        #total cost
        totalcost = misc + equipmentcost + merchcost

        #merch revenue
        merchrevenue=0
        cursor.execute("SELECT Merch_Price FROM MERCH JOIN EVENTMERCH ON MERCH.Merch_ID=EVENTMERCH.Merch_ID WHERE EVENTMERCH.Event_ID=%s;",
                       (event[0],))
        merchprices = cursor.fetchall()
        cursor.execute("Select QuantitySold From EVENTMERCH WHERE Event_ID=%s;",
                       (event[0],))
        merchquantities = cursor.fetchall()
        merchrevenue = sum(x[0] * y[0] for x, y in zip(merchprices,merchquantities))

        #ticket revenue

        ticketrevenue = event[4] * event[5]

        #total revenue
        totalrevenue = merchrevenue + ticketrevenue

        #net
        net = totalrevenue - totalcost
        cursor.execute("UPDATE EVENT SET Total_Expenses = %s, Revenue = %s, Net = %s WHERE Event_ID = %s;", 
                    (totalcost, totalrevenue, net, event[0]))
        mydb.commit
        cursor.close
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Event_Date')  # Default sorting is by name
    cursor.execute(f"SELECT * FROM EVENT ORDER BY {sort_option};")
    shows = cursor.fetchall()
    cursor.close()
    return render_template('shows.html', shows=shows, sort=sort_option)

@app.route("/eventmerch/<int:id>", methods=['GET', 'POST'])
def eventmerch(id):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM EVENTMERCH JOIN MERCH ON EVENTMERCH.Merch_ID=MERCH.Merch_ID WHERE Event_ID=%s;",
                   (id,))
    eventmerch = cursor.fetchall()

    merchforms = []
    for merch in eventmerch:
        print(merch)
        form = forms.EventMerchForm()
        form.merchid.data = merch['Merch_ID']
        form.quantity.data = merch['QuantitySold']
        merchforms.append(form)

    if request.method == 'POST':  # Check if it's a POST request

        merchid = form.merchid.data
        quantity = form.quantity.data
        cursor.execute("UPDATE EVENTMERCH SET QuantitySold = %s WHERE Event_ID = %s AND Merch_ID = %s;", 
                    (quantity, id, merchid))
        mydb.commit()
        cursor.execute("SELECT QuantityAvailable FROM MERCH WHERE MERCH_ID = %s",
                       (merchid,))
        quantityavailable = cursor.fetchone()
        cursor.execute("UPDATE MERCH SET QuantityAvailable = %s WHERE MERCH_ID = %s",
                       (quantityavailable['QuantityAvailable']-quantity, merchid))
        mydb.commit()
        cursor.close()
        return redirect(url_for('shows'))
    return render_template('eventmerch.html', eventmerch=eventmerch, merchforms=merchforms)

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
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Equipment_Type')  # Default sorting is by type
    cursor.execute(f"""SELECT E.Equipment_ID, E.Equipment_Type, E.Equipment_Cost, V.Volunteer_FName, V.Volunteer_LName, VE.Vendor_Name 
                        FROM EQUIPMENT E 
                        LEFT JOIN VOLUNTEER V ON E.Volunteer_ID = V.Volunteer_ID
                        INNER JOIN EQUIPMENTVENDOR EV ON E.Equipment_ID = EV.Equipment_ID
                        INNER JOIN VENDOR VE ON EV.Vendor_ID = VE.Vendor_ID
                        ORDER BY {sort_option};""")
    equipments = cursor.fetchall()
    cursor.close()
    return render_template('equipment.html', equipments=equipments, sort=sort_option)


@app.route('/merch')
def merch():
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Merch_Type')  # Default sorting is by type
    cursor.execute(f"""SELECT M.Merch_ID, M.Merch_Type, M.Merch_Description, M.Merch_Price, M.QuantityAvailable, V.Vendor_Name, MV.Cost
                    FROM MERCHVENDOR MV 
                    INNER JOIN MERCH M ON MV.Merch_ID = M.Merch_ID 
                    INNER JOIN VENDOR V ON MV.Vendor_ID = V.Vendor_ID 
                    ORDER BY {sort_option};""")
    merchs = cursor.fetchall()
    cursor.close()
    return render_template('merch.html', merchs=merchs, sort=sort_option)


@app.route('/vendor')
def vendor():
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Vendor_Name')  # Default sorting is by name
    cursor.execute(f"SELECT * FROM VENDOR ORDER BY {sort_option};")
    vendors = cursor.fetchall()
    cursor.close()
    return render_template('vendor.html', vendors=vendors, sort=sort_option)

@app.route('/volunteers')
def volunteers():
    cursor = mydb.cursor(dictionary=True)
    sort_option = request.args.get('sort', 'Volunteer_FName')  # Default sorting is first name
    cursor.execute(f"SELECT * FROM VOLUNTEER ORDER BY {sort_option};")
    volunteers = cursor.fetchall()
    cursor.close()
    return render_template('volunteers.html', volunteers=volunteers, sort=sort_option)

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
    cursor.execute('SELECT Volunteer_ID, Volunteer_FName FROM VOLUNTEER')
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
    if request.method == 'POST':  # Check if it's a POST request
        venue = form.venue.data
        date = form.date.data
        time = form.time.data
        ticketprice = form.ticketprice.data

        equipment = form.equipment.data
        equipment = list(map(int, equipment))
        
        merch = form.merch.data
        merch = list(map(int, merch))

        band1 = form.band1.data
        band2 = form.band2.data
        band3 = form.band3.data
        band4 = form.band4.data

        volunteer1 = form.volunteer1.data
        volunteer2 = form.volunteer2.data
        volunteer3 = form.volunteer3.data
        volunteer4 = form.volunteer4.data

        cursor.execute("INSERT INTO EVENT (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price, Misc_Expenses, Total_Expenses, Revenue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", 
                    (venue, date, time, 0, ticketprice, 0, 0, 0))
        
        mydb.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID();")
        event_ID = cursor.fetchone()
        
        for i in equipment:
            cursor.execute("INSERT INTO EVENTEQUIPMENT (Event_ID, Equipment_ID) VALUES (%s, %s);",
                           (event_ID[0], i))
        
        for i in merch:
            cursor.execute("INSERT INTO EVENTMERCH (Event_ID, Merch_ID, QuantitySold) VALUES (%s, %s, %s);",
                           (event_ID[0], i, 0))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], band1, 1))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], band2, 2))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], band3, 3))
        
        cursor.execute("INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], band4, 4))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], volunteer1, 1))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], volunteer2, 2))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], volunteer3, 3))
        
        cursor.execute("INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot) VALUES (%s, %s, %s);",
                       (event_ID[0], volunteer4, 4))

        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('shows'))
    return render_template('create-show.html', form=form)

@app.route("/create-band", methods=['GET', 'POST'])
def createband():
    form = forms.CreateBandForm()

    if request.method == 'POST':  # Check if it's a POST request
        name = form.name.data
        genre = form.genre.data
        instagram = form.instagram.data
        contact = form.contact.data
        contactphone = form.contactphone.data

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO BANDS (Band_Name, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number) VALUES (%s, %s, %s, %s, %s);", 
                        (name, genre, instagram, contact, contactphone))
        mydb.commit()
        cursor.close()
        
        return redirect(url_for('bands'))
        
    return render_template('create-band.html', form=form)



@app.route("/create-venue", methods=['GET', 'POST'])
def createvenue():
    form = forms.CreateVenueForm()

    # Get data and create Venue
    cursor = mydb.cursor()
    if request.method == 'POST':  # Check if it's a POST request
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
    return render_template('create-venue.html', form=form)

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
    if request.method == 'POST':  # Check if it's a POST request
        type = form.type.data
        cost = form.cost.data
        volunteer = form.volunteer.data
        vendor = form.vendor.data

        cursor.execute("INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID) VALUES (%s, %s, %s);", 
                        (type, cost, volunteer))
        mydb.commit()

        cursor.execute("SELECT LAST_INSERT_ID();")
        equipment_ID = cursor.fetchone()

        cursor.execute("INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID) VALUES (%s, %s);", 
                        (equipment_ID[0], vendor))

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

    if request.method == 'POST':  # Check if it's a POST request
        type = form.type.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        vendor = form.vendor.data
        cost = form.cost.data
        cursor.execute("INSERT INTO MERCH (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable) VALUES (%s, %s, %s, %s);", 
                        (type, description, price, quantity))
        
        mydb.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID();")
        merch_ID = cursor.fetchone()

        cursor.execute("INSERT INTO MERCHVENDOR (Merch_ID, Vendor_ID, QuantitySupplied, Cost) VALUES (%s, %s, %s, %s);", 
                        (merch_ID[0], vendor, quantity, cost))
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
    if request.method == 'POST':  # Check if it's a POST request
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
        return redirect(url_for('vendor'))
    return render_template('create-vendor.html', form=form)

@app.route("/create-volunteer", methods=['GET', 'POST'])
def createvolunteer():
    form = forms.CreateVolunteerForm()

    # Get data and create Volunteer
    cursor = mydb.cursor()
    if request.method == 'POST':  # Check if it's a POST request
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
        cursor.execute("INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Phone, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", 
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

    form = forms.UpdateShowForm()
    # form.name.data
    # form.genre.data
    # form.instagram.data
    # form.contact.data
    # form.contactphone.data

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
    cursor.execute('SELECT Volunteer_ID, Volunteer_FName FROM VOLUNTEER')
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
    if request.method == 'POST':  # Check if it's a POST request
        venue = form.venue.data
        date = form.date.data
        time = form.time.data
        ticketprice = form.ticketprice.data
        ticketssold = form.ticketssold.data
        miscexpenses = form.miscexpenses.data

        equipment = form.equipment.data
        equipment = list(map(int, equipment))
        
        merch = form.merch.data
        merch = list(map(int, merch))

        band1 = form.band1.data
        band2 = form.band2.data
        band3 = form.band3.data
        band4 = form.band4.data

        volunteer1 = form.volunteer1.data
        volunteer2 = form.volunteer2.data
        volunteer3 = form.volunteer3.data
        volunteer4 = form.volunteer4.data

        cursor.execute("UPDATE EVENT SET Venue_ID = %s, Event_Date = %s, Event_Time = %s, Tickets_Sold = %s, Ticket_Price = %s, Misc_Expenses = %s, Total_Expenses = %s, Revenue = %s WHERE Event_ID = %s;", 
                    (venue, date, time, ticketssold, ticketprice, miscexpenses, 0, 0, id))
        
        mydb.commit()

        cursor.execute("DELETE FROM EVENTEQUIPMENT WHERE Event_ID = %s;",
                       (id,))
        
        cursor.execute("DELETE FROM EVENTMERCH WHERE Event_ID = %s;",
                       (id,))
        
        mydb.commit()

        for i in equipment:
            cursor.execute("INSERT INTO EVENTEQUIPMENT (Event_ID, Equipment_ID) VALUES (%s, %s);",
                           (id, i))
        
        for i in merch:
            cursor.execute("INSERT INTO EVENTMERCH (Event_ID, Merch_ID, QuantitySold) VALUES (%s, %s, %s);",
                           (id, i, 0))
        
        cursor.execute("UPDATE SETLIST SET Band_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (band1, 1, id))
        
        cursor.execute("UPDATE SETLIST SET Band_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (band2, 2, id))
        
        cursor.execute("UPDATE SETLIST SET Band_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (band3, 3, id))
        
        cursor.execute("UPDATE SETLIST SET Band_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (band4, 4, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET Volunteer_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (volunteer1, 1, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET Volunteer_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (volunteer2, 2, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET Volunteer_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (volunteer3, 3, id))
        
        cursor.execute("UPDATE VOLUNTEERSCHEDULE SET Volunteer_ID = %s, Timeslot = %s WHERE Event_ID = %s;",
                       (volunteer4, 4, id))
        
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

    if request.method == 'POST':  # Check if it's a POST request
        name = form.name.data
        location = form.location.data
        genre = form.genre.data
        instagram = form.instagram.data
        contact = form.contact.data
        contactphone = form.contactphone.data
        cursor.execute("UPDATE BANDS SET Band_Name = %s, Band_Location = %s, Band_Genre = %s, Band_Instagram = %s, B_Contact_Person = %s, B_Contact_Number = %s WHERE Band_ID = %s;", 
                       (name, location, genre, instagram, contact, contactphone, id))
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

    if request.method == 'POST':  # Check if it's a POST request
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
        cursor.execute("UPDATE VENUE SET Venue_Name = %s, Venue_Street = %s, Venue_City = %s, Venue_State = %s, Venue_Zip = %s, Venue_Price = %s, Venue_Type = %s, Venue_Contact = %s, Venue_Phone = %s, Venue_Email = %s WHERE Venue_ID = %s;", 
                        (name, street, city, state, zip, price, type, contact, contactphone, contactemail, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('venues'))
    return render_template('edit-venue.html', form=form, record=record)

@app.route("/edit-equipment/<int:id>", methods=['GET', 'POST'])
def editequipment(id):
    # Get record
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM EQUIPMENT WHERE Equipment_ID = %s', (id,))
    record = cursor.fetchone()
    form = forms.CreateEquipmentForm()

    cursor.execute('SELECT Volunteer_ID, Volunteer_FName, Volunteer_LName FROM VOLUNTEER') #volunteer select
    volunteeroptions = cursor.fetchall()
    cursor.execute('SELECT Vendor_ID, Vendor_Name FROM VENDOR') #vendor select
    vendoroptions = cursor.fetchall()
    cursor.close()

    # Assign options to the SelectField
    print(volunteeroptions)
    form.volunteer.choices = [(row[0], row[1]+row[2]) for row in volunteeroptions]
    form.vendor.choices = [(row[0], row[1]) for row in vendoroptions]

    # Get data and create Equipment
    cursor = mydb.cursor()
    if request.method == 'POST':  # Check if it's a POST request
        type = form.type.data
        cost = form.cost.data
        volunteer = form.volunteer.data
        vendor = form.vendor.data

        cursor.execute("UPDATE EQUIPMENT SET Equipment_Type = %s, Equipment_Cost = %s, Volunteer_ID = %s WHERE Equipment_ID = %s;", 
                        (type, cost, volunteer, id))

        cursor.execute("UPDATE EQUIPMENTVENDOR SET Vendor_ID = %s WHERE Equipment_ID = %s;", 
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
    if request.method == 'POST':  # Check if it's a POST request
        type = form.type.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        vendor = form.vendor.data
        cost = form.cost.data
        cursor.execute("UPDATE MERCH SET Merch_Type = %s, Merch_Description = %s, Merch_Price = %s, QuantityAvailable = %s WHERE Merch_ID = %s;", 
                        (type, description, price, quantity, id))

        cursor.execute("UPDATE MERCHVENDOR SET Vendor_ID = %s, QuantitySupplied = %s, Cost = %s WHERE Merch_ID = %s;", 
                        (vendor, quantity, cost, id))
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

    if request.method == 'POST':  # Check if it's a POST request
        name = form.name.data
        street = form.street.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        phone = form.phone.data
        email = form.email.data
        cursor.execute("UPDATE VENDOR Vendor_Name = %s, Vendor_Street = %s, Vendor_City = %s, Vendor_State = %s, Vendor_Zip = %s, Vendor_Phone = %s, Vendor_Email = %s WHERE Vendor_ID = %s;", 
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

    if request.method == 'POST':  # Check if it's a POST request
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
        cursor.execute("UPDATE VOLUNTEER SET Volunteer_FName = %s, Volunteer_LName = %s, Volunteer_Email = %s, Volunteer_Avail_1 = %s, Volunteer_Avail_2 = %s, Volunteer_Avail_3 = %s, Volunteer_Avail_4 = %s WHERE Volunteer_ID = %s;", 
                        (fname, lname, phone, email, avail1, avail2, avail3, avail4, id))
        # Save Changes
        mydb.commit()
        cursor.close()
        return redirect(url_for('volunteer'))
    return render_template('edit-volunteer.html', form=form, record=record)

###########################################################################################################################################################################
    
@app.route("/delete_show/<int:id>", methods=['POST'])
def delete_show(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM EVENT WHERE Event_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('shows'))

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

@app.route("/delete_equipment/<int:id>", methods=['POST'])
def delete_equipment(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM EQUIPMENT WHERE Equipment_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('equipment'))

@app.route("/delete_merch/<int:id>", methods=['POST'])
def delete_merch(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM MERCH WHERE Merch_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('merch'))

@app.route("/delete_vendor/<int:id>", methods=['POST'])
def delete_vendor(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM VENDOR WHERE Vendor_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('vendor'))

@app.route("/delete_volunteer/<int:id>", methods=['POST'])
def delete_volunteer(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM VOLUNTEER WHERE Volunteer_ID = %s;", (id,))
    mydb.commit()
    cursor.close()
    return redirect(url_for('volunteers'))

if __name__ == '__main__':
    app.run(debug=True)
