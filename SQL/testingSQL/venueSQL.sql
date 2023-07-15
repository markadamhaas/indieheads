USE indieheads;

DROP TABLE IF EXISTS VENUE;

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