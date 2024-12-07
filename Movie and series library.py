import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIESS_LIBRARY')
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE MOVIED(TITLE VARCHAR(100) PRIMARY KEY, YEAR_OF_RELEASE INT(4),
                 "GENRE VARCHAR(100), CAST VARCHAR(100), NOMINATIONS VARCHAR(100))")
mycursor.execute("CREATE TABLE SERIESD(TITLE VARCHAR(100) PRIMARY KEY, GENRE VARCHAR(100), DIRECTOR VARCHAR(100))")

def addnewmovie():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIES_LIBRARY')
    mycursor=mydb.cursor()
    tit=input("enter title of the movie:")
    yor=int(input("enter year of release of the movie (format:YYY):"))
    genre=input("enter genre of the movie:")
    cast=input("enter notable lead cast:")
    nom=input("enter nominations")
    mycursor.execute("INSERT INTO MOVIED VALUES('{}',{},'{}','{}','{}')".format(tit.lower(),yor,genre.lower(),cast.lower(),nom.lower()))
    mydb.commit()
    print("record inserted successfully...")

def showmovie():
    import mysql.connector
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='MOVIE_AND_SERIES_LIBRARY')
    mycursor = mydb.cursor()
    print("All movie details:")
    mycursor.execute("SELECT * FROM MOVIED")
    result = mycursor.fetchall()  # Fetch all the rows
    for i in result:
        print(i)

def shownom():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIES_LIBRARY')
    mycursor=mydb.cursor()
    mov=input("enter movie name whose nominations you wish to see:")
    mycursor.execute("SELECT NOMINATIONS FROM MOVIED WHERE LOWER(TITLE)='{}'".format(mov.lower()))
    for i in mycursor:
        print(i)
def updatemovie():
    import mysql.connector
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='MOVIE_AND_SERIES_LIBRARY')
    mycursor = mydb.cursor()
    mov = input("enter title of the movie whose details you would like to change:")
    par = int(input("what would you like to change? (1.year of release, 2.genre, 3.cast, 4.nomination):"))
    
    if par == 1:
        k = int(input("enter new year of release"))
        mycursor.execute("UPDATE MOVIED SET YEAR_OF_RELEASE={} WHERE TITLE='{}'".format(k, mov.lower()))
        mydb.commit()
        print("changes made")
    elif par == 2:
        m = input("enter new genre")
        mycursor.execute("UPDATE MOVIED SET GENRE='{}' WHERE TITLE='{}'".format(m.lower(), mov.lower()))
        mydb.commit()
        print("changes made")
    elif par == 3:
        l = input("enter new cast")
        mycursor.execute("UPDATE MOVIED SET CAST='{}' WHERE TITLE='{}'".format(l.lower(), mov.lower()))
        mydb.commit()
        print("changes made")
    elif par == 4:
        n = input("enter new nominations")
        mycursor.execute("UPDATE MOVIED SET NOMINATIONS='{}' WHERE TITLE='{}'".format(n.lower(), mov.lower()))
        mydb.commit()
        print("changes made")
    else:
        print("incorrect choice")

def deletemovie():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIES_LIBRARY')
    mycursor=mydb.cursor()
    title=input("enter title of the movie whose details you would like to delete:")
    mycursor.execute("DELETE FROM MOVIED WHERE TITLE='{}'".format(title.lower()))
    mydb.commit()
    print('record deleted successfully..')

def addseries():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIES_LIBRARY')
    mycursor=mydb.cursor()
    tit=input("enter title of the series:")
    genre=input("enter genre of the series:")
    direc=input("enter name of the director")
    mycursor.execute("INSERT INTO SERIESD VALUES('{}','{}','{}')".format(tit.lower(),genre.lower(),direc.lower()))
    mydb.commit()
    print("record inserted successfully...")

def updateseries():
    import mysql.connector
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='MOVIE_AND_SERIES_LIBRARY')
    mycursor = mydb.cursor()
    ser = input("enter title of the series whose details you would like to change:")
    par = int(input("what would you like to change? (1.genre, 2.director):"))

    if par == 1:
        m = input("enter new genre")
        mycursor.execute("UPDATE SERIESD SET GENRE='{}' WHERE TITLE='{}'".format(m.lower(), ser.lower()))
        mydb.commit()
        print("changes made")
    elif par == 2:
        l = input("enter new director")
        mycursor.execute("UPDATE SERIESD SET DIRECTOR='{}' WHERE TITLE='{}'".format(l.lower(), ser.lower()))
        mydb.commit()
        print("changes made")
    else:
        print("incorrect choice")

def deleteseries():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='MOVIE_AND_SERIES_LIBRARY')
    mycursor=mydb.cursor()
    title=input("enter title of the series whose details you would like to delete:")
    mycursor.execute("DELETE FROM SERIESD WHERE TITLE='{}'".format(title.lower()))
    mydb.commit()
    print('record deleted successfully..')

def main_menu():
    c = 'y'
    while c.lower() == 'y':
        print("************Welcome to MOVIE AND SERIES LIBRARY!**********")
        print("1. Add new movie details")
        print("2. Show all movie details")
        print("3. Show nominations of movies")
        print("4. Update and make changes in movie details")
        print("5. Delete a record from movie details")
        print("6. Add new series details")
        print("7. Make changes in details/Update of series")
        print("8. Delete a record from series details")
        print("9. QUIT")
        n = int(input("Enter choice: "))
        if n == 1:
            addnewmovie()
        elif n == 2:
            showmovie()
        elif n == 3:
            shownom()
        elif n == 4:
            updatemovie()
        elif n == 5:
            deletemovie()
        elif n == 6:
            addseries()
        elif n == 7:
            updateseries()
        elif n == 8:
            deleteseries()
        elif n == 9:
            print("Exiting...")
            break
        else:
            print("Wrong choice")
        c = input("Do you wish to continue? (yes=y, no=n): ")
        
main_menu()

