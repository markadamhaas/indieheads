USE indieheads;

-- DROP TABLE VOLUNTEERSCHEDULE;

CREATE TABLE VOLUNTEERSCHEDULE (
    VolunteerSchedule_ID INT AUTO_INCREMENT PRIMARY KEY,
    Event_ID INT,
    Volunteer_ID INT,
    Timeslot INT,
    FOREIGN KEY (Event_ID) REFERENCES EVENT(Event_ID),
    FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER(Volunteer_ID)
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
