#!/usr/bin/python3
import matplotlib.pyplot as plt  # import matplotlib for plotting graphs and charts
# I have used fstrings in this code, this is when a function 
# is present inside of a string so the code can carry it out

def show_list(book_list):
    """
    This function lists out the titles of all the books and their other detials
    This also prints the total number of titles available and the value of books in stock
    """
    total_price = 0
    for book in book_list:
        print("----------------------------------------------")
        print(f"Author: {book['author']}")
        print(f"Title: {book['title']}")
        print(f"Format: {book['format']}")
        print(f"Publisher: {book['pub']}")
        print(f"Cost: {book['price']}")
        print(f"Stock: {book['stock']}")
        print(f"Genre: {book['genre']}")
        print("----------------------------------------------")
        # add stock*price of current book to the "total price" variable
        total_price += book['stock'] * book['price']

    print("----------------------------------------------")
    print(f"Total number of books available: {len(book_list)}")
    print(f"Total price of books in stock: {total_price:.2f}")
    print("----------------------------------------------")


def get_average(book_list):
    """
    A function to calculate the total price of the books in stock and then return the average cost of the books
    """
    total_price = 0
    total_books = 0
    for book in book_list:
        if book['stock'] > 0:  # check if book in stock
            total_price += book['price']  # add the book price to total price variable
            total_books += 1  

    average = total_price/total_books
    return average


def show_average(book_list):
    """
    A function to print out the average cost of books in book_list calculated from the above function (get_average)
    """
    average = get_average(book_list)
    print("----------------------------------------------")
    print(f"Average cost of books in stock is: {average:.2f}")
    print("----------------------------------------------")


def get_genre(book_list):
    """
    A function to create a list of genres for every book, and calculate how many books there are per genre
    """
    genre_list = []  # will contain the genre of every available book
    for book in book_list:
        genre_list.append(book['genre'])

    genre_dict = {}  # will contain number of books as value for every genre as a key
    for genre in set(genre_list):
        genre_dict[genre] = genre_list.count(genre)

    return genre_dict


def show_genre(book_list):
    """
    Display function to print out the genre frequency dictionary obtained in the function get_genre
    """
    genre_dict = get_genre(book_list)
    print("----------------------------------------------")
    print(f"GENRE : NUMBER OF TITLES AVAILABLE")
    for genre, count in genre_dict.items():
        print(f'{genre.capitalize()}: {count}')
    print("----------------------------------------------")


def add_book(book_list):
    """
    A function to add a new book to the book_list and print the change in stock as well as in the average
    """
    # book_list is a list of dictionaries
    # bunch of input statements to get details on the book that we need to add
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    pub = input("Enter the publication of the book: ")
    fmt = input("Enter the format of the book: ")
    price = float(input("Enter the price of the book: "))
    stock = int(input("Enter the stock of the book: "))
    genre = input("Enter the genre of the book: ")

    initial_avg = get_average(book_list)

    # to add another book to the book_list i will use append to add to the file
    new_book = {
        'title': title,
        'author': author,
        'pub': pub,
        'price': price,
        'stock': stock,
        'genre': genre,
        'format': fmt
    }
    book_list.append(new_book)
    # a) print the stock of the newly added book
    print(f'The increase in stock is {new_book["stock"]}')
    # b) get_average function before and after the book is added
    final_avg = get_average(book_list)
    diff_avg = final_avg - initial_avg
    print(f'Differance in average is {diff_avg:.2f}')

    return book_list


def modify_stock(book_list):
    """
    Function to change the stock of any given book
    """
    title = input("Enter the title of book to search: ")
    found = False  # boolean flag to check if we found the book or not
    for book in book_list:
        if book['title'].lower() == title.lower():  # ensure that the search is case-insensitive
            found = True  # change the flag to indicate that we found the book
            if book['stock'] > 0:  # check if the title is in the stock
                opt = input(
                    "Enter 'i' to increase the stock, or 'd' to decrease the stock: ")
                if opt == 'i':  # increase the stock
                    stock_diff = int(
                        input("Enter the number of books to add in the stock: "))
                    book['stock'] += stock_diff
                elif opt == 'd':  # decrease the stock
                    stock_diff = int(
                        input("Enter the number of books to remove from the stock: "))
                    # check if sufficient books are available
                    if stock_diff < book['stock']:
                        book['stock'] -= stock_diff
                    else:
                        print(f"Only {book['stock']} book(s) in stock")
                else:
                    print('Invalid option')
            else:
                print(f"{title} out of stock")

    if not found:  # if we never found the book
        print('No book found!')
    return book_list


def show_sorted(book_list):
    """
    A function to sort the book_list according to title or genre
    """
    # this will be the key to sort
    k = input("How do you want the books to be ordered?[title/genre]: ")
    if k in ['title', 'genre']:
        # lambda function to take dict "x" as input and return the value of key "k"
        sorted_book_list = sorted(book_list, key=lambda x: x[k].upper())
        # use the precoded function to print out the list
        show_list(sorted_book_list)
    else:
        print("Invalid key, try again")


def show_graph(book_list):
    """
    A function to create a bar graph of number of book per genre
    """
    genre_dict = get_genre(
        book_list)  # dict with number of books as value for genre as a key
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])  # create the axes
    ax = fig.add_subplot()  # show the axes
    genre_list = list(genre_dict.keys())  # get the genre list from genre dict
    # get the number of books as a list
    number_of_books = list(genre_dict.values())
    ax.bar(genre_list, number_of_books)  # create the graph
    plt.show()  # show the graph


def save(book_list):
    """
    Save the book_list dictionary to a txt file
    """
    with open('my_library.txt', 'w') as f:
        err = f.write(str(book_list))

    return err != 0


def load():
    """
    Load the book_list dictionary from a saved text file
    """
    with open('my_library.txt', 'r') as f:
        book_list = eval(f.read())

    return book_list


def save_txt(book_list):
    """
    Save the book_list into a txt file (my_library.txt)
    """
    target = "#Listing showing sample book details\n#AUTHOR, TITLE, FORMAT, PUBLISHER, COST?, STOCK, GENRE\n"
    for book in book_list:
        for key in book.keys():
            target += f"{book[key]}, "
        target += "\n"

    with open("book_data_file.txt", "w") as f:
        err = f.write(target)

    return err != 0


def load_txt():
    """
    Load the book_list so that it can be read in the txt file
    """
    with open("book_data_file.txt", "r") as f:
        book_list = f.readlines()
    book_list = book_list[2:]
    # for every book in the booklist convert the book entry into dictionary
    for i, book in enumerate(book_list):
        # statically creating dict
        book = book.split(', ')

        book_dict = {'author': book[0], 'title': book[1], 'format': book[2], 'pub': book[3],
                     'price': float(book[4]), 'stock': int(book[5]), 'genre': book[6]
                     }
        book_list[i] = book_dict

    return book_list


def menu(book_list):
    """
    A function with loop to facilitate the menu
    """
    while True:
        print("----------------------------------------------")
        print("--- 1. Show the list of books ----------------")
        print("--- 2. Average price of books in stock -------")
        print("--- 3. Genre wise books available ------------")
        print("--- 4. Add a new book ------------------------")
        print("--- 5. Query title to modify stock -----------")
        print("--- 6. Query books in sorted order -----------")
        print("--- 7. Show genre bar graph ------------------")
        print("--- 8. Exit ----------------------------------")
        print("----------------------------------------------")
        choice = int(input("Enter the function to perform: "))
        print("----------------------------------------------")
        if choice == 1:
            show_list(book_list)
        elif choice == 2:
            show_average(book_list)
        elif choice == 3:
            show_genre(book_list)
        elif choice == 4:
            book_list = add_book(book_list)
        elif choice == 5:
            book_list = modify_stock(book_list)
        elif choice == 6:
            show_sorted(book_list)
        elif choice == 7:
            show_graph(book_list)
        elif choice == 8:
            save(book_list)
            save_txt(book_list)
            return
        else:
            print("Invalid choice!")


book_list = load()  # load a book_list

menu(book_list)  # run the menu