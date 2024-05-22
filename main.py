import csv
import os
from login import *
from student import *
from librarian import *

def check(a,b):
    return len(a)<1 or len(b)<1

def start():
    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                  Home                  |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          1. Student Login              |')
        print('\t\t\t\t|          2. Student Register           |')
        print('\t\t\t\t|          3. Librarian Login            |')
        print('\t\t\t\t|          4. Librarian Register         |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress Enter To Exit')
        print('\t\t\t\t\tEnter Your Option')
        op=input('\t\t\t\t\t--> ').strip()
        if len(op)==0:
            break

        match op:
            case '1':
                print('\n\t\t\t\t\tStudent Id')
                st_id=input("\t\t\t\t\t-->").strip()
                st_pass=input("\t\t\t\t\tPassword\n\t\t\t\t\t-->").strip()
                if check(st_id,st_pass):
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|              Login Failed              |')
                    print('\t\t\t\t------------------------------------------')
                    
                else:
                    st_ob=info(st_id,st_pass)
                    
                    if st_ob:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|                 Welcome                |')
                        print('\t\t\t\t------------------------------------------')
                        print(st_ob)
                        st_options(st_ob)
                    else:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|         Invalid Id or Password         |')
                        print('\t\t\t\t------------------------------------------')
                    
            case '2':
                status=False
                while True:
                    st_nm=input("\t\t\t\t\tEnter Your Name\n\t\t\t\t\t-->").strip()
                    st_id=input('\t\t\t\t\tEnter Your Id\n\t\t\t\t\t-->').strip()
                    st_pass1=input("\t\t\t\t\tPassword\n\t\t\t\t\t-->").strip()
                    st_pass2=input("\t\t\t\t\tConfirm Password\n\t\t\t\t\t-->").strip()
                    if check(st_nm,st_id) or check(st_pass2,st_pass1) or st_pass1 != st_pass2: 
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|               Plz Recheck              |')
                        print('\t\t\t\t------------------------------------------')

                    else:
                        status=True
                        break
                    op2=input('\t\t\t\t\tPress Enter To Continue...\n\t\t\t\t\tPress Any Key To Exit\n\t\t\t\t\t-->').strip()
                    if len(op2)!=0:
                        break 
                
                if status:
                    object=Student(st_id,st_nm,st_pass1)
                    save_info(object)
            case '3':
                lib_id=input('\t\t\t\t\tEnter Your ID\n\t\t\t\t\t-->').strip()
                lib_pass=input('\t\t\t\t\tPassword\n\t\t\t\t\t-->').strip()
                if check(lib_id,lib_pass):
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|              Login Failed              |')
                    print('\t\t\t\t------------------------------------------')
                else:
                    lib_ob=info_li(lib_id,lib_pass)
                    if lib_ob:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|                 Welcome                |')
                        print('\t\t\t\t------------------------------------------')
                        print(lib_ob)
                        lib_options(lib_ob)
                    else:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|         Invalid Id or Password         |')
                        print('\t\t\t\t------------------------------------------')
            case '4':
                status=False
                while True:
                    lib_id=input('\t\t\t\t\tEnter Your id\n\t\t\t\t\t-->').strip()
                    lib_nm=input('\t\t\t\t\tEnter Your Name\n\t\t\t\t\t-->').strip()
                    lib_pass1=input('\t\t\t\t\tPassword\n\t\t\t\t\t-->').strip()
                    lib_pass2=input('\t\t\t\t\tConfirm Password\n\t\t\t\t\t-->').strip()
                    if check(lib_id,lib_nm) or check(lib_pass1,lib_pass2) or lib_pass2!=lib_pass1:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|               Plz Recheck              |')
                        print('\t\t\t\t------------------------------------------')

                    else :
                        status=True
                        break
                    op2=input('\t\t\t\t\tPress Enter To Continue...\n\t\t\t\t\tPress Any Key To Exit\n\t\t\t\t\t-->').strip()
                    if len(op2)!=0:
                        break 
                if status:
                    object=Librarian(lib_id,lib_nm,lib_pass1)
                    save_li_info(object)
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|              Invalid Input              |')
                print('\t\t\t\t------------------------------------------')



def st_options(st_ob):
    wr_op=3
    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Student Menu              |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             1. View Books              |')
        print('\t\t\t\t|             2. Borrow Books            |')
        print('\t\t\t\t|             3. Return Books            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress Enter To Exit')
        print('\t\t\t\t\tEnter Your Option ')
        choice=input('\t\t\t\t\t-->').strip()
        if check(choice,'ab') or wr_op<=0:
            break
        match choice:
            case '1':
                st_ob.view_books()
            case '2':
                st_ob.borrow_books()
            case '3':
                st_ob.return_books()
            case _:
                wr_op-=1
                print('\t\t\t\t------------------------------------------')
                print("\t\t\t\t|             Wrong Option               |")
                print("\t\t\t\t|      Remaining attempts : {wr_op}      |")
                print('\t\t\t\t------------------------------------------')

def lib_options(lib_ob):
    wr_op=3
    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Librarian Menu            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             1. View Books              |')
        print('\t\t\t\t|             2. Borrow Books            |')
        print('\t\t\t\t|             3. Return Books            |')
        print('\t\t\t\t|             4. Add Books               |')
        print('\t\t\t\t|             5. Remove Books            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress Enter To Exit')
        print('\t\t\t\t\tEnter Your Option ')
        choice=input('\t\t\t\t\t-->').strip()
        if check(choice,'ab') or wr_op<=0:
            break
        match choice:
            case '1':
                lib_ob.view_books()
            case '2':
                lib_ob.borrow_books()
            case '3':
                lib_ob.return_books()
            case '4':
                lib_ob.add_books()
            case '5':
                lib_ob.remove_books()
            case _:
                wr_op-=1
                print('\t\t\t\t-------------------------------------------')
                print("\t\t\t\t|              Wrong Option               |")
                print("\t\t\t\t|       Remaining Attempts : {wr_op}      |")
                print('\t\t\t\t-------------------------------------------')

                
def create(file_name):

    check_file = os.path.isfile(file_name)
    if check_file:
        return
    with open(file_name,mode='w') as file:
        pass
        #csv_writer=csv.writer(file)
  
def create_files():
    create('students.csv')
    create('librarian.csv')
    create('books.csv')
    create('borrow.csv')

create_files()
start()