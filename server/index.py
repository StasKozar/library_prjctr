from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

books = [

]


@app.route('/books', methods=['GET'])
def books():



@app.route('/rent', methods=['POST'])
def rent():



# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)