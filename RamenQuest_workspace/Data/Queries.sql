-- SQLite
-- ####################################
-- 1 - Display all types of styles that ramen come from (ONLY STYLES)
SELECT s_style      
FROM Style
ORDER BY s_style

-- 2 - Display the different type of varieties (Meaning ingredients)
SELECT v_variety
FROM Variety
ORDER BY v_variety

-- -- 3 - Display Brands that exist within the database
-- SELECT b_brand
-- FROM Brand
-- ORDER BY b_brand

-- 4 - Display the countries that ramen come from whole dataset
SELECT c_country
FROM Country
ORDER BY c_country

-- 5 - Display the ratings 
SELECT DISTINCT r_rating
FROM Ramen
ORDER BY r_rating

-- 6 - selecting ramen based on style   --!Q6
SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
FROM Ramen, Style_Brand, Country_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND sb_style LIKE '?'
ORDER BY r_rating DESC

-- 7 - selecting ramen based on the brand   --!Q6
SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
FROM Ramen, Style_Brand, Country_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND cb_brand LIKE 'Go'
ORDER BY r_rating DESC

-- 8 - selecting ramen based on the country   --!Q6
SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
FROM Ramen, Style_Brand, Country_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND cb_country LIKE '?'
ORDER BY r_rating DESC

-- 9 - selecting ramen based on the rating   --!Q6
SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
FROM Ramen, Style_Brand, Country_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND r_rating = '?'
GROUP BY r_id

-- 10 - when user inputs their info and leaves a rating on a ramen
INSERT INTO Users (u_users, u_userrating, u_id) VALUES ('?', '?', '?');

-- 11 - Will allow the user to update main database and retrieve the avg rating (their rating + provided rating)    --!Q7
UPDATE Ramen
SET r_rating = '?'
WHERE r_id = '?'

SELECT AVG(r_rating + '?')
FROM Ramen
WHERE r_id = '?';

-- 12 - Will give a recommendation when a item is selected  --!Work in progress
--!This is basically Q6 now
SELECT *
FROM Ramen, Country_Brand, Style_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND r_rating = '?'
    AND cb_brand LIKE '?'
    AND sb_style LIKE '?'
    AND cb_country LIKE '?'

-- 13 - Will return the max rating based on a specific brand    --!Q8
SELECT MAX(r_rating)
FROM Ramen, Country_Brand
WHERE r_brand = cb_brand
    AND cb_brand LIKE 'A-one'

-- 14 - Will return the max rating based on a specific style    --!Q9
SELECT MAX(r_rating), sb_style
FROM Ramen, Style_Brand
WHERE r_brand = sb_brand
    AND sb_style LIKE 'box'

-- 15 - Will return the max rating based on a specific country  --!Q10
SELECT MAX(r_rating)
FROM Ramen, Country_Brand
WHERE r_brand = cb_brand
    AND cb_country LIKE '?'

-- 16 - Will return the URL based on specific constraints from the User     --!Work in Progesss
SELECT r_url
FROM Ramen, Country_Brand, Style_Brand
WHERE r_brand = sb_brand
    AND cb_brand = sb_brand
    AND r_rating = '?'
    AND cb_brand LIKE '?'
    AND sb_style LIKE '?'
    AND cb_country LIKE '?'

-- 17 - Returns the avg rating of a certain brand
SELECT AVG(r_rating)
FROM Ramen
WHERE r_brand LIKE '?'

-- 18 - Return the avg rating of a certain style
SELECT AVG(r_rating)
FROM Ramen, Style_Brand
WHERE r_brand = sb_brand
    AND sb_style LIKE '?'

-- 19 - Return the avg rating of a certain country
SELECT AVG(r_rating)
FROM Ramen, Country_Brand
WHERE r_brand = cb_brand
    AND cb_country LIKE '?'

--20 - Return the brand(s) with a specificed rating from the user
SELECT cb_brand 
FROM Ramen, Country_Brand
WHERE r_brand = cb_brand
    AND r_rating = '?'
GROUP BY cb_brand

-- 21 - insert a Ramen into myList based on the ramen id
INSERT INTO myList
SELECT r_id, r_rating, r_brand, r_url 
FROM Ramen
WHERE r_id = 1

-- 22 - delete a ramen from myList based on the my_ramenID
DELETE FROM myList
WHERE my_ramenID = '?'

 