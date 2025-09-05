from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('loginUsername')
        password = request.form.get('loginPassword')
        languages = request.form.getlist('language')
        age = request.form.get('age')

        if username and password:
            session['username'] = username
            session['languages'] = languages
            session['age'] = age
            return redirect(url_for('dashboard'))

        return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# For Vercel deployment
app = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True)