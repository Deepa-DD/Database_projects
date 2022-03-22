import mysql.connector
from soupsieve import select
# # For creation database --------
# mydb = mysql.connector.connect(
    # host='localhost',
    # user='root',
    # password="mysql.D**pa01")
# myacces=mydb.cursor()
# myacces.execute("CREATE DATABASE Employee_Payroll_Management_System") 

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="mysql.D**pa01",
    database="Employee_Payroll_Management_System")


mycursor = mydb.cursor()

#______________________________ DELETING TABLE_________________________________________________________________________________________________________-___
# mycursor.execute("DROP TABLE Employee_Details")                


#_____________________________ CREATING TABLE CALLED EMPLOYEE_DETAILS_____________________________________________________________________________
# mycursor.execute(                                               
#     "CREATE TABLE Employee_Details(Employee_Id INT NOT NULL PRIMARY KEY,Employee_name VARCHAR(30) NOT NULL , Employee_Title VARCHAR(20) NOT NULL ,Date_of_Birth DATE NOT NULL ,Date_Of_Joining DATE  NOT NULL , State VARCHAR (20) NOT NULL ,pincode INT NOT NULL , Mobile_Number INT (10) NOT NULL ,Email_Id VARCHAR (50) NOT NULL , Pad_Card_Number INT NOT NULL )")



# ______________________________ FOR INSERTING VALUE IN THE TABLE __________________________________________________________________________________________________

# sql = "INSERT INTO Employee_Details (Employee_Id, Employee_name, Employee_Title, Date_of_Birth, Date_Of_Joining, state, pincode, Mobile_Number, Email_Id, Pad_Card_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
# (121,"Deepa", "Associate", "2001-02-17", "2021-01-21", "Delhi", 111130, 312003679, "Deepa.Deepa2@natwest.com", 1192348),
# (122, "pooja", "Line Manager", "1991-02-17", "2021-01-21", "Agra", 111160, 830048371, "pooja2@natwest.com", 9087213),
# (123, "Anil", "Senior Associate", "1989-02-19", "2020-01-2", "kolkata", 1111065, 910027453, "Anil@natwest.com", 5693546),
# (124, "Abhi", "Manager", "1999-02-09", "2019-01-21", "Karnataka" , 11471100, 736257483, "Abhi@natwest.com", 34216548),
# (125, "Reena", "junior Associate", "2009-02-16", "01-01-17", "Karnataka" , 111160, 90556271, "Reena02@natwest.com", 987321),
# (126, "Albert", "Managing Director", "2010-02-15", "17-01-28", "Jharkhand", 1111076, 992746526, "Al011@natwest.com", 789354),
# (127, "Sunil", "Associate", "1988-04-08","2011-01-01", "Delhi", 111187, 110156273, "Sunil5@natwest.com", 9783164),
# (128, "Priya", "Associate", "1979-12-19", "2010-03-12", "Haryana", 111540, 254337198, "ppriya111@natwest.com", 987205),
# (129, "Rani", "Senior Associat", "1981-12-11", "2019-01-23", "Bihar", 111135, 278934602, "Rani567@natwest.com", 732324),
# (1201, "Neha", "Associate", "1982-02-12", "2018-1-5", "Gujarat" , 111174, 943562819,"Nehaa@natwest.com", 9824587),
# (1202, "Pradeep", "Managing Director","1999-04-04", "2019-01-08", "Chhattisgarh", 1111435, 832634860, "PP@natwest.com", 6453548),
# (1203, "Aisha", "Managing Director", "1995-07-05", "2015-01-08", "Delhi", 111950, 733652551, "Aisha123@natwest.com", 76876348),
# (1211, "Deepa", "Associate", "2001-02-21", "2016-04-28", "Delhi", 111130, 633902876, "Deepa.Deepa2@natwest.com", 1103348),
# (1205, "Zoya", "junior Associate", "1984-09-04", "2020-01-23", "Madhya Pradesh", 111154, 889367483, "ZoyaMM@natwest.com", 1593348),
# (1206, "Aliya", "Director", "1999-06-09", "2011-01-23", "Karnataka", 111138, 1234526782, "Aliya@natwest.com", 9879348),
# (1207, "Anjali", "Line Manager", "1989-03-19", "2010-01-02", "Madhya Pradesh", 111578, 822679082, "AjaliKumari@natwest.com", 3553348),
# (1221, "Deepa", "Associate", "2001-02-21", "2017-01-01", "Delhi", 111130, 422617782, "Deepa.Deepa2@natwest.com", 1192348),
# (1208, "Priya", "junior Associate", "1979-07-09", "2017-01-12", "Delhi", 111100, 245135653, "ppriya111@natwest.com", 873348),
# (1298, "Anuj", "Associate", "1990-05-19", "2015-01-08", "Orissa", 115600, 555434426, "Anuj123@natwest.com", 65889348),
# (1209, "Deepshikha", "Associate", "1986-02-16", "2012-01-09", "Tripura" , 111365, 536728364, "Deep000@natwest.com", 703348),
# (12011, "Sandeep", "Managing Director","1991-10-11", "1010-01-21", "Tripura" , 111196, 963345678, "Sandy@natwest.com", 473348),
# (12021, "Kunal", "Director", "1982-07-3", "1020-01-21", "Delhi", 111153, 931344679, "Kunal.kunal@natwest.com", 9803348),
# (1231, "Jyoti", "junior Associate", "1991-02-10", "2007-01-11", "Orissa", 111143, 752445689, "jyoti@natwest.com", 5903348)]

# mycursor.executemany(sql, val)
# mydb.commit()
# mycursor.execute("SELECT * FROM Employee_Details")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# ________________________FOR SORTING DATA BY Employee_Id__________________________________________________________________________
# mycursor = mydb.cursor()
# sql = "SELECT * FROM Employee_Details ORDER BY Employee_Id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# _______________________UPDATEING NUMBER WHERE NAME = POOJA___________________________________________________________________________
# mycursor = mydb.cursor()
# sql = "UPDATE Employee_Details SET Mobile_Number = '0000001' WHERE Employee_name = 'pooja'"
# mycursor.execute(sql)
# mydb.commit()


# ______________________________DELETING ROW FROM TABLE_______________________________________________________________________________________
# mycursor = mydb.cursor()
# sql = "DELETE FROM Employee_Details WHERE Employee_Id = '1211'"
# mycursor.execute(sql)
# mydb.commit()


# __________________________________ TABLE 2__________________________________________________________________________________________

# mycursor.execute(                                               
    # "CREATE TABLE Department_Details(Employee_Id INT NOT NULL ,Department_name VARCHAR(30) NOT NULL , Department_number INT NOT NULL, Leav_in_aWeek INT NOT NULL ,Department_Location VARCHAR (50),FOREIGN KEY (Employee_Id) REFERENCES   Employee_Details(Employee_Id) )")
# sql = "INSERT Department_Details (Employee_Id, Department_name, Department_number,Leav_in_aWeek , Department_Location) VALUES ( %s,%s, %s, %s, %s)"
# val = [
#     (122,"PWD",50,1,"Delhi"),
#     (123,"Head quater",6210,1,"Pune"),
#     (124,"main Head quater",120,2,"Banglore"),
#     (125,"main Head quater",420,1,"Pune"),
#     (126,"PWD",1210,1,"Delhi"),
#     (127,"Head quater",168,1,"UP"),
#     (128,"Head quater",187,5,"MP"),
#     (129,"PWD",1789,2,"Agra"),
#     ]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)



# _______________________________INNER JOIN ______________________________________________________________________

# mycursor.execute( "select * from Employee_Details inner join Department_Details ON Employee_Details.Employee_Id=Department_Details.Employee_Id")












