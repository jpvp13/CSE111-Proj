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

CREATE TABLE Style (
   s_style TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE Users (
    u_users TEXT PRIMARY KEY NOT NULL,
    u_userrating INT NULL
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
    r_country TEXT NOT NULL,
    r_users TEXT NOT NULL
);

CREATE TABLE Style_Brand (
    sb_brand TEXT PRIMARY KEY NOT NULL,
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
select DISTINCT Brand
FROM CompleteData
ORDER BY Brand

-- c_country
SELECT DISTINCT Country
FROM CompleteData
ORDER BY Country

-- Country-Brand
SELECT Country, Brand
FROM CompleteData
GROUP BY Country, Brand

-- s_style
SELECT DISTINCT Style
FROM CompleteData
ORDER BY Style

-- Style_Brand
SELECT Brand, Style
FROM CompleteData
GROUP BY Brand, Style

-- v_variety
SELECT ID, Variety
FROM CompleteData

-- Users