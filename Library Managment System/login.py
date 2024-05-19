
from student import *
from database import Data


def info(name,password):
    dt=Data() 
    ob=dt.valid(name,password)
        
    return ob