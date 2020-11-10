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

CREATE TABLE myList (       --list where user can store a list of their favorite ramens
    my_ramenID INT PRIMARY KEY NOT NULL,
    my_rating INT NOT NULL,
    my_url TEXT NOT NULL,
    my_brand TEXT NOT NULL,
    my_style TEXT NOT NULL,
    my_country TEXT NOT NULL
);


--############################
--Drop a specified Table
-- DROP TABLE xxx

--############################
--Delete data from tables
-- DELETE FROM 


-- #########################
-- Update info from any table

-- UPDATE xxxx
-- SET xxxx
-- WHERE xxx

--############################
--Importing all tupples

-- Populating each table
-- Brand
INSERT INTO Brand
select DISTINCT Brand
FROM CompleteData
ORDER BY Brand

-- Country
INSERT INTO Country
SELECT DISTINCT Country
FROM CompleteData
ORDER BY Country

-- Country_Brand
INSERT INTO Country_Brand
SELECT Country, Brand
FROM CompleteData
GROUP BY Country, Brand;

-- Style
INSERT INTO Style 
SELECT DISTINCT Style 
FROM CompleteData 
ORDER BY Style

-- Style_Brand
INSERT INTO Style_Brand
SELECT Brand, Style
FROM CompleteData
GROUP BY Brand, Style

-- Variety
INSERT INTO Variety
SELECT ID, Variety
FROM CompleteData

-- Ramen
INSERT INTO Ramen
SELECT ID, Stars, URL, Brand, Style, Country
FROM CompleteData
ORDER BY ID

-- Users
--Will write once we have our UI 

-- ####################################
-- 1 - Display all types of styles that ramen come from (ONLY STYLES)
SELECT s_style      
FROM Style
ORDER BY s_style


-- 2 - Display the different type of varieties (Meaning ingredients)
SELECT v_variety
FROM Variety
ORDER BY v_variety

-- 3 - Display Brands that exist within the database
SELECT b_brand
FROM Brand
ORDER BY b_brand


-- 4 - Display the countries that ramen come from whole dataset
SELECT c_country
FROM Country
ORDER BY c_country

-- 5 - Display the ratings 
SELECT DISTINCT r_rating
FROM Ramen
ORDER BY r_rating

-- 6 - selecting ramen based on style
SELECT * 
FROM Ramen
WHERE r_style = '?'
ORDER BY r_rating DESC

-- 7 - selecting ramen based on the brand
SELECT * 
FROM Ramen
WHERE r_brand = '?'
ORDER BY r_rating DESC

-- 8 - selecting ramen based on the country
SELECT * 
FROM Ramen
WHERE r_country = '?'
ORDER BY r_rating DESC

-- 9 - selecting ramen based on the rating
SELECT * 
FROM Ramen
WHERE r_rating = '?'
ORDER BY r_rating DESC

-- 10 - when user inputs their info and leaves a rating on a ramen
INSERT INTO Users (u_users, u_userrating, u_id) VALUES ('?', '?', '?');

-- 11 - 
UPDATE Ramen
SET r_rating = '?' --
WHERE r_id = '?'
