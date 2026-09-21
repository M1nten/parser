import unittest
from main import opdel_rækker

#Kør tests: python3 -m unittest test.py
# Generer coverage rapport: python3 -m coverage run --source=main -m unittest test.py
# python3 -m coverage report -m

class TestOpdel_Raekker(unittest.TestCase):
    def test_a(self):
            pass

#Hvad vil jeg gerne have det her til at blive?
    def test_b(self):
            self.assertEqual(opdel_rækker(""), None)

    def test_c(self):
            self.assertEqual(opdel_rækker("blip"), ["blip"])

    def test_d(self):
            self.assertEqual(opdel_rækker("blip\n"), ["blip"])

    def test_e(self):
            self.assertEqual(opdel_rækker("blip\nblop"), ["blip", "blop"])

    def test_f(self):
            self.assertEqual(opdel_rækker("blip\nblop\n"), ["blip", "blop"])

#Hvad vil jeg gerne have det her til at blive?
    def test_g(self):
            self.assertEqual(opdel_rækker("\n"), None)

    def test_h(self):
            self.assertEqual(opdel_rækker("\n\n"), None)

class TestParser(unittest.TestCase):
    def test_a(self):
            pass

    def test_b(self):
            self.assertEqual(parser(""), None)

    def test_c(self):
            self.assertEqual(parser("blip"), ["blip"])

    def test_d(self):
            self.assertEqual(paresr("blip\n"), ["blip"])

    def test_e(self):
            self.assertEqual(parser("blip\nblop"), ["blip", "blop"])

    def test_f(self):
            self.assertEqual(parser("blip\nblop\n"), ["blip", "blop"])

    #Header
    def test_z(self):
            pass

#Hvad vil jeg gerne have det her til at blive?
    def test_g(self):
            self.assertEqual(parser("\n"), None)

    def test_h(self):
            self.assertEqual(parser("\n\n"), "")

    def test_i(self):
            self.assertEqual(parser("blub, blip"), "")

    def test_j(self):
            self.assertEqual(parser("blub, blip\n"), "")

    def test_k(self):
            self.assertEqual(parser("blub, blip\n blap"), "")

    def test_l(self):
            self.assertEqual(parser("\"blu\", \"blip\"\n \"blap\""), "")

    def test_m(self):
            self.assertEqual(parser("\"blu'\", \"bli'p\"\n \"blap\""), "")
