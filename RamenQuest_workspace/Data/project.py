#!/usr/bin/python3

import sqlite3
from sqlite3 import Error
from prettytable import from_db_cursor


def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(conn, _dbFile):
    #print("++++++++++++++++++++++++++++++++++")
    #print("Close database: ", _dbFile)

    try:
        conn.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def displayStyle(conn):             #(1)
    try:
        sql = """SELECT s_style      
                FROM Style
                ORDER BY s_style
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


def displayVariety(conn, userIngredient):           #(2)

    try:                              
        userIngredient = userIngredient + '%'
        sql = """SELECT *
                FROM Variety
                WHERE v_variety LIKE ?        
                ORDER BY v_id;
                """
        args = [userIngredient] #this is bad becasue it only returns the word, not the tuple

        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", userIngredient)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)

#! to many to display and we have another query that will print based on brands
# def displayBrand(conn):         #(3)

#     try:

#         sql = """SELECT b_brand
#                 FROM Brand
#                 WHERE b_brand
#                 ORDER BY b_brand
#                 """
#         cur = conn.cursor()
#         cur.execute(sql)

#         mytable = from_db_cursor(cur)
#         print(mytable)

#     except Error as e:
#         conn.rollback()
#         print(e)


def displayCountry(conn):         #(4)

    try:
        sql = """SELECT c_country
                FROM Country
                ORDER BY c_country
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


def displayAllRatings(conn):         #(5)

    try:
        sql = """SELECT DISTINCT r_rating
                FROM Ramen
                ORDER BY r_rating
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)

def displayRatingCustom(conn, rating):
    try:
        sql = """SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
                    FROM Ramen, Style_Brand, Country_Brand
                    WHERE r_brand = sb_brand
                        AND cb_brand = sb_brand
                        AND r_rating LIKE ?
                    ORDER BY r_rating DESC"""
        args = [rating]

        cur = conn.cursor()
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)

def displayCountryCustom(conn, country):

    try:
        sql = """SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
                    FROM Ramen, Style_Brand, Country_Brand
                    WHERE r_brand = sb_brand
                        AND cb_brand = sb_brand
                        AND cb_country LIKE ?
                    ORDER BY r_rating DESC"""
        args = [country]
        cur = conn.cursor()
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)

def displayStyleCustom(conn, style):
    try:
        sql = """SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
                    FROM Ramen, Style_Brand, Country_Brand
                    WHERE r_brand = sb_brand
                        AND cb_brand = sb_brand
                        AND sb_style LIKE ?
                    ORDER BY r_rating DESC"""
        args = [style]
        cur = conn.cursor()
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


def displayCustomAll(conn, _style, _country, _rating):         #(6)  #!Formatting is off..

    try:

        sql = """SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND sb_style LIKE ?
                    AND cb_country LIKE ?
                    AND r_rating LIKE ?
                ORDER BY r_rating DESC"""
        args = [_style, _country, _rating]



        cur = conn.cursor()
        # cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There was no results with that input\n")
            return

        cur.execute(sql, args)
        mytable = from_db_cursor(cur)

        print(mytable)
        print("\n")
            

    except Error as e:
        conn.rollback()
        print(e)

def updateRating(conn, id, rating):
    try:
        cur = conn.cursor()

        update = """UPDATE Ramen
                SET r_rating = ?
                WHERE r_id = ?;"""
        
        updateArgs = [id, rating]

        cur.execute(update, updateArgs)

        sql = """SELECT AVG(r_rating + ?)
                FROM Ramen
                WHERE r_id = ?;"""
        args = [rating, id]

        row = cur.fetchone()
        if row == None:
            print("There was no results with that input\n")
            return
        
        cur.execute(sql, args)
        mytable = from_db_cursor(cur)

        print(mytable)
        print("\n")
            
    except Error as e:
        conn.rollback()
        print(e)

HomePage = """ Please choose one of the options:
            1) Display User  Ramen Styles
            2) Display User Specific Ramen Varieties
            3) Display User Specific Ramen Brands
            4) Display Ramen Country Origns
            5) Display The Range Of Ramen Ratings
            6) Display Ramen based on user choices
            7) Update Ramen rating of user's choice

           

            'q' to exit
    
    Waiting For Input: """


def main():
    database = r"RamenQuest_workspace/Data/database.sqlite"

    conn = openConnection(database)
    user_input = input(HomePage)

    with conn:
        
        while(user_input) != '0':
            if user_input == 'q':
                exit()
            elif user_input == '1':
                print("You chose 1!")
                
                displayStyle(conn)

            elif user_input == '2':
                print("You chose 2!")
                Ingredients = """Enter a ingredient that you are interested in"""
                print(Ingredients)

                userIngredient = input("Enter Here: ")
                displayVariety(conn, userIngredient)
            
            # elif user_input == '3':
            # print("You chose 3!")

            #     displayBrand(conn)

            elif user_input == '4':
                print("You chose 4!")

                displayCountry(conn)

            elif user_input == '5':
                print("You chose 5!")

                displayAllRatings(conn)


            elif user_input == '6':
                print("You chose 6!")
                Instructions = """Styles: Bar | Bowl | Box | Can | Cup | Pack | Restaurant | Tray"""
                print(Instructions)


                type = input("Would you like all results returned, those from a specific country, those from a specific style or those that have a specific rating(style | country | rating | all): ")

                if type == "country":
                    country = input("Please choose a country: ")
                    displayCountryCustom(conn, country)

                if type == "rating":
                    rating = input("Plase choose a rating: ")
                    displayRatingCustom(conn, rating)

                if type == "style":
                    style = input("Enter a specific style: ")
                    displayStyleCustom(conn, style)

                if type == "all":
                    country = input("Please choose a country: ")

                    rating = float(input("Plase choose a rating: "))
                    

                    style = input("Enter a specific style: ")
                    
                    displayCustomAll(conn, style, country, rating)

                

            elif user_input == '7':
                print("You chose 7!")

                type = input("Will you be changing a rating? ( Yes | No): ")


                if type == "Yes":
                    id = input("Which ramen would you like to change: ")
                    rating = float(input("What is your rating on this ramen? (0.0 - 5.0): "))
                    updateRating(conn, id, rating)

    closeConnection(conn, database)

if __name__ == '__main__':
    main()