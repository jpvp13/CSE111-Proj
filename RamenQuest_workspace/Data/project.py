<<<<<<< HEAD

=======
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

import prettytable
import sqlite3
from sqlite3 import Error
from prettytable import from_db_cursor

connection = sqlite3.connect('database.sqlite', timeout=10)


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
        sql =   """
                SELECT s_style      
                FROM Style
                ORDER BY s_style;
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
        userIngredient =  userIngredient + '%'
        sql =   """
                SELECT v_id, v_variety
                FROM Variety
                WHERE v_variety LIKE ?        
                ORDER BY v_variety;
                """
        args = [userIngredient] 

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


def displayCountry(conn):         #(3)

    try:
        sql =   """
                SELECT c_country
                FROM Country
                ORDER BY c_country;
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)


def displayAllRatings(conn):         #(4)

    try:
        sql =   """
                SELECT DISTINCT r_rating
                FROM Ramen
                ORDER BY r_rating;
                """
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)

    except Error as e:
        conn.rollback()
        print(e)

def displayRatingCustom(conn, rating):  #5
    try:
        sql =   """
                SELECT r_id, r_rating, sb_style, cb_brand, cb_country
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND r_rating LIKE ?
                ORDER BY r_rating DESC;
                """
        args = [rating]

        cur = conn.cursor()
        cur.execute(sql, args)
        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", rating)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)


def displayCountryCustom(conn, country):    #5

    try:
        sql =   """
                SELECT r_id, r_rating, sb_style, cb_brand, cb_country
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND cb_country LIKE ?
                ORDER BY r_rating DESC;
                """
        args = [country]
        cur = conn.cursor()
        cur.execute(sql, args)
        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", country)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)

def displayStyleCustom(conn, style):    #5
    try:
        sql =   """
                SELECT r_id, r_rating, sb_style, cb_brand, cb_country
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND sb_style LIKE ?
                ORDER BY r_rating DESC;
                """
        args = [style]
        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", style)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)


def displayCustomAll(conn, _style, _country, _rating):         #(5)  #!Formatting is off..

    try:

        sql =   """
                SELECT r_id, r_rating, sb_style, cb_brand, cb_country
                FROM Ramen, Style_Brand, Country_Brand
                WHERE r_brand = sb_brand
                    AND cb_brand = sb_brand
                    AND sb_style LIKE ?
                    AND cb_country LIKE ?
                    AND r_rating LIKE ?
                ORDER BY r_rating DESC;
                """
        args = [_style, _country, _rating]



        cur = conn.cursor()

        row = cur.fetchone()
        if row == None:
            print("There was no results with those input\n")
            return

        cur.execute(sql, args)
        mytable = from_db_cursor(cur)

        print(mytable)
        print("\n")
            

    except Error as e:
        conn.rollback()
        print(e)




def updateSelfList(conn, id, rating): #6
    try:
        cur = conn.cursor()
        mytable = from_db_cursor(cur)
        

        update =    """
                    UPDATE myList
                    SET my_rating = ?
                    WHERE my_ramenID = ?;
                    """

        updateArgs = [rating, id]
        cur.execute(update, updateArgs)
        
        print("Database Update Complete!")

<<<<<<< HEAD
=======
        cur.execute(update, updateArgs)
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
        print(mytable)
        print("\n")
        conn.commit()
            
    except Error as e:
        conn.rollback()
        print(e)

def maxBrandRating(conn, brand):        #7  #!to many options for ratings?????###########
    try:
        print("Searching for a result like...", " '' " , brand , " '' ")
        brand = '%' + brand + '%'
        
        sql =   """
                SELECT MAX(r_rating)
                FROM Ramen, Country_Brand
                WHERE r_brand = cb_brand
                    AND cb_brand LIKE ?;
                """
        args = [brand]

        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", brand)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)

def maxStyleRating(conn, style):        #8 #!doesnt print error message, but maybe "None" inside output is enough#####
    try:
        sql = """SELECT MAX(r_rating), sb_style
                FROM Ramen, Style_Brand
                WHERE r_brand = sb_brand
                    AND sb_style LIKE ?
                """
        args = [style]

        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", style)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")
    
    except Error as e:
        conn.rollback()
        print(e)

def maxCountryRating(conn, country):        #9
    try:
        print("Searching for a result like...", " '' " , country , " '' ")
        country =  country + '%'
        sql =   """
                SELECT MAX(r_rating)
                FROM Ramen, Country_Brand
                WHERE r_brand = cb_brand
                    AND cb_country LIKE ?;
                """
        args = [country]
        cur = conn.cursor()
        cur.execute(sql, args)

        
        cur.execute(sql, args)

        mytable = from_db_cursor(cur)

        print(mytable)
        print("\n")

    except Error as e:
        conn.rollback()
        print(e)

def returnURL(conn, rating): #10 #!only return based on rating since it will be a range
    try:
        sql = """SELECT ID, URl
                FROM CompleteData
                WHERE Stars = ?;"""
        
        args = [rating]
        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", rating)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)



def avgBrandRating(conn, brand):        #11
    try:
        brand = brand + '%'
        sql =   """
                SELECT AVG(r_rating)
                FROM Ramen
                WHERE r_brand LIKE ?;
                """
        args = [brand]
        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", brand)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")

    except Error as e:
        conn.rollback()
        print(e)

def avgStyleRating(conn, style):        #12
    try:
        sql =   """
                SELECT AVG(r_rating)
                FROM Ramen, Style_Brand
                WHERE r_brand = sb_brand
                    AND sb_style LIKE ?;
                """
        args = [style]
        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", style)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")
    
    except Error as e:
        conn.rollback()
        print(e)

def avgCountryRating(conn, country):        #13
    try:
        sql =   """
                SELECT AVG(r_rating)
                FROM Ramen, Country_Brand
                WHERE r_brand = cb_brand
                    AND cb_country LIKE ?;
                """
        args = [country]
        cur = conn.cursor()
        cur.execute(sql, args)

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", country)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")
    
    except Error as e:
        conn.rollback()
        print(e)


def ListInsert(conn, ramen_id):     #14
    try:
        sql =   """
                INSERT INTO myList
                SELECT r_id, r_rating, r_brand, r_url
                FROM Ramen
                WHERE r_id = ?;
                """
        args = [ramen_id]
        cur = conn.cursor()
        cur.execute(sql, args)

        conn.commit()   #this puts things into our myList table :) will delete fresh everytime we start a new session

        mytable = from_db_cursor(cur)

        print(mytable)
        print("\n")

    
    except Error as e:
        conn.rollback()
        print(e)

def ListDelete(conn, myramen_id):       #15
    try:
        sql =   """
                DELETE 
                FROM myList
                WHERE my_ramenID = ?;
                """
        args = [myramen_id]
        cur = conn.cursor()
        cur.execute(sql, args)

        conn.commit()

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your input: ", myramen_id)
            print("Exiting back to Main Menu...\n")

        else:
            cur.execute(sql, args)

            mytable = from_db_cursor(cur)

            print(mytable)
            print("\n")
    
    except Error as e:
        conn.rolback()
        print(e)

<<<<<<< HEAD
def UserInsert(conn, user):     #16         #!doesnt work. might need to add a different column for the users name
    try:
        sql =   """
                INSERT INTO Users( u_users)
                VALUES(?);
                """
        args = [user]
        cur = conn.cursor()
        cur.execute(sql, args)

        conn.commit()

        row = cur.fetchone()
        if row == None:
            print("There are no matches that match your inputs")
            print("Exiting back to Main Menu...\n")
=======
# def UserInsert(conn, user, userRating, userID):     #17         #!doesnt work. might need to add a different column for the users name
#     try:
#         sql =   """
#                 INSERT INTO Users(u_users, u_userrating, u_id)
#                 VALUES(?, ?, ?);
#                 """
#         args = [user, userRating, userID]
#         cur = conn.cursor()
#         cur.execute(sql, args)

#         conn.commit()
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

#         row = cur.fetchone()
#         if row == None:
#             print("There are no matches that match your inputs")
#             print("Exiting back to Main Menu...\n")

#         else:
#             cur.execute(sql, args)

#             mytable = from_db_cursor(cur)

#             print(mytable)
#             print("\n")

#     except Error as e:
#         conn.rollback()
#         print(e)

def viewList(conn):

    try:
        sql = """SELECT my_ramenID AS ID, my_rating, my_brand AS Brand, v_variety AS Variety, my_url AS URL
                FROM myList, Variety
                WHERE v_id = my_ramenID
                ORDER BY my_ramenID;
                """
        
        cur = conn.cursor()
        cur.execute(sql)
        mytable = from_db_cursor(cur)
        print(mytable)
        print("\n")

    except Error as e:
        conn.rollback()
        print(e)

def viewByMyRating(conn):
    try:
        sql = """SELECT my_ramenID AS ID, my_rating, my_brand AS Brand, v_variety AS Variety, my_url AS URL
                FROM myList, Variety
                WHERE v_id = my_ramenID
                ORDER BY my_rating;
                """

        
        cur = conn.cursor()
        cur.execute(sql)
        mytable = from_db_cursor(cur)
        print(mytable)
        print("\n")

    except Error as e:
        conn.rollback()
        print(e)
<<<<<<< HEAD
=======

>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

def viewUsers(conn):
    try:
        sql = """SELECT *
                FROM Users;"""
            
        cur = conn.cursor()
        cur.execute(sql)

        mytable = from_db_cursor(cur)
        print(mytable)
        print("\n")
    except Error as e:
        conn.rollback()
        print(e)

HomePage = """Please choose one of the options:
           
            1) Display User  Ramen Styles
            2) Display User Specific Ramen Varieties
            3) Display Ramen Country Origns
            4) Display The Range Of Ramen Ratings
            5) Display Ramen based on user choices
            6) Update Ramen listing with a user comment
            7) Display highest rating based on user's choice of brand
            8) Display highest rating based on user's style
            9) Display highest rating based on user's country
            10) View a ramens URL based on their ratings
            11) Display average rating based on user's choice of brand
            12) Display average rating based on user's choice of style
            13) Display average rating based on user's choice of rating
<<<<<<< HEAD
            14) Add a Ramen into your own personal list
            15) Delete a Ramen from your own personal list
            16) Show my saved list orded by ID # or ratings
            17) Show all current users 
=======
            14)***TBA***
            15) Add a Ramen into your own personal list
            16) Delete a Ramen from your own personal list
            ** DNE **17) Add a raiting to a ramen of your choice
            18) Show my saved list orded by ID #
            19) Show my saved list ordered by ratings
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

           

            Press 'q' to exit at any time
    
    Waiting For Input: """


def main():
    database = r"RamenQuest_workspace/Data/database.sqlite"

    conn = openConnection(database)
    
    

    with conn:

        user = input("Would you like to create a user account? (Yes | No)")
        if user == "Yes":
                # userID = 0

            user = input("What is your name? ")
        # userID = userID + 1    

            UserInsert(conn, user) 
        
        while(user_input := input(HomePage)) != '0':


            if user_input == 'q':
                exit()
            elif user_input == '1': #1 in queries
                print("You chose 1!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()
                
                displayStyle(conn)
                print("Returning to Main Menu...")

            elif user_input == '2': #2 in queries
                print("You chose 2!")
                userIngredient = input("Enter a ingredient that you are interested in: ")
                
                displayVariety(conn, userIngredient)
<<<<<<< HEAD

                check = input("Quit? (q)")
                if check == "q":
                    exit()
=======
                print("Returning to Main Menu...")
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
            

            elif user_input == '3': #4 in queries
                print("You chose 3!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                displayCountry(conn)
                print("Returning to Main Menu...")

            elif user_input == '4': #5 in queries
                print("You chose 4!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                displayAllRatings(conn)
                print("Returning to Main Menu...")


            elif user_input == '5': #6-9 in queries
                print("You chose 5!")
                Instructions = """Styles: Bar | Bowl | Box | Can | Cup | Pack | Restaurant | Tray"""
                print(Instructions)

                check = input("Quit? (q)")
                if check == "q":
                    exit()


                type = input("Would you like all results returned, those from a specific country, those from a specific style or those that have a specific rating(style | country | rating | all): ")

                if type == "country":
                    country = input("Please choose a country: ")
                    check = input("Quit? (q)")
                    if check == "q":
                        exit()
                    displayCountryCustom(conn, country)
                    print("Returning to Main Menu...")

                if type == "rating":
                    rating = input("Plase choose a rating: ")

                    check = input("Quit? (q)")
                    if check == "q":
                        exit()
                    displayRatingCustom(conn, rating)
                    print("Returning to Main Menu...")

                if type == "style":
                    Instructions = """Styles: Bar | Bowl | Box | Can | Cup | Pack | Restaurant | Tray"""

                    check = input("Quit? (q)")
                    if check == "q":
                        exit()

                    style = input("Enter a specific style: ")
                    displayStyleCustom(conn, style)
                    print("Returning to Main Menu...")

                if type == "all":
                    country = input("Please choose a country: ")


                    rating = float(input("Plase choose a rating: "))
                   

                    style = input("Enter a specific style: ")

                    
                    
                    # displayCustomAll(conn, style, country, rating, brand)
                    displayCustomAll(conn, style, country, rating)
                    print("Returning to Main Menu...")

                

            elif user_input == '6': #11 in queries      #!fix this one
                print("You chose 6!")

                type = input("Would you like to make some updates to your list? ( Yes | No): ")

                if type == "Yes":

<<<<<<< HEAD
                    check = input("Quit? (q)")
                    if check == "q":
                        exit()

                    help = input("Would you like to view your list first? (Yes | No): ")
                    if help == "Yes":
                        viewList(conn)
                        id = input("Which ramen ID would you like to change: ")
                        comment = input("What would you like to change the rating to? : ")
                        updateSelfList(conn, id, comment)
                        viewList(conn)

                    elif help == "No": 
                        print("No worries!")
                        id = input("Which ramen ID would you like to change: ")

                        check = input("Quit? (q)")
                        if check == "q":
                            exit()
                        comment = input("What would you like to change the rating to? : ")
                        updateSelfList(conn, id, comment)
                        viewList(conn)
=======
                    help = input("Would you like to view your list first? (Yes | No): ")
                    if help == "Yes":
                        viewList(conn)
                        id = input("Which ramen would you like to change: ")
                        comment = input("What would you like to change the rating to? : ")
                        updateSelfList(conn, id, comment)
                        viewList(conn)
                        print("Returning to Main Menu...")

                    elif help == "No":
                        print("No worries!")
                        id = input("Which ramen would you like to change: ")
                        comment = input("What would you like to change the rating to? : ")
                        updateSelfList(conn, id, comment)
                        viewList(conn)
                        print("Returning to Main Menu...")
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                    

                    

            elif user_input == '7': #13 in queries
                print("You chose 7!")

                brand = input("Choose a brand: ")
                maxBrandRating(conn, brand)

<<<<<<< HEAD
                check = input("Quit? (q)")
                if check == "q":
                    exit()

            elif user_input == '8': #14 in queries  
=======
                print("Returning to Main Menu...")

            elif user_input == '8': #14 in queries  #!not working???
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                print("You chose 8!")

                print(" Options: Bar | Bowl | Box | Can | Cup | Pack | Resaurant | Tray")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                style = input("Choose a style: ")
                maxStyleRating(conn, style)

                print("Returning to Main Menu...")

            elif user_input == '9':    #15 in queries
                print("You chose 9!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                country = input("Choose the country: ")
                maxCountryRating(conn, country)

                print("Returning to Main Menu...")

            elif user_input == '10':    #!16 from queries
                print("You chose 10!")

<<<<<<< HEAD
                check = input("Quit? (q)")
                if check == "q":
                    exit()

                rating = float(input("What rating would you like to use to retieve URL's with? : "))
                returnURL(conn, rating)
=======
                rating = float(input("What rating would you like to use to retieve URL's with? : "))
                returnURL(conn, rating)
                print("Returning to Main Menu...")
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

            elif user_input == '11':    #17
                print("You chose 11!")

<<<<<<< HEAD
                
=======
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                type = input("Would you like to view updates based on your input? ( Yes | No): ")

                if type == "Yes":

<<<<<<< HEAD
                    check = input("Quit? (q)")
                    if check == "q":
                        exit()

=======
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                    help = input("Would you like to view your list first? (Yes | No): ")
                    if help == "Yes":
                        viewList(conn)
                        
                        brand = input("What brand would you like to use? : ")
                        avgBrandRating(conn, brand)

                    elif help == "No":
                        brand = input("What brand would you like to use? : ")
                        avgBrandRating(conn, brand)
<<<<<<< HEAD

        
=======
                
                elif type == "No":
                    print("No worries! Returning to Main Menu...")
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                

            elif user_input == '12':    #18
                print("You chose 12!")

                print(" Options: Bar | Bowl | Box | Can | Cup | Pack | Resaurant | Tray")

<<<<<<< HEAD
                check = input("Quit? (q)")
                if check == "q":
                    exit()
=======
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

                style = input("Choose the style: ")
                avgStyleRating(conn, style)

                print("Returning to Main Menu...")

            elif user_input == '13':    #19
                print("You chose 13!")
                
                check = input("Quit? (q)")
                if check == "q":
                    exit()

                country = input("Choose a country: ")
                avgCountryRating(conn, country)

<<<<<<< HEAD
            elif user_input == '14':    #21 in queries
=======
                print("Returning to Main Menu...")

            elif user_input == '14':    #!20 in queries
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89
                print("You chose 14!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                ramen_id = input("What is the id of the ramen you'd like to put in your list? ")
                ListInsert(conn, ramen_id)

                print("Returning to Main Menu...")
                
            elif user_input == '15':    #22 in queries
                print("You chose 15!")

                check = input("Quit? (q)")
                if check == "q":
                    exit()

                myramen_id = input("What is the id of the ramen you want to remove from your list? ")
                ListDelete(conn, myramen_id)

<<<<<<< HEAD
            elif user_input == '16':
                print("You chose 16!")

                response = input("Would you like to see your list ordered by ID? ( YesID | NoID): ")
                
                if(response == 'YesID'):
                    check = input("Quit? (q)")
                    if check == "q":
                        exit()
                    viewList(conn)
                elif response == 'NoID':
                    print("Thats okay!")

                response2 = input("Would you like to see your list ordered by ratings? (YesRating | NoRating): ")
                

                if(response2 == "YesRating"):
                    check = input("Quit? (q)")
                    if check == "q":
                        exit()
                    viewByMyRating(conn)
            elif user_input == "17":
                print("Displaying users...")
                viewUsers(conn)
=======
                print("Returning to Main Menu...")

            elif user_input == '17':    #10 in queries
                print("You chose 17!: ")
>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89


<<<<<<< HEAD


=======
                user = input("What is your name? ")
                userRating = input("What do you rate the ramen? ")
                userID = userID + 1     #!CHECK THIS. This doesnt work and doesnt make much sense

                # UserInsert(conn, user, userRating, userID) #!TBA
                print("Returning to Main Menu...")
            elif user_input == '18':
                print("You chose 18!")

                response = input("Would you like to see your list ordered by ID? ( YesID | NoID): ")
                
                if(response == 'YesID'):
                    viewList(conn)
                elif response == 'NoID':
                    print("Thats okay!")

                response2 = input("Would you like to see your list ordered by ratings? (YesRating | NoRating): ")


                if(response2 == "YesRating"):
                    viewByMyRating(conn)
                elif(response2 == "NoRating"):
                    print("No worries! Going back to main menu...")


>>>>>>> 3e8e4301f31ab5f83bad66541e284e93ce06ae89

    closeConnection(conn, database)

if __name__ == '__main__':
    main()