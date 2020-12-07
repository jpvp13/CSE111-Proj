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

    try:                                    #!CHECK THIS ONE
        sql = """SELECT *
                FROM Variety
                WHERE v_variety LIKE ?          
                ORDER BY v_variety;
                """
        args = [userIngredient] #this is bad becasue it only returns the word, not the tuple

        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", userIngredient)
        
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


def displayBrand(conn):         #(3)

    try:
        sql = """SELECT b_brand
                FROM Brand
                ORDER BY b_brand
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


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


def displayCustomRatings(conn, _style):         #(6)

    try:
        sql = """SELECT r_id, r_rating, sb_style, cb_brand, cb_country, r_url
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND sb_style LIKE '?'
                ORDER BY r_rating DESC
                """
        args = [_style]
        cur = conn.cursor()
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


HomePage = """ Please choose one of the options:
            1) Display Ramen Styles
           

            'q' to exit
    
    Waiting For Input:
            """


def main():
    database = r"RamenQuest_workspace/Data/database.sqlite"

    conn = openConnection(database)

    with conn:
        while(user_input := input(HomePage)) != '0':
            if user_input == 'q':
                exit()
            elif user_input == '1':
                
                displayStyle(conn)

            elif user_input == '2':
                Ingredients = """Enter a ingredient that you are interested in: """
                print(Ingredients)

                userIngredient = input("Enter Here: ")
                displayVariety(conn, userIngredient)
            
            elif user_input == '3':

                displayBrand(conn)

            elif user_input == '4':

                displayCountry(conn)

            elif user_input == '5':

                displayAllRatings(conn)


            elif user_input == '6':
                Instructions = """Styles: Bar | Bowl | Box | Can | Cup | Pack | Restaurant | Tray"""
                print(Instructions)

                selectedStyle = input("Enter a specific style: ")
                displayCustomRatings(conn, selectedStyle)

            # elif user_input == '7':

            # elif user_input == '8':

            # elif user_input == '9':

            # elif user_input == '10':

            # elif user_input == '11':

            # elif user_input == '12':

            # elif user_input == '13':

            # elif user_input == '14':

            # elif user_input == '15':

            # elif user_input == '16':

            # elif user_input == '17':
            
            # elif user_input == '18':

            # elif user_input == '19':

            # elif user_input == '20':

            # elif user_input == '21':

            # elif user_input == '22':

    

    closeConnection(conn, database)

if __name__ == '__main__':
    main()