# ============================================================================
# MAIN PROGRAM - ADVANCED OOP CONCEPTS DEMONSTRATION
# ============================================================================
# This program demonstrates:
# 1. Abstract Base Classes and Interfaces
# 2. Inheritance and Polymorphism
# 3. Encapsulation with Properties
# 4. Exception Handling
# 5. Type Hints and Validation
# 6. Class Methods and Static Methods
# ============================================================================

from animals import Animal, Dog, Cat, Bird, Elephant
from bank import (BankAccount, SavingsAccount, CheckingAccount,
                  InvalidPINError, InsufficientFundsError, TransactionError)


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def demo_inheritance_and_polymorphism():
    """
    Demonstrate inheritance and polymorphism with animal classes.
    
    Key concepts:
    - All animals inherit from the Animal base class
    - Each animal overrides the introduce() method (polymorphism)
    - Each animal has unique methods (bark, meow, chirp, etc.)
    """
    
    print_section("1. ABSTRACT BASE CLASSES & POLYMORPHISM")
    
    # Create different animal objects
    # Each is created from a different class that inherits from Animal
    dog = Dog("Buddy", 2023, "Golden Retriever", is_trained=True)
    cat = Cat("Whiskers", 2021, "Orange")
    bird = Bird("Tweety", 2022, can_fly=True, is_migratory=True)
    elephant = Elephant("Dumbo", 1990, "African Plains Herd", intelligence_level=9)
    
    # Store all animals in a list
    animals = [dog, cat, bird, elephant]
    
    print("\n--- Animal Introductions (Polymorphism in Action) ---")
    print("Notice how introduce() behaves differently for each animal:")
    for animal in animals:
        print(f"  • {animal.introduce()}")
    
    print("\n--- Abstract Method Implementation: make_sound() ---")
    print("All animals implement make_sound() differently:")
    for animal in animals:
        print(f"  • {animal.make_sound()}")
    
    print("\n--- Animal-Specific Methods ---")
    print(f"  {dog.make_sound()}")
    print(f"  {dog.learn_trick('Sit')}")
    print(f"  {dog.perform_tricks()}")
    print(f"  {dog.fetch('tennis ball')}")
    
    print(f"\n  {cat.make_sound()}")
    print(f"  {cat.nap()}")
    print(f"  {cat.nap()}")
    print(f"  {cat.make_sound()}")
    print(f"  {cat.scratch('couch')}")
    
    print(f"\n  {bird.make_sound()}")
    print(f"  {bird.fly(15000)}")
    print(f"  {bird.land()}")
    
    print(f"\n  {elephant.make_sound()}")
    print(f"  {elephant.remember('Met a lion in the savanna')}")
    print(f"  {elephant.remember('Found a watering hole')}")
    print(f"  {elephant.recall_memories()}")
    
    print("\n--- Class Methods: Total Animals Created ---")
    print(f"  Total animals instantiated: {Animal.total_animals()}")
    
    print("\n--- Static Methods: Validate Birth Year ---")
    print(f"  Is 2020 valid birth year? {Animal.is_valid_birth_year(2020)}")
    print(f"  Is 1800 valid birth year? {Animal.is_valid_birth_year(1800)}")


def demo_properties_and_getters():
    """
    Demonstrate properties with getters and setters.
    
    Properties allow us to define custom logic when accessing attributes,
    making them appear like regular attributes to the outside world.
    """
    
    print_section("2. PROPERTIES & VALIDATION")
    
    print("\n--- Creating Animals with Validation ---")
    
    # Valid creation
    dog = Dog("Rex", 2020, "Labrador")
    print(f"✓ Dog created: {dog}")
    
    # Access properties (not calling methods, but using property decorators)
    print(f"  Name: {dog.name}")
    print(f"  Age: {dog.age} years old")
    print(f"  Species: {dog.species}")
    print(f"  Breed: {dog.breed}")
    
    # Modify property with setter
    dog.name = "Rexington"
    print(f"  Updated name: {dog.name}")
    
    print("\n--- Handling Validation Errors ---")
    try:
        invalid_dog = Dog("", 2020, "Poodle")
    except ValueError as e:
        print(f"✗ Error creating dog: {e}")
    
    try:
        dog.name = ""
    except ValueError as e:
        print(f"✗ Error updating name: {e}")
    
    print("\n--- String Representations ---")
    dog = Dog("Buddy", 2020, "Husky")
    print(f"  str(dog):  {str(dog)}")
    print(f"  repr(dog): {repr(dog)}")


def demo_advanced_encapsulation():
    """
    Demonstrate advanced encapsulation with custom exceptions
    and comprehensive validation.
    """
    
    print_section("3. ADVANCED ENCAPSULATION & EXCEPTION HANDLING")
    
    print("\n--- Creating Bank Accounts with Validation ---")
    
    # Valid account creation
    account1 = BankAccount("John Doe", 1000, "1234")
    print(f"✓ Account created: {account1}")
    
    print("\n--- Account Information ---")
    print(account1.check_balance("1234"))
    
    print("\n--- Deposit Operations ---")
    print(account1.deposit(500))
    print(account1.deposit(-100))  # Handled as error
    
    print("\n--- Withdrawal Operations with Exception Handling ---")
    print(account1.withdraw(200, "1234"))
    print(account1.withdraw(200, "9999"))  # Wrong PIN
    print(account1.withdraw(5000, "1234"))  # Insufficient funds
    
    print("\n--- Transaction History ---")
    print(account1.get_statement("1234"))
    
    print("\n--- Error Handling on Account Creation ---")
    try:
        invalid_account = BankAccount("", 1000, "1234")
    except Exception as e:
        print(f"✗ {type(e).__name__}: {e}")
    
    try:
        invalid_account = BankAccount("Jane", 1000, "12")  # PIN too short
    except Exception as e:
        print(f"✗ {type(e).__name__}: {e}")


def demo_savings_account():
    """
    Demonstrate SavingsAccount with inheritance and special features.
    """
    
    print_section("4. INHERITANCE: SAVINGS ACCOUNT")
    
    print("\n--- Creating Savings Account with Minimum Balance ---")
    savings = SavingsAccount("Alice Smith", 5000, "5678", 0.05)
    print(f"✓ Savings Account: {savings}")
    
    print("\n--- Account Details ---")
    print(savings.check_balance("5678"))
    
    print("\n--- Interest Management ---")
    print(f"Annual Interest Rate: {savings.interest_rate * 100}%")
    print(f"Interest Accrued: ${savings.interest_accrued:.2f}")
    
    print("\n--- Apply Interest ---")
    print(savings.apply_interest("5678"))
    print(savings.apply_interest("5678"))  # Apply again
    print(f"Total Interest Earned: ${savings.interest_accrued:.2f}")
    
    print("\n--- Minimum Balance Protection ---")
    result = savings.withdraw(5000, "5678")  # Would violate minimum
    print(result)
    
    result = savings.withdraw(400, "5678")  # OK - leaves $4700
    print(result)
    
    print("\n--- Transaction History ---")
    print(savings.get_statement("5678"))


def demo_checking_account():
    """
    Demonstrate CheckingAccount with overdraft protection.
    """
    
    print_section("5. INHERITANCE: CHECKING ACCOUNT")
    
    print("\n--- Creating Checking Account with Overdraft ---")
    checking = CheckingAccount("Bob Johnson", 1500, "9999", overdraft_limit=500)
    print(f"✓ Checking Account: {checking}")
    
    print("\n--- Account Details ---")
    print(checking.check_balance("9999"))
    
    print("\n--- Overdraft Protection ---")
    print(f"Current Balance: ${checking.balance:.2f}")
    print(f"Overdraft Limit: ${checking.overdraft_limit:.2f}")
    print(f"Available Funds: ${checking.available_funds:.2f}")
    
    print("\n--- Large Withdrawal (with Overdraft) ---")
    print(checking.withdraw(1800, "9999"))  # Goes into overdraft
    
    print("\n--- Check Writing ---")
    print(checking.write_check(200, "Electric Company", "9999"))
    
    print("\n--- Transaction History ---")
    print(checking.get_statement("9999"))
    
    print("\n--- Attempting to exceed overdraft ---")
    result = checking.withdraw(500, "9999")
    print(result)


def demo_polymorphism_benefits():
    """
    Demonstrate the power of polymorphism with different account types.
    """
    
    print_section("6. POLYMORPHISM: WORKING WITH MULTIPLE ACCOUNT TYPES")
    
    # Create different account types
    basic = BankAccount("Account 1", 1000, "1111")
    savings = SavingsAccount("Account 2", 2000, "2222", 0.05)
    checking = CheckingAccount("Account 3", 1500, "3333", 500)
    
    accounts = [basic, savings, checking]
    
    print("\n--- All Accounts Inherit Common Interface ---")
    for account in accounts:
        print(f"  • {account.__class__.__name__}: {account.holder_name}")
    
    print("\n--- Deposit Money (Polymorphic Behavior) ---")
    for account in accounts:
        account.deposit(500)
        print(f"  ✓ {account.holder_name} balance: ${account.balance:.2f}")
    
    print("\n--- Display Type Information ---")
    for account in accounts:
        print(f"  {account.__class__.__name__}:")
        print(f"    - Type: {type(account).__name__}")
        print(f"    - Is AbstractAccount: {hasattr(account, 'balance')}")
        print(f"    - Has deposit method: {hasattr(account, 'deposit')}")


def print_oop_concepts_summary():
    """
    Print a comprehensive summary of advanced OOP concepts.
    """
    
    print_section("7. ADVANCED OOP CONCEPTS SUMMARY")
    
    concepts = {
        "Abstract Base Classes (ABC)": (
            "Classes that define interfaces/contracts for subclasses.\n"
            "    Cannot be instantiated directly. Enforce implementation\n"
            "    of abstract methods in child classes."
        ),
        "Abstract Methods": (
            "Methods marked with @abstractmethod that MUST be implemented\n"
            "    by all subclasses. Ensures consistent interface."
        ),
        "Properties (@property)": (
            "Decorators that allow getter/setter methods to work like\n"
            "    attributes. Enables validation and computed values."
        ),
        "Multiple Inheritance": (
            "A class can inherit from multiple parent classes (mixins).\n"
            "    Example: Dog(Carnivore, Animal)"
        ),
        "Polymorphism": (
            "Different classes implementing the same method differently.\n"
            "    Same interface, different behavior."
        ),
        "Encapsulation": (
            "Public: accessible from outside (_name convention)\n"
            "    Protected: single underscore (_name)\n"
            "    Private: double underscore (__name)"
        ),
        "Custom Exceptions": (
            "Create custom exception classes for specific error conditions.\n"
            "    Enables precise error handling."
        ),
        "Type Hints": (
            "Use type hints (-> str, param: int) for clarity and\n"
            "    documentation. Helps IDEs provide better assistance."
        ),
        "Class Methods (@classmethod)": (
            "Methods that operate on the class itself, not instances.\n"
            "    Receive 'cls' instead of 'self'."
        ),
        "Static Methods (@staticmethod)": (
            "Methods that don't depend on class or instance state.\n"
            "    Don't receive 'self' or 'cls'."
        ),
    }
    
    for concept, explanation in concepts.items():
        print(f"\n► {concept}:")
        for line in explanation.split("\n"):
            print(f"    {line}")


def main() -> None:
    """Main function to run all demonstrations."""
    
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "ADVANCED PYTHON OOP PROJECT".center(68) + "║")
    print("║" + "Comprehensive Examples of OOP Concepts".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    
    # Run all demonstrations
    demo_inheritance_and_polymorphism()
    demo_properties_and_getters()
    demo_advanced_encapsulation()
    demo_savings_account()
    demo_checking_account()
    demo_polymorphism_benefits()
    print_oop_concepts_summary()
    
    print_section("DEMONSTRATION COMPLETE")
    print("\n📚 Learn More:")
    print("  • animals.py: Abstract classes, inheritance, properties")
    print("  • bank.py: Custom exceptions, validation, abstract interfaces")
    print("  • main.py: This comprehensive demonstration\n")


if __name__ == "__main__":
    # This runs only if the file is executed directly
    # not if it's imported as a module
    main()
