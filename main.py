import sys

def get_csv_file(path: str) -> str:
    with open(path) as f:
        csv_file = f.read()
        return csv_file

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    #file_path = "csv_filer/employees.ascii.csv"
    csv_string = get_csv_file(file_path)
    print(repr(csv_string))


main()
