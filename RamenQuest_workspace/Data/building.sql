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


SELECT r_id, r_rating, s_style, cb_brand, cb_country, r_url
FROM Ramen, Style, Country_Brand
WHERE r_style = s_style
    AND r_brand = cb_brand
    AND cb_country = r_country
    AND s_style LIKE '?'
ORDER BY r_rating DESC

-- 7 - selecting ramen based on the brand


SELECT r_id, r_rating, s_style, cb_brand, cb_country, r_url
FROM Ramen, Style, Country_Brand
WHERE cb_brand = r_brand
    AND cb_brand LIKE '?'
    AND cb_country = r_country
    AND s_style = r_style
ORDER BY r_rating DESC


-- 8 - selecting ramen based on the country

SELECT r_id, r_rating, s_style, cb_brand, cb_country, r_url
FROM Ramen, Style, Country_Brand
WHERE cb_country LIKE '?'
    AND cb_brand = r_brand
    AND cb_country = r_country
    AND s_style = r_style
ORDER BY r_rating DESC

-- 9 - selecting ramen based on the rating
SELECT r_id, r_rating, s_style, cb_brand, cb_country, r_url
FROM Ramen, Style, Country_Brand
WHERE r_rating LIKE 2
    AND cb_brand = r_brand
    AND cb_country = r_country
    AND s_style = r_style
ORDER BY r_rating DESC


-- 10 - when user inputs their info and leaves a rating on a ramen
INSERT INTO Users (u_users, u_userrating, u_id) VALUES ('?', '?', '?');

-- 11 - Will allow the user to update main database and retrieve the avg rating (their rating+ provided rating)
UPDATE Ramen
SET r_rating = '?'
WHERE r_id = '?'


-- 12 - Will give a recommendation when a item is   --!Work in progress
SELECT *
FROM Ramen, Country_Brand,Style
WHERE r_id = '?'
    AND r_rating = '?'
    AND r_url= '?'
    AND cb_brand = '?'
    AND s_style = '?'
    AND cb_country = '?'


-- 13 - Will return the max rating based on a specific brand
SELECT MAX(r_rating)
FROM Ramen
WHERE r_brand = '?'

-- 14 - Will return the max rating based on a specific style
SELECT MAX(r_rating)
FROM Ramen
WHERE r_style= '?'

-- 15 - Will return the max rating based on a specific country
SELECT MAX(r_rating)
FROM Ramen
WHERE r_country = '?'


-- 16 - Will return the URL based on specific constraints from the User     --!Work in Progesss
SELECT r_url
FROM Ramen, Country_Brand, Style
WHERE r_id = '?'
    AND r_rating = '?'
    AND r_url= '?'
    AND cb_brand = '?'
    AND s_style = '?'
    AND cb_country = '?'

-- 17 - Returns the avg rating of a certain brand
SELECT AVG(r_rating)
FROM Ramen
WHERE r_brand = '?'

-- 18 - Return the avg rating of a certain style
SELECT AVG(r_rating)
FROM Ramen
WHERE r_style = '?'

-- 19 - Return the avg rating of a certain country
SELECT AVG(r_rating)
FROM Ramen
WHERE r_country = '?'

--20 - Return the brand(s) with a specificed rating from the user
SELECT cb_brand 
FROM Ramen, Country_Brand
WHERE r_brand = cb_brand
    AND r_rating LIKE '2.9'
GROUP BY cb_brand
