from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data to serve through the API
books = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year_published': 1925
    },
    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year_published': 1960
    }
]


# Define API endpoints
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})


@app.route('/api/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ''),
        'year_published': request.json.get('year_published', '')
    }
    books.append(book)
    return jsonify({'book': book}), 201


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    book = book[0]
    if not request.json:
        abort(400)
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    book['year_published'] = request.json.get('year_published', book['year_published'])
    return jsonify({'book': book})


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
