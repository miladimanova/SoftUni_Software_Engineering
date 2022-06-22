book_to_search = input()
count_of_books = 0
while True:
    book_name = input()
    if book_name == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count_of_books} books.')
        break
    if book_name == book_to_search:
        print(f'You checked {count_of_books} books and found it.')
        break
    count_of_books += 1

