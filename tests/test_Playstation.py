import unittest
import os
import sys
from pystationapi.Playstation  import Playstation
class TestPlaystation(unittest.TestCase):
    def test_catalog(self):
        """
        Test the api if answer correctly
        """
        playstation = Playstation()
        prova = playstation.to_json_from_category(Playstation.SALES,3)
        print(prova)
