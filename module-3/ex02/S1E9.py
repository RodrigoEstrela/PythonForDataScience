from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class to serve as a base for a Character
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor receives: [first_name] and [is_alive]-OPTIONAL"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Sets the [is_alive] attribute to False"""
        pass


class Stark(Character):
    """
    Concrete class based of the Character class
    Builds a Character from the Stark Family from GoT
    """
    def __init__(self, first_name, is_alive=True):
        """Constructor receives: [first_name] and [is_alive]-OPTIONAL"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Sets the [is_alive] attribute to False"""
        self.is_alive = False
