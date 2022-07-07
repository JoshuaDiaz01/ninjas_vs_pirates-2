from classes.character import Character
from classes.character import Ninja
from classes.character import Pirate



michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(michelangelo)
michelangelo.show_stats()