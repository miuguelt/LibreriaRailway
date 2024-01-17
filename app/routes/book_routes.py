from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.book import Book
from app import db

bp = Blueprint('book', __name__)

@bp.route('/')
def index():
    #data = Book.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    #return render_template('books/index.html', data=data)
    return "Entra a libros"

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('book.index'))

    return render_template('books/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        
        db.session.commit()
        
        return redirect(url_for('book.index'))

    return render_template('books/edit.html', book=book)

@bp.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get_or_404(id)
    
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('book.index'))
