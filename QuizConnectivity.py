import pymysql

#Connection Object
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="Raveen9893",database="quizapp")

#Cursor object
mycursor = mydb.cursor()
#==============================================
print("Connectivity Successful......")
