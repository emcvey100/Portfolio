#need to finish comments
class Book:
    """
    A class to represent a book.
    Attributes:
        isbn (str): The International Standard Book Number of the book.
        title (str): The title of the book.
        edition (int): The edition of the book.
        num_of_pages (int): The number of pages in the book.
        price (float): The price of the book.
        author (str): The author of the book.
        publisher (str): The publisher of the book.
        language (str): The language of the book.
        description (str): A brief description of the book.
        genre (list): A list of genres the book belongs to.
    Methods:
        set_edition(edition): Sets the edition of the book if not already set.
        set_num_of_pages(num_of_pages): Sets the number of pages if not already set.
        set_price(price): Changes the price of the book.
        add_genre(genre): Adds a genre to the book.
        add_description(description): Adds a description to the book.
        ISBN_check(isbn)
        __str__(): Returns a string representation of the book's information.
    """
    def __init__(self, isbn, title, language, author, num_of_pages=None, edition=None, price=5.99):
        """
        Constructs all the necessary attributes for the book object.
        Parameters:
            isbn (str): The International Standard Book Number of the book to set.
            title (str): The title of the book to set.
            language (str): The language of the book to set.
            author (str): The author of the book to set.
            num_of_pages (int): The number of pages in the book to set. Defaults to None.
            edition (int): The edition of the book to set. Defaults to None.
            price (float): The price of the book to set. Defaults to 5.99.
        """
        self.isbn = isbn
        self.title = title
        self.edition = edition
        self.num_of_pages = num_of_pages
        self.price = float(price)
        self.author = author
        self.publisher = None
        self.language = language
        self.description = None
        self.genre=[]
    def set_edition(self, edition):
        """
        Sets the edition of the book if not already set.
        Parameters:
            edition (int): The edition of the book to set.
        Returns:
            bool: True if the edition was set, False if it was already set.
        """
        if self.edition == None: #No edition is set
            self.edition = edition
            return True
        return False
    def set_num_of_pages(self, num_of_pages):
        """
        Sets the number of pages if not already set.
        Parameters:
            num_of_pages(int): The number of pages in the book to set.
        Returns:
            bool: True if the num_of_pages is set, False if it was already set.
        """
        if self.num_of_pages == None:
            self.num_of_pages = num_of_pages
            return True
        return False
    def set_price(self, price):
        """
        Changes the price of the book.
        Parameters:
            price(float): The changed price of the book.
        Returns:
            bool: When finished returns True.
        """
        self.price = float(price)
        return True
    def add_genre(self, genre):
        """
        Adds a genre to the book.
        Parameters:
            genre(str): A genre of the book to be added.
        Returns:
            bool: When finished returns True.
        """
        self.genre.append(genre)
        return True
    def add_description(self, description):
        """
        Adds a description to the book.
        Parameters:
            description(str): A description of the book to be set.
        Returns:
            bool: When finished returns True.
        """
        self.description = description
        return True
    def ISBN_check(self):
        """
        Checks if the isbn is real.
        Returns:
            bool: True if a real isbn, False if not real isbn.
        """
        if len(self.isbn) == 10:#ISBN-10 check digit
            total = 0
            for i in range(9):
                total += int(self.isbn[i]) * (10 - i)
            check_digit = (11 - (total % 11)) % 11
            if check_digit == 10:
                return self.isbn[9] == 'X'
            else:
                return check_digit == int(self.isbn[9])
        elif len(self.isbn) == 13:#ISBN-13 check digit
            total = 0
            for i in range(12):
                if i % 2 == 0:
                    total += int(self.isbn[i])
                else:
                    total += int(self.isbn[i]) * 3
            check_digit = (10 - (total % 10)) % 10
            return check_digit == int(self.isbn[12])
        else:#not ISBN-10 or ISBN-13
            return False
    def change_ISBN(self, isbn):
        """
        Change the ISBN number when ISBN number is incorrect.
        Parameters:
            isbn(int): An ISBN number to be set.
        Returns:
            bool: True when number has been set, False if ISBN number not set.
        """
        if self.ISBN_check:
            return False
        else:
            self.isbn = isbn
            return False
    def __str__(self):
        """
        Returns all the books' information as a string.
        Returns:
            str: A string of all the book's information
        """
        '''Return book information'''
        return_value= f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Language: {self.language}, Edition: {self.edition}, Price: ${self.price:.2f}"
        if self.description != None:
            return_value += f", Description: {self.description}"
        if self.genre!= []:
            return_value += f", Genre: {', '.join(self.genre)}"
        if self.publisher != None:
            return_value += f", Publisher: {self.publisher}"
        if self.edition != None:
            return_value += f", Edition: {self.edition}"
        if self.num_of_pages != None:
            return_value += f", Pages: {self.num_of_pages}"
        return return_value

class Bookshelf:
    """
    A class representing a bookshelf.
    Attributes:
        shelf(list[Book]): A list of Books with the bookshelf
    Methods:
        check_book(isbn): Checks if book is in shelf.
        remove_book(isbn): Removes book from the shelf.
        add_book(book): Adds book to the shelf.
    """
    def __init__(self):
        """Constructs the nesasary attributes for Bookshelf class. """
        self.shelf = []
    def check_book(self, isbn):
        """
        Checks if book is in shelf.
        Parameters:
            isbn(int): A ISBN number of what book wanted to return.
        Returns:
            Book: Returns the whole book on the shelf.
        """
        for book in self.shelf:
            if book.isbn == isbn:
                return book
        return None
    def remove_book(self, isbn):
        """
        Remove book from the shelf.
        Parameters:
            isbn(int): A ISBN number of the book removed.
        Returns:
            bool: Returns True if book removed.
        """
        for book in self.shelf:
            if book.isbn == isbn:
                self.shelf.remove(book)
                return True
        return False
    def add_book(self, book):
        """
        Adds book to the shelf.
        Parameters:
            book(Book): A book to be added to the shelf.
        """
        if type(book) == Book:
            self.shelf.append(book)
    def add_book():
        pass

class Shop:
    """
    A class representing a shop that sells and loans books.
    Attributes:
        bookshelfs(dictionary[Bookshelf]): A dictionary of bookshelfs at the shop.
        money(int): Money of the shop.
        loaned_books(list[Book]): List of books that are loaned.
    Methods:
        add_book(bookshelf, book):
        add_book(bookshelf, isbn, title, language, author, num_of_pages, edition, price)
        loan_book(bookshelf, isbn):
        return_book(bookshelf, isbn):
        sell_book(bookshelf, isbn):
        buy_book(bookshelf, isbn, title, language, author, num_of_pages=None, edition=1, price=0)
        buy_book()
        see_book
        change_book
    """
    def __init__(self):
        self.bookshelfs = {}
        self.money = 0
        self.loaned_books = Bookshelf()
    def add_book(self, bookshelf, book):
        if bookshelf in self.bookshelfs:
            self.bookshelfs[bookshelf].add_book(book)
        else:
            self.bookshelfs[bookshelf] = Bookshelf()
            self.bookshelfs[bookshelf].add_book(book)
    def add_book(self, bookshelf, isbn, title, language, author, num_of_pages=None, edition=1, price=5.99):
        if bookshelf in self.bookshelfs:
            self.bookshelfs[bookshelf].add_book(Book(isbn, title, language, author, num_of_pages, edition, price))
        else:
            self.bookshelfs[bookshelf] = Bookshelf()
            self.bookshelfs[bookshelf].add_book(Book(isbn, title, language, author, num_of_pages, edition, price))
    def loan_book(self, bookshelf, isbn):
        if bookshelf in self.bookshelfs:
            book = self.bookshelfs[bookshelf].check_book(isbn)
            if book:
                self.bookshelfs[bookshelf].remove_book(isbn)
                self.loaned_books.add_book(book)
                return True
        return False
    def return_book(self, bookshelf, isbn):
        if bookshelf in self.bookshelfs:
            book = self.loaned_books.check_book(isbn)
            if book:
                self.loaned_books.remove_book(isbn)
                self.bookshelfs[bookshelf].add_book(book)
                return True
        return False
    def sell_book(self, bookshelf, isbn):
        if bookshelf in self.bookshelfs:
            if self.bookshelfs[bookshelf].check_book(isbn):
                self.money += self.bookshelfs[bookshelf].check_book(isbn).price
                return True
        return False    
    def buy_book(self, bookshelf, isbn, title, language, author, num_of_pages=None, edition=1, price=0):
        self.add_book(bookshelf, isbn, title, language, author, num_of_pages, edition, price)
        self.money -= float(price)
    def buy_book(self, bookshelf, book):
        pass
    def see_books(self, bookshelf):
        if bookshelf in self.bookshelfs:
            return [book.book_info() for book in self.bookshelfs[bookshelf].shelf]
        return []
    def change_book(self, bookshelf, isbn, new_info, type_of_info):
        if bookshelf in self.bookshelfs:
            book = self.bookshelfs[bookshelf].check_book(isbn)
            if book:
                if type_of_info == "price":
                    x = book.set_price(new_info)
                elif type_of_info == "edition":
                    x = book.set_edition(new_info)
                elif type_of_info == "num_of_pages":
                    x = book.set_num_of_pages(new_info)
                elif type_of_info == "description":
                    x = book.add_description(new_info)
                elif type_of_info == "genre":
                    x = book.add_genre(new_info)
                return x
        return False

def trial():
    '''Trial function to test the Shop class and its methods'''
    shop = Shop()
    shop.add_book("Fiction", "978-3-16-148410-0", "The Great Gatsby", "English", "F. Scott Fitzgerald", 180, 1, 10.99)
    shop.add_book("Science", "978-0-262-03384-8", "A Brief History of Time", "English", "Stephen Hawking", 256, 1, 15.99)
    
    print(shop.bookshelfs["Fiction"].shelf[0].title)  # Output: The Great Gatsby
    print(shop.bookshelfs["Science"].shelf[0].title)  # Output: A Brief History of Time
    
    shop.loan_book("Fiction", "978-3-16-148410-0")
    print(len(shop.bookshelfs["Fiction"].shelf))  # Output: 0
    print(len(shop.loaned_books.shelf))  # Output: 1
    
    shop.sell_book("Science", "978-0-262-03384-8")
    print(shop.money)  # Output: 15.99

    shop.buy_book("Fiction", "978-1-56619-909-4", "To Kill a Mockingbird", "English", "Harper Lee", 281, 1, 12.99)
    shop.return_book("Fiction", "978-3-16-148410-0")
    x = shop.see_books("Fiction")
    for i in x:
        print(i)
        #Output:    Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 978-1-56619-909-4, Language: English, Edition: 1, Pages: 281, Price: $12.99
        #          Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 978-3-16-148410-0, Language: English, Edition: 1, Pages: 180, Price: $10.99
    shop.change_book("Fiction", "978-1-56619-909-4", 14.99, "price")
    shop.change_book("Fiction", "978-1-56619-909-4", 2, "edition")
    shop.change_book("Fiction", "978-1-56619-909-4", 300, "num_of_pages")
    shop.change_book("Fiction", "978-1-56619-909-4", "A novel about racial injustice.", "description")
    shop.change_book("Fiction", "978-1-56619-909-4", "Classic", "genre")
    shop.change_book("Fiction", "978-1-56619-909-4", "Drama", "genre")
    x = shop.see_books("Fiction")
    for i in x:
        print(i)
        #Output:  Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 978-1-56619-909-4, Language: English, Edition: 1, Pages: 281, Price: $14.99
        #         Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 978-3-16-148410-0, Language: English, Edition: 1, Pages: 180, Price: $10.99

####text version of functions to interact with the Shop class
def add_book(shop):
    '''Function to add a book to the shop'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    language = input("Enter language: ")
    author = input("Enter author: ")
    num_of_pages = input("Enter number of pages (optional): ")
    edition = input("Enter edition (optional): ")
    price = input("Enter price: ")
    if num_of_pages == "":
        num_of_pages = None
    if edition == "":
        edition = 1
    if price == "":
        price = 5.99
    shop.add_book(bookshelf, isbn, title, language, author, num_of_pages, edition, price)
def loan_book(shop):
    '''Function to loan a book from the shop'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    if shop.loan_book(bookshelf, isbn):
        print("Book loaned successfully!")
    else:
        print("Book not found.")
def sell_book(shop):
    '''Function to sell a book from the shop'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    if shop.sell_book(bookshelf, isbn):
        print("Book sold successfully!")
    else:
        print("Book not found.")
def buy_book(shop):
    '''Function to buy a book for the shop'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    language = input("Enter language: ")
    author = input("Enter author: ")
    num_of_pages = input("Enter number of pages (optional): ")
    edition = input("Enter edition (optional): ")
    price = input("Enter price: ")
    if num_of_pages == "":
        num_of_pages = None
    if edition == "":
        edition = 1
    if price == "":
        price = 0
    shop.buy_book(bookshelf, isbn, title, language, author, num_of_pages, edition, price)
def see_books(shop):
    '''Function to see books in a bookshelf'''
    bookshelf = input("Enter bookshelf name: ")
    books = shop.see_books(bookshelf)
    if books:
        for book in books:
            print(book)
    else:
        print("No books found.")
def change_book(shop):
    '''Function to change book information'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    type_of_info = input("Enter type of information to change (price, edition, num_of_pages, description, genre): ")
    new_info = input("Enter new information: ")
    if type_of_info in ["price", "edition", "num_of_pages"]:
        new_info = float(new_info) if type_of_info == "price" else int(new_info)
    if shop.change_book(bookshelf, isbn, new_info, type_of_info):
        print("Book information updated successfully!")
    else:
        print("Book not found or invalid information.")
def total_money_earned(shop):
    '''Function to see total money earned'''
    print(f"Total money earned: ${shop.money:.2f}")
def total_loaned_books(shop):
    '''Function to see total loaned books'''
    print(f"Total loaned books: {len(shop.loaned_books.shelf)}")
    print("Books in loaned books:")
    for book in shop.loaned_books.shelf:
        print(book.book_info())
    if len(shop.loaned_books.shelf) == 0:
        print("No books in loaned books.")
def see_all_books(shop):
    '''Function to see all books in the shop'''
    print("All books in the shop:")
    for bookshelf, books in shop.bookshelfs.items():
        print(f"Bookshelf: {bookshelf}")
        for book in books.shelf:
            print(book.book_info())
def return_book(shop):
    '''Function to return a book to the shop'''
    bookshelf = input("Enter bookshelf name: ")
    isbn = input("Enter ISBN: ")
    if shop.return_book(bookshelf, isbn):
        print("Book returned successfully!")
    else:
        print("Book not found in loaned books.")
def main_text():
    '''Main function to run the bookshop'''
    shop = Shop()
    open = True
    while open:
        print("Welcome to the Bookshop!")
        print("1. Add a book")
        print("2. Loan a book")
        print("3. Sell a book")
        print("4. Buy a book")
        print("5. See books in a bookshelf")
        print("6. Change book information")
        print("7. See total money earned")
        print("8. See loaned books")
        print("9. See all books in the shop")
        print("10. Return a book")
        print("11. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(shop)
        elif choice == "2":
            loan_book(shop)
        elif choice == "3":
            sell_book(shop)
        elif choice == "4":
            buy_book(shop)
        elif choice == "5":
            see_books(shop)
        elif choice == "6":
            change_book(shop)
        elif choice == "7":
            total_money_earned(shop)
        elif choice == "8":
            total_loaned_books(shop)
        elif choice == "9":
            see_all_books(shop)
        elif choice == "10":
            return_book(shop)
        elif choice == "11":
            open = False
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for visiting the Bookshop!")
    total_money_earned(shop)
    total_loaned_books(shop)
    see_all_books(shop)
    print("Goodbye!")

#trial()
main_text()
