USE indieheads;

DROP TABLE EQUIPMENT;
DROP TABLE VOLUNTEER;

CREATE TABLE VOLUNTEER (
   Volunteer_ID INT AUTO_INCREMENT PRIMARY KEY,
   Volunteer_FName VARCHAR(50),
   Volunteer_LName VARCHAR(50),
   Volunteer_Phone VARCHAR(12),
   Volunteer_Email VARCHAR(50),
   Volunteer_Avail_1 BIT,
   Volunteer_Avail_2 BIT,
   Volunteer_Avail_3 BIT,
   Volunteer_Avail_4 BIT
);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Phone, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('John', 'Doe', 'johndoe@virginia.edu', '555-875-9076', 1, 1, 1, 1);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('Jane', 'Doe', 'janedoe@virginia.edu', 1, 1, 1, 0);

INSERT INTO VOLUNTEER (Volunteer_FName, Volunteer_LName, Volunteer_Email, Volunteer_Avail_1, Volunteer_Avail_2, Volunteer_Avail_3, Volunteer_Avail_4)
VALUES ('Jake', 'Doe', 'jakedoe@virginia.edu', 0, 1, 1, 1);