DROP TABLE TOI;
DROP TABLE THEHINDU;

CREATE TABLE THEHINDU (
    AUTHOR VARCHAR(30),
    TITLE VARCHAR(200) PRIMARY KEY,
    DESCRIPTION VARCHAR(800),
    URL VARCHAR(200),
    IMGURL VARCHAR(200),
    PUBAT VARCHAR(25)
);

CREATE TABLE TOI (
    AUTHOR VARCHAR(30),
    TITLE VARCHAR(200) PRIMARY KEY,
    DESCRIPTION VARCHAR(800),
    URL VARCHAR(200),
    IMGURL VARCHAR(200),
    PUBAT VARCHAR(25)
);
