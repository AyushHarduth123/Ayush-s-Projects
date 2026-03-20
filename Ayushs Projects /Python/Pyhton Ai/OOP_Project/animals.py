# ============================================================================
# ADVANCED OOP CONCEPTS: ABSTRACT CLASSES, INHERITANCE, POLYMORPHISM
# ============================================================================
# This module demonstrates:
# - Abstract Base Classes (ABC) - enforcing structure for subclasses
# - Method overriding and polymorphism
# - Properties with getters and setters
# - Class methods and static methods
# - Complex inheritance hierarchies
# ============================================================================

from abc import ABC, abstractmethod
from datetime import datetime


# Abstract Base Class - cannot be instantiated directly
class Animal(ABC):
    """
    Abstract base class for all animals.
    
    This class defines the interface (contract) that all animal subclasses
    must implement. It cannot be instantiated directly - you must create
    a subclass and implement all abstract methods.
    
    Attributes:
        name (str): Animal's name
        birth_date (datetime): When the animal was born
        _species (str): Protected attribute for the animal's species
    """
    
    # Class variable - shared by all instances
    total_animals_created = 0
    
    def __init__(self, name, birth_year):
        """
        Initialize an animal with validation.
        
        Args:
            name (str): The animal's name
            birth_year (int): Year the animal was born
            
        Raises:
            ValueError: If name is empty or birth_year is invalid
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(birth_year, int) or birth_year < 1900:
            raise ValueError("Birth year must be a valid year (>= 1900)")
        
        self._name = name
        self._birth_year = birth_year
        self._species = self.__class__.__name__
        Animal.total_animals_created += 1
    
    # ========== ABSTRACT METHODS - MUST BE IMPLEMENTED BY SUBCLASSES ==========
    
    @abstractmethod
    def make_sound(self):
        """
        Abstract method that all animals must implement.
        Each animal makes a different sound.
        
        Returns:
            str: The sound the animal makes
        """
        pass
    
    @abstractmethod
    def get_diet_type(self):
        """
        Abstract method to return the diet type.
        
        Returns:
            str: Type of diet (carnivore, herbivore, omnivore)
        """
        pass
    
    # ========== CONCRETE METHODS ==========
    
    @property
    def name(self):
        """Property to get the animal's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Property setter with validation."""
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def age(self):
        """Property that calculates age from birth year."""
        return datetime.now().year - self._birth_year
    
    @property
    def species(self):
        """Read-only property for species."""
        return self._species
    
    def introduce(self):
        """Introduce the animal with basic information."""
        return f"I am {self._name}, a {self.age}-year-old {self._species}."
    
    @classmethod
    def total_animals(cls):
        """
        Class method - can be called on the class itself.
        Returns the total number of animals created.
        
        Returns:
            int: Total animals instantiated
        """
        return cls.total_animals_created
    
    @staticmethod
    def is_valid_birth_year(year):
        """
        Static method - doesn't depend on instance or class state.
        Validates if a year is reasonable for an animal.
        
        Args:
            year (int): Year to validate
            
        Returns:
            bool: True if year is valid
        """
        current_year = datetime.now().year
        return 1900 <= year <= current_year
    
    def __str__(self):
        """String representation of the animal."""
        return f"{self._name} ({self._species}, age {self.age})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(name='{self._name}', birth_year={self._birth_year})"


# ========== CARNIVORE MIXIN - SHARED BEHAVIOR FOR MEAT EATERS ==========
class Carnivore:
    """Mixin class that provides carnivore-specific behavior."""
    
    def hunt(self):
        """Carnivores hunt for food."""
        return f"{self.name} is hunting prey..."
    
    def get_diet_type(self):
        """Carnivores eat meat."""
        return "Carnivore"


# ========== HERBIVORE MIXIN - SHARED BEHAVIOR FOR PLANT EATERS ==========
class Herbivore:
    """Mixin class that provides herbivore-specific behavior."""
    
    def graze(self):
        """Herbivores graze for food."""
        return f"{self.name} is grazing on plants..."
    
    def get_diet_type(self):
        """Herbivores eat plants."""
        return "Herbivore"


# ========== CONCRETE ANIMAL CLASSES ==========

class Dog(Carnivore, Animal):
    """
    Dog class combining Carnivore mixin with Animal base class.
    
    Demonstrates:
    - Multiple inheritance (Carnivore mixin + Animal base)
    - Overriding abstract methods
    - Adding specialized attributes and methods
    """
    
    def __init__(self, name, birth_year, breed, is_trained=False):
        """
        Initialize a dog.
        
        Args:
            name (str): Dog's name
            birth_year (int): Birth year
            breed (str): Dog's breed
            is_trained (bool): Whether the dog is trained
        """
        super().__init__(name, birth_year)
        if not isinstance(breed, str) or not breed:
            raise ValueError("Breed must be a non-empty string")
        self._breed = breed
        self._is_trained = is_trained
        self._tricks = []
    
    @property
    def breed(self):
        """Get the dog's breed."""
        return self._breed
    
    @property
    def is_trained(self):
        """Check if dog is trained."""
        return self._is_trained
    
    def make_sound(self):
        """Override abstract method - dogs bark."""
        if self.is_trained:
            return f"{self.name} barks obediently: Woof! Woof!"
        return f"{self.name} barks loudly: WOOF! WOOF! WOOF!"
    
    def learn_trick(self, trick_name):
        """
        Dog learns a new trick.
        
        Args:
            trick_name (str): Name of the trick to learn
            
        Returns:
            str: Confirmation message
        """
        if trick_name not in self._tricks:
            self._tricks.append(trick_name)
            return f"{self.name} learned a new trick: {trick_name}"
        return f"{self.name} already knows this trick!"
    
    def perform_tricks(self):
        """Display all tricks the dog knows."""
        if not self._tricks:
            return f"{self.name} hasn't learned any tricks yet."
        return f"{self.name} can do: {', '.join(self._tricks)}"
    
    def fetch(self, item):
        """Dog fetches an item."""
        return f"{self.name} fetches the {item} happily!"
    
    def introduce(self):
        """Override parent's introduce method."""
        parent_intro = super().introduce()
        return f"{parent_intro} I'm a {self._breed} dog. {self.make_sound()}"


class Cat(Carnivore, Animal):
    """
    Cat class - another carnivore demonstrating polymorphism.
    
    Shows how different animals implement the same abstract methods
    differently.
    """
    
    def __init__(self, name, birth_year, color, indoor=True):
        """
        Initialize a cat.
        
        Args:
            name (str): Cat's name
            birth_year (int): Birth year
            color (str): Cat's color
            indoor (bool): Whether the cat is an indoor cat
        """
        super().__init__(name, birth_year)
        self._color = color
        self._indoor = indoor
        self._nap_count = 0
    
    @property
    def color(self):
        """Get the cat's color."""
        return self._color
    
    def make_sound(self):
        """Override abstract method - cats meow."""
        if self._nap_count > 5:
            return f"{self.name} meows groggily: Meooooow..."
        return f"{self.name} meows: Meow! Meow!"
    
    def nap(self):
        """Cats nap frequently."""
        self._nap_count += 1
        return f"{self.name} takes a nap... (total naps today: {self._nap_count})"
    
    def scratch(self, surface):
        """Cats scratch surfaces."""
        return f"{self.name} scratches the {surface} ruthlessly!"
    
    def introduce(self):
        """Override parent's introduce method."""
        parent_intro = super().introduce()
        location = "indoor" if self._indoor else "outdoor"
        return f"{parent_intro} I'm a {self._color} {location} cat."


class Bird(Animal):
    """
    Bird class - demonstrates handling of can_fly variations.
    
    Not a carnivore or herbivore, shows flexible diet handling.
    """
    
    def __init__(self, name, birth_year, can_fly=True, is_migratory=False):
        """
        Initialize a bird.
        
        Args:
            name (str): Bird's name
            birth_year (int): Birth year
            can_fly (bool): Whether the bird can fly
            is_migratory (bool): Whether the bird migrates
        """
        super().__init__(name, birth_year)
        self._can_fly = can_fly
        self._is_migratory = is_migratory
        self._altitude = 0  # Current flying altitude in feet
    
    @property
    def can_fly(self):
        """Check if the bird can fly."""
        return self._can_fly
    
    @property
    def altitude(self):
        """Get current altitude."""
        return self._altitude
    
    def make_sound(self):
        """Override abstract method - birds chirp."""
        return f"{self.name} chirps: Tweet! Tweet! Tweet!"
    
    def get_diet_type(self):
        """Most birds are omnivores."""
        return "Omnivore"
    
    def fly(self, altitude):
        """
        Bird flies to a specific altitude.
        
        Args:
            altitude (int): Target altitude in feet
            
        Returns:
            str: Flight status message
        """
        if not self._can_fly:
            return f"{self.name} cannot fly and stays on the ground."
        
        if altitude > 40000:
            return f"{self.name} cannot fly that high!"
        
        self._altitude = altitude
        flight_type = "migrating" if self._is_migratory else "flying"
        return f"{self.name} is {flight_type} at {altitude} feet altitude."
    
    def land(self):
        """Bird lands."""
        self._altitude = 0
        return f"{self.name} has landed safely."
    
    def introduce(self):
        """Override parent's introduce method."""
        parent_intro = super().introduce()
        ability = "can fly" if self._can_fly else "cannot fly"
        migratory = " (migratory)" if self._is_migratory else ""
        return f"{parent_intro} I'm a bird that {ability}{migratory}."


class Elephant(Herbivore, Animal):
    """
    Elephant class - demonstrates herbivore and social behavior.
    
    Shows how to handle complex attributes and methods.
    """
    
    def __init__(self, name, birth_year, herd_name, intelligence_level=7):
        """
        Initialize an elephant.
        
        Args:
            name (str): Elephant's name
            birth_year (int): Birth year
            herd_name (str): Name of the herd
            intelligence_level (int): Intelligence level (1-10)
        """
        super().__init__(name, birth_year)
        self._herd_name = herd_name
        self._intelligence_level = max(1, min(10, intelligence_level))  # Clamp between 1-10
        self._memories = []
    
    @property
    def herd_name(self):
        """Get the herd name."""
        return self._herd_name
    
    @property
    def intelligence_level(self):
        """Get intelligence level."""
        return self._intelligence_level
    
    def make_sound(self):
        """Override abstract method - elephants trumpet."""
        return f"{self.name} trumpets loudly: PAOOOOOW!"
    
    def remember(self, event):
        """Elephants remember events - they never forget!"""
        self._memories.append(event)
        return f"{self.name} remembers: {event}"
    
    def recall_memories(self):
        """Recall all memories."""
        if not self._memories:
            return f"{self.name} has no memories yet."
        memory_list = "\n  ".join(self._memories)
        return f"{self.name}'s memories:\n  {memory_list}"
    
    def introduce(self):
        """Override parent's introduce method."""
        parent_intro = super().introduce()
        return f"{parent_intro} I'm part of the {self._herd_name} herd (IQ: {self._intelligence_level}/10)."
