use indieheads;

DROP TABLE EVENT;

CREATE TABLE EVENT (
    Event_ID INT AUTO_INCREMENT PRIMARY KEY,
    Venue_ID INT,
    Event_Date DATE,
    Event_Time DATETIME,
    Tickets_Sold INT,
    Ticket_Price INT,
    Total_Expenses INT,
    Revenue INT,
    FOREIGN KEY (Venue_ID) REFERENCES VENUE(Venue_ID)
);
