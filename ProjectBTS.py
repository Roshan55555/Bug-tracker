#LOGIN AND SIGNUP MODULE
import mysql.connector
import random

def emplogin():
    while True:
        id = input("Enter employee login id :")
        pss=input("Enter the password :")
        db=mysql.connector.connect(host='localhost',database='iitk_db',username='root',password='password')
        mycursor=db.cursor()
        sql="select * from employee where empLoginId='%s'"
        value=(id)
        completesql=sql%value
        mycursor.execute(completesql)
        try:
            row=mycursor.fetchmany(1)[0]
            dbpass=row[1]
            if dbpass==pss:
                print("Login successfull")
                dbtype=row[2]

                if dbtype=="ADMIN":
                    print("Welcome Administrator")

                    return 1
                else:
                    print("Welcome expert")
                break

            else:
                print("Incorrect password")
                continue

        except IndexError:
            print("The entered login id is incorrect")
            continue

    
    
    
def culogin():
    while True:
        id = input("Enter customer login id :")
        pss = input("Enter the password :")
        db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
        mycursor = db.cursor()
        sql = "select * from customer where custLoginId='%s'"
        value = (id)
        completesql = sql % value
        mycursor.execute(completesql)
        try:
            row = mycursor.fetchmany(1)[0]
            dbpass = row[1]
            if dbpass == pss:
                print("Login successfull")
                auth=1
                dbname=row[2]
                print("Hello",dbname)
                return auth

            else:
                print("Incorrect password")
                continue


        except IndexError:
            print("The entered login id is incorrect")
            continue




def newcustomer():
    while True:

            lg = random.randint(2003, 10000)
            hj = "CU"+str(lg)

            nm = input("Enter your name : ")
            age=int(input("Enter your age :"))
            ph=input("Enter your phone number :")
            em = input("Enter your email address :")
            ps = input("Set your password :")
            db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
            mycursor = db.cursor()
            try:

                sql="insert into customer values('%s','%s','%s',%d,'%s','%s')"
                values=(hj,ps,nm,age,ph,em)
                complete_sql=sql%values
                mycursor.execute(complete_sql)
                db.commit()

                if mycursor.rowcount==1:
                    print("Sign up  successfull")
                    print("Your login id is ",hj)
                    print("Your password is",ps)
                    break
                else:
                    print("Sign up unsuccessfull.Please try again")
                    continue
            except IndexError :
                print("System Error,Please try again.Sorry for the inconvenience :)")
                continue
            except ValueError:
                print("System Error,Please try again.Sorry for the inconvenience :)")
                continue

            except :
                print("System Error,Please try again.Sorry for the inconvenience :)")
                continue


    db.commit()
    db.close()
#--ADMIN MODULE
def amsearch():
    D = {1:"view" ,2:"search by name",3:"search by id"}
    for h in D:
        print(h   ,"="  ,D[h])
    fc=int(input("Enter the number corresponding to the function do you want to perform"))
    db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
    mycursor = db.cursor()
    try:
        while True:
            if fc==1:
                sql="select * from customer"
                mycursor.execute(sql)
                print("%-20s%-20s%-20s%-20s%-20s%-20s" % ("LoginId", "Password", "Name","Age","PhoneNO","Email"))
                for row in mycursor:
                    print("%-20s%-20s%-20s%-20s%-20s%-20s" % (row[0],row[1],row[2],row[3],row[4],row[5]))


                break
            if fc==2:
                nm=input("Enter the name of the customer to search :")
                try:
                    sql = "select * from customer where custName='%s'"
                    values=(nm)
                    complete_sql=sql%values
                    mycursor.execute(complete_sql)
                    print("%-20s%-20s%-20s%-20s%-20s%-20s" % ("LoginId", "Password", "Name", "Age", "PhoneNO", "Email"))
                    for row in mycursor:
                        print("%-20s%-20s%-20s%-20s%-20s%-20s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
                    if mycursor.rowcount==0:
                        print("Invalid name ,Try again")
                    break
                except:
                    print("Wrong information entered")
                    continue
            if fc==3:
                try:
                    nm = input("Enter the id of the customer to search :")
                    sql = "select * from customer where custLoginid='%s'"
                    values = (nm)
                    complete_sql = sql % values
                    mycursor.execute(complete_sql)
                    print("%-20s%-20s%-20s%-20s%-20s%-20s" % ("LoginId", "Password", "Name", "Age", "PhoneNO", "Email"))

                    for row in mycursor:
                        print("%-20s%-20s%-20s%-20s%-20s%-20s" % (row[0], row[1], row[2], row[3], row[4], row[5]))

                    if mycursor.rowcount==0:
                        print("Invalid name ,Try again")


                    break
                except:
                    print("Wrong information entered")
                    continue
    except ValueError:
        print("")

def emservices():
    G={1:"add new",2:"view all employees" ,3:"search by name",4:"search by id",5:"search by type",6:"activate" ,7: "deactivate",8:"change password" }
    for a in G:
        print(a   ,"="   ,G[a])
    inp=int(input("Enter the number corresponding to the function do you want to perform :"))
    db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
    mycursor=db.cursor()
    try:
        while True:


            if inp==1:


                        nm=input("Enter the name of new employee :")
                        ph=input("Enter the phone no of new employee:")
                        em=input("Enter the email address :")
                        pw=input("Enter the password of new employee")
                        ps1=str(random.randint(1000,50000))
                        ty=input("Enter the employee type :")
                        if ty.lower()=="admin":
                            ps2="AD"+str(ps1)
                        else:
                            ps2="EX"+str(ps1)

                        sql="insert into employee(empLoginID,empPassword,empType,empName,empPhone,empEmail) values('%s','%s','%s','%s','%s','%s')"
                        values=(ps2,pw,ty,nm,ph,em)
                        complete_sql=sql%values
                        mycursor.execute(complete_sql)
                        db.commit()
                        if mycursor.rowcount == 1:
                            print("Data inserted successfully")
                        else:
                            print("Data could not be inserted")

                        break


            if inp==2:
                sql="select * from employee"
                mycursor.execute(sql)
                print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % ("LoginId", "Password", "Type", "Name", "PhoneNO", "Email","EmpStatus"))
                for row in mycursor:
                    print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (row[0], row[1], row[2], row[3], row[4], row[5],row[6]))
                break

            if inp==3:
                nm = input("Enter the name of the employee to search :")
                try:
                    sql = "select * from employee where empName='%s'"
                    values = (nm)
                    complete_sql = sql % values
                    mycursor.execute(complete_sql)
                    print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % ("LoginId", "Password", "Type", "Name", "PhoneNO", "Email", "EmpStatus"))



                    for row in mycursor:
                        print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                    if mycursor.rowcount==0:
                        print("Invalid name ,Try again")

                    break
                except IndexError:
                    print("Wrong information entered")
                    continue

            if inp==4:
                nm = input("Enter the id of the employee to search :")
                try:
                    sql = "select * from employee where empLoginId='%s'"
                    values = (nm)
                    complete_sql = sql % values
                    mycursor.execute(complete_sql)
                    print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
                    "LoginId", "Password", "Type", "Name", "PhoneNO", "Email", "EmpStatus"))
                    for row in mycursor:
                        print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                    if mycursor.rowcount==0:
                        print("Invalid id ,Try again")
                        continue

                    break
                except IndexError:
                    print("Wrong information entered")
                    continue

            if inp==5:
                nm = input("Enter the type of the employee to search :")
                try:
                    sql = "select * from employee where empType='%s'"
                    values = (nm)
                    complete_sql = sql % values
                    mycursor.execute(complete_sql)
                    print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
                        "LoginId", "Password", "Type", "Name", "PhoneNO", "Email", "EmpStatus"))
                    for row in mycursor:
                        print("%-20s%-20s%-20s%-20s%-20s%-20s%-20s" % (
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                    if mycursor.rowcount==0:
                        print("Invalid type ,Try again")

                    break
                except IndexError:
                    print("Wrong information entered")
                    continue






            if inp==6:

                    id=input("Enter the employee id whose status is to be changed")
                    sql="update employee set empStatus='ACTIVE' where empLoginId = '%s'"
                    values=(id)
                    complete_sql=sql%values
                    mycursor.execute(complete_sql)
                    for row in mycursor:
                        print(row)
                    if mycursor.rowcount==1:
                        print("status changed successfully")
                    else:
                        print("status is already ACTIVE")
                    db.commit()
                    break
            if inp==7:
                    id = input("Enter the employee id whose status is to be changed")
                    sql = "update employee set empStatus='INACTIVE' where empLoginId = '%s'"
                    values = (id)
                    complete_sql = sql % values
                    mycursor.execute(complete_sql)
                    for row in mycursor:
                        print(row)

                    if mycursor.rowcount==1:
                        print("status changed successfully")
                    else:
                        print("status is already INACTIVE")
                    db.commit()
                    break

            if inp==8:
                try:
                    id = input("Enter your employee id :")
                    ow=input("Enter your old password :")
                    nw=input("Enter your new password :")
                    sql="update employee set empPassword = '%s' where empLoginId = '%s' and empPassword='%s' "
                    values=(nw,id,ow)
                    complete_sql=sql%values
                    mycursor.execute(complete_sql)
                    db.commit()

                    if mycursor.rowcount == 1:
                        print("Password changed successfully.")

                    break




                except IndexError:
                    print("System Error,Please try again.Sorry for the inconvenience :)")
                    continue
    except:
        print("System error .Sorry for inconvenience :)")

def bugservice():
    G={1:"view all bugs",2:"search by bugid",3:"search by status",4:"search by customer id",5:"Assign work to expert",6:"Logout" }
    for i in G:
        print(i  ,'='  ,G[i])
    fn=int(input("Enter the number corresponding to the function would you like to perform ?"))
    db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
    mycursor = db.cursor()
    while True:
        if fn==1:
            sql="select * from bug"
            mycursor.execute(sql)
            print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate","ExpertLoginId","SolvedDate0","Solution"))
            for row in mycursor:
                print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8],row[9]))
            break
        elif fn==2:
            try:
                bg=int(input("Enter the bugid"))
                sql="select * from bug where bugId=%d"
                values=(bg)
                complete_sql=sql%values
                mycursor.execute(complete_sql)
                print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                    "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
                    "ExpertLoginId", "SolvedDate0", "Solution"))
                for row in mycursor:
                    print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

                break
            except IndexError:
                print("Invalid entry")
                continue
        elif fn==3:
            nm = input("Enter the type of the bugid to search ,Enter 'New Bug' if the bug is new:")
            try:
                sql = "select * from bug where bugStatus='%s'"
                values = (nm)
                complete_sql = sql % values
                mycursor.execute(complete_sql)
                print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                    "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
                    "ExpertLoginId", "SolvedDate0", "Solution"))
                for row in mycursor:
                    print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                break
            except IndexError:
                print("Wrong information entered")
                continue
        elif fn==4:
            nm = input("Enter the  customer id to search :")
            try:
                sql = "select * from bug where custLoginId='%s'"
                values = (nm)
                complete_sql = sql % values
                mycursor.execute(complete_sql)
                print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
                "ExpertLoginId", "SolvedDate0", "Solution"))
                for row in mycursor:


                    print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                break
            except IndexError:
                print("Wrong information entered")
                continue
        elif fn==5:

                bh=int(input("Enter the bugid to be assigned"))
                lg=input("Enter the expert login id ")
                sql = "select * from employee where empLoginId='%s'"
                value = (lg)
                completesql = sql % value
                mycursor.execute(completesql)
                try:
                    row = mycursor.fetchmany(1)[0]
                    emptype = row[2]
                    if lg.lower()[0:2] == "ex":


                        sql="update bug set expertAssignedDate=now(),expertLoginId='%s' where bugId=%d "
                        values = (lg, bh)
                        complete_sql = sql % values
                        mycursor.execute(complete_sql)
                        db.commit()
                        if mycursor.rowcount == 1:
                            print("Work assigned successfully")
                        else:
                            print("Work  could not be assigned successfully")
                        break
                    else:
                        print("the entered login id is not of an expert type of employee")
                        break

                except :
                    print("Wrong information entered")



        elif fn==6:
            break
        else:
            print("Invalid text")
            continue
#CUSTOMER MODULE
def conn():
   db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
   return db




def cusup():

    print("ENTER THE DETAILS TO UPDATE")
    id=input("Enter your customer ID")
    nm=input("Enter the name to update :")
    ag=int(input("Enter new age :"))
    ph=input("Enter the updated phone number")
    em=input("Enter the updated email address")
    db=conn()
    mycursor=db.cursor()
    try:
        sql="update customer set custName='%s',custAge=%d,custPhone='%s',custEmail='%s' where custLoginId='%s'"
        values=(nm,ag,ph,em,id)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount==1:
            print("Details updated  successfully")
        else:
            print("System Error,Please try again :)")
    except ValueError:
        print("phone number should be in digits.")
    except IndexError:
        print("Invaid id")


def pnb():
    id=input("Enter your customer login id")
    ty=input("Enter your product type")
    dsc=input("Describe the bug you are facing :")
    db=conn()
    mycursor=db.cursor()
    try:
        sql="insert into bug(custLoginId,productName,bugDesc) values('%s','%s','%s')"
        values=(id,ty,dsc)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount==1:
            print("Bug posted successfully")
        else:
            print("Bug could not be posted successfully")
    except IndexError:
        print("Invalid data")


def vab():
    db=conn()
    mycursor=db.cursor()
    try:
        sql="select * from bug"
        mycursor.execute(sql)
        print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
            "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
            "ExpertLoginId", "SolvedDate0", "Solution"))
        for row in mycursor:
            print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    except :
        print("System error ,please try again")


def bbos():
    try:
        st=input("Enter the bug status(new bug or old bug) to search :")
        db=conn()
        mycursor=db.cursor()
        sql="select * from bug where bugStatus='%s'"
        values=(st)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
            "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
            "ExpertLoginId", "SolvedDate0", "Solution"))
        for row in mycursor:
            print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    except:
        print("System error,Please try again.")

def vbs():
    try:
        lg=input("Enter customer login id  :")
        bg=input("Enter the bug id :")
        db=conn()
        mycursor=db.cursor()
        sql="select * from bug where custLoginId='%s' and bugId='%s'"
        values=(lg,bg)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        row=mycursor.fetchmany(1)[0]
        slu=row[9]
        print("Solution =",slu)
    except IndexError:
        print("System error,Please try again.")
    except:
        print("System error,Please try again.")

def cp():
    try:

        id = input("Enter the customer id ")
        ow=input("Enter old password :")
        nw = input("Enter the new password :")

        db = conn()
        mycursor = db.cursor()
        sql = "update customer set custPassword = '%s' where custLoginId = '%s' and custPassword='%s' "
        values = (nw, id,ow)
        complete_sql = sql % values
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount == 1:
            print("Password changed successfully.")
        else:
            print("Password could not be changed")


    except IndexError:
        print("System Error,Please try again.Sorry for the inconvenience :)")
#EXPERT MODULE

def vasb():
    try:
        lg=input("Enter the expert login ID")
        db=mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
        mycursor=db.cursor()
        sql="select * from bug where expertLoginId='%s'"
        values=(lg)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s"% (
            "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
            "ExpertLoginId", "SolvedDate0", "Solution"))
        for row in mycursor:
            print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8], row[9]))
    except:
        print("System error,Please try again.")


def fab():
    try:
        lg=input("Enter the expert login ID")
        db=mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
        mycursor=db.cursor()
        sql="select * from bug where expertLoginId='%s' and bugStatus='new bug'"
        values=(lg)
        complete_sql=sql%values
        mycursor.execute(complete_sql)
        print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s" % (
            "BugId", "BugPostingdate", "custLoginID", "bugstatus", "ProductName", "BugDesc", "AssignedDate",
            "ExpertLoginId", "SolvedDate0", "Solution"))
        for row in mycursor:
            print("%-20s%-30s%-20s%-20s%-20s%-40s%-20s%-20s%-20s%-20s"% (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8], row[9]))
    except:
        print("System error,Please try again.")



def stb():
    lg = input("Enter the expert login id :")
    bd = int(input("Enter the bugId :"))
    sl = input("Enter the solution for the Bug :")


    db = mysql.connector.connect(host='localhost',database='iitk_db',username='root',password='password')
    mycursor = db.cursor()
    try:
        sql = "update bug set solution='%s' ,bugSolvedDate=now(),bugStatus='Old Bug' where expertLoginId ='%s' and bugId=%d "
        values = (sl, lg, bd)
        complete_sql = sql % values
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount==1:
            print("Solution uploaded successfully")
        else:
            print("Solution could not be uploaded")
    except:
        print("System error,Please try again.")
def ecp():
    db=conn()
    mycursor=db.cursor()
    try:
        id = input("Enter the expert id : ")
        ow=input("Enter old password :")
        nw = input("Enter the new password :")
        sql = "update employee set empPassword = '%s' where empLoginId = '%s' and empPassword='%s' "
        values = (nw, id,ow)
        complete_sql = sql % values
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount == 1:
            print("Password changed successfully.")
        else:
            print("Password could not be changed.Please try again")

    except :
        print("System Error,Please try again.Sorry for the inconvenience :)")




# -----------------------------------------------------------------------------

def expackage():

    while True:
        try:
            D={1:"View Assigned Bug",2:"Filter Assigned Bug",3:"Solve the Bug",4:"Change Password",5:"LogOut"}
            for x in D:
                print(x,"  =  ",D[x])
            fn = int(input("Enter the number corresponding to the function  you would like to perform ?"))

            if fn==1:
                vasb()
                continue
            if fn==2:
                fab()
                continue
            if fn==3:
                stb()
                continue
            if fn==4:
                ecp()
                continue
            if fn==5:
                return
        except:
            print("System error.Please try again later.")

def cupackage():
    try:


        while True:
            G = { 1: "Update account", 2: "Post new Bug", 3: "View all bugs",
                 4: "Search bugs based on status", 5: "View bug solution",6:"Change Password",7:"Log Out"}
            for x in G:
                print(x,"  =  ",G[x])
            fn = int(input("Enter the number corresponding to the function  you would like to perform ?"))


            if fn==1:
                cusup()
                continue
            elif fn==2:
                pnb()
                continue
            elif fn==3:
                vab()
                continue
            elif fn==4:
                bbos()
                continue
            elif fn==5:
                vbs()
                continue
            elif fn==6:
                cp()
                continue
            elif fn==7:
                return
            else:
                print("Invalid text")
    except:
        print("System error.Sorry for inconvenience :)")
def admpackage():

    while True:
        G = {1:"customer services",2: "employee services", 3:"bug services",4:"Logout"}
        for x in G:
            print(x  ,  "="   ,G[x])
        n=int(input(" Enter the number corresponding to the services  you want to perform ?"))
        if n==1:
            amsearch()
            continue
        elif n==2:
            emservices()
            continue
        elif n==3:
            bugservice()
            continue
        elif n==4:
            quit()
        else:
            print("Invalid text")
            continue
while True:
    tp = {1:"Employee",2:"Customer",3:"New Customer"}
    for x in tp:
        print(x,  "="  ,tp[x])
    usr=int(input("Enter the number corresponding to the type of user you are "))
    print("**********************", usr)
    if usr == 1:
        emplogin()
        id = input("Please enter login id once again")
        db = mysql.connector.connect(host='localhost', database='iitk_db', username='root', password='password')
        mycursor = db.cursor()
        sql = "select * from employee where empLoginId='%s'"
        value = (id)
        completesql = sql % value
        mycursor.execute(completesql)
        try:
            row=mycursor.fetchmany(1)[0]
            emptype=row[2]
            if emptype=="ADMIN":
                admpackage()
                break
            else:
                expackage()
                break
        except IndexError:
            print("System error.Please try again later")


    elif usr == 2:
        n=culogin()
        if n==1:
            cupackage()
        else:
            print("Login unsuccessful")
            continue




    elif usr == 3:
        newcustomer()
        print("You are redirected to login page :)")
        n=culogin()
        if n == 1:
            cupackage()
        else:
            print("Login unsuccessful")
            continue


    else:
        print("Invalid text")
        continue








