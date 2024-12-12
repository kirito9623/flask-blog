from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Datos de ejemplo (podrías usar una base de datos)
posts = [
    {'id': 1, 'title': 'Primer Post', 'content': 'Contenido del primer post'},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Contenido del segundo post'},
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'id': len(posts) + 1, 'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == "__main__":
    app.run(debug=True)

    
    