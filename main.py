from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from api_fetch import get_book_info
from functions import hash_password
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = b'test_secret_key_1004'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    desc = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=True)
    page_count = db.Column(db.Integer, nullable=True)


class Users(UserMixin, db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(250), nullable=False)
    user_email = db.Column(db.String(250), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        desc, date, page_count, avg_rating = get_book_info(title)
        new_book = Book(user_id=f'{current_user.user_email.split("@")[0]}', title=title, author=author, rating=avg_rating, desc=desc,
                        date=date,
                        page_count=page_count)
        db.session.add(new_book)
        db.session.commit()
    books = db.session.execute(db.select(Book).order_by(Book.id)).fetchall()
    return render_template('index.html', books=books)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/info/<int:book_id>')
def book_info(book_id):
    book = db.get_or_404(Book, book_id)
    return render_template('info.html', book=book)


@app.route('/signout')
def sign_out():
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']
        password = hash_password(request.form['user_password'])
        split_email = email.split('@')[0]
        new_user = Users(user_id=split_email, user_name=name, user_email=email, user_password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['user_email']
        split_email = email.split('@')[0]
        password = request.form['user_password']
        user = Users.query.filter_by(user_email=email).first()
        books = db.session.execute(db.select(Book).order_by(Book.id)).fetchall()
        login_user(user)
        return redirect(url_for('home'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()