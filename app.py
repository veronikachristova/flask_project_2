from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/knihy/', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/knihy/', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

#DU:
#Získanie Konkrétnej Knižky

@app.route('/knihy/<int:id>', methods=['GET'])
def get_specific_book(id):
    hladane_id = id
    book = next((book for book in books if book['id'] == hladane_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Kniha s daným ID neexistuje'}), 404


#updatovanie title a autora knihy

@app.route('/knihy/<int:id>', methods=['PUT'])
def update_title_and_author(id):
    hladane_id = id
    title = request.json.get('title')
    author = request.json.get('author')
    book = next((book for book in books if book['id'] == hladane_id), None)
    if book:
        book['title'] = title
        book['author'] = author
        return jsonify(book), 200
    else:
        return jsonify({'error': f'Kniha s ID: {id} neexistuje'}), 404

#vymazanie knizky
@app.route('/knihy/<int:id>', methods=['DELETE'])
def delete_book(id):
    hladane_id = id
    book = next((book for book in books if book['id'] == hladane_id), None)
    if book:
        books.remove(book)
        return jsonify(f'Kniha s id:{id} bola vymazana'), 200
    else:
        return jsonify({'error': f'Kniha s ID: {id} neexistuje'}), 404


if __name__ == "__main__":
    app.run()


