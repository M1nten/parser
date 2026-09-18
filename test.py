import unittest
#udskift med den rigtige funktion
from main import add
from main import get_csv_file
from main import opdel_rækker
from main import streng_er_tom

#Brug kommandoen python3 -m unittest test.py til at køre tests i terminalen

#eksempel på hvordan man bruger unittest
class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

#eksempel på test af stringmetoder
class TestFiler(unittest.TestCase):

    def setUp(self):
        pass

    def test_strings_a(self):
            self.assertEqual(get_csv_file("blip.csv"), 'aaaa\n')
    def test_tom_fil(self):
            self.assertEqual(get_csv_file("tom.csv"), '')

    def test_t_fil(self):
        self.assertIn("serur", get_csv_file("csv_filer/yrk.csv"))

    def test_andetfilformat(self):
        self.assertEqual("miav\n", get_csv_file("andre_filtyper/eksempel.md"))

    def test_tom_fil(self):
        self.assertEqual(True, streng_er_tom(""))

class TestGet_csv_file(unittest.TestCase):
    # def test_tomfil(self):
    #     content = get_csv_file()

    #Skal måske ikke være der for evigt

    # def test_indeholderbackslash(self):
    #     content = get_csv_file("csv_filer/employees.ascii.csv")
    #     self.assertIn(
    #                 "\n",
    #                 content,
    #                 "There are no '\\n' in the csv-file"
    #             )
    #

    # Skal laves om til en test af hvad der sker hvis der er linjeskift elle ej...
    def test_indeholderbackslash(self):
         self.assertIn("\n", get_csv_file("csv_filer/employees.ascii.csv"), "There are no '\\n' in the csv-file")

    def test_en_anden_filindeholderbackslash(self):
        content = get_csv_file("csv_filer/sogne.dawa.csv")
        self.assertIn(
                    "\n",
                    content,
                    "There are no '\\n' in the csv-file"
                )

if __name__ == "__main__":
    unittest.main()
