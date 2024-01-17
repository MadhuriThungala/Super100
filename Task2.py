class Lib:
    def __init__(self):
        self.available_books = []
        self.members = []
    def new_membership(self, member):
        if member not in self.members:
            self.members.append(member)
        else:
            print(f"Member with {member_name}  is already present")
    def cancel_membership(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print("member not exists")
    def add_book(self,name_of_book):
        if name_of_book not in self.available_books:
            self.available_books.append(name_of_book)
        else:
            print("Book is available")
class Book:
    def __init__(self, name_of_book, count):
        self.name_of_book = book_name
        self.count = count
    def borrows(self):
        if(self.count>0):
            self.count-=1
            return True
        else:
            return False
    def returns(self):
        self.counts+=1
class Member:
    def __init__(self, name):
        self.name = name
        self.books_taken = []
    def borrow_book(self, book):
        self.books_taken.append(book)
    def return_book(self,book):
        self.books_taken.remove(book)
