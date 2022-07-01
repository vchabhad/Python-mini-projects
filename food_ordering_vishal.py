# Final project for edyoda's python module
#food ordering system with user and admin panel
#created by vishal

class Restaurant:
    
    def __init__(self, name):
        self.restaurant_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]


    
    
    def admin_register(self):
        try:
            self.admin_email=input("Enter your email id : ")
            self.admin_pass=input("Enter your password : ")
            self.admin_details={"Email_ID":self.admin_email,"Password":self.admin_pass}
            print("\n !! Admin Account is Created Successfully !! \n")
            print( "*" * 18 + f"!!  Welcome To {self.restaurant_name} Restaurant  !!" + "*" * 15 + "\n")
            print("Admin Details : ")
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])
        except Exception as e:
            print("\n\t!! Please Provide Valid Inputs !!\n ")
            
            
    def admin_login(self):
        try:
            print( "*" * 18 + f"!!  Welcome To {self.restaurant_name} Restaurant  !!" + "*" * 15 + "\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.admin_details.values())!=0:
                if email==self.admin_email and pas==self.admin_pass:
                    print("\n\t!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("\t1. Add Food Item \n\t2. Edit Food Item\n\t3. View Food Item\n\t4. Delete Food Item\n\t5. Exit\n" + "_" * 72)
                        z=input("Please Select Your Operation : ")
                        if z=="1":
                            self.add_food_item()
                        elif z=="2":
                            self.edit_food_item()
                        elif z=="3":
                            self.view_food_item()
                        elif z=="4":
                            self.delete_food_item()
                        elif z=="5":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no Admin Account with this Email ID !\n\n!! Please register yourself as an admin First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")
            
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs only : "))
            discount=float(input("Enter the discount in Rs only : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
        
        
    def edit_food_item(self):
        try:
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("\t1. Update Food Name\n\t2. Update Quantity\n\t3. Update Price\n\t4. Update Discount\n\t5. Update Stock \n " + "_" * 72)
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")  
            
            
    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")
            

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID :")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
                

                   
        
    def user_register(self):
        try:
            user_name=input("Enter your full name : ")
            phone_no=int(input("Enter your 10 digit phone number : "))
            email=input("Enter your email id : ")
            password=input("Enter your password : ")
            address=input("Enter your address with area PIN code ")
            self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
            print("\n\t!! Your Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restaurant_name} Restaurant\n")
            print("User Details : ")
            for i in self.user_details:
                print(i, ":", self.user_details[i])        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")      
            
               
    def user_login(self):
        try:
            print(f"Welcome TO {self.restaurant_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.user_details.values())!=0:                                                            
                if email==self.user_details["Email_ID"] and pas==self.user_details["Password"]:     
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("\t1. Place New Order\n\t2. Check Order History\n\t3. Update Your Profile Details\n\t4. Exit" + "_" * 72)
                        z=input("Please Select Your Operation : ")
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no User Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  
            
            
    def place_order(self):
        try:
            if len(self.food)!=0:
                print("list of Availabe Food Items :\n"+  "_" * 72)
                menu=[]
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"],self.food[items]["Price"]]) 
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\n\tEnter 1 to Place the Order\n\tEnter 2 to Exit ")
                    x=input("Please Select Your Operation : " + "_" * 72)
                    if x=="1":
                        print("Enter the Food number You want to ordered separated by comma" + "_" * 72)
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                        print("\nList of food item you selected : \n" + "_" * 72)
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")     
                
                
    def ordered_history(self):
        print("\nList of Previous ordered : \n" + "_" * 72)
        for i in self.ordered_item:
            print(i)
            
            
    def update_details(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("\t1. Name\n\t2. Phone number\n\t3. Email ID\n\t4. Password\n\t5. Address\n\t6. Exit\n" +  "_" * 72)
                x=input("Please Select Your Operation : ")
                if x=="1":
                    self.user_details["User Name"]=input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x=="2":
                    self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")      
                elif x=="3":
                    self.user_details["Email_ID"]=input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")
                    
                elif x=="4":
                    self.user_details["Password"]=input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="5":
                    self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")
                    
                if x in ["1","2","3",'4',"5"]:
                    for i in self.user_details:
                        print(i, ":",self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")      
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")
            


try:
    def main():
        obj=Restaurant("Vishal's ")

        
        print("*" * 28 + "FOOD ORDERING SYSTEM" + "*" * 24 + "\n")
        print( "*" * 18 + f"!!  Welcome To {obj.restaurant_name} Restaurant  !!" + "*" * 15 + "\n")
        
        
        while True:
            print("\t1. Admin\n \t2. User\n \t3. Exit\n" + "_" * 72)
            print()
            x=input(("Please Select Your Operation : "))
            if x=="1":
                while True:
                    print("\nEnter the Below Options\n")
                    print("\t1. Register\n\t2. Login\n\t3. Exit\n" + "_" * 72)
                    y=input(("Please Select Your Operation : "))
                    if y=="1":
                        obj.admin_register()
                    elif y=="2":
                        obj.admin_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")
                    
            elif x=="2":
                while True:
                    print("\nEnter the Below Options\n")
                    print("\t1. Register\n\t2. Login\n\t3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("Something went wrong please give input carefully")
             
        
if __name__=='__main__':
    main()


 

