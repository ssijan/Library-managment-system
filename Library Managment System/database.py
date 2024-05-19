
from student import Student

class Data:
    def __init__(self) -> None:
        pass
    def valid(self, id, pas):
        status=False
        if id=='sijan' and pas=='sijan':
            status=Student(id,pas)
        return status
            