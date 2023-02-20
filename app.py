from database import add_book, update_title, update_author, update_quantity, delete_book, search_book_by_author,search_book_by_id,search_book_by_title

def select_menu(): 
    return int(input("""
                    0. Exit
                    1. Add a book 
                    2. Uodate a book 
                    3. Delete a book 
                    4. Search for a book
                """))
    
def update_book_info():
    id = int(input("Id: "))
    while True:
        selected = int(input(("""
            What do you want to update:
            0. Exit 
            1. Title 
            2. Author 
            3. Quantity 
            """)))
        if selected == 0: 
            break;
        elif selected == 1: 
            title = input("Title: ")
            update_title(id, title)
        elif selected == 2: 
            author = input("Author: ")
            update_author(id, author)
        elif selected ==3: 
            quantity = input("Quantity: ")
            update_quantity(id, quantity)
   
def search_book():
    while True:
        selected = int(input(("""
            Search for books by:
            0. Exit 
            1. Id
            2. Title
            3. Author 
            """)))
        if selected == 0: 
            break;
        elif selected == 1: 
            id = int(input("Id: "))
            book = search_book_by_id(id)
            if book != None: 
                print( f"""
            Id:        {book[0]}
            Title:     {book[1]}
            Author:    {book[2]}
            Quantity:  {book[3]}
        
        """)
            else: 
                print("No such book found")
            
        elif selected == 2: 
            title = input("Title: ")
            books =search_book_by_title(title)
            if len(books) !=0:
                for book in books: 
                    print( f"""
                Id:        {book[0]}
                Title:     {book[1]}
                Author:    {book[2]}
                Quantity:  {book[3]}
            
            """)
            else: 
                print("No such book found")
           
        elif selected ==3: 
            author = input("Author: ")
            books = search_book_by_author(author)
            if len(books) !=0:
                for book in books: 
                    print( f"""
                Id:        {book[0]}
                Title:     {book[1]}
                Author:    {book[2]}
                Quantity:  {book[3]}
            
            """)
            else: 
                print("No such book found")
     
    


while True: 
    selected = select_menu()
    if selected == 0: 
        break
    elif selected == 1: 
        print("Adding a book")
        id = int(input("id: "))
        title = input("Title: ")
        author = input("Author: ")
        qty = int(input("Quantity: "))
        add_book(id,title,author,qty)
    elif selected == 2: 
        update_book_info()
    elif selected == 3: 
        id = int(input("Id: "))
        delete_book(id)
    elif selected == 4: 
        search_book()
        
        
        
        
    
    
