import mysql.connector as a
con= a.connect(host="localhost", user="root", passwd="Bank@123456", database="employee")

def npersonal():
	n=input("Enter Employee Name: ")
	c=input("Enter City Name: ")
	d=input("Enter D.O.B: ")
	p=int(input("Enter Phone No: "))
	data = (n, c, d, p)
	sql = "insert into personal values(%s, %s, %s, %s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data Entered Sucessfully")
	print(">------------------------------------<")
	main()

def personal():
	sql="select*from personal"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print(i)
	main()

def noffice():
	ec=input("Enter Employee Code: ")
	n=input("Enter Name of Employee: ")
	ps=input("Enter post of Employee: ")
	j=input("Enter D.O.J: ")
	bp=int(input("Enter Basic Pay of Employee: "))
	data=(ec, n, ps, j, bp)
	sql="insert into office values(%s, %s, %s, %s, %s)"
	c=con.cursor()
	c.execute(sql, data)
	con.commit()
	print("Data Entered Sucessfully")
	print(">------------------------------------<")
	main()

def office():
	sql="select*from office"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print(i)
	main()

def nsalary():
	ec=input("Enter Employee Code: ")
	v=(ec,)
	sql="select Basicpay from office where ecode = %s"
	c=con.cursor()
	c.execute(sql,v)
	bs=c.fetchone()
	n=input("Enter Name of Employee: ")
	y=input("Enter year: ")
	m=input("Enter Month: ")
	wd=int(input("Enter Total Working Days: "))
	td=int(input("Enter Total Days: "))
	fp=bs[0]/td*wd
	data=(ec, n, y, m, wd, fp)
	sql="insert into salary values(%s, %s, %s, %s, %s, %s)"
	c=con.cursor()
	c.execute(sql, data)
	con.commit()
	print("Data Entered Sucessfully")
	print(">------------------------------------<")
	main()

def salary():
	sql="select* from salary"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print(i)
	main()

def main():
	print('''
		1. Add New Employee Personal Details
		2. Display Employee Personal Details
		3. Add New Employee Office Details
		4. Dispaly Employee Office Details
		5. Enter Salary Details of Employee
		6. Display Salary Details of Employee''')

	choice=input('Enter Task No: ')

	while True:
		if(choice =='1'):

			npersonal()

		elif(choice =='2'):

			personal()

		elif(choice =='3'):

			noffice()

		elif(choice =='4'):

			office()

		elif(choice =='5'):

			nsalary()

		elif(choice =='6'):

			salary()	

		else:
			("Wrong Choice--------")
main()
	
