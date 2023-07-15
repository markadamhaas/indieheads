USE indieheads;

DROP TABLE VENDOR;

CREATE TABLE VENDOR (
   Vendor_ID INT AUTO_INCREMENT PRIMARY KEY,
   Vendor_Name VARCHAR(50),
   Vendor_Street VARCHAR(50),
   Vendor_City VARCHAR(50),
   Vendor_State VARCHAR(20),
   Vendor_Zip VARCHAR(10),
   Vendor_Phone VARCHAR(12),
   Vendor_Email VARCHAR(50)
);

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone)
VALUES ('UREC', '555-987-2345');

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone)
VALUES ('Beezin', '555-123-8675');

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone)
VALUES ('Yaard Sale', '555-123-8675');

INSERT INTO VENDOR (Vendor_Name, Vendor_Phone)
VALUES ('Brandon Bitgood', '555-965-2254');