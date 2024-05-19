

from login import *
 
def check(a,b):
    return len(a)<1 or len(b)<1
flag=True
while True:
    print("1.Student Login")
    print("2.Student Register")
    print("3.Librarian Login\n4.Librarian Register")
    print("Enter Your Option")
    op=input("-->").strip()

    match op:
        case '1':
            print('Student Id or Name')
            st_id=input("-->").strip()
            st_pass=input("Password\n-->").strip()
            if check(st_id,st_pass):
                print("Invalid Id or Password\n\n")
            else:
                st_ob=info(st_id,st_pass)
                if st_ob:
                    print("Succese\n")
                    print(st_ob)
                else:
                    print("Fail\n")
                
        case '2':
            
            while True:
                st_nm=input("Student Id or Name\n-->").strip()
                st_pass1=input("Password\n-->").strip()
                st_pass2=input("Confirm Password\n-->").strip()
                if check(st_nm,st_pass1) or check(st_nm,st_pass1) or st_pass1 != st_pass2: 
                    print("Plz Rechack\n")
                else:
                    break
                op2=input('1.To Continue\n2.To exit\n-->').strip()
                if op2=='2':
                    break   
                
            print("ok") 
        case '3':
            lib_id=input('Enter Name or id\n-->').strip()
            lib_pass=input('Password\n-->').strip()
            if check(lib_id,lib_pass):
                print("Invalid Id or Password\n\n")
            else:
                lib_ob=info(lib_id,lib_pass)
                if lib_ob:
                    print("Succese\n")
                else:
                    print("Fail\n")
        case '4':
            while True:
                lib_id=input('Enter Name or id\n-->').strip()
                lib_pass1=input('Password\n-->').strip()
                lib_pass2=input('Confirm Password\n-->').strip()
                if check(lib_id,lib_pass1) or check(lib_id,lib_pass2) or lib_pass2!=lib_pass1:
                    print('Plz Rechack\n')
                else :
                    break
                op2=input('1.To Continue\n2.To exit\n-->').strip()
                if op2=='2':
                    break 
            print('ok')      
                    
            
        case _:
            print('Invlid Input\n\n')
    