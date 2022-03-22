import mysql.connector
# For creation database --------
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password="mysql.D**pa01")
# myacces=mydb.cursor()
# myacces.execute("CREATE DATABASE Restaurant_Management_System") 




mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="mysql.D**pa01",
    database="Restaurant_Management_System")


mycursor = mydb.cursor()

# # DELETING DATABASE___________________________________________________________________________________________________________________
# mycursor.execute("DROP Database Restaurant_Management_System")                


# _____________________________________CREATING TABLE 1____________________________________________________________________________________________________
# mycursor.execute(                                               
#     "CREATE TABLE Chef_Details(Chef_Id INT NOT NULL PRIMARY KEY,Chef_name VARCHAR(30) NOT NULL , Chef_Salary VARCHAR(20) NOT NULL ,Chef_Joining_Date DATE  NOT NULL , Chef_Mobile_Number INT (10) NOT NULL )")
# ADDING DATA IN TABLE CALLED CHEF DEAILS ------------------------------->> WITH PRIMARY KEY
# sql = "INSERT INTO Chef_Details (Chef_Id,Chef_name, Chef_Salary, Chef_Joining_Date,Chef_Mobile_Number) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     (836,"Deepa",50000,"2018-03-24",1234567891),
#     (123,"Priya",60000,"2019-08-24",1234567894),
#     (135,"Gautami",23000,"2021-01-24",1234567895),
#     (194,"Sonali",47000,"2020-11-24",1234567892),
#     (790,"Khushi",10000,"2018-09-24",1234567893)]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mycursor.executemany(sql, val)
# mydb.commit()
# mycursor.execute("SELECT * FROM Chef_Details")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# _________________________________FOR SORTING_______________________________________________________
# mycursor = mydb.cursor()
# sql = "SELECT * FROM Chef_Details ORDER BY Chef_Id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# ____________________________________UPDATEING__________________________________________________________
# mycursor = mydb.cursor()
# sql = "UPDATE Chef_Details SET Chef_Salary = '10000' WHERE Chef_name = 'priya'"
# mycursor.execute(sql)
# mydb.commit()

# mycursor.execute("SELECT AVG(Chef_Salary) FROM Products Meal_Details; ")

# ________________________________Count_____________________________________________________________________________
# mycursor.execute(" SELECT COUNT(Chef_Salary) From Chef_Details")


# ________________________________AVRAGE_____________________________________________________________________________
# mycursor.execute("SELECT AVG(Chef_Salary) AS AveragePrice FROM Chef_Details")


# ________________________________MAX()____________________________________________________________________________________
# mycursor.execute("SELECT MAX(Chef_Salary)  FROM Chef_Details")

# ________________________________MIN()___________________________________________________________________________
# mycursor.execute("SELECT MIN(Chef_Salary)  FROM Chef_Details")


# __________________________________LIKE_________________________________________________________________________
# mycursor.execute("SELECT * FROM Chef_Details WHERE Chef_Name LIKE '%a';") 


# _______________________________________TABLE 2_________________________________________________________________
# # mycursor.execute("CREATE TABLE Meal_Details(Meal_Id INT NOT NULL PRIMARY KEY,Meal_Name VARCHAR (30) NOT NULL, Meal_Price INT NOT NULL, Meal_Quentity INT NOT NULL,Cehf_Id INT NOT NULL,FOREIGN KEY (Cehf_Id) REFERENCES  Chef_Details(Chef_Id))")
#  ADDING DATA IN MEAL DETAIL
# sql = "INSERT INTO Meal_Details (Meal_Id,Meal_name, Meal_Price, Meal_Quentity ,Cehf_Id ) VALUES ( %s,%s, %s, %s, %s)"
# val = [
#     (111,"Dhosa",500,6,790),
#     (222,"Pizza",6000,4,123),
#     (333,"Burger",200,94,836),
#     (444,"Pani puri",4700,62,194),
#     (555,"Cake",1210,36,135),
#     (666,"Dosa",100,13,123),
#     (777,"Momo",12000,56,135),
#     (888,"Rice",12,6,123)]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mycursor.executemany(sql, val)
# mydb.commit()
# mycursor.execute("SELECT * FROM Meal_Details")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# ____________________________________________SORTING___________________________________________________________________________
# mycursor = mydb.cursor()
# sql = "SELECT * FROM Meal_Details ORDER BY Meal_Id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# __________________________________________UPDATEING NUMBER _________________________________________________________--
# mycursor = mydb.cursor()
# sql = "UPDATE Chef_Details SET Meal_name = 'XYZ' WHERE Chef_name = 'momo'"
# mycursor.execute(sql)
# mydb.commit()


# ______________________________________CREATING TABLE 3________________________________________________
# mycursor.execute(
#   "CREATE TABLE Waiter_Details(Waiter_Id INT NOT NULL PRIMARY KEY,Waiter_Name VARCHAR(30) NOT NULL , Waiter_salary INT NOT NULL ,Waiter_Mobile_Number INT (10) NOT NULL , Waiter_Joining_date DATE not null )")

#  ADDING DATA IN MEAL DETAILS--------------------------->>
# sql = "INSERT INTO Waiter_Details (Waiter_Id,Waiter_name, Waiter_salary,Waiter_Mobile_Number, Waiter_Joining_date ) VALUES ( %s,%s, %s, %s, %s)"
# val = [
#     (901,"Kunal",5000,82673667,"2019-01-23"),
#     (902,"Anokhi",6000,41325246,"2020-07-27"),
#     (903,"Vishakha",20000,9523544,"2019-11-03"),
#     (904,"konchi",4700,672673652,"2016-01-01"),
#     (905,"Sonu",1210,35263426,"2009-12-03"),
#     (906,"Sonam",10000,123314513,"2017-11-10"),
#     (907,"Akriti",12000,511362986,"2020-07-21"),
#     (908,"Akhil",1900,62425389,"2002-11-12"),
#     ]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#__________________________________________ TABLE 4________________________________________________________________________________
# mycursor.execute("CREATE TABLE Customer_Details ( Custumer_Id INT NOT NULL,Customer_Name VARCHAR (30) NOT NULL,Customer_Number VARCHAR (10) NOT NULL,Waiter_Id1 INT NOT NULL,FOREIGN KEY (Waiter_Id1) REFERENCES   Waiter_Details(Waiter_Id))")

#  ADDING DATA IN CUSTOMER DETAILS--------------------------->>

# sql = "INSERT INTO  Customer_Details (Custumer_Id,Customer_Name, Customer_Number,Waiter_Id1 ) VALUES ( %s, %s, %s, %s)"
# val = [
#     (100001,"Hina",82673667,902),
#     (100002,"Gunjan",41325246,904),
#     (100003,"Anil",9523544,907),
#     (100004,"Kaushik",4672673652,902),
#     (100007,"Deepashikha",511362986,903),
#     (100008,"Roshni",1900967889,908),
#     ]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)



# mycursor.execute("SELECT *  FROM Chef_Details LEFT JOIN Meal_Details ON Chef_Details.Chef_Id = Meal_Details.Cehf_Id")