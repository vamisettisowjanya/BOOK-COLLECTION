from flask import Flask, render_template, request, redirect, url_for, session


# Configure Flask to look for templates in the project root so we can render
# the existing index.html and login.html without moving files.
app = Flask(__name__, template_folder='.', static_folder='.')
app.secret_key = 'change-this-secret-key'


@app.route('/')
def home():
    # Render the landing page. The page already includes inline Jinja
    # expressions (e.g., {{ ('#home') }}), so use render_template.
    return render_template(
        'index.html',
        username=session.get('username'),
        languages=session.get('languages', []),
        age=session.get('age'),
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Collect form fields
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        languages = request.form.getlist('language')  # can be multiple
        age = request.form.get('age')

        # Very basic acceptance; add real auth as needed
        if not username or not password:
            # Re-render the page; the HTML has no error slot, so we simply reload
            return render_template('login.html')

        session['username'] = username
        session['languages'] = languages
        session['age'] = age

        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    # Use host='0.0.0.0' if you need external access on a network
    app.run(debug=True)