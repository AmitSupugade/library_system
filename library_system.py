
# =============================================================================
#
# Implemented by Amit Supugade
#
# =============================================================================
"""
Problem statement-
    This is a (simplistic) library of books and users where we can add books
    and users, and allow users to checkout those books. As this library exists
    in the land of Utopia, there are no due dates for books being checked out.
    However, we're not going to let this be a free-for-all, and so a user can
    only checkout a total of MAX_LOANS_PER_USER books at a time.
	
Assumption- All objects are created with correct arguments.
"""


#Implementation of Book class
class Book(object):
    
    #Initialize book object
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        
    #Function to return isbn of a book
    def get_isbn(self):
        return self.isbn

    #Function to return title of a book
    def get_title(self):
        return self.title
		

#Implementation of User class
class User(object):
    
    #Initialize User object
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    #Function to return email of user
    def get_email(self):
        return self.email
  
    #Function to return first name of user
    def get_first_name(self):
        return self.first_name

    #Function to return last name of user
    def get_last_name(self):
        return self.last_name



"""
Library data storage:
self.books-
self.books contains all the information about books in the
library. It is dictionary with isbn as key storing another dictionary
with three keys as 'book','total','available' which stores book object,
total book count and available book count respectively.

self.users-
self.users contains all the information about users of
library. It is dictionary with email as key storing another dictionary
with two keys as 'user' storing user object and 'books' storing list of
books checked out by user.

The data is stored in dictionaries to store it in structured format.
"""

#Implementation of Library class
class Library(object):
    MAX_LOANS_PER_USER = 5

    #Initialize Library object
    def __init__(self):
        self.books = {} #isbn : {'book': book_object, 'total': total_count, 'available': available_count}
        self.users = {} #email : {'user': user_object, 'books': []} 



    #Function to check and raise ValueError
    def is_valueError(self, o):
        if o == None:
            raise ValueError("Null Object")


        
    #Function to check and raise KeyError
    def is_keyError(self, o):
        if o == None:
            raise KeyError("Invalid object")


        
    #Function to add a new book to the library
    def add_book(self, book):
        self.is_valueError(book)
        isbn = book.get_isbn()
        
        if not self.books.has_key(isbn):
            self.books[isbn] = {'book': book, 'total': 1 , 'available': 1}
            return self.books[isbn]['total']
        elif self.books[isbn]['book'].get_title() == book.get_title():
            self.books[isbn]['total'] += 1
            self.books[isbn]['available'] += 1
            return self.books[isbn]['total']
        else:
            return False



    #Function to return the list of all books    
    def get_books(self):
        list_books = []
        for value in self.books.itervalues():
            list_books.append(value['book'])
        return list_books



    #Function to return a particular book with the given ISBN number
    def get_book(self, isbn):
        self.is_valueError(isbn)
        if self.books.has_key(isbn):
            return self.books[isbn]['book']
        else:
            return None



    #Function to get an number of total books in the library
    def get_number_of_books(self, unique=True):
        count = 0
        if unique:
            count = len(self.books.keys())
        else:
            for value in self.books.itervalues():
                count += value['total']
        return count



    #Function to get number of total copies of book with the given ISBN
    def get_number_of_copies(self, isbn):
        count = 0
        self.is_valueError(isbn)
        if self.books.has_key(isbn):
            count = self.books[isbn]['total']
        return count


    
    #Function to get number of available copies of book with the given ISBN
    def get_number_of_available_copies(self, isbn):
        count = 0
        self.is_valueError(isbn)
        if self.books.has_key(isbn):
            count = self.books[isbn]['available']
        return count


    
    #Function to search all books by title
    def search_books_by_title(self, title):
        list_books = []
        self.is_valueError(title)
        title = title.lower()
        for value in self.books.itervalues():
            if value['book'].get_title().lower().find(title) != -1:
                list_books.append(value['book'])
        return list_books
    


    #Function to add a new user to the library
    def add_user(self, user):
        self.is_valueError(user)
        email = user.get_email().lower()
        if self.users.has_key(email):
            raise ValueError
        else:
            self.users[email] = {'user': user, 'books': []}
        if self.users.has_key(email):
            return True
        return False



    #Function to get list of all users
    def get_users(self):
        list_users = []
        for value in self.users.itervalues():
            list_users.append(value['user'])
        return list_users



    #Function to get user by email
    def get_user_by_email(self, email):
        self.is_valueError(email)
        email = email.lower()
        if self.users.has_key(email):
            return self.users[email]['user']
        else:
            return None

    
    #Function to search all users by email
    def search_users_by_email(self, email):
        list_users = []
        self.is_valueError(email)
        email = email.lower()
        for key in self.users.iterkeys():
            if key.find(email) != -1:
                list_users.append(self.users[key]['user'])
        return list_users



    #Function to check if book has been checked out by user
    def is_checked_out(self, email, isbn):
        for b in self.users[email]['books']:
            if b.get_isbn() == isbn:
                return True
        return False


        
    #Function to allow the user to checkout an book
    def checkout_book(self, user, book):
        self.is_valueError(user)
        self.is_valueError(book)
        isbn = book.get_isbn()
        email = user.get_email().lower()
        u = self.get_user_by_email(email)
        self.is_keyError(u)
        b = self.get_book(isbn)
        self.is_keyError(b)
        
        if len(self.users[email]['books']) >= self.MAX_LOANS_PER_USER:
            return False
        if self.is_checked_out(email, isbn):
            return False
        if self.books[isbn]['available'] <= 0:
            return False
        
        self.users[email]['books'].append(b)
        self.books[isbn]['available'] -= 1
        if self.is_checked_out(email, isbn):
            return True
        return False



    #Function to allow the user to return an book
    def return_book(self, user, book):
        self.is_valueError(user)
        self.is_valueError(book)
        isbn = book.get_isbn()
        email = user.get_email().lower()
        u = self.get_user_by_email(email)
        self.is_keyError(u)
        b = self.get_book(isbn)
        self.is_keyError(b)

        if not self.is_checked_out(email, isbn):
            raise ValueError

        self.users[email]['books'].remove(b)
        self.books[isbn]['available'] += 1
        if not self.is_checked_out(email, isbn):
            return True
        return False
        


    #Function to get list of Books that the user has checked out
    def get_checkouts_for_user(self, user):
        self.is_valueError(user)
        email = user.get_email().lower()
        u = self.get_user_by_email(email)
        self.is_keyError(u)
        return self.users[email]['books']


    
# =============================================================================
#
#END
#
# =============================================================================


########################################################################

"""
library = Library()
library.add_book(Book('12345', u"Catcher in the Rye"))
library.add_book(Book('12346', u"Catcher in the Rye"))
library.add_book(Book('12347', u"Catcher in the Rye"))
library.add_book(Book('12348', u"Catcher in the Rye"))
library.add_book(Book('12349', u"Catcher in the Rye"))
library.add_book(Book('34567', u"To Kill A Mockingbird"))
library.add_book(Book('34567', u"To Kill A Mockingbird"))
library.add_book(Book('12345', u"Catcher in the Rye"))

library.add_user(User(u"john@doe.com", u"John", u"Doe"))
library.add_user(User(u"susan@doe.com", u"Susan", u"Doe"))

book1 = library.get_book('12345')
book2 = library.get_book('12346')
book3 = library.get_book('12347')
book4 = library.get_book('12348')
book5 = library.get_book('12349')
book6 = library.get_book('34567')
user1 = library.get_user_by_email(u"susan@doe.com")
user2 = User(u"ron@doe.com", u"John", u"Doe")
book7 = Book('29870', u"Catcher in the Rye")
library.checkout_book(user1, book1)
try:
    library.checkout_book(user1, book1)
except KeyError:
    print "Expected!!"
library.checkout_book(user1, book2)
library.checkout_book(user1, book3)
library.checkout_book(user1, book4)
library.checkout_book(user1, book5)

print "********************************************"
print library.get_books()
print "********************************************"
print library.get_users()
print "********************************************"

print len(library.get_checkouts_for_user(user1))
print library.get_number_of_copies('12345')
print "12349", library.get_number_of_available_copies('12349')

library.return_book(user1, book1)

print library.get_checkouts_for_user(user1)
#print library.search_books_by_title('KilL')
#print library.get_user_by_email('susan@doe.com')
#print library.search_users_by_email('@doe.c')

"""
########################################################################

if __name__ == '__main__':

    library = Library()

    library.add_book(Book('12345', u"Catcher in the Rye"))
    assert library.get_number_of_books(unique=True) == 1, "Oops!"
    assert library.get_number_of_books(unique=False) == 1, "Oops!"
    assert library.get_number_of_copies('12345') == 1, "Oops!"

    library.add_book(Book('12345', u"Catcher in the Rye"))
    assert library.get_number_of_books(unique=True) == 1, "Oops!"
    assert library.get_number_of_books(unique=False) == 2, "Oops!"
    assert library.get_number_of_copies('12345') == 2, "Oops!"

    library.add_book(Book('12345', u"Catcher in the Rye"))
    assert library.get_number_of_books(unique=True) == 1, "Oops!"
    assert library.get_number_of_books(unique=False) == 3, "Oops!"
    assert library.get_number_of_copies('12345') == 3, "Oops!"

    library.add_book(Book('23456', u"Moby Dick"))
    library.add_book(Book('23456', u"Moby Dick"))
    
    library.add_book(Book('34567', u"To Kill A Mockingbird"))
    
    # The following should not be allowed
    library.add_book(Book('34567', u"Diffrent title"))
    
    assert library.get_number_of_books(unique=True) == 3, "Oops!"
    assert library.get_number_of_books(unique=False) == 6, "Oops!"
    assert library.get_number_of_copies('23456') == 2, "Oops!"
    assert library.get_number_of_copies('34567') == 1, "Oops!"

    # Add some users
    library.add_user(User(u"john@doe.com", u"John", u"Doe"))
    library.add_user(User(u"susan@doe.com", u"Susan", u"Doe"))

    assert len(library.get_users()) == 2, "Oops!"

    try:
        library.add_user(User(u"John@Doe.com", u"John", u"Doe"))
    except ValueError:
        pass
    else:
        raise RuntimeError("Oops!")

    # Search for a book and user
    mockingbird = library.search_books_by_title("Mockingbird")[0]
    susan = library.search_users_by_email("susan")[0]

    assert mockingbird.isbn == '34567', "Oops!"
    assert susan.email == u"susan@doe.com", "Oops!"

    # Checkout a book
    library.checkout_book(susan, mockingbird)

    assert len(library.get_checkouts_for_user(susan)) == 1, "Oops!"
    assert library.get_number_of_available_copies(mockingbird.isbn) == 0, "Oops!"

    # Can't check it out twice!
    assert library.checkout_book(susan, mockingbird) == False, "Oops!"

    # Get a user by email
    john = library.get_user_by_email(u"john@doe.com")

    # Try to checkout the book that is not available
    assert library.checkout_book(john, mockingbird) == False, "Oops!"
    assert len(library.get_checkouts_for_user(john)) == 0, "Oops!"

    # Return the book
    library.return_book(susan, mockingbird)
    assert library.get_number_of_available_copies(mockingbird.isbn) == 1, "Oops!"

    assert library.checkout_book(john, mockingbird) == True, "Oops!"
    assert len(library.get_checkouts_for_user(john)) == 1, "Oops!"

    assert library.get_number_of_available_copies(mockingbird.isbn) == 0, "Oops!"

    print "Success!!"