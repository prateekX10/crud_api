from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data (can be replaced with database)
books = [
    {"id": 1, "tittle": "Book 1", "author": "Author 1"},
    {"id": 2, "tittle": "Book 2", "author": "Author 2"},
    {"id": 3, "tittle": "Book 3", "author": "Author 3"}
]

# Get all books
@app.route('/books', methods = ['GET'])
def get_books():
 return (books)


#Get a specific book by ID
@app.route('/books/<int:book_id>', methods = ['GET'])
def get_book(book_id):
 for book in books:
  if book['id'] == book_id:
   return book
  
 return {'error': 'book not found'} 

#Create a book
@app.route('/books', methods = ['POST'])
def create_book():
 new_book = {'id':len(books)+1, 'tittle':request.json['tittle'], 'author':request.json['author']}
 books.append(new_book)
 return new_book

#Update a book
@app.route('/books/<int:book_id>', methods = ['PUT'])
def update_book(book_id):
 for book in books:
  if book['id'] == book_id:
   book['tittle']=request.json['tittle']
   book['author']=request.json['author']
   return book
 return {'error':'book not found'} 

#Delete a book
@app.route('/books/<int:book_id>', methods = ['DELETE'])
def delete_book(book_id):
 for book in books:
  if book['id'] == book_id:
   books.remove(book)
   return {"Data":"Books removed successfully"}
 return {"error":"book not found"}
   

if __name__ == '__main__':
 app.run(debug=True)