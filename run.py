from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

app.debug = True


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
    cursor.execute("SELECT * FROM BANDS;")
    bands = cursor.fetchall()
    
    band_details = None
    members = None
    if 'band_id' in request.args:
        band_id = request.args.get('band_id')
        cursor.execute("SELECT * FROM BANDS WHERE Band_ID = %s;", (band_id,))
        band_details = cursor.fetchone()
        cursor.execute("SELECT * FROM MEMBERS WHERE Band_ID = %s;", (band_id,))
        members = cursor.fetchall()
    
    search_results = None
    if request.method == 'POST':
        query = request.form.get('q')
        cursor.execute("SELECT * FROM BANDS WHERE Band_Name LIKE %s;", ('%' + query + '%',))
        search_results = cursor.fetchall()
    
    cursor.close()
    
    return render_template('bands.html', bands=bands, band_details=band_details, members=members, search_results=search_results)

@app.route('/search', methods=['POST'])
def search():
    q = request.form.get('q')
    # Perform the search and store the results in the `bands` variable
    bands = perform_search_on_bands(q)
    return render_template('bands.html', bands=bands)

def perform_search_on_bands(q):
    cursor = mydb.cursor(dictionary=True)

    query = f"SELECT * FROM BANDS WHERE Band_Name LIKE '%{q}%'"
    cursor.execute(query)
    results = cursor.fetchall()

    return results

@app.route('/sort', methods=['POST'])
def sort():
    option = request.form.get('sort-option')
    print(option)
    # Sort the bands according to the selected option and store the results in the `bands` variable
    bands = perform_sort_on_bands(option)
    return render_template('bands.html', bands=bands)

def perform_sort_on_bands(option):
    cursor = mydb.cursor(dictionary=True)
    if option == 'name':
        query = f"SELECT * FROM BANDS ORDER BY Band_Name"

    if option == 'location':
        query = f"SELECT * FROM BANDS ORDER BY Band_Location"

    if option == 'genre':
        query = f"SELECT * FROM BANDS ORDER BY Band_Genre"
    cursor.execute(query)
    results = cursor.fetchall()

    return results

@app.route('/band_details/<int:id>')
def band_details(id):
    
    cursor = mydb.cursor(dictionary=True)
    # Fetch band details
    cursor.execute("SELECT * FROM BANDS WHERE Band_ID = %s;", (id,))
    band = cursor.fetchone()

    # Fetch band members
    cursor.execute("SELECT * FROM MEMBERS WHERE Band_ID = %s;", (id,))
    members = cursor.fetchall()

    return render_template('band-details.html', band=band, members=members)

@app.route('/shows')
def shows():
    # Add the code to retrieve shows data from the database and render the template
    return render_template('shows.html')

@app.route('/venues')
def venues():
    # Add the code to retrieve venues data from the database and render the template
    return render_template('venues.html')

@app.route('/equipment')
def equipment():
    # Add the code to retrieve equipment data from the database and render the template
    return render_template('equipment.html')

@app.route('/merch')
def merch():
    # Add the code to retrieve merch data from the database and render the template
    return render_template('merch.html')

if __name__ == '__main__':
    app.run(debug=True)
