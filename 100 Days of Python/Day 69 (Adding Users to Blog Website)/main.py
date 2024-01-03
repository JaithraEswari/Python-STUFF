from datetime import date
from flask import Flask, abort, render_template, redirect, request, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = relationship('User', back_populates='blogposts')
    author_id = db.Column(db.Integer, ForeignKey('users.id'),nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    blog_comments = relationship('Comment',back_populates='parent_post')

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    blogposts = relationship('BlogPost',back_populates='author')
    user_comment = relationship('Comment',back_populates='comment_author')

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    comment_author = relationship('User', back_populates='user_comment')
    parent_post= relationship('BlogPost', back_populates='blog_comments')

with app.app_context():
    db.create_all()

def admin_only(func):
    @wraps(func)
    def function1(*args, **kwargs):
        if current_user.id == 1:
            func(*args, **kwargs)
        else:
            abort(403)
    return function1

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET','POST'])
def register():
    register_user = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user :
            flash('User already registered, Login with your email address')
            return redirect('login')
        else:
            new_user = User(email = request.form.get('email'),
                                name = request.form.get('name'),
                                password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)) # type: ignore
        
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("get_all_posts"))
    return render_template("register.html", form= register_user)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('That email does not exist, please try again')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password): # type: ignore
            flash('Password incorrect, Please try again')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form= login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):
    comment_form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
    if request.method == "POST":
        if current_user.is_authenticated:
            new_comment = Comment(
                text=request.form.get('comment'),
                comment_author = current_user,
                parent_post = requested_post
            )
            db.session.add(new_comment)
            db.session.commit()
        else:
            flash('Need to be logged in')
            return redirect('login')
    return render_template("post.html", post=requested_post, form=comment_form, gravatar=gravatar)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if request.method == "POST":
        new_post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            body=request.form.get('body'),
            img_url=request.form.get('img_url'),
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        ) # type: ignore
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)