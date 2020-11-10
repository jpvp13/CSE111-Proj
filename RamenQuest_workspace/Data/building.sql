-- Creating Table

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
    u_users TEXT PRIMARY KEY NOT NULL,
    u_userrating INT NULL,
    u_id INT NULL
);

CREATE TABLE Variety (
    v_id TEXT PRIMARY KEY NOT NULL,
    v_variety TEXT NOT NULL
);

CREATE TABLE Ramen (
    r_id INT PRIMARY KEY NOT NULL,
    r_rating INT NOT NULL,
    r_url TEXT NOT NULL,
    r_brand TEXT NOT NULL,
    r_style TEXT NOT NULL,
    r_country TEXT NOT NULL
);

CREATE TABLE Style_Brand (
    sb_brand TEXT NOT NULL,
    sb_style TEXT NOT NULL
);


--############################
--Drop a specified Table
-- DROP TABLE xxx

--############################
--Delete data from tables
-- DELETE FROM xxx

--############################
--Importing all tupples

-- b_brand
INSERT INTO Brand
select DISTINCT Brand
FROM CompleteData
ORDER BY Brand

-- c_country
INSERT INTO Country
SELECT DISTINCT Country
FROM CompleteData
ORDER BY Country

-- Country-Brand
INSERT INTO Country_Brand
SELECT Country, Brand
FROM CompleteData
GROUP BY Country, Brand;

-- s_style
INSERT INTO Style 
SELECT DISTINCT Style 
FROM CompleteData 
ORDER BY Style

-- Style_Brand
INSERT INTO Style_Brand
SELECT Brand, Style
FROM CompleteData
GROUP BY Brand, Style

-- v_variety
INSERT INTO Variety
SELECT ID, Variety
FROM CompleteData

-- Ramen
INSERT INTO Ramen
SELECT ID, Stars, URL, Brand, Style, Country
FROM CompleteData
ORDER BY ID

-- Users

