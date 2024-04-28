import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
import psycopg2
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/', methods=['GET'])
def get_home():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = psycopg2.connect(
            host='localhost',
            dbname='chitter',
            user='Umut',
            password='123'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users WHERE email=%s AND pass=%s", (email, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('get_home'))  # Redirect to the home page if login is successful
        else:
            # Handle invalid credentials
            error = 'Invalid email or password. Please try again.'
            return render_template('login.html', error=error)

    # Render the login page for GET requests
    return render_template('login.html')

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
