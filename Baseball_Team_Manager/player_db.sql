-- Drop the table if it already exists
DROP TABLE IF EXISTS Player;

-- Create the table
CREATE TABLE Player(
    playerID    INTEGER PRIMARY KEY     NOT NULL,
    batOrder    INTEGER                 NOT NULL,
    firstName   TEXT                    NOT NULL,
    lastName    TEXT                    NOT NULL,
    position    TEXT                    NOT NULL,
    atBats      INTEGER                 NULL,
    hits        INTEGER                 NULL
);

-- Populate the table
INSERT INTO Player VALUES
(1,1,'Tommy','La Stella','3B',1316,360),
(2,2,'Mike','Yastrzemski','RF',563,168),
(3,3,'Donovan','Solano','2B',1473,407),
(4,4,'Buster','Posey','C',4575,1380),
(5,5,'Brandon','Belt','1B',3811,1003),
(6,6,'Brandon','Crawford','SS',4402,1099),
(7,7,'Alex','Dickerson','LF',586,160),
(8,8,'Austin','Slater','CF',569,147),
(9,9,'Kevin','Gausman','P',56,2);