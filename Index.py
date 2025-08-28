"""
This Python script demonstrates Object-Oriented Programming (OOP) concepts
by creating a Superhero class and an inherited FlyingSuperhero class.

It includes:
1. A base class with attributes and methods.
2. A constructor (__init__) to initialize objects.
3. An inheritance layer to create a specialized subclass.
4. An example of polymorphism by overriding a method.
"""

# Part 1: The Base Class and Constructor
# -----------------------------------------------------------------------------
class Superhero:
    """
    Represents a generic superhero with a name, power, and health.
    """
    # The constructor method to initialize a new Superhero object
    def __init__(self, name, power, health=100):
        self.name = name          # The superhero's name (e.g., 'Captain Comet')
        self.power = power        # The superhero's primary ability (e.g., 'Super strength')
        self.health = health      # The superhero's current health, defaults to 100

    # Part 2: Attributes and Methods
    # -----------------------------------------------------------------------------
    def display_info(self):
        """
        A method to print the superhero's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Health: {self.health}%")

    def take_damage(self, amount):
        """
        Simulates the superhero taking damage, decreasing their health.
        """
        if self.health - amount <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
        else:
            self.health -= amount
            print(f"{self.name} took {amount} damage. Current health: {self.health}%.")


# Part 3: Inheritance and Polymorphism
# -----------------------------------------------------------------------------
class FlyingSuperhero(Superhero):
    """
    Represents a specialized superhero who can fly.
    This class inherits from the Superhero class.
    """
    # The constructor for the subclass. It calls the parent's constructor
    # using 'super()' and adds a new attribute, 'flight_speed'.
    def __init__(self, name, power, flight_speed, health=100):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed  # The superhero's flight speed in mph

    # An example of Polymorphism: Overriding the parent's method
    # This method has the same name as the parent's but provides
    # more specific information.
    def display_info(self):
        """
        Overrides the parent method to also display flight speed.
        """
        # Call the parent's display_info method to reuse its logic
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} mph")

    # A new method specific to the FlyingSuperhero class
    def fly(self):
        """
        A method to print a flight action.
        """
        print(f"{self.name} is flying high at {self.flight_speed} mph!")


# --- Object Creation and Demonstration ---
print("--- Creating Superhero Objects ---")
# Create an object from the base class
hero1 = Superhero("Captain Comet", "Super strength")
hero1.display_info()
hero1.take_damage(20)
print("-" * 25)

# Create another object with a unique value
hero2 = Superhero("The Sentinel", "Invisibility", 85)
hero2.display_info()
print("-" * 25)

print("\n--- Creating a FlyingSuperhero Object ---")
# Create an object from the inherited class
flying_hero = FlyingSuperhero("Skymaster", "Flight", 750, 90)
flying_hero.display_info()
flying_hero.fly()
flying_hero.take_damage(30)
