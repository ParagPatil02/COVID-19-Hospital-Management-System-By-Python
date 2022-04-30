for i in range(81):
    print("*",end="")

for i in range(3):
    print("*                                                                                *")
print("*                    -: WELCOME TO COVID 19 MANAGEMENT SYSTEM :-                 *") 
print("*                    -:   BE SAFE ...........BE COVID FREE    :-                 *") 

for i in range(3):
    print("*                                                                                *")

for i in range(81):
    print("*",end="")

import mysql.connector
mydba=mysql.connector.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydba.cursor()

mycursor.execute("create database if not exists covid_19_project")
mycursor.execute("use covid_19_project")
mycursor.execute("create table if not exists doctor(Name varchar(20) not null ,Education varchar(15) not null,DAge int not null ,Gender varchar(7) not null,Mobile_no BIGINT not null,Dward_no int not null)")
mycursor.execute("create table if not exists patient(Patient_id int not null,Name varchar(20) not null,Address varchar(20) not null,Age int not null,Gender varchar(7) not null,Mobile_no BIGINT not null,Covid_test_result varchar(20) not null, ward_no int not null,Date DATE not null, PRIMARY KEY (Patient_id)) ")
mycursor.execute("create table if not exists oxygen_cylinders_info(Name varchar(20) not null,Patient_id BIGINT not null,Book_status varchar(20) not null)")
mycursor.execute("create table if not exists discharge_patient_name(Name varchar(20),Date DATE not null)")

def delete(Patient_id):
    query="delete from patients where Patient_id={}".format(Patient_id)
    mycursor.execute(query)
    mydba.commit()
    print("Deleted")

def mainfunction():
    for i in range(81):
        print("-",end="")
    main_menu()
    for i in range(81):
        print("-",end="")
    print("")
    choice1=int(input("=> Enter choice : "))
    if (choice1==1):
        admin_panel()
    if(choice1==2):
        doctor_menu()
    if (choice1==3):
        patient()
    if(choice1==4):
        covid_p_detail()
    if(choice1==5):
        end()
    
def main_menu():
    print("\n[1]-> Admin panel  \n[2]-> Doctor menu   \n[3]-> Patients   \n[4]-> Covid patients details")
    print("[5]-> Exit")
print("\n")    


def end():
    print("....................You have successfully Exit.................")    
    print("..............-: BE SAFE ...........BE COVID FREE :-............")
def admin_panel():
        for i in range(81):
            print("-",end="")
        print("")
        print("[1]-> Add patients")
        print("[2]-> Oxygen cylinder releated details" )
        print("[3]-> Help and guidelines releted to a covid 19 ")
        print("[4]-> Main menu ")
        for i in range(81):
            print("-",end="")
        print("")
        choice12=int(input("=>Enter your choice :"))
        for i in range (81):
            print("-",end="")
        print("\n")

        if(choice12==1):
            print("\t----------------Please fill imformation here----------------")
            if(choice12==1):
                sql = "INSERT INTO patient(Patient_id,Name,Address,Age,Gender,Mobile_no,Covid_test_result,ward_no,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                Patient_id=input("Enter patient_id :")
                Name=input("=>Enter name  :")
                Address=input("=>Enter a address:")
                Age=input("=>Enter age :")
                Gender=input("=>Enter gender :")      
                Mobile_no=input("=>Enter moblile no:")
                Covid_test_result=input("=>Enter covid_test_result :")
                ward_no=input("=>Enter Ward number :")
                date=input("=>Enter Date (yymmdd) :")
                val=(Patient_id,Name,Address,Age,Gender,Mobile_no,Covid_test_result,ward_no,date)
                mycursor.execute(sql,val)
                mydba.commit()              
                print("You have successfully entered patients data......!!")
                
                mainfunction()


        if(choice12==2):
            print("[1]-> Book Oxygen Cylinder")
            print("[5]-> Main menu") 
            choice123=int(input("=>Enter choice :"))
            if(choice123==1):
                sql = "INSERT INTO oxygen_cylinders_info(Name,Patient_id,Book_status) VALUES (%s,%s,%s)"
                Name=input("=>Enter patient name  :")
                Patient_id=input("=>Enter patient id:")
                Book_status=input("=>Enter a book status:")
                val=(Name,Patient_id,Book_status)
                mycursor.execute(sql,val)
                mydba.commit()  
                print("You have successfully booked cylinder......!!")
                for i in range(81):
                    print("-",end="")
                print("\n")            
                
                mainfunction()  

            if(choice123==5):
                for i in range(81):
                    print("-",end="")
                print("")
                
                mainfunction()
        if(choice12==3):
            #help and guidelines
            f=open("guidelines.txt","r")
            print(f.read())
            f.close()
            print("")
            mainfunction()
        if(choice12==4):
           
            mainfunction()
        else:
            mainfunction()


def doctor_menu():
    for i in range(81):
        print("-",end="")
    print("")
    
    print("[1]-> Doctors information ")
    print("[2]-> Ward info under doctor observation")
    print("[5]-> Main menu :")
    for i in range(81):
        print("-",end="")
    print("")
    choice22=int(input("=>Enter choice : "))
    for i in range(81):
        print("-",end="")
    print("")

    if(choice22==1):
        
        mycursor.execute("select * from doctor")
        result=mycursor.fetchall()
        for row in result:
            print("Name : ",row[0])
            print("Education :",row[1])
            print("Age: ",row[2])
            print("Gender: ",row[3])
            print("Mobile no :",row[4])
            print("")

        choice223=int(input("=>Add doctor information press 1 Otherwise press any key for main menu :"))
        if(choice223==1):
            sql = "INSERT INTO doctor(Name,Education,DAge,Gender,Mobile_no,Dward_no) VALUES (%s,%s,%s,%s,%s,%s)"
            Name=input("=>Enter name  :")
            Education=input("=>Enter education :")
            DAge=input("=>Enter age :")
            Gender=input("=>Enter gender :")
            Mobile_no=input("=>Enter moblile no:")
            Dward_no=input("=>Enter ward no :")
            val=(Name,Education,DAge,Gender,Mobile_no,Dward_no)
            mycursor.execute(sql,val)
            mydba.commit()                            
            print("You have successfully entered doctor data......!!")
            
            
            mainfunction()
        else:
            
           
            mainfunction()





    if(choice22==2):
        mycursor.execute("select Name ,Dward_no from doctor")
        fetc=mycursor.fetchall()
        for r in fetc:
            print("Name :",r[0])
            print("Ward No :",r[1])
            print("\n")
        print("")
        mainfunction()

    if(choice22==5):
        mainfunction()

def patient():
    for i in range(81):
        print("-",end="")
    print("")
    print("[1]->Patient information(name and all) ")
    print("[2]->Basic Covid test ")
    print("[3]->Add Discahrge patient")
    print("[5]->Main menu :")
    for i in range(81):
        print("-",end="")
    print("")
    choice32=int(input("=>Enter choice : "))
    for i in range(81):
        print("-",end="")
    print("")

    if(choice32==1):
    
        mycursor.execute("select * from patient")
        result=mycursor.fetchall()
        for row in result:
            print("Patient_id :",row[0])
            print("Name :",row[1])
            print("Address :",row[2])
            print("Age :",row[3])
            print("Gender :",row[4])
            print("Mobile_no :",row[5])
            print("Covid_test_result :",row[6])
            print("Ward number :",row[7])
            print("Date of Admit :",row[8])
            print("")
        print("")
        mainfunction()
    
    if(choice32==2):
        print("Enter 'Y' for Yes and 'N' for No")
        fever=input("=>Fever : ")
        cough=input("=>Cough :")
        tired=input("=>Tiredness :")
        lotos=input("loss of test or smell :")
        if(fever=='Y'or 'y' and cough=='Y'or 'y' and tired=='Y'or 'y' and lotos=='Y'or 'y'):
            print("\n90'%' chances of Covid")
        elif(fever=='Y' or 'y'and  cough=='Y'or 'y' and  tired=='Y'or 'y' and  lotos=='N'or 'n'):
            print("\n80 '%'chances of Covid")
        elif(fever=='Y'or 'y' and  cough=='Y'or 'y' and  tired=='N'or 'n' and lotos=='N'or 'n'):
            print("\n50'%' chances 50'%' chances of Commn Cold")
        elif(fever=='Y' or 'y' and  cough=='N'or 'n' and  tired=='N'or 'n' and  lotos=='N'or 'n'):
            print("\nYou have less chances to Covid ")
        else:
            print("\nYou have 0'%' chances of Covid")
        mainfunction()


    if(choice32==3):
        sql = "INSERT INTO discharge_patient_name (Name,Date) VALUES (%s,%s)"
        Name=input("=>Enter name :")
        Date=input("=>Enter date:")
        val=(Name,Date)
        mycursor.execute(sql,val)
        mydba.commit()
        print("You have successfully entered a data......!!")
        for i in range(81):
            print("-",end="")
        print("")
        mainfunction()
    if(choice32==5):
        for i in range(81):
            print("-",end="")
      
        mainfunction()


def covid_p_detail():
    for i in range(81):
        print("-",end="")
    print("")
    print("  \n[1]->Discharge patient list ")
    print("\n[5]->Main Menu")
    for i in range(81):
        print("-",end="")
    print("")
    choice42=int(input("=>Enter choice :"))
    for i in range(81):
        print("-",end="")
    print("")

    
    
    if(choice42==1):
        
        mycursor.execute("select * from discharge_patient_name")
        result=mycursor.fetchall()
        for row in result:
            print("Name: ",row[0])
            print("Date: ",row[1])
            print("\n")
        print("")
        mainfunction()
        

    if(choice42==5):
        for i in range(81):
            print("-",end="")
       
        mainfunction()
        



mainfunction() 
