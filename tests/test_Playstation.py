import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pystationapi  import Playstation
class TestPlaystation(unittest.TestCase):
    def test_catalog(self):
        """
        Test the api if answer correctly
        """
        playstation = Playstation()
        prova = playstation.to_json_from_category()
        print(prova)
