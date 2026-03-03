
class Player:

    # Konstruktor
    def __init__(self, name):
        # Startposition des Spielers soll immer 10,200 sein.
        self.name = name
        self.health = 100

    def heal(self, life):
        self.health += life

    def hurt(self, damage):
        self.health -= damage

    def is_dead(self):
        """returns true if health is below or equal 0"""
        return self.health <= 0
