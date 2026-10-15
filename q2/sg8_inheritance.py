class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def get_title(self):
        return self.title
        
    def get_author(self):
        return self.author
        
    def set_title(self, title):
        self.title = title
        
    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

  class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)
        
    def get_number_of_pages(self):
        return self._number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.number_of_pages = number_of_pages

      
