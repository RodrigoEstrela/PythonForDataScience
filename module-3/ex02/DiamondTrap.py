from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Not really a Baratheon, are you?"""

    def set_eyes(self, eyes):
        """Changes the eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Changes the hair color"""
        self.hairs = hairs

    def get_eyes(self):
        """Returns the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Returns the hair color"""
        return self.hairs
