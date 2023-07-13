USE indieheads;

DROP TABLE MERCH;

CREATE TABLE MERCH (
   Merch_ID INT AUTO_INCREMENT PRIMARY KEY,
   Merch_Type VARCHAR(30),
   Merch_Description VARCHAR (200),
   Merch_Price INT,
   QuantityAvailable INT
);