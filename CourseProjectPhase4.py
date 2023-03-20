#Nicole Chambers
#CIS261
#Course Project Phase 4

import datetime

def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    with open('user.txt', 'a') as UserFile:
        while True:
            username = GetUserName()
            if username.upper() == "END":
                break
            userpwd = GetUserPassword()
            userrole = GetUserRole()
            UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
            UserFile.write(UserDetail)
        UserFile.close()   
        printuserinfo()

def GetUserName():
    username = input("Enter username or END to Quit: ")
    return username

def GetUserPassword():
    userpwd = input("Enter pwd: ")
    return userpwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if userrole in ["Admin", "User"]:
            return userrole
        else:
            userrole = input('Please input a valid userrole (Admin or User): ')

def printuserinfo():
    with open("user.txt","r") as UserFile:
        for UserDetail in UserFile:
            UserDetail = UserDetail.replace("\n", "")
            UserList = UserDetail.split("|")
            username = UserList[0]
            userpassword = UserList[1]
            userrole = UserList[2]
            print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)

def Login():
    with open('user.txt', 'r') as UserList:
        UserName = input("Enter User Name: ")
        UserRole = "None"
        for UserDetail in UserList:
            UserDetail = UserDetail.replace("\n", "")
            UserList = UserDetail.split("|")
            if UserName == UserList[0]:
                UserRole = UserList[2]
                return UserRole, UserName
        return UserRole, UserName

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    with open("Employees.txt","r") as EmpFile:
      while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue  # skip next if statement and re-start loop
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue        
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate  = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True   
    if (DetailsPrinted):  #skip of no detail lines printed
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

if __name__ == "__main__":
