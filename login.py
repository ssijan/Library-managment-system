
from database import Data
def info(name,password):
    dt=Data() 
    ob=dt.valid(name,password)  
    return ob

def save_info(self):
    dt=Data()
    dt.save_st_info(self)
    print('\t\t\t\t------------------------------------------')
    print('\t\t\t\t|           Registration Done            |')
    print('\t\t\t\t------------------------------------------')

def info_li(name,password):
    dt=Data() 
    ob_li=dt.valid_li(name,password)  
    return ob_li

def save_li_info(self):
    dt=Data()
    dt.save_li_info(self)
    print('\t\t\t\t------------------------------------------')
    print('\t\t\t\t|           Registration Done            |')
    print('\t\t\t\t------------------------------------------')