from flask import *
import os

os.system("pip install -r requirements.txt")
app = Flask(__name__)

class Book:
    was_created = False
    content = ''

@app.route('/', methods = ['post', 'get'])
def home_screen():
    res = "Welcome, {}!".format(os.getlogin())
    next_page = request.form.get("next")
    if next_page == 'Create':
        return redirect(url_for('create_screen'))
    elif next_page == 'Read':
        return redirect(url_for('read_screen'))
    elif next_page == 'Update':
        return redirect(url_for('update_screen'))
    elif next_page == 'Delete':
        return redirect(url_for('delete_screen'))
    return render_template("home_screen.html", template_string = res)

@app.route('/create/', methods = ['post', 'get'])
def create_screen():
    if request.form.get("next") == 'Exit':
        return redirect(url_for('home_screen'))
    t = render_template("create_book_screen.html", was_created = Book.was_created)
    Book.was_created = True
    Book.content = 'There are no words in your Book. It\'s time to fix it!'
    return t

@app.route('/read/', methods = ['post', 'get'])
def read_screen():
    if request.form.get("next") == 'Exit':
        return redirect(url_for('home_screen'))
    return render_template("read_book_screen.html", was_created = Book.was_created, content = Book.content)

@app.route('/update/', methods = ['post', 'get'])
def update_screen():
    if request.form.get("next") == 'Exit':
        return redirect(url_for('home_screen'))
    new_content = request.form.get('content')
    if new_content != None:
        Book.content = new_content
    return render_template("update_book_screen.html", was_created = Book.was_created)

@app.route('/delete/', methods = ['post', 'get'])
def delete_screen():
    answer = request.form.get('answer')
    if request.form.get('next') == 'Exit':
        return redirect(url_for('home_screen'))
    if answer == 'Yes':
        Book.was_created = False
        return redirect(url_for('home_screen'))
    elif answer == 'No':
        return redirect(url_for('home_screen'))
    return render_template("delete_book_screen.html", was_created = Book.was_created)

if __name__ == "__main__":
    app.run()