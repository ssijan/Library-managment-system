class Book:
    def __init__(self,
                 book_id,
                 book_name,
                 book_author,
                 book_copies):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author 
        self.book_copies = book_copies
        if int(self.book_copies) > 0:
            self.book_availability_status = 'Available'
        else:
            self.book_availability_status = 'Unavailable'

    def __str__(self):
        return (f"""
                    \t\t\tBook ID           : {self.book_id}
                    \t\t\tBook Name         : {self.book_name}
                    \t\t\tBook Author       : {self.book_author}
                    \t\t\tBook Copies       : {self.book_copies}
                    \t\t\tBook Status       : {self.book_availability_status}
                   """)
