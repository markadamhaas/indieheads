USE indieheads;

-- DROP TABLE IF EXISTS EVENTMERCH;

CREATE TABLE EVENTMERCH (
    EventMerch_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Merch_ID INT,
    QuantitySold INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
    FOREIGN KEY (Merch_ID) REFERENCES MERCH(Merch_ID)
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