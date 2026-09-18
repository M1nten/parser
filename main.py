import sys

#testfunktion
def add(a, b):
    return a + b

# Funktion til at Læse filen
def get_csv_file(path: str) -> str:
    with open(path) as f:
        csv_file = f.read()
        return csv_file

# Funktion til at opdele en csv-streng på baggrund af \n
def opdel_rækker(csv_streng:str):
    list_csv = []
    while (len(csv_streng)>0):
        if "\n" in csv_streng:
            marker = csv_streng.index('\n')
            slice = csv_streng[0:marker]
            list_csv.append(slice)
            csv_streng = csv_streng[len(slice)+1:]

# Tager hånd om den sidste række som ikke afsluttes af \n
        else:
            print(csv_streng)
            list_csv.append(csv_streng)
            return list_csv
    return list_csv

def main() -> None:
    # Gør at man kan vælge hvilken fil man læser, når man kører main.py
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]

    #kalder funktion til at lave en streng
    csv_streng = get_csv_file(file_path)

    #kalder funktion til at opdele strengen efter rækker (\n)
    liste_med_rækker = opdel_rækker(csv_streng)

    #printer liste med rækkerne
    print(liste_med_rækker)



main()
