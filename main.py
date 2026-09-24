import sys
from time import sleep

# Henter filstien fra terminalkommandoen og stopper programmet
# hvis brugeren ikke har angivet en filsti.
def hent_fil_sti() -> str:
    if len(sys.argv) < 2:
        print("Brug af programmet: python3 main.py <fil_sti>")
        sys.exit(1)

    return sys.argv[1]

def velkomst() -> None:
    print("Velkommen til Minnas CSV-parser.")
    løfte = input("Lover du at lade være med at forsøge at parse en fil med komma (,) eller linjeskift (\\n) indeni felterne? (ja/nej) \n")
    if løfte.strip().lower() == "ja":
        print("Awesome! Værsgod:")
        sleep(1)
    else:
        print("Fair nok. Men dit format bliver måske liiidt mærkeligt... Værsgod:")
        sleep(1)

# Læser filen og returnerer den som en streng.
def læs_fil(filsti: str) -> str:
    with open(filsti) as f:
        return f.read()

# Hjælpefunktion: Checker om strengen er tom.
def streng_er_tom(streng: str) -> bool:
    return streng == ""

# Opdeler filens indhold ved hvert linjeskift og returnerer rækkerne
# som en liste af strenge.
def opdel_rækker(csv_streng: str) -> list[str]:
    if streng_er_tom(csv_streng):
        return []

    liste_med_rækker = []
    while len(csv_streng)>0:
        if "\n" in csv_streng:
            marker = csv_streng.index('\n')
            række = csv_streng[0:marker]
            liste_med_rækker.append(række)
            csv_streng = csv_streng[len(række)+1:]

    # Tager hånd om den sidste række, der ikke afsluttes af \n
        else:
            liste_med_rækker.append(csv_streng)
            break

    return liste_med_rækker

#Hjælpefunktion: opdeler en streng til en liste af strenge (seperator = komma )
def opdel_til_felter_strengversion(streng):
    liste_med_felter = []

    while (len(streng)>0):
        if "," in streng:
            marker = streng.index(',')
            slice = streng[:marker]
            liste_med_felter.append(slice)
            streng = streng[marker+1:]

        else:
            liste_med_felter.append(streng)
            return liste_med_felter

    return liste_med_felter

#Opdeler hver rækker i felter (seperator: komma) og returnerer en liste af lister (af strenge)
def parse_til_liste_af_lister(liste_med_rækker):
    liste_med_lister = []

    while len(liste_med_rækker)>1:
        liste_med_lister.append(opdel_til_felter_strengversion(liste_med_rækker[0]))
        del liste_med_rækker[0]
    if liste_med_rækker:
        liste_med_lister.append(opdel_til_felter_strengversion(liste_med_rækker[0]))

    return liste_med_lister


def main() -> None:
    filsti = hent_fil_sti()
    velkomst()
    csv_streng = læs_fil(filsti)
    liste_med_rækker = opdel_rækker(csv_streng)

    #Færdigparset liste af lister
    liste_af_lister = parse_til_liste_af_lister(liste_med_rækker)
    print(liste_af_lister)

main()
