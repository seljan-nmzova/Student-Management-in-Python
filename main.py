#First step create class Student

class Student:
    def __init__(self, trno, fname,lname,email,phone):
        self.trno = trno
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone

 #Create function and append new student

    def enter(self, trno, fname,lname,email,phone):
        det = Student( trno, fname,lname,email,phone)
        ls.append(det)

    #Create function and display student info
    
    def display(self, det):
     print("Tracking-number: ", det.trno)
     print("First name: ", det.fname)
     print("Last name: ", det.lname)
     print("Email address: ", det.email)
     print("Phone number: ", det.phone)
     print("\n")


# Create function and update student info
    def update(self,trno, No):
        i = obj.search(trno)
        newnum = No
        ls[i].newNo = newnum 

#Search function
        def search(self, trno):
         for i in range(ls.__len__()):
             if(ls[i].trno):
                 return i

# Delete student info

    def delete(self, trno):
        i = obj.search(trno)
        del ls[i]

# Create a list to add students

    students = []
    obj = student('', 0,0,0,0 )
    print("\n Operations used, ")

# ch=int(input("Enter choice: "))
if (ch==1):
    obj.enter("10", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("9", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("8", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("7", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("6", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("5", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("4", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("3", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("2", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)
    obj.enter("1", "Seljan", "Nmzova", "seljan.nmzova@gmail.com", 994774421768)


    if (ch == 2):
        print("\n")
        print("\n list of students\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])

    elif (ch == 3):
        obj.delete (9)
          print(ls.__len__())
          print("list after deletion")
        
    elif (ch==4):
        obj.update(6,7)
        print(ls.__len__())
        print("list after update")
        for i in range(ls.__len__()):
            obj.display(ls[i])


        


