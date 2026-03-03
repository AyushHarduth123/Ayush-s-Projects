--ASSIGNMENT 2

Drop table customer;
Drop table employee;
Drop table empoyees;
Drop table Environment_Activities;
drop table funding;
drop table locations;
Drop table donator;
Drop table donation;
Drop table delivery;
Drop table returns;
drop table invoice;

drop table billing;
drop table course;
drop table delivery_items;
drop table driver;
drop table driver_deliveries;
drop table employees;
drop table Enviroment_Activities;
drop table locatons;
drop table results;
drop table staff;
drop table student;
drop table vehicle;

drop table booking;
drop table bus;
drop table cancellations;
drop table customer;
drop table locations;




Select * From Customer;
Select * From Employee;
Select * From donator;
Select * From donation;
Select * From delivery;
Select * From returns;
Select * From invoice;

--QUESTION 1
-- Code to create CUSTOMER table
CREATE TABLE CUSTOMER (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    address VARCHAR(255),
    contact_number VARCHAR(255),
    email VARCHAR(255)
);

-- Code to insert data into CUSTOMER table
INSERT INTO CUSTOMER (customer_id, first_name, surname, address, contact_number, email) VALUES 
(11011, 'Jack', 'Smith', '18 Water Rd', '0877277521', 'jsmith@isat.com');
INSERT INTO CUSTOMER (customer_id, first_name, surname, address, contact_number, email) VALUES 
(11012, 'Pat', 'Hendricks', '22 Water Rd', '0863257857', 'ph@mcom.co.za');
INSERT INTO CUSTOMER (customer_id, first_name, surname, address, contact_number, email) VALUES 
(11013, 'Andre', 'Clark', '101 Summer Lane', '0834567891', 'aclark@mcom.co.za');
INSERT INTO CUSTOMER (customer_id, first_name, surname, address, contact_number, email) VALUES 
(11014, 'Kevin', 'Jones', '55 Mountain Way', '0612547895', 'kj@isat.co.za');
INSERT INTO CUSTOMER (customer_id, first_name, surname, address, contact_number, email) VALUES 
(11015, 'Lucy', 'Williams', '5 Main Rd', '0827238521', 'lw@mcal.co.za');

-- Code to create EMPLOYEE table
CREATE TABLE EMPLOYEE (
    employee_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    contact_number VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255)
);

-- Code to insert data into EMPLOYEE table
INSERT INTO EMPLOYEE (employee_id, first_name, surname, contact_number, address, email) VALUES 
('emp101', 'Jeff', 'Davis', '0877277521', '10 main road', 'jand@isat.com');
INSERT INTO EMPLOYEE (employee_id, first_name, surname, contact_number, address, email) VALUES 
('emp102', 'Kevin', 'Marks', '0837377522', '18 water road', 'km@isat.com');
INSERT INTO EMPLOYEE (employee_id, first_name, surname, contact_number, address, email) VALUES 
('emp103', 'Adanya', 'Andrews', '0817117523', '21 circle lane', 'aa@isat.com');
INSERT INTO EMPLOYEE (employee_id, first_name, surname, contact_number, address, email) VALUES 
('emp104', 'Adebayo', 'Dryer', '0797215244', '1 sea road', 'aryer@isat.com');
INSERT INTO EMPLOYEE (employee_id, first_name, surname, contact_number, address, email) VALUES 
('emp105', 'Xolani', 'Samson', '0827122255', '12 main road', 'xosam@isat.com');



-- Code to create DONATOR table
CREATE TABLE DONATOR (
    donator_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    contact_number VARCHAR(255),
    email VARCHAR(255)
);

-- Code to insert data into DONATOR table
INSERT INTO DONATOR (donator_id, first_name, surname, contact_number, email) VALUES 
(20111, 'Jeff', 'Watson', '0827172250', 'jwatson@ymail.com');
INSERT INTO DONATOR (donator_id, first_name, surname, contact_number, email) VALUES 
(20112, 'Stephen', 'Jones', '0837865670', 'joness@ymail.com');
INSERT INTO DONATOR (donator_id, first_name, surname, contact_number, email) VALUES 
(20113, 'James', 'Joe', '0878978650', 'jj@isat.com');
INSERT INTO DONATOR (donator_id, first_name, surname, contact_number, email) VALUES 
(20114, 'Kelly', 'Ross', '0826575650', 'kross@gsat.com');
INSERT INTO DONATOR (donator_id, first_name, surname, contact_number, email) VALUES 
(20115, 'Abraham', 'Clark', '0797656430', 'aclark@ymail.com');



-- Code to create DONATION table
CREATE TABLE DONATION (
    donation_id INT PRIMARY KEY,
    donator_id INT,
    donation VARCHAR(255),
    price DECIMAL(10, 2),
    donation_date DATE,
    FOREIGN KEY (donator_id) REFERENCES DONATOR(donator_id)
);

-- Code to insert data into DONATION table with corrected date format
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7111, 20111, 'KIC Fridge', 599.00, TO_DATE('2024-05-01', 'YYYY-MM-DD'));
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7112, 20112, 'Samsung 42inch LCD', 1299.00, TO_DATE('2024-05-03', 'YYYY-MM-DD'));
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7113, 20113, 'Sharp Microwave', 1599.00, TO_DATE('2024-05-03', 'YYYY-MM-DD'));
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7114, 20115, '6 Seat Dining Room Table', 799.00, TO_DATE('2024-05-05', 'YYYY-MM-DD'));
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7115, 20114, 'Lazyboy Sofa', 1199.00, TO_DATE('2024-05-07', 'YYYY-MM-DD'));
INSERT INTO DONATION (donation_id, donator_id, donation, price, donation_date) VALUES 
(7116, 20113, 'JVC Surround Sound System', 179.00, TO_DATE('2024-05-09', 'YYYY-MM-DD'));




-- Code to create DELIVERY table
CREATE TABLE DELIVERY (
    delivery_id INT PRIMARY KEY,
    delivery_notes VARCHAR(255),
    dispatch_date DATE,
    delivery_date DATE
);

-- Code to insert data into DELIVERY table with corrected date format
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(511, 'Double packaging requested', TO_DATE('2024-05-10', 'YYYY-MM-DD'), TO_DATE('2024-05-15', 'YYYY-MM-DD'));
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(512, 'Delivery to work address', TO_DATE('2024-05-12', 'YYYY-MM-DD'), TO_DATE('2024-05-15', 'YYYY-MM-DD'));
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(513, 'Signature required', TO_DATE('2024-05-12', 'YYYY-MM-DD'), TO_DATE('2024-05-17', 'YYYY-MM-DD'));
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(514, 'No notes', TO_DATE('2024-05-12', 'YYYY-MM-DD'), TO_DATE('2024-05-15', 'YYYY-MM-DD'));
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(515, 'Birthday present wrapping required', TO_DATE('2024-05-18', 'YYYY-MM-DD'), TO_DATE('2024-05-19', 'YYYY-MM-DD'));
INSERT INTO DELIVERY (delivery_id, delivery_notes, dispatch_date, delivery_date) VALUES 
(516, 'Delivery to work address', TO_DATE('2024-05-20', 'YYYY-MM-DD'), TO_DATE('2024-05-25', 'YYYY-MM-DD'));





-- Code to create RETURNS table
CREATE TABLE RETURNS (
    return_id VARCHAR(10) PRIMARY KEY,
    return_date DATE,
    reason VARCHAR(255),
    customer_id INT,
    donation_id INT,
    employee_id VARCHAR(10),
    FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY (donation_id) REFERENCES DONATION(donation_id),
    FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id)
);

-- Code to insert data into RETURNS table with corrected date format
INSERT INTO RETURNS (return_id, return_date, reason, customer_id, donation_id, employee_id) VALUES 
('ret001', TO_DATE('2024-05-25', 'YYYY-MM-DD'), 'Customer not satisfied with product', 11011, 7116, 'emp101');
INSERT INTO RETURNS (return_id, return_date, reason, customer_id, donation_id, employee_id) VALUES 
('ret002', TO_DATE('2024-05-25', 'YYYY-MM-DD'), 'Product had broken section', 11013, 7114, 'emp103');


-- Code to create INVOICE table
CREATE TABLE INVOICE (
    invoice_num INT PRIMARY KEY,
    customer_id INT,
    invoice_date DATE,
    employee_id VARCHAR(10),
    donation_id INT,
    delivery_id INT,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id),
    FOREIGN KEY (donation_id) REFERENCES DONATION(donation_id),
    FOREIGN KEY (delivery_id) REFERENCES DELIVERY(delivery_id)
);

-- Code to insert data into INVOICE table with corrected date format
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8111, 11011, TO_DATE('2024-05-15', 'YYYY-MM-DD'), 'emp103', 7111, 511);
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8112, 11013, TO_DATE('2024-05-15', 'YYYY-MM-DD'), 'emp101', 7114, 512);
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8113, 11012, TO_DATE('2024-05-17', 'YYYY-MM-DD'), 'emp101', 7112, 513);
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8114, 11015, TO_DATE('2024-05-17', 'YYYY-MM-DD'), 'emp102', 7113, 514);
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8115, 11011, TO_DATE('2024-05-17', 'YYYY-MM-DD'), 'emp102', 7115, 515);
INSERT INTO INVOICE (invoice_num, customer_id, invoice_date, employee_id, donation_id, delivery_id) VALUES 
(8116, 11015, TO_DATE('2024-05-18', 'YYYY-MM-DD'), 'emp103', 7116, 516);





SET serveroutput ON;

--Question 2
SELECT 
    c.first_name || ' ' || c.surname AS CUSTOMER,
    i.employee_id AS EMPLOYEE_ID,
    d.delivery_notes AS DELIVERY_NOTES,
    dn.donation AS DONATION,
    i.invoice_num AS INVOICE_NO,
    i.invoice_date AS INVOICE_DATE
FROM 
    INVOICE i
JOIN 
    CUSTOMER c ON i.customer_id = c.customer_id
JOIN 
    DELIVERY d ON i.delivery_id = d.delivery_id
JOIN 
    DONATION dn ON i.donation_id = dn.donation_id
WHERE 
    i.invoice_date > TO_DATE('2024-05-16', 'YYYY-MM-DD');
    

--Question 3

--The NUMBER GENERATED BY DEFAULT AS IDENTITY clause in the funding_id column 
--ensures that a unique ID is automatically generated for each new record inserted
--into the FUNDING table.

CREATE TABLE FUNDING (
    funding_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    funder VARCHAR2(100),
    funding_amount NUMBER
);

--3. Here is some example data to add to the table 
INSERT INTO FUNDING (funder, funding_amount) VALUES ('Global Aid', 5000);


SELECT * FROM FUNDING;

--Question 4
SET SERVEROUTPUT ON;


BEGIN
    FOR donation_rec IN (
        SELECT 
            c.first_name || ', ' || c.surname AS customer_name,
            dn.donation AS donation_purchased,
            dn.price AS donation_price,
            r.reason AS return_reason
        FROM 
            CUSTOMER c
        JOIN 
            RETURNS r ON c.customer_id = r.customer_id
        JOIN 
            DONATION dn ON r.donation_id = dn.donation_id
        
    ) LOOP
        DBMS_OUTPUT.PUT_LINE('CUSTOMER:             ' || donation_rec.customer_name);
        DBMS_OUTPUT.PUT_LINE('DONATION PURCHASED:   ' || donation_rec.donation_purchased);
        DBMS_OUTPUT.PUT_LINE('PRICE:                ' || donation_rec.donation_price);
        DBMS_OUTPUT.PUT_LINE('RETURN REASON:        ' || donation_rec.return_reason);
        DBMS_OUTPUT.PUT_LINE('--------------------------------------------------');
    END LOOP;
END;

--Question 5

SET SERVEROUTPUT ON;

BEGIN
    FOR rec IN (
        SELECT 
            SUBSTR(c.first_name, 1, 1) || '.' || c.surname AS customer_name,
            SUBSTR(e.first_name, 1, 1) || '.' || e.surname AS employee_name,
            dn.donation,
            TO_CHAR(d.dispatch_date, 'DD/MON/YY') AS dispatch_date,
            TO_CHAR(d.delivery_date, 'DD/MON/YY') AS delivery_date,
            (d.delivery_date - d.dispatch_date) AS days_to_delivery
        FROM 
            CUSTOMER c
        JOIN 
            INVOICE i ON c.customer_id = i.customer_id
        JOIN 
            DELIVERY d ON i.delivery_id = d.delivery_id
        JOIN 
            EMPLOYEE e ON i.employee_id = e.employee_id
        JOIN 
            DONATION dn ON i.donation_id = dn.donation_id
        WHERE 
            c.customer_id = 11011
        ORDER BY 
            d.dispatch_date
    ) LOOP
        DBMS_OUTPUT.PUT_LINE('CUSTOMER: ' || rec.customer_name);
        DBMS_OUTPUT.PUT_LINE('EMPLOYEE: ' || rec.employee_name);
        DBMS_OUTPUT.PUT_LINE('DONATION: ' || rec.donation);
        DBMS_OUTPUT.PUT_LINE('DISPATCH DATE: ' || rec.dispatch_date);
        DBMS_OUTPUT.PUT_LINE('DELIVERY DATE: ' || rec.delivery_date);
        DBMS_OUTPUT.PUT_LINE('DAYS TO DELIVERY: ' || rec.days_to_delivery);
        DBMS_OUTPUT.PUT_LINE('-------------------------------------');
    END LOOP;
END;


--Question 6
SET SERVEROUTPUT ON;

DECLARE
    CURSOR customer_cursor IS
        SELECT 
            c.first_name,
            c.surname,
            SUM(d.price) AS total_amount_spent,
            CASE 
                WHEN SUM(d.price) >= 1500 THEN ' ( *** )'
                ELSE ''
            END AS customer_rating
        FROM 
            CUSTOMER c
        JOIN 
            INVOICE i ON c.customer_id = i.customer_id
        JOIN 
            DONATION d ON i.donation_id = d.donation_id
        GROUP BY 
            c.first_name, c.surname;


    customer_rec customer_cursor%ROWTYPE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Sample Output:');
    DBMS_OUTPUT.PUT_LINE('PL/SQL procedure successfully completed.');
    DBMS_OUTPUT.PUT_LINE('');
    
    OPEN customer_cursor;
    LOOP
        FETCH customer_cursor INTO customer_rec;
        EXIT WHEN customer_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE('FIRST NAME: ' || customer_rec.first_name);
        DBMS_OUTPUT.PUT_LINE('SURNAME   : ' || customer_rec.surname);
        DBMS_OUTPUT.PUT_LINE('AMOUNT    : R ' || customer_rec.total_amount_spent || customer_rec.customer_rating);
        DBMS_OUTPUT.PUT_LINE('----------------------------------------------------------------------');
    END LOOP;
    CLOSE customer_cursor;
END;
/

--Question 7
-- 7.1 %Type Attribute 
DECLARE
    v_customer_id CUSTOMER.customer_id%TYPE;
    v_first_name CUSTOMER.first_name%TYPE;
BEGIN
    -- Assign values to the variables
    v_customer_id := 11011;
    v_first_name := 'Jack';

    -- Output the values
    DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id);
    DBMS_OUTPUT.PUT_LINE('First Name: ' || v_first_name);
END;
/


--7.2 %RowType
DECLARE
    v_customer_record CUSTOMER%ROWTYPE;
BEGIN
    -- Select a row into the record
    SELECT * INTO v_customer_record FROM CUSTOMER WHERE customer_id = 11011;

    -- Output the values
    DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_record.customer_id);
    DBMS_OUTPUT.PUT_LINE('First Name: ' || v_customer_record.first_name);
    DBMS_OUTPUT.PUT_LINE('Surname: ' || v_customer_record.surname);
    DBMS_OUTPUT.PUT_LINE('Address: ' || v_customer_record.address);
    DBMS_OUTPUT.PUT_LINE('Contact Number: ' || v_customer_record.contact_number);
    DBMS_OUTPUT.PUT_LINE('Email: ' || v_customer_record.email);
END;
/


--7.3 User Defined exeception
DECLARE
    e_invalid_customer EXCEPTION;
    v_customer_id CUSTOMER.customer_id%TYPE := 99999; -- Non-existent customer ID
BEGIN
    -- Check if the customer ID exists
    DECLARE
        v_count INTEGER;
    BEGIN
        SELECT COUNT(*) INTO v_count FROM CUSTOMER WHERE customer_id = v_customer_id;
        IF v_count = 0 THEN
            RAISE e_invalid_customer;
        END IF;
    END;

    -- If no exception, output a success message
    DBMS_OUTPUT.PUT_LINE('Customer ID ' || v_customer_id || ' is valid.');

EXCEPTION
    WHEN e_invalid_customer THEN
        DBMS_OUTPUT.PUT_LINE('Error: Invalid customer ID ' || v_customer_id);
END;
/

--Question 8
SELECT 
    c.first_name,
    c.surname,
    SUM(d.price) AS total_amount_spent,
    CASE 
        WHEN SUM(d.price) >= 1500 THEN '***'
        WHEN SUM(d.price) BETWEEN 1000 AND 1400 THEN '**'
        ELSE '*'
    END AS customer_rating
FROM 
    CUSTOMER c
JOIN 
    INVOICE i ON c.customer_id = i.customer_id
JOIN 
    DONATION d ON i.donation_id = d.donation_id
GROUP BY 
    c.first_name, c.surname;



