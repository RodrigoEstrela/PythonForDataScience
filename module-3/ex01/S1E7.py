from S1E9 import Character


class Baratheon(Character):
    """Builds a Character from the Baratheon Family from GoT"""
    def __init__(self, first_name, is_alive=True):
        """Constructor receives: [first_name] and [is_alive]-OPTIONAL"""
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.__name__
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Sets the [is_alive] attribute to False"""
        self.is_alive = False

    def __str__(self):
        """Customizes the __str__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Customizes the __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Builds a Character from the Lannister Family from GoT"""
    def __init__(self, first_name, is_alive=True):
        """Constructor receives: [first_name] and [is_alive]-OPTIONAL"""
        super().__init__(first_name, is_alive)
        self.family_name = Lannister.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Sets the [is_alive] attribute to False"""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, is_alive):
        """Creates a Lannister Character"""
        return Lannister(first_name, is_alive)

    def __str__(self):
        """Customizes the __str__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Customizes the __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
