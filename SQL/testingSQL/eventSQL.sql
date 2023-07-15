use indieheads;

-- DROP TABLE SETLIST;
-- DROP TABLE VOLUNTEERSCHEDULE;
-- DROP TABLE EVENTMERCH;
-- DROP TABLE EVENTEQUIPMENT;
DROP TABLE IF EXISTS EVENT;

CREATE TABLE EVENT (
    Event_ID INT AUTO_INCREMENT PRIMARY KEY,
    Venue_ID INT,
    Event_Date DATE,
    Event_Time VARCHAR(5),
    Tickets_Sold INT,
    Ticket_Price INT,
    Total_Expenses INT,
    Revenue INT,
    FOREIGN KEY (Venue_ID) REFERENCES VENUE(Venue_ID)
);


INSERT INTO EVENT (Venue_ID, Event_Date, Event_Time, Tickets_Sold, Ticket_Price)
VALUES 
(1, '2023-09-01', '19:00', 50, 10),
(2, '2023-10-01', '20:00', 100, 10);
