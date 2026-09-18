import unittest
#udskift med den rigtige funktion
from main import add
from main import get_csv_file
from main import opdel_rækker

#Brug kommandoen python3 -m unittest test.py til at køre tests i terminalen

#eksempel på hvordan man bruger unittest
class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

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
