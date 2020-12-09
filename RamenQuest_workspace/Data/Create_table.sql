-- SQLite
-- Creating Table


CREATE TABLE CompleteData (
    ID  INT NOT NULL PRIMARY KEY,
    URl VARCHAR(50) NOT NULL,
    Brand TEXT NOT NULL,
    Variety TEXT NOT NULL,
    Style TEXT NOT NULL,
    Country TEXT NOT NULL,
    Stars INT NOT NULL
);


CREATE TABLE Country (
   c_country TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE Brand (
    b_brand TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE Country_Brand (
    cb_country TEXT NOT NULL,
    cb_brand TEXT NOT NULL
);

CREATE TABLE Style (
   s_style TEXT PRIMARY KEY NOT NULL
);


CREATE TABLE Users (
    u_id INTEGER PRIMARY KEY NULL,
    u_users TEXT  NOT NULL
);


CREATE TABLE Variety (
    v_id TEXT PRIMARY KEY NOT NULL,
    v_variety TEXT NOT NULL
);

CREATE TABLE Ramen (
    r_id INT PRIMARY KEY NOT NULL,
    r_rating INT NOT NULL,
    r_brand TEXT NOT NULL,
    r_url TEXT NOT NULL
);

CREATE TABLE Style_Brand (
    sb_brand TEXT NOT NULL,
    sb_style TEXT NOT NULL
);

CREATE TABLE myList (       --list where user can store a list of their favorite ramens
    my_ramenID INT PRIMARY KEY NOT NULL,
    my_rating INT NOT NULL,
    my_brand TEXT NOT NULL,
    my_url TEXT NOT NULL
);


 