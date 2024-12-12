from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Agregando la base de datos SQLALCHEMY

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Base de datos SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=db.func.now())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea las tablas definidas en los modelos
    app.run(debug=True)



# Datos de ejemplo (podrías usar una base de datos)
posts = [
    {'id': 1, 'title': 'Primer Post', 'content': 'Contenido del primer post'},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Contenido del segundo post'},
]

@app.route('/')
def index():
    posts = Post.query.all()  # Obtiene todas las publicaciones
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)  # Obtiene la publicación o devuelve un error 404
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)  # Crea una nueva instancia del modelo
        db.session.add(new_post)  # Agrega la publicación a la sesión
        db.session.commit()  # Guarda los cambios en la base de datos
        return redirect(url_for('index'))
    return render_template('new_post.html')



if __name__ == "__main__":
    app.run(debug=True)



    
    