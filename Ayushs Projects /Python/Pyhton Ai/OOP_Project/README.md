# Advanced Python OOP Project

A comprehensive demonstration of Object-Oriented Programming (OOP) concepts in Python with professional-grade implementation.

## 🎯 Concepts Covered

### Core OOP Principles
- **Classes and Objects**: Creating blueprints and instances
- **Attributes & Methods**: Data and behavior encapsulation
- **Constructors (__init__)**: Object initialization with validation
- **String Representations**: `__str__()` and `__repr__()` methods

### Intermediate Concepts
- **Inheritance**: Single and multiple inheritance using mixins
- **Polymorphism**: Method overriding and different implementations
- **Encapsulation**: Public, protected (_), and private (__) attributes
- **Properties (@property)**: Getters and setters with validation

### Advanced Concepts
- **Abstract Base Classes (ABC)**: Defining interfaces for subclasses
- **Abstract Methods**: Enforcing implementation in child classes
- **Custom Exceptions**: Creating domain-specific error handling
- **Type Hints**: Annotations for clarity and IDE support
- **Class Methods (@classmethod)**: Class-level operations
- **Static Methods (@staticmethod)**: Utility functions without state
- **Transaction Logging**: Audit trails and history tracking

## 📁 Project Structure

```
OOP_Project/
├── main.py              # Comprehensive demonstrations
├── animals.py           # Abstract classes, inheritance, mixins
├── bank.py              # Encapsulation, exceptions, validation
└── README.md            # This file
```

## 🚀 Running the Project

```bash
python main.py
```

The program will execute 7 comprehensive demonstrations showcasing different OOP concepts.

## 📚 File Details

### animals.py
Demonstrates advanced inheritance and polymorphism:

- **Animal** (Abstract Base Class)
  - Enforces interface with abstract methods
  - Class methods for shared functionality
  - Static methods for validation
  - Properties with read-only access
  - Automatic age calculation

- **Dog** (Multiple Inheritance: Carnivore + Animal)
  - Training state management
  - Trick learning system
  - Method overriding for polymorphism

- **Cat** (Carnivore + Animal)
  - Nap tracking
  - Different behavior patterns

- **Bird** (Animal)
  - Altitude tracking
  - Migration capabilities
  - Flying mechanics

- **Elephant** (Herbivore + Animal)
  - Memory storage system
  - Intelligence levels
  - Social herd structure

### bank.py
Demonstrates advanced encapsulation and exception handling:

- **Custom Exceptions**
  - `InsufficientFundsError`
  - `InvalidPINError`
  - `InvalidAccountError`
  - `TransactionError`

- **Transaction Class**
  - Timestamped records
  - Balance tracking
  - Transaction type classification

- **AbstractAccount** (Interface)
  - Defines contract for all account types
  - Abstract methods: deposit, withdraw, get_statement

- **BankAccount** (Base Implementation)
  - Comprehensive validation
  - Transaction logging
  - PIN authentication
  - Type hints throughout
  - Withdrawal/deposit limits

- **SavingsAccount** (Inheritance)
  - Interest calculation
  - Minimum balance enforcement
  - Interest accrual tracking

- **CheckingAccount** (Inheritance)
  - Overdraft protection
  - Check writing simulation
  - Available funds calculation

### main.py
Seven comprehensive demonstrations:

1. **Abstract Base Classes & Polymorphism**
   - Creating instances of different animal types
   - Polymorphic method calls
   - Class and static methods

2. **Properties & Validation**
   - Property access and modification
   - Input validation
   - Error handling

3. **Advanced Encapsulation**
   - Custom exception handling
   - Transaction validation
   - Account creation validation

4. **Savings Account Features**
   - Interest management
   - Minimum balance protection
   - Transaction history

5. **Checking Account Features**
   - Overdraft protection
   - Check writing
   - Balance management

6. **Polymorphism Benefits**
   - Working with multiple account types
   - Common interface usage
   - Type information

7. **OOP Concepts Summary**
   - Comprehensive explanation of all concepts
   - Use cases and benefits
   - Best practices

## 🔑 Key Design Patterns Used

### Abstraction
- Abstract base classes define contracts for subclasses
- Concrete implementations provide specific behavior

### Encapsulation
- Private attributes with `__` prefix
- Protected attributes with `_` prefix
- Public interface through methods

### Inheritance
- Hierarchical class structure
- Code reuse through parent classes
- Multiple inheritance with mixins

### Polymorphism
- Same method names, different implementations
- Duck typing with abstract interfaces
- Runtime behavior determination

### Exception Handling
- Custom exception classes for specific errors
- Try-except blocks for error recovery
- Validation before operations

## 💡 Learning Points

1. **Why Abstract Classes Matter**
   - Define contracts for all subclasses
   - Prevent incomplete implementations
   - Enforce consistent interfaces

2. **Properties vs Direct Attributes**
   - Validation on access
   - Computed properties
   - Read-only access control

3. **Custom Exceptions**
   - More specific error handling
   - Better code readability
   - Easier debugging

4. **Type Hints**
   - Improve code documentation
   - Help IDE provide better assistance
   - Catch type errors early

5. **Encapsulation in Practice**
   - Protect sensitive data (PIN)
   - Control access to methods
   - Maintain object integrity

## 🧪 Example Usage

```python
# Create an animal
dog = Dog("Buddy", 2023, "Golden Retriever", is_trained=True)

# Use polymorphic methods
dog.make_sound()  # Outputs: Buddy barks obediently: Woof! Woof!

# Use properties
dog.age  # Returns calculated age based on birth year

# Create a bank account
account = SavingsAccount("John", 5000, "1234", 0.05)

# Perform transactions
account.deposit(1000)
account.withdraw(500, "1234")
account.apply_interest("1234")

# View history
print(account.get_statement("1234"))
```

## 📝 Notes

- PIN validation is demonstrated throughout the banking system
- All numeric inputs are validated before processing
- Transaction history is maintained for audit purposes
- Properties provide clean interface while maintaining encapsulation
- Abstract classes ensure all implementations are complete

## 🎓 Best Practices Demonstrated

✅ Use type hints for clarity  
✅ Validate input at entry points  
✅ Create custom exceptions for specific errors  
✅ Use properties for controlled access  
✅ Document complex logic with docstrings  
✅ Follow naming conventions (_protected, __private)  
✅ Use abstract base classes to define interfaces  
✅ Implement `__str__()` and `__repr__()` for debugging  
✅ Keep methods focused and single-responsibility  
✅ Use meaningful variable and method names
