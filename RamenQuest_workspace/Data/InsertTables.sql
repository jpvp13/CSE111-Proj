

--Drop a specified Table
-- DROP TABLE xxx

--############################
--Delete data from tables
-- DELETE FROM xxx


-- #########################
-- Update info from any table

-- UPDATE xxxx
-- SET xxxx
-- WHERE xxx


--Importing all tupples

-- Populating each table

-- Brand
INSERT INTO Brand
select DISTINCT Brand
FROM CompleteData
ORDER BY Brand

-- Country
INSERT INTO Country
SELECT Country
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
SELECT ID, Stars, Brand, URL
FROM CompleteData
ORDER BY ID

