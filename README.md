Superhero Class Project

This project demonstrates core concepts of Object-Oriented Programming (OOP) in Python, including classes, objects, attributes, methods, constructors, and inheritance.

Project Structure

The project consists of a single Python file (superhero_classes.py, though the code is provided here), which defines two main classes:

Superhero (Base Class): Represents a generic superhero with fundamental attributes and abilities.

FlyingSuperhero (Subclass): A specialized type of superhero that inherits all properties from the base class and adds its own unique features.

Key Concepts Demonstrated

Classes and Objects: We define Superhero and FlyingSuperhero as blueprints for creating individual superhero objects.

Constructors (__init__): The __init__ method is used to initialize new objects with unique values for their attributes (e.g., name, power, health).

Attributes and Methods:


Attributes are the properties of an object (e.g., self.name, self.health).

Methods are the actions an object can perform (e.g., display_info(), take_damage()).

Inheritance: The FlyingSuperhero class inherits from the Superhero class, meaning it automatically gets all the attributes and methods of its parent. This promotes code reuse and a logical structure.

Polymorphism: The display_info() method in the FlyingSuperhero class overrides the parent's method to provide more specific information. This demonstrates how a method can behave differently based on the object type, even if they share the same name.
