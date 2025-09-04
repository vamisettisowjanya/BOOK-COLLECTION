from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os


# Configure Flask with absolute path
app = Flask(__name__)
app.secret_key = 'change-this-secret-key'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Collect form fields
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        languages = request.form.getlist('language')  # can be multiple
        age = request.form.get('age')

        session['username'] = username
        session['languages'] = languages
        session['age'] = age

        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# Add this at the bottom
app = app.wsgi_app

if __name__ == '__main__':
    # Use host='0.0.0.0' if you need external access on a network
    app.run(debug=True)