import sys

#testfunktion
def add(a, b):
    return a + b

# Implementer check af om det er en csv_fil
def check_filtype(filepath):
    pass

# Funktion til at Læse filen og generere en streng
def get_csv_file(path: str) -> str:
    with open(path) as f:
        csv_file = f.read()
        return csv_file

# Check for tomme strenge
def streng_er_tom(streng:str):
    return streng == ""

# Funktion til at opdele en streng til flere strenge (seperator = '\n')
def opdel_rækker(csv_streng:str):
    if streng_er_tom(csv_streng) == False:
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

    else:
        # Hvad skal der stå her?
        return

#funktion der opdeler en string til en liste af string (seperator = ',' )
def opdel_til_felter_strengversion(streng):
    liste_med_felter = []

    while (len(streng)>0):
        if "," in streng:
            marker = streng.index(',')
            slice = streng[0:marker]
            liste_med_felter.append(slice)
            streng = streng[len(slice)+1:]

        else:
            liste_med_felter.append(streng)
            return liste_med_felter

    return liste_med_felter

#funktion der opdeler en liste af strenge til en liste af lister (seperator: ',')
def opdel_til_felter_listeversion(liste_med_strenge):
    liste_med_lister = []

    i = 0
    #while i<31:
    while len(liste_med_strenge)>1:
        liste_med_lister.append(opdel_til_felter_strengversion(liste_med_strenge[i]))
        del liste_med_strenge[i]

    liste_med_lister.append(opdel_til_felter_strengversion(liste_med_strenge[0]))

    return liste_med_lister


def main() -> None:
    # Gør at man kan vælge hvilken fil man læser, når man kører main.py
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]

    #kalder funktion til at lave en streng
    csv_streng = get_csv_file(file_path)

    #kalder funktion til at opdele strengen efter rækker (\n) --> liste
    liste_med_rækker = opdel_rækker(csv_streng)

    #kalder funktion til opdele rækkerne i felter --> liste af lister
    listede_liste = opdel_til_felter_listeversion(liste_med_rækker)

    print(listede_liste)

    #printer liste med rækkerne
   # print(liste_med_rækker[0])


    # afprøve opdel til felter
    #print(opdel_til_felter_strengversion(liste_med_rækker[0]))


main()
