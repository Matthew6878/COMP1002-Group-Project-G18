# A TEAM EFORT BY TEAM 18
# Matthew | Gigi | Aura | Kam kei
# COMP1002 GROUP PROJECT



import datetime 

#Three Initial txt files to store menu and sales information
Menu_data = "menu.txt"
Set_data = "set.txt"
Sales = "sales.txt"
date = datetime.datetime.now()
fname = []
price = []
# Three dictionaries to store the food name,price and sale

price_data = {"Peking Roasted Duck":20,"Kung Pao Chicken": 35,"Sweet and Sour Pork" : 26, "Dim Sum ":15,\
        "Sushi":40,"Sashimi":38,"Unagi - Grilled Eel":25,"Tempura":34,"Soba (Buckwheat Noodles) and Udon (Wheat Noodles)":45,\
        "Paella Valenciana":36,"Patatas bravas":39,"Jamón":52,"Tortilla":45,\
        "Baba Ganoush":67,"Fattoush":68,"Falafel":67,\
        "Coffee (hot)":6,"Coffee (cold)":8,"Soft Drink":6,"Mr.Juice":7,"Pearl milk tea":8,\
        "Sushi +  Pearl milk tea":43,"Kung Pao Chicken +  Soft drink":38,"Patatas bravas + Mr. Juice":40}

price_a = {0:"Peking Roasted Duck",1:"Kung Pao Chicken",2:"Sweet and Sour Pork" ,3: "Dim Sum ",\
        4: "Sushi" ,5:"Sashimi",6: "Unagi - Grilled Eel",7:"Tempura",8:"Soba (Buckwheat Noodles) and Udon (Wheat Noodles)",\
        9: "Paella Valenciana",10: "Patatas bravas",11:"Jamón",12:"Tortilla",\
        13:"Baba Ganoush",14:"Fattoush",15:"Falafel",\
        16:"Coffee (hot)",17:"Coffee (cold)",18:"Soft Drink",19:"Mr.Juice",\
        20:"Pearl milk tea", 21:"Sushi +  Pearl milk tea",22:"Kung Pao Chicken +  Soft drink",23:"Patatas bravas + Mr. Juice"
        }

price_b = {0:20,1: 35,2 : 26, 3:15,\
        4:40,5:38,6:25,7:34,8:45,\
        9:36,10:39,11:52,12:45,\
        13:67,14:68,15:67,\
        16:6,17:8,18:6,19:7,20:8,\
        21:43,22:38,23:40}

num_data = {"Peking Roasted Duck": 0 ,"Kung Pao Chicken":0,"Sweet and Sour Pork" : 0 , "Dim Sum ":0 ,\
        "Sushi":0,"Sashimi":0,"Unagi - Grilled Eel":0 ,"Tempura":0 ,"Soba (Buckwheat Noodles) and Udon (Wheat Noodles)":0,\
        "Paella Valenciana":0,"Patatas bravas":0,"Jamón":0,"Tortilla":0,\
        "Baba Ganoush":0,"Fattoush":0,"Falafel":0,\
        "Coffee (hot)":0,"Coffee (cold)":0,"Soft Drink":0,"Mr.Juice":0,"Pearl milk tea":0,\
        "Sushi +  Pearl milk tea":0,"Kung Pao Chicken +  Soft drink":0,"Patatas bravas + Mr. Juice":0}
order_list= [ ]
order_price = [ ]


def order():
    '''make the order and collect the details for making payment and receipt
       Parameter:
       r (integer) : for user to choose a set or a food item
       reply2 (integer): for user to continue the order or not
       Output:
       what the items are ordered and their prices
       Example:
       what do you need?
Ma Po Tofu              HK$29.00
please confirm the name of food again(e.g Sushi):
Ma Po Tofu                      
please confirm the price again(e.g 45.00):
29.00
Ma Po Tofu              HK$29.00
    '''
    print("Do you want to order a set or not(1 for set, 0 for menu)")
    r = eval(input())
    #validation for user input
    while (r not in {1,0}):
            print("Invalid input. Please input 1 or 0")
            r = eval(input())
    if(r == 1): # separate the order of set and just only the food
        f_set = open("set.txt","r")
        c_set = f_set.read()
        print(c_set)
        f_set.close()
        print("what do you need?")
        ans = input()
        order_list.append(ans)
        print("please confirm the name of food again(e.g Sushi):")
        fname.append(input())
        print("please confirm the price again(e.g 45.00):")
        price.append(input())
        f_set = open("set.txt","r")
        print(ans)
        f_order = open("order.txt", "a")
        f_order.write(date.strftime("%x %X ")) # mark the time for receipt and sales statistics
        f_order.write("  ")
        f_order.write(ans)
        f_order.write("\n")
        f_order.close()
        f_sales = open("sales.txt","a")
        f_sales.write(date.strftime("%x %X "))# mark the time for receipt and sales statistics
        f_sales.write("  ")
        f_sales.write(ans)
        f_sales.write("\n")
        f_sales.close()

        f_set.close()
    elif(r == 0):
        f_set = open("menu.txt","r")
        c_set = f_set.read()
        print(c_set)
        f_set.close()
        print("what do you need?")
        ans = input()
        order_list.append(ans)
        print("please confirm the name of food again(e.g Sushi):")
        fname.append(input())
        print("please confirm the price again(e.g 45.00):")
        price.append(float(input()))
        print(ans)
        f_order = open("order.txt", "a")
        f_order.write(date.strftime("%x %X "))# mark the time for receipt and sales statistics
        f_order.write("   ")
        f_order.write(ans)
        f_order.write("\n")
        f_order.close()
        f_sales = open("sales.txt","a")
        f_sales.write(date.strftime("%x %X "))# mark the time for receipt and sales statistics
        f_sales.write("   ")
        f_sales.write(ans)
        f_sales.write("\n")
        f_sales.close()
            
        f_set.close()
    print("Do you want to order another items?(1 for yes , 0 for no)")
    reply2 = eval(input())
    while (reply2 not in {1,0}):
            print("Invalid input. Please input 1 or 0")
            reply2= eval(input())
    if(reply2 == 1):
        order()
    elif(reply2 == 0):
        change_money()
        
        


def change_money():
     ''' caculate the total price 
         Parameter:
         i (integer): an index to find the items in the price list 
         sum (integer): to sum up the total amount of price
         output:
         Show what items are ordered and the total price
         Example:
          HAPPY YUMMY RESTAURANT              
========================================================
12/01/22 16:24:43    Tortilla                HK$45.00

Total : $ 45.0
     '''
     f_order = open("order.txt", "r")
     print(f_order.read())
     f_order.close()
     i = 0
     sum = 0.00
     
     for i in range(len(price)):
         sum = sum + float(price[i])
         i = i+1
     print("Total : $",sum)
     tempt = "Thankyou  welcome"
     tempt = tempt.center(50)
     f_order= open("order.txt", "a")
     f_order.write("Total : $" + str(sum))
     f_order.write("\n")
     f_order.write(tempt)
     f_order.close()
     payment(sum)

def payment(sum):
    ''' do the payment
        Parameter:
        reply (integer): for user to choose which payment method
        sum (integer): is the total price
        remain (integer) : the remaining money before the payment 
        re (integer): the remaining money after the order
        Output:
        the remaining money after the payment
        Example:
Total : $ 45.0
Which payment do you use?(1:Octopus 2:Payme 3:Credit card)
1
please enter your balance:
300
your balance is  255.0
    '''
    print("Which payment do you use?(1:Octopus 2:Payme 3:Credit card)")
    reply = eval(input())
    if(reply == 1):
      print("please enter your balance:")
      remain = eval(input())
      if(remain < sum):
          print("your balance is insufficient!")
          payment(sum)
      else: 
            re = remain - sum
            print("your balance is ",re)
            receipt()
            
    elif(reply==2):
        print("please enter your balance:")
        remain = eval(input())
        if(remain < sum):
            print("your balance is insufficient!")
            payment(sum)
        else: 
            re = remain - sum
            print("your balance is ",re)
            receipt()
    elif(reply==3):
        print("please enter your balance:")
        remain = eval(input())
        if(remain < sum):
            print("your balance is insufficient!")
            payment(sum)
        else: 
            re = remain - sum
            print("your balance is ",re)
            receipt()
    else: 
        print("your choice is out of range please enter again.")
        payment(sum)



 
def receipt():
    ''' the extra function in this program
        Parameter:
        reply (integer): for user to choose for receiving the receipt or not
        Output:
        print the receipt
        Example:
        Here is the receipt:
              HAPPY YUMMY RESTAURANT              
========================================================
12/01/22 11:53:00    Sashimi                 HK$38.00
Total : $38.0
                Thankyou  welcome                 
    '''
    print("do you need a receipt?(1 for yes, 0 for no)")
    reply = int(input())
    while (reply not in {1,0}):
            print("Invalid input. Please input 1 or 0")
            reply= int(input())
    if(reply == 1):
         print("Here is the receipt:")
         f_order = open("order.txt","r")
         print(f_order.read())
         f_order.close()
         f_order = open("order.txt","r+")
         f_order.truncate(0)
         f_order.close()
    elif(reply == 0):
         print("Thank you welcome")
         f_order = open("order.txt","r+")
         f_order.truncate(0)
         f_order.close()
         quit


     




     
     



def change_menu():
    ''' update the menu and set at the bottom
        Parameter:
        reply (integer) : for user to choose updating the menu or not
        re (integer) : for user to choose updating the menu or set
        a (string) : store the food name 
        b (float) : store the food price
        Output:
        Which item has updated and it will add at the bottom of menu or set 
        for exmaple:
        updated menu:
        Sushi      HK$45.0
    '''
    print("Do you want to change update food name and price ?(1 for update, 0 for no need to update )")
    reply = eval(input())
    while (reply not in {1,0}):
            print("Invalid input. Please input 1 or 0")
            reply = eval(input())
    if reply == 1:
        print("which menu do you want to change? (1 for menu, 0 for set)")
        re = eval(input())
        if(re == 1):
         f_menu = open("menu.txt","r")
         print(f_menu.read())
         f_menu.close()
         
         print("please confirm the food name : ")
         a = input()
         print("please confirm the price : ")
         b = float(input())
         keylist = list(price_a.keys())
         val_list = list(price_a.values())
         position = val_list.index(a)
         price_b[position] = b
         f_menu = open("menu.txt", "a")
         f_menu.write("\nudated menu:\n")
         f_menu.write(str(a)     +"     HK$"+ str(b))
         f_menu.close()
         main()
        elif (re ==0):
           f_set = open("set.txt","r")
           print(f_set.read())
           f_set.close()
           f_set = open("set.txt", "a")
           f_set.write("\nudated menu:\n")
           print("please input the name of food and price:")
           ans = input()
           f_set.write(ans)
           f_set.close()
           print("please confirm the food name by enter it again: ")
           a = str(input())
           print("please confirm the price by enter it again: ")
           b = float(input())
           f_set = open("set.txt", "a")
           f_set.write("udated menu:\n")
           f_set.write(a+"     HK$"+ str(b))
           f_set.close()
           main()
    elif reply == 0 :
           main()



def sales_information():
    '''
A function to check sales information for different day or period.
When user input the date, the program select the relative data from sales.txt file which stored all the orders.

Parameter:
rp: integer; for user to choose when they want to check
d: string; selected date by user (the first day of a period)
e: string; the last day of a period

Return:
All the sales in the selected period of time.
The best and worst sales items and the required number of sales.

For example:
Sales information on 11/10/22 :
11/10/22 10:36:13    Sushi +  Pearl milk tea     	HK$43.00
11/10/22 10:37:12    Sushi +  Pearl milk tea     	HK$43.00
11/10/22 10:37:12    Dim Sum            	HK$15.00
11/10/22 13:33:14    Kung Pao Chicken +  Soft drink    HK$38.00
11/10/22 13:33:14    Mr.Juice                HK$7.00
 
The total sales of 11/10/22 is HK$ 146.0
The best sales item(s): [' Sushi ', '  Pearl milk tea'] and the required number of sales is 2
The worst sales item(s): [' Dim Sum', ' Kung Pao Chicken ', '  Soft drink', ' Mr.Juice'] and the required number of sales is 1
    '''
    sales = [] 
    show = []
    total = []
    year = []
    meal = [] 
    items = [] 
    info = []#a list to store sales of the selected time
    max_list = []#a list to store the best sales items
    min_list = []#a list to store the worst sales items
    count = {} #a dictionary to store the number of sales of each items sold in selected period of time
    income = 0 #to calculate the total income of the selected time
    x = 0 #list index
    ed = 0

    print("when you want to check the sales information(1 for day , 2 for week ,3 for month, 4 for year , 5 for a period")
    rp = eval(input())
    check = open("sales.txt", "r")
    lines = check.readlines()

    for line in lines:
       sales = sales + [line.strip().split()] 
       show = show + [line.strip().split(",")] #split each line of sales.txt into one single list for showing sales information
       total = total + [line.strip().split("HK$")] #separate the price for calculating total income
       year = year + [line.strip().split("/")] #separate the month and day of sales from other information

    while (rp not in {1,2,3,4,5}):
        print("Invalid input. Please input 1, 2, 3, 4 or 5")
        rp = int(input())

    if rp == 1: #checking for specific day
        print("Which day do you want to check? (MM/DD/YY)")
        d = str(input())
        for s in sales:
            if d in s:
                info.append(show[x])
                income = income + eval(total[x][1])
            x = x + 1
            if x >len(sales): #to prevent the list index out of range
                x = 0
        if income == 0:
            print("There is no sales.")
        else:
            print("Sales information on",d,":")
            for o in info:
               for i in o: 
                print(i)
            print(" ")
            print("The total sales of",d,"is HK$",income)
            for i in info:
                for o in i:
                    meal = meal + [o.strip().split("   ")] #separate the whole set or item sold from other information
            for m in meal:
                if len(m) > 1:
                    me = m[1]
                    items = items + [me.split("+")] #separete the items of a set meal
            for item in items: #counting the number of sales of each items
                for i in item:
                    if (i not in count.keys()):
                        count[i] = 1
                    else:
                        count[i] += 1
            for m, n in count.items():
                if n == max(count.values()):
                    max_list.append(m)
                elif n == min(count.values()):
                    min_list.append(m)
            print("The best sales item(s):",max_list,"and the required number of sales is",max(count.values()))
            print("The worst sales item(s):",min_list,"and the required number of sales is",min(count.values())) 

    elif rp == 2:
        print("Please enter the first day of the week that you want to check (MM/DD/YY)")
        d = str(input())
        end = d.split("/")
        day = int(end[1]) + 6 #calulate the last day of the selected week
        e = end[0]+"/"+str(day)+"/"+end[2] #last day of the selaected week in string
        for yr in year:
            if (end[0] == yr[0]) and (int(yr[1]) in range(int(end[1]),day)) and (end[2] == yr[2][:2]):
                info.append(show[x])
                income = income + eval(total[x][1])
            x += 1
        if x >len(sales):
                x = 0
        if income == 0:
            print("There is no sales.")
        else:
            print("Sales information of the month:")
            for o in info:
               for i in o: 
                print(i)
            print(" ")
            print("The total sales of is HK$",income)
            for i in info:
                for o in i:
                    meal = meal + [o.strip().split("   ")]
            for m in meal:
                if len(m) > 1:
                    me = m[1]
                    items = items + [me.split("+")]
            for item in items:
                for i in item:
                    if (i not in count.keys()):
                        count[i] = 1
                    else:
                        count[i] += 1
            for m, n in count.items():
                if n == max(count.values()):
                    max_list.append(m)
                elif n == min(count.values()):
                    min_list.append(m)
            print("The best sales item(s):",max_list,"and the required number of sales is",max(count.values()))
            print("The worst sales item(s):",min_list,"and the required number of sales is",min(count.values())) 


    elif rp == 3:
        print("Which month do you want to check?(MM)")
        d = str(input())
        for s in year:
            if d == s[0]: #s[0] is the location of month data
                info.append(show[x])
                income = income + eval(total[x][1])
            x = x + 1
            if x >len(sales):
                x = 0
        if income == 0:
            print("There is no sales.")
        else:
            print("Sales information of the month:")
            for o in info:
               for i in o: 
                print(i)
            print(" ")
            print("The total sales of is HK$",income)
            for i in info:
                for o in i:
                    meal = meal + [o.strip().split("   ")]
            for m in meal:
                if len(m) > 1:
                    me = m[1]
                    items = items + [me.split("+")]
            for item in items:
                for i in item:
                    if (i not in count.keys()):
                        count[i] = 1
                    else:
                        count[i] += 1
            for m, n in count.items():
                if n == max(count.values()):
                    max_list.append(m)
                elif n == min(count.values()):
                    min_list.append(m)
            print("The best sales item(s):",max_list,"and the required number of sales is",max(count.values()))
            print("The worst sales item(s):",min_list,"and the required number of sales is",min(count.values())) 

    elif rp ==4:
        print("Which year do you want to check?(YY)")
        d = str(input())
        for yr in year:
            if len(yr) > 1:
                if d == yr[2][:2]: #comparing d with the first two characters from yr[2] which is year
                    info.append(show[x])
                    income = income + eval(total[x][1])
            x = x + 1
            if x >len(sales):
                x = 0
        if income == 0:
            print("There is no sales.")
        else:
            print("Sales information of the year:")
            for o in info:
               for i in o: 
                print(i)
            print(" ")
            print("The total sales of is HK$",income)
            for i in info:
                for o in i:
                    meal = meal + [o.strip().split("   ")]
            for m in meal:
                if len(m) > 1:
                    me = m[1]
                    items = items + [me.split("+")]
            for item in items:
                for i in item:
                    if (i not in count.keys()):
                        count[i] = 1
                    else:
                        count[i] += 1
            print("The best sales item is",max(count.keys()),"and the required number of sales is",max(count.values()))
            print("The worst sales item is",min(count.keys()),"and the required number of sales is",min(count.values())) 

    elif rp == 5:
        print("Please enter the first day of the period that you want to check (MM/DD/YY)")
        d = str(input())
        print("Please enter the last day of the period that you want to check (MM/DD/YY)")
        e = str(input())
        for s in sales: #finding the list index for the first day of the selected period
            x += 1
            if len(s) > 1:
                if d == s[0]:
                    break
        for s in sales: #finding the list index for the last day of the selected period
            ed += 1
            if len(s) > 1:
                if e == s[0]:
                    break
        info.append(show[(x-1):ed]) 
        for t in total[(x-1):ed]:
            if len(t) > 1:
                income = income + eval(t[1])
        if income == 0:
            print("There is no sales.")
        else:
            print("Sales information of the year:")
            for o in info:
               for i in o:
                   for z in i:
                        meal = meal + [z.strip().split("   ")]
                        print(z)
            print(" ")
            print("The total sales of is HK$",income)
            for m in meal:
                if len(m) > 1:
                    me = m[1]
                    items = items + [me.split("+")]
            for item in items:
                for i in item:
                    if (i not in count.keys()):
                        count[i] = 1
                    else:
                        count[i] += 1
            for m, n in count.items():
                if n == max(count.values()):
                    max_list.append(m)
                elif n == min(count.values()):
                    min_list.append(m)
            print("The best sales item(s):",max_list,"and the required number of sales is",max(count.values()))
            print("The worst sales item(s):",min_list,"and the required number of sales is",min(count.values())) 

    main()


def sale_number():
    '''
A function to show sales number
Parameter:
r: integer; for user to choose best or worst sales
Return:
The best or worst sales of meal set(s) and the required number of sales.

For example:
The best sales of meal set(s): ['Sushi +  Pearl milk tea']
The required number of sales is 9
    '''
    max_list = []
    min_list = []
    c = []
    print("Which sales information do you want to check?(1 for the best sales of meal set , 0 for the worst sales of meal set)")
    r = eval(input())
    while (r not in {1,0}):
            print("Invalid input. Please input 1 or 0")
            r = int(input())
    f = open("sales.txt" , "r")
    for line in f:
        c = c + [line.strip().split("    ")]
    for cc in c:
        if len(cc) > 1:
            if cc[1] in price_data:
                list1 = cc[1]
                list1 = list1.split("    ")
                num_data[list1[0]]= num_data.get(list1[0]) + 1
    if (r == 1):
        for m, n in num_data.items():
            if n == max(num_data.values()):
                max_list.append(m)
        print("The best sales of meal set(s):",max_list)
        print("The required number of sales is",max(num_data.values()))
    if (r == 0):
        for m, n in num_data.items():
            if n == min(num_data.values()):
                min_list.append(m)
        print("The worst sales of meal set(s):",min_list)
        print("The required number of sales is",min(num_data.values()))
    main()

#Menu Printing functions
def mainMenu():
    print("\n   -------------------------------\n")
    print("    Welcome to Yummy Restaurant\n    --- A Project by Team 18 --- \n\n--------------------------------------\n")
    print("1 - order\n2 - update menu\n3 - check the best and least sales of meal sets\n4 - check Sales information\n5 - quit")


def main():
    '''The starting point of this function 
       for example:
       Welcome to Yummy Restaurant
    --- A Project by Team 18 --- 

--------------------------------------

1 - order
2 - update menu
3 - check the best and least sales of meal sets
4 - check Sales information
5 - quit
    '''
    mainMenu()
    usersystem = int(input("Option: "))
    while (usersystem>5 or usersystem<1):
        print("\n   Input is out of range\nPlease Choose 1,2,3,4 or 5 only!")
        usersystem = int(input("Option: "))

    if usersystem == 1:
        store_name = "HAPPY YUMMY RESTAURANT"
        store_name = store_name.center(50)
        f_order = open("order.txt", "a")
        f_order.write(store_name)
        f_order.write("\n")
        f_order.write("========================================================\n")
        f_order.close()
        order()

        

    elif usersystem == 2:
        change_menu()
    elif usersystem == 3:
        sale_number()
    elif usersystem == 4:
        sales_information()
    elif usersystem == 5:
        print("welcome")
        quit()

main()

'''
reference list :

read and write file
https://www.geeksforgeeks.org/reading-writing-text-files-python/

keys and values in dictionary
https://www.askpython.com/python/dictionary/how-to-update-a-python-dictionary

center function
https://www.w3schools.com/python/ref_string_center.asp

docstrings
https://www.programiz.com/python-programming/docstrings

truncate function
https://www.pythonforbeginners.com/basics/how-to-clear-a-text-file-in-python





'''
