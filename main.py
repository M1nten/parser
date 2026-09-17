def main() -> None:
    file_path = "csv_filer/employees.ascii.csv"
    csv_string = get_csv_file(file_path)
    print(csv_string)


def get_csv_file(path: str) -> str:
    with open(path) as f:
        return f.read()


main()



#  def main() -> None:
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)


# def get_book_text(path: str) -> str:
#     with open(path) as f:
#         return f.read()
