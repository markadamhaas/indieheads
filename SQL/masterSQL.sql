CREATE DATABASE IF NOT EXISTS indieheads;
 
USE indieheads;

DROP TABLE IF EXISTS MERCHVENDOR;
DROP TABLE IF EXISTS EVENTMERCH;
DROP TABLE IF EXISTS MERCH;
DROP TABLE IF EXISTS EVENTEQUIPMENT;
DROP TABLE IF EXISTS SETLIST;
DROP TABLE IF EXISTS VOLUNTEERSCHEDULE;
DROP TABLE IF EXISTS EVENT;
DROP TABLE IF EXISTS VENUE;
DROP TABLE IF EXISTS BANDS;
DROP TABLE IF EXISTS EQUIPMENTVENDOR;
DROP TABLE IF EXISTS EQUIPMENT;
DROP TABLE IF EXISTS VENDOR;
DROP TABLE IF EXISTS VOLUNTEER;

USE indieheads;

CREATE TABLE BANDS (
    Band_ID INT AUTO_INCREMENT PRIMARY KEY,
    Band_Name VARCHAR(75) NOT NULL,
    Band_Location VARCHAR(50),
    Band_Genre VARCHAR(50),
    Band_Instagram VARCHAR(50),
    B_Contact_Person VARCHAR(75),
    B_Contact_Number VARCHAR(12)
);

INSERT INTO BANDS 
(Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES 
('7th Grade Girl Fight', 'Charlottesville', 'Pop', '@7thgradegirlfight', NULL, NULL),
('Almost Nothing', 'UVA', 'Pop', NULL, 'Meg', '571-439-6105'),
('Backseat Driver', 'UVA', 'Soul/R&B', '@backseatdriverisagoodband', 'John Leo', '757-763-9551'),
('Beezin', 'UVA', 'Jazz', '@we.beezin', NULL, NULL),
('Cave Noise', 'UVA', 'Classic Rock', '@cave.noise', NULL, NULL),
('Clusterfunk', 'UVA', 'Jazz', '@clusterfunk_uva', NULL, NULL),
('Cougar Beatrice', 'Charlottesville', 'Indie Rock', '@cougarbeatrice', 'Jimmy', '757-710-5613'),
('Crushing Quiet', 'Charlottesville', 'Jazz', NULL, 'Ben', '864-617-9297'),
('Ellie Bashkow Trio', 'UVA', 'Pop', NULL, 'Ellie', NULL),
('Homework Beer', 'UVA', 'Indie Rock', '@homeworkbeerofficial', 'Ethan', '703-675-9310'),
('Indecisive', 'UVA', 'Classic Rock', '@we.are_indecisive', NULL, NULL),
('JEEZ', 'UVA', 'Pop', NULL, 'Ellie Bashkow', '434-831-6351'),
('Logistical Nightmare', 'UVA', 'Classic Rock', '@logisticalnightmare.band', 'Tommy', '804-937-1084'),
('Mellowdrama', 'UVA', 'Indie Rock', '@officialmellowdrama', NULL, NULL),
('Orion and the Melted Crayons', 'Charlottesville', 'Indie Rock', '@orionandthemeltedcrayons', NULL, NULL),
('Sneaky Lynx', 'UVA', 'Soul/R&B', '@sneakylynxband', 'Ethan', '540-846-1701'),
('Souwa Cweam', 'UVA', 'Indie Rock', NULL, NULL, NULL),
('The Lint Collectors', 'Charlottesville', 'Soul/R&B', '@thelintcollectors', NULL, NULL),
('Work In Progress', 'UVA', NULL, '@workinprogress_cville', 'Michael', '203-658-4120'),
('Yaard Sale', 'Charlottesville', 'Midwest Emo', '@musicbyyardsale', 'Cadin', '434-962-1044');

CREATE TABLE VOLUNTEER (
   Volunteer_ID INT AUTO_INCREMENT PRIMARY KEY,
   Volunteer_FName VARCHAR(50),
   Volunteer_LName VARCHAR(50),
   Volunteer_Phone VARCHAR(12),
   Volunteer_Email VARCHAR(50),
   Volunteer_Avail_1 BIT,
   Volunteer_Avail_2 BIT,
   Volunteer_Avail_3 BIT,
   Volunteer_Avail_4 BIT
);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Phone, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('John', 'Doe', 'johndoe@virginia.edu', '555-875-9076', 1, 1, 1, 1);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('Jane', 'Doe', 'janedoe@virginia.edu', 1, 1, 1, 0);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('Jake', 'Doe', 'jakedoe@virginia.edu', 0, 1, 1, 1);

CREATE TABLE EQUIPMENT (
   Equipment_ID INT AUTO_INCREMENT PRIMARY KEY,
   Equipment_Type VARCHAR(30),
   Equipment_Cost DECIMAL,
   Volunteer_ID INT,
   FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER(Volunteer_ID)
    ON DELETE SET NULL
);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Drumkit (Backline)', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Drumkit (Backline)', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Audio Engineer', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Audio Engineer', 50, NULL);

CREATE TABLE MERCH (
   Merch_ID INT AUTO_INCREMENT PRIMARY KEY,
   Merch_Type VARCHAR(30),
   Merch_Description VARCHAR (200),
   Merch_Price DECIMAL,
   QuantityAvailable INT
);

INSERT INTO MERCH (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable)
VALUES 
('Black T-Shirt', 'Club logo printed on a black t-shirt', 20.00, 100),
('White T-Shirt', 'Club logo printed on a white t-shirt', 20.00, 100),
('Poster', 'Club poster with show info', 5.00, 200),
('Pin', 'Pin with band logo', 2.00, 50),
('Lighter', 'Lighter with printed club logo on the side', 10.00, 120);

CREATE TABLE VENDOR (
   Vendor_ID INT AUTO_INCREMENT PRIMARY KEY,
   Vendor_Name VARCHAR(50) NOT NULL,
   Vendor_Street VARCHAR(50),
   Vendor_City VARCHAR(50),
   Vendor_State VARCHAR(2),
   Vendor_Zip VARCHAR(5),
   Vendor_Phone VARCHAR(12),
   Vendor_Email VARCHAR(50)
);

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone)
VALUES 
('UREC', '555-987-2345'),
('Beezin', '555-123-8675'),
('Yaard Sale', '555-123-8675'),
('Brandon Bitgood', '555-965-2254');

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone, Vendor_Email)
VALUES ('CustomInk', '555-678-9854', 'support@CustomInk.com');

INSERT INTO VENDOR (Vendor_Name, Vendor_Street, Vendor_City, Vendor_State, Vendor_Zip, Vendor_Email)
VALUES ('1515', '1515 Univeristy Ave', 'Charlottesville', 'VA', '22903', '1515@virginia.edu');

CREATE TABLE VENUE (
   Venue_ID INT AUTO_INCREMENT PRIMARY KEY,
   Venue_Name VARCHAR(50),
   Venue_Street VARCHAR(100),
   Venue_City VARCHAR(30),
   Venue_State VARCHAR(2),
   Venue_Zip VARCHAR(5),
   Venue_Price DECIMAL(8,2),
   Venue_Type VARCHAR(30),
   Venue_Contact VARCHAR(50),
   Venue_Phone VARCHAR(12),
   Venue_Email VARCHAR(25)
);

INSERT INTO VENUE (Venue_Name, Venue_Street, Venue_City, Venue_State, Venue_Zip, Venue_Price, Venue_Type, Venue_Contact, Venue_Phone)
VALUES 
('Crew House', '600 14th St. NW', 'Charlottesville', 'VA', '22903', '200', 'Porch', 'John', '781-708-2296'),
('14th St House 1', '362 14th St. NW', 'Charlottesville', 'VA', '22903', '250', 'Porch', 'Amanda', '678-879-2384'),
('Uni Circle House', '8 University Court', 'Charlottesville', 'VA', '22903', '225', 'Porch', 'Hannah', '678-879-2384'),
('Sailing House', '519 14th St', 'Charlottesville', 'VA', '22903', '260', 'Backyard', 'Kate', '757-773-0577'),
('14th St House 2', '519 14th St', 'Charlottesville', 'VA', '22903', '200', 'Backyard', 'CJ', '555-423-1000'),
('Montebello House', '325 Montebello Cir', 'Charlottesville', 'VA', '22903', '190', 'Backyard', 'Mike', '555-983-2245'),
('AVP House', '303 14th St', 'Charlottesville', 'VA', '22903', '200', 'Basement', 'Erik', '555-224-9845');


CREATE TABLE EQUIPMENTVENDOR (
    EquipmentVendor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Equipment_ID INT,
    Vendor_ID INT,
    FOREIGN KEY (Equipment_ID) REFERENCES EQUIPMENT(Equipment_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Vendor_ID) REFERENCES VENDOR(Vendor_ID)
        ON DELETE SET NULL
);

-- UREC --
INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID)
VALUES (1, 1), (3, 1), (6, 1);

-- Yaard Sale --
INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID)
VALUES (2, 3), (4, 3);

-- Beezin --
INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID)
VALUES (5, 2);

-- Brandon --
INSERT INTO EQUIPMENTVENDOR (Equipment_ID, Vendor_ID)
VALUES (7, 4);

CREATE TABLE EVENT (
    Event_ID INT AUTO_INCREMENT PRIMARY KEY,
    Venue_ID INT,
    Event_Date DATE,
    Event_Time VARCHAR(5),
    Tickets_Sold INT,
    Ticket_Price DECIMAL,
    Misc_Expenses DECIMAL,
    Total_Expenses DECIMAL,
    Revenue DECIMAL,
    FOREIGN KEY (Venue_ID) REFERENCES VENUE(Venue_ID)
        ON DELETE SET NULL
);

INSERT INTO EVENT (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price, Misc_Expenses)
VALUES 
(1, '2023-09-01', '19:00', 250, 50, 10),
(2, '2023-10-01', '20:00', 300, 100, 10);    

CREATE TABLE EVENTEQUIPMENT (
    EventEquipment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Equipment_ID INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Equipment_ID) REFERENCES EQUIPMENT(Equipment_ID)
        ON DELETE CASCADE
);

INSERT INTO EVENTEQUIPMENT (Event_ID, Equipment_ID) 
VALUES 
(1, 3), 
(1, 5),
(1, 7);

INSERT INTO EVENTEQUIPMENT (Event_ID, Equipment_ID) 
VALUES 
(2, 1), 
(2, 4),
(2, 7);

CREATE TABLE EVENTMERCH (
    EventMerch_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Merch_ID INT,
    QuantitySold INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Merch_ID) REFERENCES MERCH(Merch_ID)
        ON DELETE CASCADE
);

INSERT INTO EVENTMERCH (Event_ID, Merch_ID, QuantitySold)
VALUES
(1, 1, 20),
(1, 2, 15),
(1, 3, 25),
(1, 4, 10),
(1, 5, 30),
(2, 1, 25),
(2, 2, 15),
(2, 3, 20),
(2, 4, 30),
(2, 5, 10);

CREATE TABLE MERCHVENDOR (
    MerchVendor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Merch_ID INT,
    Vendor_ID INT,
    QuantitySupplied INT,
    Cost DECIMAL,
    FOREIGN KEY (Merch_ID) REFERENCES MERCH(Merch_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Vendor_ID) REFERENCES VENDOR(Vendor_ID)
        ON DELETE SET NULL
);

INSERT INTO MERCHVENDOR (Merch_ID, Vendor_ID, QuantitySupplied)
VALUES
(1, 4, 500, 50),
(2, 4, 600, 75),
(5, 4, 550, 60),
(3, 5, 400, 40),
(4, 5, 700, 80);

CREATE TABLE SETLIST (
    Set_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Band_ID INT,
    Timeslot INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Band_ID) REFERENCES BANDS(Band_ID)
        ON DELETE SET NULL
);

INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) 
VALUES 
(1, 1, 1), 
(1, 2, 2), 
(1, 3, 3), 
(1, 4, 4);

INSERT INTO SETLIST (Event_ID, Band_ID, Timeslot) 
VALUES 
(2, 1, 1), 
(2, 2, 2), 
(2, 3, 3), 
(2, 4, 4);

CREATE TABLE VOLUNTEERSCHEDULE (
    VolunteerSchedule_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Volunteer_ID INT,
    Timeslot INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
        ON DELETE CASCADE
    FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER(Volunteer_ID)
        ON DELETE SET NULL
);

INSERT INTO VOLUNTEERSCHEDULE (Event_ID, Volunteer_ID, Timeslot)
VALUES
(1, 1, 1),
(1, 1, 2),
(1, 2, 3),
(1, 1, 4),
(2, 2, 1),
(2, 2, 2),
(2, 2, 3),
(2, 3, 4);