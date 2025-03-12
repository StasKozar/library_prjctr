from flask import Flask, jsonify, request
from datetime import date

# Create a Flask application instance
app = Flask(__name__)

books = [
  {"id": 1, "author": "Jack London", "title": "The Call of the Wild"},
  {"id": 2, "author": "Jack London", "title": "White Fang"},
  {"id": 3, "author": "Jack London", "title": "The Sea-Wolf"}
]

rent = [
    {"id": 3, "start_date": "2024-01-01", "end_date": "2024-01-31"}
]

@app.route('/books', methods=['GET'])
def books():
    result = []
    author = request.args['author']
    if not author:
        return jsonify(books)

    for book in books:
        if book['author'] == author:
            result.append(book)

    return jsonify(result)



@app.route('/rent', methods=['POST'])
def rent():
    data = request.json
    book_id = data.get("id")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"})

    for period in book["rented_dates"]:
        if not (end_date < period["start_date"] or start_date > period["end_date"]):
            return jsonify({"message": "The book is already rented for these dates"})

    for rented_book in rent:
        if book_id == rented_book["id"]:

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)