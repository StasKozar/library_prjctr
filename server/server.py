from flask import Flask, jsonify, request

# Create a Flask application instance
app = Flask(__name__)

books = [
    {"id": 1, "author": "Jack London", "title": "The Call of the Wild", "rented_dates": []},
    {"id": 2, "author": "Jack London", "title": "White Fang", "rented_dates": []},
    {"id": 3, "author": "Jack London", "title": "The Sea-Wolf", "rented_dates": []}
]


@app.route('/books', methods=['GET'])
def get_books():
    result = []
    author = request.args.get('author')
    if not author:
        return jsonify(books), 200

    for book in books:
        if book['author'] == author:
            result.append(book)

    if not result:
        return jsonify("No books found"), 404

    return jsonify(result), 200


@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.json
    book_id = int(data.get("id"))
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    for period in book["rented_dates"]:
        if not (end_date < period["start_date"] or start_date > period["end_date"]):
            return jsonify({"message": "The book is already rented for these dates"}), 400

    book["rented_dates"].append({"start_date": start_date, "end_date": end_date})
    return jsonify({"message": "Book rented successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)