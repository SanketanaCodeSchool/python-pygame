#Create a base class Book with attributes title and author. A derived class EBook should also store file_size and format. 
# Add methods to display the complete book info.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}")



class Ebook(Book):
    def __init__(self, title, author, file_size, format):
        super().__init__(title, author)
        self.file_size = file_size
        self.format = format

    def ebook_info(self):
        super().book_info()
        print(f"File Size: {self.file_size}MB, Format: {self.format}")


a = Book("Intro to Python", "Vibha")
b = Ebook("Python Tricks", "Vibha", 20, "PDF")
a.book_info()
b.ebook_info()