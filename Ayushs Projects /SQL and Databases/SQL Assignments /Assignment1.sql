


drop table customer;
drop table Driver_Deliveries;
drop table Vehicle;
drop table Driver;
drop table Delivery_Items;
drop table Staff;
drop table Billing;



-- Customer Table
CREATE TABLE Customer (
    CUSTOMER_ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR2(50),
    SURNAME VARCHAR2(50),
    ADDRESS VARCHAR2(100),
    PHONE_NUM VARCHAR2(20),
    EMAIL VARCHAR2(50)
);
 
-- Staff Table
CREATE TABLE Staff (
    STAFF_ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR2(50),
    SURNAME VARCHAR2(50),
    POSITION VARCHAR2(50),
    PHONE_NUM VARCHAR2(20),
    ADDRESS VARCHAR2(100),
    EMAIL VARCHAR2(50)
);
 
-- Billing Table
CREATE TABLE Billing (
    BILL_ID NUMBER PRIMARY KEY,
    CUSTOMER_ID NUMBER,
    STAFF_ID NUMBER,
    BILL_DATE DATE,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID),
    FOREIGN KEY (STAFF_ID) REFERENCES Staff(STAFF_ID)
);
 
-- Delivery_Items Table
CREATE TABLE Delivery_Items (
    DELIVERY_ITEM_ID NUMBER PRIMARY KEY,
    DESCRIPTION VARCHAR2(200),
    STAFF_ID NUMBER,
    FOREIGN KEY (STAFF_ID) REFERENCES Staff(STAFF_ID)
);
 
-- Driver Table
CREATE TABLE Driver (
    DRIVER_ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR2(50),
    SURNAME VARCHAR2(50),
    DRIVER_CODE VARCHAR2(10),
    PHONE_NUM VARCHAR2(20),
    ADDRESS VARCHAR2(100)
);
 
-- Vehicle Table
CREATE TABLE Vehicle (
    VIN_NUMBER VARCHAR2(20) PRIMARY KEY,
    VEHICLE_TYPE VARCHAR2(50),
    MILEAGE NUMBER,
    COLOUR VARCHAR2(20),
    MANUFACTURER VARCHAR2(50)
);
 
-- Driver_Deliveries Table
CREATE TABLE Driver_Deliveries (
    DRIVER_DELIVERY_ID NUMBER PRIMARY KEY,
    VIN_NUMBER VARCHAR2(20),
    DRIVER_ID NUMBER,
    DELIVERY_ITEM_ID NUMBER,
    FOREIGN KEY (VIN_NUMBER) REFERENCES Vehicle(VIN_NUMBER),
    FOREIGN KEY (DRIVER_ID) REFERENCES Driver(DRIVER_ID),
    FOREIGN KEY (DELIVERY_ITEM_ID) REFERENCES Delivery_Items(DELIVERY_ITEM_ID)
);

SELECT * FROM BILLING;
SELECT * FROM CUSTOMER;
SELECT * FROM DRIVER;
SELECT * FROM STAFF;
SELECT * FROM DELIVERY_ITEMS;
SELECT * FROM VEHICLE;
SELECT * FROM DRIVER_DELIVERIES;

--Question 3
CREATE USER C##John IDENTIFIED BY Johnch2024;
CREATE USER C##Hannah IDENTIFIED BY Hannahch2024;

GRANT SELECT ON Customer TO C##John;
GRANT SELECT ON Billing TO C##John;
GRANT SELECT ON Delivery_Items TO C##John;
GRANT SELECT ON Driver TO C##John;
GRANT SELECT ON Driver_Deliveries TO C##John;
GRANT SELECT ON Staff TO C##John;
GRANT SELECT ON Vehicle TO C##John;


GRANT INSERT ON Customer TO C##Hannah;
GRANT INSERT ON Billing TO C##Hannah;
GRANT INSERT ON Delivery_Items TO C##Hannah;
GRANT INSERT ON Driver TO C##Hannah;
GRANT INSERT ON Driver_Deliveries TO C##Hannah;
GRANT INSERT ON Staff TO C##Hannah;
GRANT INSERT ON Vehicle TO C##Hannah;


--Question 4
-- Create a PL/SQL block to use a cursor for the report
SET ServerOutput on;
-- Create a PL/SQL block to use a cursor for the report

-- Create a PL/SQL block to use an explicit cursor for the report

DECLARE
    -- Define an explicit cursor to select the relevant data
    CURSOR driver_cursor IS
        SELECT d.FIRST_NAME AS driver_first_name,
               d.SURNAME AS driver_surname,
               d.DRIVER_CODE AS driver_code,
               v.VIN_NUMBER AS vin_number,
               v.MILEAGE AS mileage
        FROM Driver d
        JOIN Driver_Deliveries dd ON d.DRIVER_ID = dd.DRIVER_ID
        JOIN Vehicle v ON dd.VIN_NUMBER = v.VIN_NUMBER
        WHERE v.MILEAGE < 80000;

    -- Define variables to hold the cursor data
    v_driver_first_name Driver.FIRST_NAME%TYPE;
    v_driver_surname Driver.SURNAME%TYPE;
    v_driver_code Driver.DRIVER_CODE%TYPE;
    v_vin_number Vehicle.VIN_NUMBER%TYPE;
    v_mileage Vehicle.MILEAGE%TYPE;

BEGIN
    -- Open the cursor
    OPEN driver_cursor;

    -- Loop through the results
    LOOP
        -- Fetch a record from the cursor into the variables
        FETCH driver_cursor INTO v_driver_first_name, v_driver_surname, v_driver_code, v_vin_number, v_mileage;
        
        -- Exit the loop if no more rows are found
        EXIT WHEN driver_cursor%NOTFOUND;

        -- Display the results
        DBMS_OUTPUT.PUT_LINE('-----------------------------------');
        DBMS_OUTPUT.PUT_LINE('DRIVER:      ' || v_driver_first_name || ', ' || v_driver_surname);
        DBMS_OUTPUT.PUT_LINE('CODE:        ' || v_driver_code);
        DBMS_OUTPUT.PUT_LINE('VIN NUMBER:  ' || v_vin_number);
        DBMS_OUTPUT.PUT_LINE('MILEAGE:     ' || v_mileage);
        DBMS_OUTPUT.PUT_LINE('-----------------------------------');
    END LOOP;

    -- Close the cursor
    CLOSE driver_cursor;

END;
/


--Question 5
--5.1
DECLARE
    -- Define a cursor to select the staff with the highest number of deliveries
    CURSOR staff_cursor IS
        SELECT s.STAFF_ID, s.FIRST_NAME,s.SURNAME,COUNT(dd.DELIVERY_ITEM_ID) 
        AS deliveries_processed
        FROM Staff s
        JOIN Delivery_Items di ON s.STAFF_ID = di.STAFF_ID
        JOIN Driver_Deliveries dd ON di.DELIVERY_ITEM_ID = dd.DELIVERY_ITEM_ID
        GROUP BY s.STAFF_ID, s.FIRST_NAME, s.SURNAME
        ORDER BY deliveries_processed DESC
        FETCH FIRST ROW ONLY; -- Fetch the top record with the highest count

    v_staff_id Staff.STAFF_ID%TYPE;
    v_first_name Staff.FIRST_NAME%TYPE;
    v_surname Staff.SURNAME%TYPE;
    v_deliveries_processed NUMBER;
BEGIN
    -- Open the cursor
    OPEN staff_cursor;

    -- Fetch the top record
    FETCH staff_cursor INTO v_staff_id, v_first_name, v_surname, v_deliveries_processed;
    
    -- Display the results if a record is found
    IF staff_cursor%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('----------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('STAFF ID:              ' || v_staff_id);
        DBMS_OUTPUT.PUT_LINE('FIRST NAME:            ' || v_first_name);
        DBMS_OUTPUT.PUT_LINE('SURNAME:               ' || v_surname);
        DBMS_OUTPUT.PUT_LINE('DELIVERIES PROCESSED:  ' || v_deliveries_processed);
        DBMS_OUTPUT.PUT_LINE('----------------------------------------------');
    ELSE
        DBMS_OUTPUT.PUT_LINE('No staff found with delivery records.');
    END IF;

    -- Close the cursor
    CLOSE staff_cursor;
END;
/


--5.3.2
-- Create a view to get the count of deliveries processed by each staff member
CREATE OR REPLACE VIEW Staff_Delivery_Count AS
SELECT s.STAFF_ID,
       s.FIRST_NAME,
       s.SURNAME,
       COUNT(dd.DELIVERY_ITEM_ID) AS deliveries_processed
FROM Staff s
JOIN Delivery_Items di ON s.STAFF_ID = di.STAFF_ID
JOIN Driver_Deliveries dd ON di.DELIVERY_ITEM_ID = dd.DELIVERY_ITEM_ID
GROUP BY s.STAFF_ID, s.FIRST_NAME, s.SURNAME;


--Second part

DECLARE
    -- Define a cursor to select the staff with the highest number of deliveries from the view
    CURSOR staff_cursor IS
        SELECT STAFF_ID,
               FIRST_NAME,
               SURNAME,
               deliveries_processed
        FROM Staff_Delivery_Count
        ORDER BY deliveries_processed DESC
        FETCH FIRST ROW ONLY; -- Fetch the top record with the highest count

    v_staff_id Staff.STAFF_ID%TYPE;
    v_first_name Staff.FIRST_NAME%TYPE;
    v_surname Staff.SURNAME%TYPE;
    v_deliveries_processed NUMBER;
BEGIN
    -- Open the cursor
    OPEN staff_cursor;

    -- Fetch the top record
    FETCH staff_cursor INTO v_staff_id, v_first_name, v_surname, v_deliveries_processed;
    
    -- Display the results if a record is found
    IF staff_cursor%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('----------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('STAFF ID:              ' || v_staff_id);
        DBMS_OUTPUT.PUT_LINE('FIRST NAME:            ' || v_first_name);
        DBMS_OUTPUT.PUT_LINE('SURNAME:               ' || v_surname);
        DBMS_OUTPUT.PUT_LINE('DELIVERIES PROCESSED:  ' || v_deliveries_processed);
        DBMS_OUTPUT.PUT_LINE('----------------------------------------------');
    ELSE
        DBMS_OUTPUT.PUT_LINE('No staff found with delivery records.');
    END IF;

    -- Close the cursor
    CLOSE staff_cursor;
END;
/

--6.2
-- Create a sequence to generate unique customer IDs
CREATE SEQUENCE customer_id_seq
START WITH 11020   -- Starting value
INCREMENT BY 1    -- Increment step
MINVALUE 11020    -- Minimum value
MAXVALUE 99999    -- Maximum value
CACHE 20;         -- Cache 20 values for performance

-- Insert a new customer using the sequence for the customer ID
INSERT INTO Customer (CUSTOMER_ID, FIRST_NAME, SURNAME, ADDRESS, PHONE_NUM, EMAIL)
VALUES (customer_id_seq.NEXTVAL, 'Alice', 'Johnson', '789 Oak Street', '0834567890', 'alice.johnson@example.com');

-- Retrieve the next value from the sequence
SELECT customer_id_seq.NEXTVAL AS next_customer_id FROM dual;

