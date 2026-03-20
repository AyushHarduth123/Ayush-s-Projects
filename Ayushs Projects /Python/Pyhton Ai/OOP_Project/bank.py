# ============================================================================
# ADVANCED ENCAPSULATION WITH VALIDATION, DECORATORS, AND ERROR HANDLING
# ============================================================================
# This module demonstrates:
# - Property decorators with validation
# - Custom exceptions
# - Context managers for transaction safety
# - Transaction logging and audit trail
# - Abstract base classes for account types
# ============================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Tuple


# ========== CUSTOM EXCEPTIONS ==========

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds for withdrawal."""
    pass


class InvalidPINError(Exception):
    """Raised when an incorrect PIN is provided."""
    pass


class InvalidAccountError(Exception):
    """Raised when account data is invalid."""
    pass


class TransactionError(Exception):
    """Raised when a transaction cannot be completed."""
    pass


# ========== ABSTRACT BASE CLASS FOR ACCOUNTS ==========

class AbstractAccount(ABC):
    """
    Abstract base class defining the interface for all account types.
    
    All account types must implement these methods and properties.
    """
    
    @property
    @abstractmethod
    def balance(self):
        """Get current balance."""
        pass
    
    @abstractmethod
    def deposit(self, amount: float) -> str:
        """Deposit money."""
        pass
    
    @abstractmethod
    def withdraw(self, amount: float, pin: str) -> str:
        """Withdraw money."""
        pass
    
    @abstractmethod
    def get_statement(self, pin: str) -> str:
        """Get account statement."""
        pass


# ========== TRANSACTION LOG CLASS ==========

class Transaction:
    """
    Represents a single transaction.
    
    Attributes:
        transaction_type (str): 'DEPOSIT' or 'WITHDRAWAL'
        amount (float): Amount transacted
        timestamp (datetime): When the transaction occurred
        balance_after (float): Balance after transaction
    """
    
    def __init__(self, transaction_type: str, amount: float, balance_after: float):
        """Initialize a transaction record."""
        if transaction_type not in ['DEPOSIT', 'WITHDRAWAL']:
            raise ValueError("Transaction type must be 'DEPOSIT' or 'WITHDRAWAL'")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()
        self.balance_after = balance_after
    
    def __str__(self):
        """String representation of transaction."""
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time_str}] {self.transaction_type:10} ${self.amount:>10.2f} | Balance: ${self.balance_after:>10.2f}"


# ========== MAIN BANK ACCOUNT CLASS ==========

class BankAccount(AbstractAccount):
    """
    Enhanced BankAccount class with advanced features:
    
    - Property-based access with validation
    - Transaction logging and audit trail
    - Custom exception handling
    - Type hints for clarity
    - PIN authentication
    """
    
    def __init__(self, holder_name: str, initial_balance: float, pin: str):
        """
        Initialize a bank account with validation.
        
        Args:
            holder_name (str): Name of account holder
            initial_balance (float): Starting balance
            pin (str): 4-digit PIN for security
            
        Raises:
            InvalidAccountError: If parameters are invalid
        """
        if not holder_name or not isinstance(holder_name, str):
            raise InvalidAccountError("Holder name must be a non-empty string")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise InvalidAccountError("Initial balance must be non-negative number")
        if len(pin) != 4 or not pin.isdigit():
            raise InvalidAccountError("PIN must be exactly 4 digits")
        
        self._holder_name = holder_name
        self._balance = float(initial_balance)
        self.__pin = pin  # Double underscore for privacy
        self._transactions: List[Transaction] = []
        
        # Log initial balance
        if initial_balance > 0:
            initial_transaction = Transaction('DEPOSIT', initial_balance, self._balance)
            self._transactions.append(initial_transaction)
        
        self._account_opened = datetime.now()
    
    # ========== PROPERTIES WITH VALIDATION ==========
    
    @property
    def holder_name(self) -> str:
        """Get account holder's name (read-only)."""
        return self._holder_name
    
    @property
    def balance(self) -> float:
        """Get current balance (read-only)."""
        return round(self._balance, 2)
    
    @property
    def account_age_days(self) -> int:
        """Get how many days the account has been open."""
        return (datetime.now() - self._account_opened).days
    
    @property
    def transaction_count(self) -> int:
        """Get the number of transactions."""
        return len(self._transactions)
    
    # ========== TRANSACTION METHODS ==========
    
    def deposit(self, amount: float) -> str:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            str: Confirmation message
            
        Raises:
            TransactionError: If deposit fails validation
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TransactionError("Amount must be a number")
            if amount <= 0:
                raise TransactionError("Deposit amount must be positive")
            if amount > 1_000_000:
                raise TransactionError("Deposit amount exceeds maximum limit of $1,000,000")
            
            self._balance += amount
            transaction = Transaction('DEPOSIT', amount, self.balance)
            self._transactions.append(transaction)
            
            return f"✓ Deposit successful: ${amount:.2f}\n  New balance: ${self.balance:.2f}"
        
        except TransactionError as e:
            return f"✗ Deposit failed: {str(e)}"
    
    def withdraw(self, amount: float, pin: str) -> str:
        """
        Withdraw money from the account (requires PIN).
        
        Args:
            amount (float): Amount to withdraw
            pin (str): PIN for authentication
            
        Returns:
            str: Confirmation or error message
            
        Raises:
            InvalidPINError: If PIN is incorrect
            InsufficientFundsError: If insufficient balance
            TransactionError: If withdrawal fails validation
        """
        try:
            # Verify PIN first
            if not self._verify_pin(pin):
                raise InvalidPINError("Incorrect PIN provided")
            
            # Validate amount
            if not isinstance(amount, (int, float)):
                raise TransactionError("Amount must be a number")
            if amount <= 0:
                raise TransactionError("Withdrawal amount must be positive")
            if amount > 10_000:
                raise TransactionError("Single withdrawal limited to $10,000")
            
            # Check sufficient funds
            if amount > self._balance:
                raise InsufficientFundsError(
                    f"Insufficient funds. Available: ${self._balance:.2f}"
                )
            
            self._balance -= amount
            transaction = Transaction('WITHDRAWAL', amount, self.balance)
            self._transactions.append(transaction)
            
            return f"✓ Withdrawal successful: ${amount:.2f}\n  New balance: ${self.balance:.2f}"
        
        except (InvalidPINError, InsufficientFundsError, TransactionError) as e:
            return f"✗ Withdrawal failed: {str(e)}"
    
    def check_balance(self, pin: str) -> str:
        """
        Check account balance (requires PIN).
        
        Args:
            pin (str): PIN for authentication
            
        Returns:
            str: Balance information or error message
        """
        if not self._verify_pin(pin):
            return "✗ Access denied: Incorrect PIN"
        
        return (f"Account Balance Information\n"
                f"{'='*40}\n"
                f"Holder: {self._holder_name}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Account Age: {self.account_age_days} days\n"
                f"Transactions: {self.transaction_count}")
    
    def get_statement(self, pin: str) -> str:
        """
        Get detailed account statement with transaction history.
        
        Args:
            pin (str): PIN for authentication
            
        Returns:
            str: Full account statement or error message
        """
        if not self._verify_pin(pin):
            return "✗ Access denied: Incorrect PIN"
        
        if not self._transactions:
            return f"No transactions for {self._holder_name}"
        
        statement = f"ACCOUNT STATEMENT - {self._holder_name}\n"
        statement += "=" * 80 + "\n"
        statement += "Transaction History:\n"
        statement += "-" * 80 + "\n"
        
        for transaction in self._transactions:
            statement += str(transaction) + "\n"
        
        statement += "-" * 80 + "\n"
        statement += f"Current Balance: ${self.balance:.2f}\n"
        statement += f"Total Transactions: {self.transaction_count}"
        
        return statement
    
    # ========== PROTECTED/PRIVATE METHODS ==========
    
    def _verify_pin(self, pin: str) -> bool:
        """
        Protected method to verify PIN.
        
        Args:
            pin (str): PIN to verify
            
        Returns:
            bool: True if PIN matches
        """
        return pin == self.__pin
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"BankAccount(holder='{self._holder_name}', "
                f"balance=${self.balance:.2f}, "
                f"transactions={self.transaction_count})")


# ========== SAVINGS ACCOUNT WITH INTEREST ==========

class SavingsAccount(BankAccount):
    """
    Savings account with automatic interest calculation.
    
    Extends BankAccount with:
    - Interest rate management
    - Interest accrual
    - Special restrictions (minimum balance)
    """
    
    def __init__(self, holder_name: str, initial_balance: float, 
                 pin: str, annual_interest_rate: float):
        """
        Initialize a savings account.
        
        Args:
            holder_name (str): Account holder name
            initial_balance (float): Starting balance (minimum $100)
            pin (str): 4-digit PIN
            annual_interest_rate (float): Annual interest rate (0.0 to 1.0)
            
        Raises:
            InvalidAccountError: If parameters invalid
        """
        if initial_balance < 100:
            raise InvalidAccountError("Savings account requires minimum $100 balance")
        if not (0 <= annual_interest_rate <= 1):
            raise InvalidAccountError("Interest rate must be between 0 and 1")
        
        super().__init__(holder_name, initial_balance, pin)
        self._annual_interest_rate = annual_interest_rate
        self._interest_accrued = 0.0
    
    @property
    def interest_rate(self) -> float:
        """Get annual interest rate."""
        return self._annual_interest_rate
    
    @property
    def interest_accrued(self) -> float:
        """Get total interest accrued."""
        return round(self._interest_accrued, 2)
    
    def apply_interest(self, pin: str) -> str:
        """
        Apply annual interest to the savings account.
        
        Args:
            pin (str): PIN for authentication
            
        Returns:
            str: Interest applied message or error
        """
        if not self._verify_pin(pin):
            return "✗ Access denied: Incorrect PIN"
        
        interest = self._balance * self._annual_interest_rate
        self._balance += interest
        self._interest_accrued += interest
        
        # Create internal transaction record
        transaction = Transaction('DEPOSIT', interest, self.balance)
        self._transactions.append(transaction)
        
        return (f"✓ Interest Applied!\n"
                f"  Interest earned: ${interest:.2f}\n"
                f"  New balance: ${self.balance:.2f}\n"
                f"  Total interest earned: ${self._interest_accrued:.2f}")
    
    def withdraw(self, amount: float, pin: str) -> str:
        """
        Override withdraw with minimum balance requirement.
        
        Args:
            amount (float): Amount to withdraw
            pin (str): PIN for authentication
            
        Returns:
            str: Withdrawal confirmation or error message
        """
        # Check minimum balance constraint
        if (self._balance - amount) < 100:
            return ("✗ Withdrawal failed: Savings account must maintain "
                   "minimum balance of $100")
        
        # Call parent's withdraw method
        return super().withdraw(amount, pin)


# ========== CHECKING ACCOUNT ==========

class CheckingAccount(BankAccount):
    """
    Checking account with overdraft protection.
    
    Features:
    - Overdraft limit
    - Lower fees
    - Check writing capability
    """
    
    def __init__(self, holder_name: str, initial_balance: float, 
                 pin: str, overdraft_limit: float = 500):
        """
        Initialize a checking account.
        
        Args:
            holder_name (str): Account holder name
            initial_balance (float): Starting balance
            pin (str): 4-digit PIN
            overdraft_limit (float): Maximum overdraft allowed
        """
        super().__init__(holder_name, initial_balance, pin)
        self._overdraft_limit = overdraft_limit
        self._checks_written = 0
    
    @property
    def overdraft_limit(self) -> float:
        """Get overdraft limit."""
        return self._overdraft_limit
    
    @property
    def available_funds(self) -> float:
        """Get available funds including overdraft."""
        return round(self._balance + self._overdraft_limit, 2)
    
    def withdraw(self, amount: float, pin: str) -> str:
        """
        Withdraw with overdraft protection.
        
        Args:
            amount (float): Amount to withdraw
            pin (str): PIN for authentication
            
        Returns:
            str: Withdrawal confirmation or error
        """
        if not self._verify_pin(pin):
            return "✗ Access denied: Incorrect PIN"
        
        if amount > self.available_funds:
            return (f"✗ Withdrawal failed: Insufficient funds. "
                   f"Available: ${self.available_funds:.2f}")
        
        self._balance -= amount
        transaction = Transaction('WITHDRAWAL', amount, self.balance)
        self._transactions.append(transaction)
        
        if self._balance < 0:
            return (f"⚠ Withdrawal successful with overdraft\n"
                   f"  Amount: ${amount:.2f}\n"
                   f"  Balance: ${self.balance:.2f} (OVERDRAWN)\n"
                   f"  Available overdraft: ${self._overdraft_limit + self._balance:.2f}")
        
        return f"✓ Withdrawal successful: ${amount:.2f}\n  New balance: ${self.balance:.2f}"
    
    def write_check(self, amount: float, payee: str, pin: str) -> str:
        """
        Write a check (simulated withdrawal).
        
        Args:
            amount (float): Check amount
            payee (str): Who the check is for
            pin (str): PIN for authentication
            
        Returns:
            str: Check written confirmation or error
        """
        result = self.withdraw(amount, pin)
        if result.startswith("✓") or result.startswith("⚠"):
            self._checks_written += 1
            return f"{result}\n  Check #{self._checks_written} written to {payee}"
        return result
