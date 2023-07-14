USE indieheads;

DROP TABLE BANDS;

CREATE TABLE BANDS (
    Band_ID INT AUTO_INCREMENT PRIMARY KEY,
    Band_Name VARCHAR(75) NOT NULL,
    Band_Location VARCHAR(50),
    Band_Genre VARCHAR(50),
    Band_Instagram VARCHAR(50),
    B_Contact_Person VARCHAR(75),
    B_Contact_Number VARCHAR(12)
);

-- CREATE TABLE MEMBERS (
--     Member_ID INT AUTO_INCREMENT PRIMARY KEY,
--     Band_ID INT,
--     Member_FName VARCHAR(50) NOT NULL,
-- 	Member_LName VARCHAR(50),
--     Member_Role VARCHAR(255),
--     FOREIGN KEY (Band_ID) REFERENCES BANDS(Band_ID)
-- );

-- 7th Grade Girl Fight
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('7th Grade Girl Fight', 'Charlottesville', 'Pop', '@7thgradegirlfight', NULL, NULL);

-- Almost Nothing
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Almost Nothing', 'UVA', 'Pop', NULL, 'Meg', '571-439-6105');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Meg', 'Gibson', 'vocals'),
--    	(@last_band_id, 'Emma', ' Gorman', NULL);

-- Backseat Driver
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Backseat Driver', 'UVA', 'Soul/R&B', '@backseatdriverisagoodband', 'John Leo', '757-763-9551');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'John Leo', 'Lluecke', NULL),
--    	(@last_band_id, 'Peter', 'Wellman', NULL);

-- Beezin
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Beezin', 'UVA', 'Jazz', '@we.beezin', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Caleb', 'Barnes', NULL),
--    	(@last_band_id, 'Reza Manuel', 'Mirzaiee', NULL),
--    	(@last_band_id, 'Julia', NULL, NULL);

-- Cave Noise
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Cave Noise', 'UVA', 'Classic Rock', '@cave.noise', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Matt', 'Walker', NULL),
--    	(@last_band_id, 'Connor', 'Bettge', NULL),
--    	(@last_band_id, 'Evan', 'Buchanan', NULL);
  	 
-- Clusterfunk
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Clusterfunk', 'UVA', 'Jazz', '@clusterfunk_uva', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Ethan', 'Blaser', NULL),
--    	(@last_band_id, 'Hanna', 'vocalist', NULL),
--    	(@last_band_id, 'Caleb', 'Barnes', NULL),
--    	(@last_band_id, 'Alex', 'Hails', NULL),
--    	(@last_band_id, 'Rex', 'Serpe', NULL);

-- Cougar Beatrice
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Cougar Beatrice', 'Charlottesville', 'Indie Rock', '@cougarbeatrice', 'Jimmy', '757-710-5613');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'John', 'Gordon', 'lead vocals/guitar'),
--    	(@last_band_id, 'Gabriel', 'Aguto', 'guitar'),
--    	(@last_band_id, 'Jimmy', 'Lord', 'bass'),
--    	(@last_band_id, 'Matt', 'McDonnell', 'drums');

-- Crushing Quiet
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Crushing Quiet', 'Charlottesville', 'Jazz', NULL, 'Ben', '864-617-9297');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Ben', 'Cook', 'drummer');

-- Ellie Bashkow Trio
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Ellie Bashkow Trio', 'UVA', 'Pop', NULL, 'Ellie', NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Ellie', 'Bashkow', NULL);

-- Homework Beer
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Homework Beer', 'UVA', 'Indie Rock', '@homeworkbeerofficial', 'Ethan', '703-675-9310');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Jack', 'Mills', "vocals"),
--    	(@last_band_id, 'Jonah', 'Garces-Foley', "drums"),
--    	(@last_band_id, 'Ethan', 'Frantz', "guitar"),
--    	(@last_band_id, 'Kyle', 'Goodson', "bass");
  	 
-- Indecesive
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Indecisive', 'UVA', 'Classic Rock', '@we.are_indecisive', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Dade', 'Walker', 'bass'),
--    	(@last_band_id, 'Alex', 'Schaefer', 'drums'),
--    	(@last_band_id, 'Erik', 'Holmer', 'guitar');

-- JEEZ
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('JEEZ', 'UVA', 'Pop', NULL, 'Ellie Bashkow', '434-831-6351');

-- Logistical Nightmare
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Logistical Nightmare', 'UVA', 'Classic Rock', '@logisticalnightmare.band', 'Tommy', '804-937-1084');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'John', 'Barnes', 'vocals'),
--    	(@last_band_id, 'Noah', 'Hassett', 'drums'),
--    	(@last_band_id, 'Tommy', 'Manley', 'guitar'),
--    	(@last_band_id, 'Owen', 'Manley', 'part time keyboard');

-- Mellowdrama
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Mellowdrama', 'UVA', 'Indie Rock', '@officialmellowdrama', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Haile', 'Mokrzycki', 'vocalist'),
--    	(@last_band_id, 'Cameron', 'Meredith', 'bass');

-- Orion and the Melted Crayons
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Orion and the Melted Crayons', 'Charlottesville', 'Indie Rock', '@orionandthemeltedcrayons', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Orion', 'Faruque', NULL),
--    	(@last_band_id, 'Ellie', 'Bashkow', NULL);

-- Sneaky Lynx
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Sneaky Lynx', 'UVA', 'Soul/R&B', '@sneakylynxband', 'Ethan', '540-846-1701');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Ethan', 'Green', 'vocalist'),
--    	(@last_band_id, 'Cameron', 'Meredith', 'bass');

-- Souwa Cweam
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Souwa Cweam', 'UVA', 'Indie Rock', NULL, NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Ellie', 'Bashbow', NULL),
--    	(@last_band_id, 'Nahlij', 'Corbin', NULL);

-- The Lint Collectors
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('The Lint Collectors', 'Charlottesville', 'Soul/R&B', '@thelintcollectors', NULL, NULL);
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'John Leo', 'Llueke', NULL),
--    	(@last_band_id, 'Evan', 'Sposato', NULL);

-- Work In Progress
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Work In Progress', 'UVA', NULL, '@workinprogress_cville', 'Michael', '203-658-4120');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Michael', 'McNulty', 'guitar'),
--    	(@last_band_id, 'Carolyn', 'Carbaugh', 'vocalist');

-- Yaard Sale
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Yaard Sale', 'Charlottesville', 'Midwest Emo', '@musicbyyardsale', 'Cadin', '434-962-1044');
-- SET @last_band_id = LAST_INSERT_ID();
-- INSERT INTO MEMBERS (Band_ID, Member_FName, Member_LName, Member_Role)
-- VALUES (@last_band_id, 'Cadin', 'Koslowski', 'vocalist'),
--    	(@last_band_id, 'Jacob', NULL, 'drummer'),
--    	(@last_band_id, 'Mack', 'Koslowski', 'bass');