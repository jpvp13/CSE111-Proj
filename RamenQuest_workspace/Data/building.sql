-- Creating Table

CREATE TABLE Country (
   c_country TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE Brand (
    b_brand TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE Country_Brand (
    cb_country TEXT PRIMARY KEY NOT NULL,
    cb_brand TEXT NOT NULL
);

--############################
--Drop a specified Table
-- DROP TABLE xxx

--############################
--Delete data from tables
DELETE FROM Country WHERE c_country = ''

--############################
--Importing all tupples

