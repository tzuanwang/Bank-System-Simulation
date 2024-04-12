# Implement a library management system which will handle the following tasks:
# 1. Customer should be able to display all the books available in the library
# 2. Handle the process when a customer requests to borrow a book
# 3. Update the library collection when the customer returns a book

# Class => Library
# Layers of abstraction => display available books, lend a book, add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book

class Library:

    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks

    def displayBook(self):
        print()
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('You have now borrow the book.')
            self.availableBooks.remove(requestedBook)
        else:
            print('Sorry, the book is not available in our list.')

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book. Thank you!')


class Customer:
    def requestBook(self):
        print('Enter a book you would like to borrow: ')
        self.book = input()
        return self.book

    def returnBook(self):
        print('Enter the name of the book which you are returning: ')
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich', 'Who Will Cry When You Die', 'For One More Day'])
customer = Customer()

while True:
    print('Enter 1 to display the available books.')
    print('Enter 2 to request for a book.')
    print('Enter 3 to return a book.')
    print('Enter 4 to exit.')

    userChoice = int(input())

    if userChoice == 1:
        library.displayBook()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    else:
        quit()