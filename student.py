
from database import Data

class Student:
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
        
    def __str__(self):
        return (f"""
                \t\t\tStudent ID     : {self.id}
                \t\t\tStudent Name   : {self.name}\n""")
            
    
        