# Developed by Hyper Vare(https://hypervare.com)
import datetime

class cars:
    def __init__(self, brand, model, rent_hrs, rent_daily, rent_week, in_stock):
        self.brand = brand
        self.model = model
        self.rent_hrs = rent_hrs
        self.rent_daily = rent_daily
        self.rent_week = rent_week
        self.in_stock = in_stock
        def car(brand, model, rent_hrs, rent_daily, rent_week, in_stock):

            try:
                ID_file = open("last_car_ID.txt", "r")
                car_ID = int(ID_file.read())
                car_ID += 1
                ID_file.close()
            except:
                ID_file = open("last_car_ID.txt", "w")
                car_ID = 0000
                ID_file.write(str(car_ID))
                ID_file.close()

            file = open("cars_detail.txt", "a")
            cardata = [str(car_ID)+" ", brand+" ", model+" ", str(rent_hrs)+" ", str(rent_daily)+" ", str(rent_week)+" ", str(in_stock)+" ", "\n"]
            ID_file = open("last_car_ID.txt", "w")
            ID_file.write(str(car_ID))
            ID_file.close()
            file.writelines(cardata)
            file.close()

        car(self.brand, self.model, self.rent_hrs, self.rent_daily, self.rent_week, self.in_stock)

class customers:
    def __init__(self, name, age, date, time, return_data, rent_pay, rent_car_id):
        self.name = name
        self.age = age
        self.date = date
        self.time = time
        self.return_data = return_data
        self.rent_pay = rent_pay
        self.rent_car_id = rent_car_id

        def user_data_creator(name, age, date, time, return_data, rent_pay, rent_car_id):

            try:
                ID_file1 = open("last_user_ID.txt", "r")
                user_ID = int(ID_file1.read())
                user_ID += 1
                ID_file1.close()
            except:
                ID_file1 = open("last_user_ID.txt", "w")
                user_ID = 0000
                ID_file1.write(str(user_ID))
                ID_file1.close()

            file = open("users_detail.txt", "a")
            def car_stock(id):
                ID_File = open("cars_detail.txt", "r")
                detail_list = ID_File.readlines()
                filter_list = []
                for i in range(len(detail_list)):
                    single_detail = detail_list[i]
                    single_detail.replace(" \n", "")
                    filter_list.append(single_detail.split())

                for j in range(len(filter_list)):
                    if id == filter_list[j][0]:
                        if int(filter_list[j][6]) > 0:
                            minus_stock = int(filter_list[j][6]) - 1
                            detail_list[int(id)] = str(id)+" "+filter_list[j][1]+" "+filter_list[j][2]+" "+filter_list[j][3]+" "+filter_list[j][4]+" "+filter_list[j][5]+" "+str(minus_stock)+" "+"\n"
                            file = open("cars_detail.txt", "w")
                            file.writelines(detail_list)
                            file.close()
                        else:
                            print("Out of Stock.")
                    else:
                        pass
            userdata = [str(user_ID)+" ", name+" ", age+" ", date+" ", time+' ', return_data+' ', str(rent_pay)+' ', rent_car_id+" ", "\n"]
            file.writelines(userdata)
            ID_file1 = open("last_user_ID.txt", "w")
            ID_file1.write(str(user_ID))
            ID_file1.close()
            car_stock(rent_car_id)
            file.close()


        user_data_creator(self.name, self.age, self.date, self.time, self.return_data, self.rent_pay, self.rent_car_id)


class bills:
    def __init__(self, user_name, car_brand_, car_model_, user_hold_data, user_last_pay, user_total_pay, due_payment, stock_car_id):
        self.user_name = user_name
        self.car_brand_ = car_brand_
        self.car_model_ = car_model_
        self.user_hold_data = user_hold_data
        self.user_last_pay = user_last_pay
        self.user_total_pay = user_total_pay
        self.due_payment = due_payment
        def bill(user_name_bill, car_brand_bill, car_model_bill, user_hold_data_bill, user_last_pay_bill, user_total_pay_bill, due_payment_bill, stock_car):
            try:
                ID_file = open("last_bill_ID.txt", "r")
                bill_ID = int(ID_file.read())
                bill_ID += 1
                ID_file.close()
            except:
                ID_file = open("last_bill_ID.txt", "w")
                bill_ID = 0000
                ID_file.write(str(bill_ID))
                ID_file.close()
            def car_stock(id):
                ID_File = open("cars_detail.txt", "r")
                detail_list = ID_File.readlines()
                filter_list = []
                for i in range(len(detail_list)):
                    single_detail = detail_list[i]
                    single_detail.replace(" \n", "")
                    filter_list.append(single_detail.split())

                for j in range(len(filter_list)):
                    if id == filter_list[j][0]:
                        if int(filter_list[j][6]) > 0:
                            add_stock = int(filter_list[j][6]) + 1
                            detail_list[int(id)] = str(id)+" "+filter_list[j][1]+" "+filter_list[j][2]+" "+filter_list[j][3]+" "+filter_list[j][4]+" "+filter_list[j][5]+" "+str(add_stock)+" "+"\n"
                            file = open("cars_detail.txt", "w")
                            file.writelines(detail_list)
                            file.close()
                        else:
                            print("Out of Stock.")
                    else:
                        pass
            file = open("bills_detail.txt", "a")
            billdata = [str(bill_ID)+" ", user_name_bill+" ", car_brand_bill+" ", car_model_bill+" ", user_hold_data_bill+" ", user_last_pay_bill+" ", user_total_pay_bill+" ", due_payment_bill+" ", "\n"]
            file.writelines(billdata)
            ID_file = open("last_bill_ID.txt", "w")
            ID_file.write(str(bill_ID))
            ID_file.close()
            car_stock(stock_car)
            file.close()

        bill(self.user_name, self.car_brand_, self.car_model_, self.user_hold_data, self.user_last_pay, self.user_total_pay, self.due_payment, stock_car_id)


car_brands_list = ["", "Audi", "Rolls Royce", "TATA", "Mahindra", "Maserati", "Honda", "Lamborghini", "KIA", "Ferrai", "BMW", "Land Rover", "Ford", "Volvo", "Pagani", "Aston Martin", "Nissan", "Toyota", "Hyundai", "Volkswagen", "Jeep"]
# No changes in above lines, they are fixed.

def holding_data():
    print("\nFor Hours Press(H).")
    print("For Days Press(D).")
    print("For Weeks Press(W).")
    hold_data = input("Enter Here: ")
    if hold_data == "H" or hold_data == "h":
        rent_data = input("For How Many Hours: ")
        if rent_data == "" or rent_data == " ":
            rent_data = "1-hrs"
            return rent_data
        else:
            rent_data += "-hrs"
            return rent_data
    elif hold_data == "D" or hold_data == "d":
        rent_data = input("For How Many Days: ")
        if rent_data == "" or rent_data == " ":
            rent_data = "1-dys"
            return rent_data
        else:
            rent_data += "-dys"
            return rent_data
    elif hold_data == "W" or hold_data == "w":
        rent_data = input("For How Many Weeks: ")
        if rent_data == "" or rent_data == " ":
            rent_data = "1-wks"
            return rent_data
        else:
            rent_data += "-wks"
            return rent_data
    else:
        print("!!!!! Invalid Entry !!!!!")
        holding_data()

def integerFilter():
    rent = input("Enter Its Rent: ")
    rent = rent.replace(",", "")
    try:
        rent = int(rent)
        return rent
    except:
        if (rent == "") or (rent == " "):
            rent = 0
            return rent
        else:
            print("!!!!!!!!!! Invalid Entry !!!!!!!!!!")
            integerFilter()

def users_detail_presenter():
    ID_File = open("users_detail.txt", "r")
    detail_list = ID_File.readlines()
    print("\nUsers We Have:-")
    for i in range(len(detail_list)):
        single_detail = detail_list[i]
        single_detail.replace(" \n", "")
        print(single_detail.split())
    sel_user = input("Enter User's ID: ")
    return sel_user

def cars_detail_presenter():
    ID_File = open("cars_detail.txt", "r")
    detail_list = ID_File.readlines()
    print("\nCars We Have:-")
    for i in range(len(detail_list)):
        single_detail = detail_list[i]
        single_detail.replace(" \n", "")
        print(single_detail.split())
    sel_car = input("Enter Car's ID: ")
    return sel_car

# execution of code starts from here.
print("\n")
print("##### Admin Panel #####")

def main():

# Multihandler function.

    def data_manager():

        # single functions

        def detail_changer(ind, id):
            ID_File = open("cars_detail.txt", "r")
            dataToChange = ID_File.readlines()
            print("\nCar Brands:-")
            for i in range(1, len(car_brands_list)):
                print(str(i)+".", car_brands_list[i])
            print("\n")
            brand_index = input("Enter Brand No: ")
            try:
                brand = car_brands_list[int(brand_index)]
            except:
                if (brand_index == "") or (brand_index == " "):
                    brand = car_brands_list[0]
                elif brand_index == "close":
                    exit()
                elif brand_index == "back":
                    data_manager()
                elif brand_index == "exit":
                    main()
                else:
                    print("!!!!!!!!!! Invalid Entry !!!!!!!!!!")
                    data_manager()
            model = input("Enter Brand's Model: ")
            print("Hourly Rent")
            rent_hrs = integerFilter()
            print("Daily Rent")
            rent_daily = integerFilter()
            print("Weekly Rent")
            rent_week = integerFilter()
            in_stock = input("Enter Car's Stock: ")
            dataToChange[ind] = str(id)+" "+brand+" "+model+" "+str(rent_hrs)+" "+str(rent_daily)+" "+str(rent_week)+" "+str(in_stock)+" "+"\n"
            file = open("cars_detail.txt", "w")
            file.writelines(dataToChange)
            file.close()

        def car_data(id):
            ID_File = open("cars_detail.txt", "r")
            detail_list = ID_File.readlines()
            ID = ""
            filter_list = []
            for i in range(len(detail_list)):
                single_detail = detail_list[i]
                single_detail.replace(" \n", "")
                filter_list.append(single_detail.split())

            for j in range(len(filter_list)):
                if id == filter_list[j][0]:
                    detail_changer(j, id)
            else:
                print("Data Not Found.")
                ID = input("\nEnter Car's ID: ")
                car_data(ID)

        # part of data manager
        print("\nTo Manage Cars Data Press(C).")
        print("To Manage Users Data Press(U).")
        admin_manage = input("Enter your Key: ")
        if admin_manage == "c" or admin_manage == "C":
            print("\nTo Enter New Car's Data Press(N).\nTo Update Existing Car's Data Press(U).\nTo Delete Car's Data Press(D).\n")
            admin_work = input("Enter Your Key: ")
            while(True):
                if admin_work == "n" or admin_work == "N":
                    print("\nCar Brands:-")
                    for i in range(1, len(car_brands_list)):
                        print(str(i)+".", car_brands_list[i])
                    print("\n")
                    brand_index = input("Enter Brand No: ")
                    try:
                        brand = car_brands_list[int(brand_index)]
                    except:
                        if (brand_index == "") or (brand_index == " "):
                            brand = car_brands_list[0]
                        else:
                            print("!!!!!!!!!! Invalid Entry !!!!!!!!!!")
                            data_manager()
                    model = input("Enter Brand's Model: ")
                    print("Hourly Rent")
                    rent_hrs = integerFilter()
                    print("Daily Rent")
                    rent_daily = integerFilter()
                    print("Weekly Rent")
                    rent_week = integerFilter()
                    in_stock = input("Enter Car's Stock: ")
                    if (brand and model != "") or (brand and model != " "):
                        cars(brand, model, rent_hrs, rent_daily, rent_week, in_stock)
                    elif brand_index == "close":
                        exit()
                    elif brand_index == "back":
                        data_manager()
                    elif brand_index == "exit":
                        main()
                    else:
                        print("!!!!! Invaild Entry !!!!!")
                        data_manager()
                elif admin_work == "u" or admin_work == "U":
                    ID = input("\nEnter Car's ID: ")
                    car_data(ID)
                elif admin_work == "d" or admin_work == "D":
                    print("Delete Data")
                    exit()
                elif admin_work == "back":
                    data_manager()
                elif admin_work == "exit":
                    main()
                elif admin_work == "close":
                    exit()
                else:
                    print("!!!!!! Invalid Key Pressed. !!!!!!")
                    data_manager()
        elif admin_manage == "u" or admin_manage == "U":
            def rent_manager():
                def detail_changer(ind, id):
                    ID_File = open("users_detail.txt", "r")
                    dataToChange = ID_File.readlines()
                    name = input("Enter Customer's Name: ")
                    age = input("Enter Customer's Age: ")
                    tempdate = datetime.datetime.now()
                    date = tempdate.strftime("%x")
                    temptime = datetime.datetime.now()
                    time = temptime.strftime("%I:%M:%p")
                    return_data = holding_data()
                    rent_car_id = cars_detail_presenter()
                    rent_pay = integerFilter()
                    dataToChange[ind] = str(id)+" "+name+" "+age+" "+date+" "+time+' '+return_data+' '+str(rent_pay)+' '+rent_car_id+" "+"\n"
                    file = open("users_detail.txt", "w")
                    file.writelines(dataToChange)
                    file.close()

                def user_id(id):
                    ID_File = open("users_detail.txt", "r")
                    detail_list = ID_File.readlines()
                    ID = ""
                    filter_list = []
                    for i in range(len(detail_list)):
                        single_detail = detail_list[i]
                        single_detail.replace(" \n", "")
                        filter_list.append(single_detail.split())

                    for j in range(len(filter_list)):
                        if id == filter_list[j][0]:
                            detail_changer(j, id)
                    else:
                        print("Data Not Found.")
                        ID = input("\nEnter User's ID: ")
                        user_id(ID)

                print("\n")
                print("To Enter New User's Data Press(N).")
                print("To Enter Upadte User's Data Press(U).")
                print("To Enter Delete User's Data press(D).")
                _ = input("Enter Here: ")
                if _ == 'n' or _  == 'N':
                    name = input("Enter Customer's Name: ")
                    age = input("Enter Customer's Age: ")
                    tempdate = datetime.datetime.now()
                    date = tempdate.strftime("%x")
                    temptime = datetime.datetime.now()
                    time = temptime.strftime("%I:%M:%p")
                    return_data = holding_data()
                    rent_car_id = cars_detail_presenter()
                    rent_pay = integerFilter()
                    customers(name, age, date, time, return_data, rent_pay, rent_car_id)
                elif _ == 'u' or _ == 'U':
                    ID = input("\nEnter User's ID: ")
                    user_id(ID)
                elif _ == 'd' or _ == 'D':
                    pass
                else:
                    print("!!!!! Invalid Entry !!!!!")
                    rent_manager()
            rent_manager()
        elif admin_manage == "close":
            exit()
        elif admin_manage == "back":
            main()
        elif admin_manage == "exit":
            main()
        else:
            print("!!!!!! Invalid Key Pressed. !!!!!!")
            data_manager()

    # part of rent manager
    def rent_manager():

        def detail_changer(ind, id):
            ID_File = open("users_detail.txt", "r")
            dataToChange = ID_File.readlines()
            name = input("Enter Customer's Name: ")
            age = input("Enter Customer's Age: ")
            tempdate = datetime.datetime.now()
            date = tempdate.strftime("%x")
            temptime = datetime.datetime.now()
            time = temptime.strftime("%I:%M:%p")
            return_data = holding_data()
            rent_car_id = cars_detail_presenter()
            rent_pay = integerFilter()
            dataToChange[ind] = str(id)+" "+name+" "+age+" "+date+" "+time+' '+return_data+' '+str(rent_pay)+' '+rent_car_id+" "+"\n"
            file = open("users_detail.txt", "w")
            file.writelines(dataToChange)
            file.close()

        def user_id(id):
            ID_File = open("users_detail.txt", "r")
            detail_list = ID_File.readlines()
            ID = ""
            filter_list = []
            for i in range(len(detail_list)):
                single_detail = detail_list[i]
                single_detail.replace(" \n", "")
                filter_list.append(single_detail.split())

            for j in range(len(filter_list)):
                if id == filter_list[j][0]:
                    detail_changer(j, id)
            else:
                print("Data Not Found.")
                ID = input("\nEnter User's ID: ")
                user_id(ID)

        print("\n")
        print("To Enter New User's Data Press(N).")
        print("To Enter Upadte User's Data Press(U).")
        print("To Enter Delete User's Data press(D).")
        _ = input("Enter Here: ")
        if _ == 'n' or _  == 'N':
            name = input("Enter Customer's Name: ")
            age = input("Enter Customer's Age: ")
            tempdate = datetime.datetime.now()
            date = tempdate.strftime("%x")
            temptime = datetime.datetime.now()
            time = temptime.strftime("%I:%M:%p")
            return_data = holding_data()
            rent_car_id = cars_detail_presenter()
            rent_pay = integerFilter()
            customers(name, age, date, time, return_data, rent_pay, rent_car_id)
        elif _ == 'u' or _ == 'U':
            ID = input("\nEnter User's ID: ")
            user_id(ID)
        elif _ == 'd' or _ == 'D':
            pass
        else:
            print("!!!!! Invalid Entry !!!!!")
            rent_manager()


    def bill_manager():
        def bill_generator():
            _id_ = users_detail_presenter()
            user_file = open("users_detail.txt", "r")
            user_detail = user_file.readlines()
            car_file = open("cars_detail.txt", "r")
            car_detail = car_file.readlines()
            due_payment = ""
            user_name = ''
            car_brand_ = ''
            car_model_ = ''
            user_hold_data = ''
            user_last_pay = ''
            user_total_pay = ''
            stock_car_id = ''
            for i in range(len(user_detail)):
                p = user_detail[i].split()
                if p[0] == _id_:
                    user_hold_data += p[6]
                    check_t = p[6].split("-")
                    t_num = check_t[0]
                    t_char = check_t[1]
                    if t_char == 'hrs':
                        car_id_check = p[8]
                        stock_car_id += car_id_check
                        user_name += p[1]+" "+p[2]
                        for j in range(len(car_detail)):
                            q = car_detail[j].split()
                            if car_id_check == q[0]:
                                car_brand_ += q[1]
                                car_model_ += q[2]
                                total_pay = int(q[3]) * int(t_num)
                                user_total_pay += str(total_pay)
                                user_last_pay += p[7]
                                due_pay = (total_pay - int(p[7]))
                                if due_pay > 0:
                                    due_payment += str(due_pay)
                                else:
                                    due_payment += "No Dues"
                    elif t_char == 'dys':
                        car_id_check = p[8]
                        stock_car_id += car_id_check
                        user_name += p[1]+" "+p[2]
                        for j in range(len(car_detail)):
                            q = car_detail[j].split()
                            if car_id_check == q[0]:
                                car_brand_ += q[1]
                                car_model_ += q[2]
                                total_pay = int(q[4]) * int(t_num)
                                user_total_pay += str(total_pay)
                                user_last_pay += p[7]
                                due_pay = (total_pay - int(p[7]))
                                if due_pay > 0:
                                    due_payment += str(due_pay)
                                else:
                                    due_payment += "No Dues"
                    elif t_char == 'wks':
                        car_id_check = p[8]
                        stock_car_id += car_id_check
                        user_name += p[1]+" "+p[2]
                        for j in range(len(car_detail)):
                            q = car_detail[j].split()
                            if car_id_check == q[0]:
                                car_brand_ += q[1]
                                car_model_ += q[2]
                                total_pay = int(q[5]) * int(t_num)
                                user_total_pay += str(total_pay)
                                user_last_pay += p[7]
                                due_pay = (total_pay - int(p[7]))
                                if due_pay > 0:
                                    due_payment += str(due_pay)
                                else:
                                    due_payment += "No Dues"
                    else:
                        print("Invalid Data")
            def duplicate_bill_matcher(_user_name_, _car_brand_, _car_model_, _user_hold_data_, _user_last_pay_, _user_total_pay_, _due_payment_):
                _bill_file_ = open("bills_detail.txt")
                m = _bill_file_.readlines()
                al = 0
                for i in range(len(m)):
                    single_m = m[i].split()
                    if _user_name_ == str(single_m[1]+" "+single_m[2]) and _car_brand_ == single_m[3] and _car_model_ == single_m[4] and _user_hold_data_ == single_m[5] and _user_last_pay_ == single_m[6] and _user_total_pay_ == single_m[7] and _due_payment_ == single_m[8]:
                        al += 1
                        break
                    else:
                        pass
                if al > 0:
                    print("Already Generated.\n")
                    print(user_name, car_brand_, car_model_, user_hold_data, user_last_pay, user_total_pay, due_payment)
                else:
                    print(user_name, car_brand_, car_model_, user_hold_data, user_last_pay, user_total_pay, due_payment, "\n")
                    bills(user_name, car_brand_, car_model_, user_hold_data, user_last_pay, user_total_pay, due_payment, stock_car_id)
                    print("Successfully Created.")
            duplicate_bill_matcher(user_name, car_brand_, car_model_, user_hold_data, user_last_pay, user_total_pay, due_payment)

        print("\nTo Generate Bill Press(G): ")
        print("To Print Bill Press(P): ")
        work = input("Enter Here: ")
        if work == 'G' or work == 'g':
            bill_generator()
        elif work == "p" or work == "P":
            id_bill = input("Enter Bill ID: ")
            def bill_printer(bill_id):
                try:
                    bills_detail_file = open("bills_detail.txt", "r")
                    b = bills_detail_file.readlines()
                    for i in range(len(b)):
                        bill_id_checker = b[i].split()
                        if bill_id_checker[0] == bill_id:
                            print(b[i])
                except:
                    print("No Bill Data Found.")
            bill_printer(id_bill)
        else:
            print("!!!!! Invaild Entry !!!!!")
            bill_manager()

# part of mainx
    print("\n")
    print("To Access Data Manager Press(D).")
    print("To Access Rent Manager Press(R).")
    print("To Access Bill Manager Press(B).")
    admin_work = input("Enter Your Key: ")
    if admin_work == "D" or admin_work == "d":
        data_manager()
    elif admin_work == "R" or admin_work == "r":
        rent_manager()
    elif admin_work == "B" or admin_work == "b":
        bill_manager()
    elif admin_work == "close":
        exit()
    elif admin_work == "back":
        main()
    elif admin_work == "exit":
        exit()
    else:
        print("!!!!!! Invalid Entry !!!!!!")
        main()

if __name__ ==  "__main__":
    main()
