USE indieheads;

DROP TABLE IF EXISTS SETLIST;

CREATE TABLE SETLIST (
    Set_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Band_ID INT,
    Timeslot INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
    FOREIGN KEY (Band_ID) REFERENCES BANDS(Band_ID)
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