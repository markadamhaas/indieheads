USE indieheads;

DROP TABLE IF EXISTS MERCH;

CREATE TABLE MERCH (
   Merch_ID INT AUTO_INCREMENT PRIMARY KEY,
   Merch_Type VARCHAR(30),
   Merch_Description VARCHAR (200),
   Merch_Price INT,
   QuantityAvailable INT
);

INSERT INTO MERCH (Merch_Type, Merch_Description, Merch_Price, QuantityAvailable)
VALUES 
('Black T-Shirt', 'Club logo printed on a black t-shirt', 20.00, 100),
('White T-Shirt', 'Club logo printed on a white t-shirt', 20.00, 100),
('Poster', 'Club poster with show info', 5.00, 200),
('Pin', 'Pin with band logo', 2.00, 50),
('Lighter', 'Lighter with printed club logo on the side', 10.00, 120);
