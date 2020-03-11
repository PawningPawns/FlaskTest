from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = '1ef49e123ade35471031b544a7240d1f'

posts = [

    {
        'author': 'Neil Pasricha',
        'title': 'Blogpost 1',
        'content': 'The Book of Awesome',
        'date_posted': 'March 9 2020'
    },

    {

        'author': 'John Doe',
        'title': 'Blogpost 2',
        'content': 'The Book of Something',
        'date_posted': 'March 10 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.date}!', 'success')
        return redirect(url_for(home))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
