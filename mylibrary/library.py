class Library():
    book_list = []
    def add_book(self, title, author):
        self.book_list.append({"title": title, "author": author})
        print(f"{title} of {author} added")
    def remove_book(self, title):
        for book in self.book_list:
            if book["title"] == title:
                self.book_list.remove(book)
    def search_book(self,title):
        for book in self.book_list:
            if book.get("title") == title:
                aut = book.get("author")
        print(f"book with {title} title is written by {aut}")
    def show_books(self):
        print("i have this books : ")
        for book in self.book_list:
            print(f"{book["title"]} written by {book["author"]}")

