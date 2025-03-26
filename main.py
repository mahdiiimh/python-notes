import library

b1 = library.Library()
other_order = "yes"
if __name__ != "__main__" :
     print("please use this code as a package")
     
while other_order == "yes":
    print("Welcome , please choose what you want to do. ")
    print("1. add book to  Library. ")
    print("2. remove book from Library. ")
    print("3. search book in  Library. ")
    print("4. show books in Library. ")
    user_input = input("please enter your choice (1,2,3,4) : ")
    if user_input == "1" :
        book_name = input("please enter your book title : ")
        book_author = input("please enter the book author : ")
        b1.add_book(book_name,book_author)
    elif user_input == "2":
        book_name = input("please enter your book title : ")
        b1.remove_book(book_name)
    elif user_input == "3":
        book_name = input("please enter your book title : ")
        b1.search_book(book_name)
    elif user_input == "4":
        b1.show_books()
    
    other_order = input(" do you have any other orders (yes/no) : ")


