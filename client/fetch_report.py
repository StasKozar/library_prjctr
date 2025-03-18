import requests
import sys

def search_books(author=None, title=None):
    url = 'http://127.0.0.1:5000/books'
    params = {}
    if author:
        params['author'] = author
    if title:
        params['title'] = title
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        books = response.json()
        print("Books found:")
        for book in books:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("Error:", response.json().get("error", "Unknown error"))

def rent_book(book_id, start_date, end_date):
    url = 'http://127.0.0.1:5000/rent'
    data = {
        "id": book_id,
        "start_date": start_date,
        "end_date": end_date
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("Book rented successfully!")
    else:
        print("Error:", response.json().get("message", "Unknown error"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_report.py <command> [parameters]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "search":
        if len(sys.argv) != 4:
            print("Usage: python fetch_report.py search <author or title> <value>")
            sys.exit(1)
        search_books(sys.argv[2], sys.argv[3])
    
    elif command == "rent":
        if len(sys.argv) != 6:
            print("Usage: python fetch_report.py rent <book_id> <start_date> <end_date>")
            sys.exit(1)
        rent_book(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Unknown command")
