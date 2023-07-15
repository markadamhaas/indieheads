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


-- 7th Grade Girl Fight
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('7th Grade Girl Fight', 'Charlottesville', 'Pop', '@7thgradegirlfight', NULL, NULL);

-- Almost Nothing
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Almost Nothing', 'UVA', 'Pop', NULL, 'Meg', '571-439-6105');


-- Backseat Driver
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Backseat Driver', 'UVA', 'Soul/R&B', '@backseatdriverisagoodband', 'John Leo', '757-763-9551');


-- Beezin
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Beezin', 'UVA', 'Jazz', '@we.beezin', NULL, NULL);


-- Cave Noise
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Cave Noise', 'UVA', 'Classic Rock', '@cave.noise', NULL, NULL);

  	 
-- Clusterfunk
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Clusterfunk', 'UVA', 'Jazz', '@clusterfunk_uva', NULL, NULL);


-- Cougar Beatrice
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Cougar Beatrice', 'Charlottesville', 'Indie Rock', '@cougarbeatrice', 'Jimmy', '757-710-5613');


-- Crushing Quiet
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Crushing Quiet', 'Charlottesville', 'Jazz', NULL, 'Ben', '864-617-9297');


-- Ellie Bashkow Trio
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Ellie Bashkow Trio', 'UVA', 'Pop', NULL, 'Ellie', NULL);


-- Homework Beer
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Homework Beer', 'UVA', 'Indie Rock', '@homeworkbeerofficial', 'Ethan', '703-675-9310');

  	 
-- Indecesive
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Indecisive', 'UVA', 'Classic Rock', '@we.are_indecisive', NULL, NULL);


-- JEEZ
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('JEEZ', 'UVA', 'Pop', NULL, 'Ellie Bashkow', '434-831-6351');

-- Logistical Nightmare
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Logistical Nightmare', 'UVA', 'Classic Rock', '@logisticalnightmare.band', 'Tommy', '804-937-1084');


-- Mellowdrama
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Mellowdrama', 'UVA', 'Indie Rock', '@officialmellowdrama', NULL, NULL);


-- Orion and the Melted Crayons
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Orion and the Melted Crayons', 'Charlottesville', 'Indie Rock', '@orionandthemeltedcrayons', NULL, NULL);


-- Sneaky Lynx
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Sneaky Lynx', 'UVA', 'Soul/R&B', '@sneakylynxband', 'Ethan', '540-846-1701');


-- Souwa Cweam
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Souwa Cweam', 'UVA', 'Indie Rock', NULL, NULL, NULL);


-- The Lint Collectors
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('The Lint Collectors', 'Charlottesville', 'Soul/R&B', '@thelintcollectors', NULL, NULL);


-- Work In Progress
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Work In Progress', 'UVA', NULL, '@workinprogress_cville', 'Michael', '203-658-4120');


-- Yaard Sale
INSERT INTO BANDS (Band_Name, Band_Location, Band_Genre, Band_Instagram, B_Contact_Person, B_Contact_Number)
VALUES ('Yaard Sale', 'Charlottesville', 'Midwest Emo', '@musicbyyardsale', 'Cadin', '434-962-1044');
