USE indieheads;

DROP TABLE IF EXISTS VENDOR;

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