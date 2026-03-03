CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100) NOT NULL,
    Surname NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    PhoneNumber NVARCHAR(15) NOT NULL,
    Address NVARCHAR(200) NOT NULL
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY,
    ProductName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(500) NOT NULL,
    Price DECIMAL(18, 2) NOT NULL,
    Category NVARCHAR(100) NOT NULL,
    Quantity INT NOT NULL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY,
    CustomerID INT NOT NULL,
    CustomerName NVARCHAR (100) NOT NULL,
    Product NVARCHAR (100) NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);




       SELECT * FROM PRODUCTS;
	   SELECT * FROM ORDERS;
	   SELECT * FROM CUSTOMERS;

       DROP TABLE PRODUCTS;
       DROP TABLE CUSTOMERS;
       DROP TABLE ORDERS;

-- Insert data into Customers table
INSERT INTO Customers (Name, Surname, Email, PhoneNumber, Address)
VALUES 
('Alice', 'Smith', 'alice@example.com', '123-456-7890', '123 Main St'),
('Bob', 'Johnson', 'bob@example.com', '234-567-8901', '456 Elm St'),
('Carol', 'Williams', 'carol@example.com', '345-678-9012', '789 Oak St');

-- Insert data into Products table
INSERT INTO Products (ProductName, Description, Price, Category, Quantity)
VALUES
('Laptop', '15-inch laptop with 8GB RAM and 256GB SSD', 799.99, 'Electronics', 50),
('Smartphone', 'Latest model with 128GB storage and 5G capability', 699.99, 'Electronics', 100),
('Headphones', 'Noise-canceling over-ear headphones', 199.99, 'Accessories', 150);

-- Insert data into Orders table
INSERT INTO Orders (CustomerID, CustomerName, Product, ProductID, Quantity)
VALUES
(1, 'Alice Smith', 'Laptop', 1, 2), -- Alice orders 2 Laptops
(2, 'Bob Johnson', 'Smartphone', 2, 1), -- Bob orders 1 Smartphone
(3, 'Carol Williams', 'Headphones', 3, 3); -- Carol orders 3 Headphones


INSERT INTO Orders (CustomerID, CustomerName, Product, ProductID, Quantity)
VALUES
(1, 'Ayush Harduth', 'Fireworks', 4, 5); -- Alice orders 2 Laptops