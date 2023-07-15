USE indieheads;

DROP TABLE IF EXISTS EQUIPMENT;

CREATE TABLE EQUIPMENT (
   Equipment_ID INT AUTO_INCREMENT PRIMARY KEY,
   Equipment_Type VARCHAR(30),
   Equipment_Cost INT,
   Volunteer_ID INT,
   FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER(Volunteer_ID)
);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Drumkit (Backline)', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Drumkit (Backline)', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('PA System', 30, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Audio Engineer', 50, NULL);

INSERT INTO EQUIPMENT (Equipment_Type, Equipment_Cost, Volunteer_ID)
VALUES ('Audio Engineer', 50, NULL);