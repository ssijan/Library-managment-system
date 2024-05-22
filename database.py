import csv
import os
from books import *

class Data:
    def __init__(self) -> None:
        pass
    def valid(self, id, pas):
        status=False
        from student import Student
        with open('students.csv',mode='r',encoding='utf=8') as file:
            read_ob=csv.reader(file)
            for row in read_ob:
                if row[0]==id and row[2]==pas:
                    status=Student(row[0],row[1],row[2])
                    break
        return status
    
    def save_st_info(self,ob):
        info=[ob.id,ob.name,ob.pas]
        with open('students.csv',mode='a',newline='',encoding='utf-8') as file:
            write_ob=csv.writer(file)
            write_ob.writerow(info)
            
    def view_books(self):
        cnt=1
        with open('books.csv',mode='r') as file:
            vw=csv.reader(file)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                All Books               |')
            print('\t\t\t\t------------------------------------------')
            for data in vw:
                self.display(data)
                if cnt%4==0:
                    n=input('Press enter to view more...\nPress other key to exit\n-->')
                    if len(n)!=0:
                        break
                cnt+=1
    
    def display(self,data):
        print(f"""
              \t\t\t\tBook ID           : {data[0]}
              \t\t\t\tBook Name         : {data[1]}
              \t\t\t\tBook Author       : {data[2]}
              \t\t\t\tBook Copies       : {data[3]}
              \t\t\t\tBook Status       : {data[4]}\n""")

    def valid_li(self, id, pas):
        status=False
        from librarian import Librarian
        with open('librarian.csv',mode='r',encoding='utf=8') as file:
            read_ob=csv.reader(file)
            for row in read_ob:
                if row[0]==id and row[2]==pas:
                    status=Librarian(row[0],row[1],row[2])
                    break
        return status

    def save_li_info(self,ob):
        info=[ob.id,ob.name,ob.pas]
        with open('librarian.csv',mode='a',newline='',encoding='utf-8') as file:
            write_ob=csv.writer(file)
            write_ob.writerow(info)   
                
    def save_book(self,book_ob):
        info=[book_ob.book_id,book_ob.book_name,book_ob.book_author,book_ob.book_copies,book_ob.book_availability_status]
        with open('books.csv',mode='a',newline='',encoding='utf-8') as file:
            wr_book=csv.writer(file)
            wr_book.writerow(info)
    
    def view_and_select_book(self,book_info):
        status=False
        with open('books.csv',mode='r',encoding='utf-8') as file:
            ob_book=csv.reader(file)
            for i in ob_book:
                if i[0]==book_info or i[1]==book_info:
                    self.display(i)
                    status= i[0]
                    break
        return status
    
    def remove_book(self,ob_book):
        status = False
        with open('books.csv', mode='r', encoding='utf-8') as file:
            read = csv.reader(file)

            with open('temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                temp_books = csv.writer(temp_file)

                for book in read:
                    if book[0] == ob_book and not status:
                        status = book
                        continue
                    temp_books.writerow(book)

        os.remove('books.csv')
        os.rename('temp.csv', 'books.csv')  
        
        if status:
            status = Book(status[0], status[1], status[2], status[3])
        return status 
    

    def borrow_book(self,ob_book):
        status = False
        with open('books.csv', mode='r', encoding='utf-8') as file:
            read = csv.reader(file)
            
            with open('temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                temp_books = csv.writer(temp_file)
                for book in read:
                    cnt=int(book[3])
                    if book[0] == ob_book and cnt>0:
                        cnt-=1
                        book[3]=str(cnt)
                        if cnt<=0:
                            book[4]='Unavailable'
                        status=book
                    temp_books.writerow(book)
                    
        os.remove('books.csv')
        os.rename('temp.csv', 'books.csv') 
    
        if status:
            status = Book(status[0], status[1], status[2], status[3])
        return status 
    
    
    def return_book(self,ob_book):
        status = False
        with open('books.csv', mode='r', encoding='utf-8') as file:
            read = csv.reader(file)
            
            with open('temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                temp_books = csv.writer(temp_file)
                for book in read:
                    cnt=int(book[3])
                    if book[0] == ob_book :
                        cnt+=1
                        book[3]=str(cnt)
                        if cnt>0:
                            book[4]='Available'
                        status=book
                    temp_books.writerow(book)
                    
        os.remove('books.csv')
        os.rename('temp.csv', 'books.csv') 
    
        if status:
            status = Book(status[0], status[1], status[2], status[3])
        return status 
    
    
        
                