import sqlite3

db = sqlite3.connect('data/ebookstore')

cursor = db.cursor()

# # Create a table 
# cursor.execute(
#     '''
#     CREATE TABLE books (
#         id INTEGER, 
#         Title VARCHAR(255),
#         Author VARCHAR(255), 
#         Qty INTEGER
#     );
#     '''
# )

# db.commit()
# cursor.execute("delete from books")
# db.commit()

# cursor.execute(
#     '''
#     INSERT INTO books 
#     VALUES 
#     (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
#     (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
#     (3003,'The Lion, the Witch and the Wardrobe','C.S. Lewis', 25),
#     (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
#     (3005, 'Alice in Wonderland', 'Lewis Carroll',12)

#     '''
# )
# db.commit()


def add_book(id, title, author, qty): 
    cursor.execute(
        '''
        INSERT INTO books VALUES (?,?,?,?)
        ''', (id, title,author,qty)
    )
    db.commit()
    
def update_title(id, title): 
    cursor.execute(
        '''
        UPDATE books SET Title = ? WHERE id = ?
        ''', (title, id )
    )
    db.commit()
   
    
def update_author(id, author): 
    cursor.execute(
    '''
    UPDATE books SET Author = ? WHERE id = ?
    ''', (author,id)
)
    db.commit()

def update_quantity(id, quantity): 
    cursor.execute(
        '''
        UPDATE books SET Qty = ? WHERE id = ?
        ''', (quantity, id )
    )
    db.commit()
    
    
def delete_book(id):
    cursor.execute(
        '''
    DELETE FROM books WHERE id = ?
        ''', (id, )
    )
    db.commit()
    
def search_book_by_id(id): 
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
    book = cursor.fetchone()
    return book 
    



def search_book_by_title(title):
    cursor.execute('''SELECT * FROM books WHERE Title LIKE '%' || ? || '%' ''', (title,))
    books = cursor.fetchall()
    return books
        
    
    
def search_book_by_author(author):
    cursor.execute('''SELECT * FROM books WHERE Author LIKE '%' || ? || '%' ''', (author,))
    books = cursor.fetchall()
    return books