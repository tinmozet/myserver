
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Credentials for accessing the M3U8 channels
USERNAME = "admin"
PASSWORD = "password"

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME or request.form['password'] != PASSWORD:
            error = 'Invalid credentials. Please try again.'
        else:
            # If login successful, redirect to the channels page
            return redirect(url_for('channels'))
    return render_template('login.html', error=error)

# M3U8 channels route (accessible after login)
@app.route('/channels')
def channels():
    # Here you can implement the logic for serving M3U8 channels
    return "Welcome to the M3U8 channels page!"

if __name__ == '__main__':
    app.run(debug=True)
 
