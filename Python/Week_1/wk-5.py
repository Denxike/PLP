class Character:
    """A base class for characters."""
    def __init__(self, name):
        self.name = name

    def introduce(self):
        """Introduces the character."""
        print(f"Hello, I am {self.name}.")

# Derived class inheriting from Character
class Superhero(Character):
    # Constructor to initialize Superhero objects
    def __init__(self, name, secret_identity, power, strength_level):
        # Call the constructor of the base class (Character)
        super().__init__(name)
        self.secret_identity = secret_identity
        self.power = power
        self.strength_level = strength_level # Example attribute

    # Method to use the superhero's power
    def use_power(self):
        print(f"{self.name} uses their {self.power}!")
        # Add more specific actions based on power if needed

    # Method to reveal the secret identity (example of encapsulation - controlled access)
    def reveal_identity(self):
        print(f"My secret identity is {self.secret_identity}.")

    # Example of overriding a base class method (Polymorphism potential)
    def introduce(self):
        """Introduces the superhero, adding a bit more flair."""
        print(f"Greetings! I am the mighty {self.name}, protector of the innocent!")

# --- How to use Assignment 1 classes ---
print("--- Assignment 1: Superhero Class ---")

# Create instances (objects) of the Superhero class
superman = Superhero("Superman", "Clark Kent", "Flight and Super Strength", 100)
batman = Superhero("Batman", "Bruce Wayne", "Intelligence and Gadgets", 85)

# Use methods of the objects
superman.introduce()
superman.use_power()
superman.reveal_identity()

print("-" * 20) # Separator

batman.introduce()
batman.use_power()
# Batman might not want to reveal his identity! (Demonstrates method usage)
# batman.reveal_identity()

print("-" * 40) # Separator


# --- Activity 2: Polymorphism Challenge (Animals) ---

# Base class (optional, but good for structure)
class Animal:
    """A base class for animals."""
    def move(self):
        """Generic move method (to be overridden by subclasses)."""
        pass # Placeholder

# Derived class 1: Dog
class Dog(Animal):
    """Represents a dog."""
    def move(self):
        """Dog-specific move action."""
        print("The dog is running! 🐕")

# Derived class 2: Bird
class Bird(Animal):
    """Represents a bird."""
    def move(self):
        """Bird-specific move action."""
        print("The bird is flying! 🐦")

# Derived class 3: Fish
class Fish(Animal):
    """Represents a fish."""
    def move(self):
        """Fish-specific move action."""
        print("The fish is swimming! 🐠")

# --- How to demonstrate Polymorphism ---
print("--- Activity 2: Polymorphism Challenge (Animals) ---")

# Create a list of different animal objects
animals = [Dog(), Bird(), Fish()]

# Iterate through the list and call the 'move' method on each object
# Polymorphism in action: The same method call 'animal.move()'
# executes different code depending on the actual type of the 'animal' object.
for animal in animals:
    animal.move()

print("-" * 40) # Separator
