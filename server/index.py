from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

books = [

]


@app.route('/books', methods=['GET'])
def books():



@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.json
    book_id = data.get("id")
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
    app.run(debug=True)



# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)