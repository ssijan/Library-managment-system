from books import *
from database import Data

class Librarian:
    def __init__(self,id,nm,pas):
        self.id=id
        self.pas=pas
        self.name=nm
    
    def view_books(self):
        dt=Data()
        dt.view_books()
        
        
    def borrow_books(self):
        bk_info=input('\t\t\t\t\tEnter Book Id or Name\n\t\t\t\t\t-->').strip()
        dt = Data()
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Before Borrow             |')
        print('\t\t\t\t------------------------------------------')
        selected_book_id = dt.view_and_select_book(bk_info)
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return

        status = dt.borrow_book(selected_book_id)

        if status:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             After Borrow               |')
            print('\t\t\t\t------------------------------------------')
            print(status)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|              Borrowed By               |')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|         Transaction Successful         |')
            print('\t\t\t\t------------------------------------------')
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|    Error  :  Book is not available     |')
            print('\t\t\t\t------------------------------------------')
            
            
    def return_books(self):
        bk_info=input('\t\t\t\t\tEnter Book Id or Name\n\t\t\t\t\t-->').strip()
        dt = Data()
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|           Before Return Book           |')
        print('\t\t\t\t------------------------------------------')
        selected_book_id = dt.view_and_select_book(bk_info)
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return

        status = dt.return_book(selected_book_id)

        if status:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|          After Return Book             |')
            print('\t\t\t\t------------------------------------------')
            print(status)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|              returned By               |')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|         Transaction Successful         |')
            print('\t\t\t\t------------------------------------------')
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|    Error  :  Book is not available     |')
            print('\t\t\t\t------------------------------------------')
  
  
    def add_books(self):
        try:
            print('\t\t\t\t\tEnter Book ID')
            book_id = input('\t\t\t\t\t-> ').strip()
            print('\t\t\t\t\tEnter Book Name')
            book_name = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter Book Author')
            book_author = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter No. of copies')
            book_copies = input('\t\t\t\t\t-> ').strip()

            if len(book_name) == 0 or len(book_author) == 0  or  int(book_copies) <= 0:
                raise Exception('Invalid Input')
        except Exception as exp:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|           Some Error occur             |')
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t\t\t{exp}')
            print('\t\t\t\t------------------------------------------')

        else:
            dt=Data()
            book_obj = Book(book_id,book_name,book_author,book_copies)

            dt.save_book(book_obj)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|               Book Saved               |')
            print('\t\t\t\t------------------------------------------')
            print(book_obj)
            print('\t\t\t\t------------------------------------------')

    def remove_books(self):
        bk_info=input('\t\t\t\t\tEnter Book Id or Name\n\t\t\t\t\t-->').strip()
        dt = Data()
        selected_book_id = dt.view_and_select_book(bk_info)
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|              No Book Found             |')
            print('\t\t\t\t------------------------------------------')
            return

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                 Alert!                 |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\tAre you sure to remove the book? Y/n')
        option = input('\t\t\t\t\t-> ')

        if option == 'Y':
            status = dt.remove_book(selected_book_id)
            if status:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|              Book Deleted              |')
                    print('\t\t\t\t------------------------------------------')
                    print(status)
                    print('\t\t\t\t------------------------------------------')
            else:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|         Error  :  Check Book ID        |')
                print('\t\t\t\t------------------------------------------')

        
    def __str__(self):
        return (f"""
                \t\t\tLibrarian ID     : {self.id}
                \t\t\tLibrarian Name   : {self.name}\n""")
            
        