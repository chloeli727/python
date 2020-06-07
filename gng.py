#!/usr/bin/env python3

import psycopg2

if_total = 0
of_total = 0

def main():
    dbconn = psycopg2.connect(host='studsql.csc.uvic.ca', user='paraguay', password='9MM|QscGV4')
    cursor = dbconn.cursor()

    global if_total
    global of_total
    
    print("""Please select what would you like to do, press a number between 1-5:
    1: Get some basic information about GnG through 10 queries
    2: Setting up a campaign with volunteers, activities, etc.
    3: Get some accounting information
    4: Membership history
    5: Look at the existing attributs in a specific table
    """)
    while True:
        ch = input("Please enter your choice of selection: ")
        try:
            choice = int(ch)
            if choice < 1 or choice > 5:
                print("Invalid input!")
                print("Please enter a number from 1-5")
                continue
        except ValueError:
            print("Invalid input!")
            print("Please enter a number from 1-5")
            continue
        else:
            break

    if choice == 1:
        print("""Enter a query number from 1-10:
    1. List the fund number, name of the funder, and the date of fundraising that
    a funder donated between $100 and $2000 during fundraising.
    2. List the campaign ID, city of campaign, and length of campaign(in weeks) that
    the employee who is in charge of the campaign is a salaried employee.
    3. List the name of the funder and payment method who donated more than $50 and
    use the same payment method as other funders whose name is May and donated less
    than 200 during fundraising.
    4. List all the information on website that will take place in Victoria.
    5. List campaign ID, status of campaign, manager's first name, and manager's last
    name on website for campaigns on the same date, but with different status.
    6. List the cost and length(in weeks) of campaign for campaigns that have the longest
    length.
    7. List the date on website and date for fundraising that the payment method during 
    fundraising is Visa.
    8. List date of fundraising, name of funder, amount, payment method when funder name
    is the same as a donor name.
    9. Find how many people donated by cheque during fundraising events.
    10. Find the average cost of all campaigns.
    """)
        while True:
            ans = input("Please enter a query number from 1-10: ")
            try:
                val = int(ans)
                if val < 1 or val > 10:
                    print("Invalid input!")
                    print("Please enter a number from 1-10")
                    continue
            except ValueError:
                print("Invalid input!")
                print("Please enter a number from 1-10")
                continue
            else:
                break
            
        query1 = "SELECT * FROM q1"
        query2 = "SELECT * FROM q2"
        query3 = "SELECT * FROM q3"
        query4 = "SELECT * FROM q4"
        query5 = "SELECT * FROM q5"
        query6 = "SELECT * FROM q6"
        query7 = "SELECT * FROM q7"
        query8 = "SELECT * FROM q8"
        query9 = "SELECT * FROM q9"
        query10 = "SELECT * FROM q10"

        if val == 1:
            cursor.execute(query1)
        elif val == 2:
            cursor.execute(query2)
        elif val == 3:
            cursor.execute(query3)
        elif val == 4:
            cursor.execute(query4)
        elif val == 5:
            cursor.execute(query5)
        elif val == 6:
            cursor.execute(query6)
        elif val == 7:
            cursor.execute(query7)
        elif val == 8:
            cursor.execute(query8)
        elif val == 9:
            cursor.execute(query9)
        elif val == 10:
            cursor.execute(query10)
       
        result = cursor.fetchall()
        for row in result:
            for col in row:
                    print(col, end='  ')
            print()

    elif choice == 2:
        while True:
            print("1: Add new volunteers to the organization.")
            print("2: Scheduling events.")
            print("3: Look at an campaign's status")
            ph2_1 = input("Press 1, 2, or 3 to modify the campaigns:")
            try:
                ph2_2 = int(ph2_1)
                if ph2_2 !=1 and ph2_2 !=2 and ph2_2 !=3:
                    print("1: Add new volunteers to the organization.")
                    print("2: Scheduling events.")
                    print("3: Look at an campaign's status")
                    print("Press 1, 2, or 3 to modify the campaigns:")
                    continue
            except ValueError:
                print("1: Add new volunteers to the organization.")
                print("2: Scheduling events.")
                print("3: Look at an campaign's status")
                print("Press 1, 2, or 3 to modify the campaigns:")
                continue
            else:
                ph2_2 = int(ph2_1)
                break

        if ph2_2 == 1:
            get_max_id = cursor.execute("SELECT max(empid) FROM employee")
            max_id = cursor.fetchall()
            for i in max_id:
                init_empID = i[0]
            init_empID += 1
                    
                    
            count_e = 0
            e1 = 1

            while e1 != 0:
                lastname = input("Enter employee's last name: ")
                firstname = input("Enter employee's first name: ")
                eType = input("Enter employee's type(must choose one in between: Volunteer2, Volunteer3, Salaried): ")
                eventHrs = input("Enter total hours for a event: ")
                        
                insert_query1 = (
                    "INSERT INTO employee(empID, lastname, firstname, eType, eventHrs)"
                    "VALUES (%s,%s,%s,%s,%s)"
                )
                insert_record1 = (init_empID, lastname, firstname, eType, eventHrs)
                cursor.execute(insert_query1, insert_record1)
                init_empID += 1
                dbconn.commit()
                count_e += 1
                    
                e2 = input("Press 0 to exit, press anything to continue: ")
                try:
                    e1 = int(e2)
                    if e1 == 0:
                        break
                    else:
                        continue
                except ValueError:
                    continue
            
            print(count_e, "employee(s) have added")

        elif ph2_2 == 2:
            get_min_cid = cursor.execute("SELECT min(campid) FROM website")
            min_cid = cursor.fetchall()
            for j in min_cid:
                init_campID = j[0]
            init_campID += 1
            init_status = 'phrase1'
            count_c = 0
            c1 = 1

            while c1 != 0:
                c_date = input("Enter a date of a campaign(ex. YYYYMMDD): ")
                m_first = input("Enter manager's first name who is in charge of the campaign: ")
                m_last = input("Enter manager's last name who is in charge of the campaign: ")
                insert_query2 = (
                    "INSERT INTO website(campid, date, status, manager_firstname, manager_lastname)"
                    "VALUES (%s,%s,%s,%s,%s)"
                )
                insert_record2 = (init_campID, c_date, init_status, m_first, m_last)
                cursor.execute(insert_query2, insert_record2)
                init_campID += 1
                dbconn.commit()
                count_c += 1

                c2 = input("Press 0 to exit, press anything to continue: ")
                try:
                    c1 = int(c2)
                    if c1 == 0:
                        break
                    else:
                        continue
                except ValueError:
                    continue
            
            print(count_c, "campaign(s) have added")

        elif ph2_2 == 3:
            while True:
                c_id = input("Enter an campID of an campaign: ")
                try:
                    c_id2 = int(c_id)
                except ValueError:
                    print("Please enter an campID!")
                    continue
                else:
                    c_id2 = int(c_id)
                    break
            get_status = "SELECT status from website where campid=%s"
            c_id3 = (c_id2,)
            cursor.execute(get_status, c_id3)
            get_status2 = cursor.fetchall()
            if not get_status2:
                print("The campid is not exist.")
            else:
                print(get_status2[0][0])
        

    elif choice == 3:
        
        in_f = cursor.execute("SELECT date, amount from fundraising")
        inf_table = cursor.fetchall()
        print("  date | amount")
        print("----------------")
        for row in inf_table:
            for col in row:
                    print(col, end='  ')
            print()

        ift = cursor.execute("SELECT amount FROM fundraising")
        ift2 = cursor.fetchall()
            
        for row in ift2:
            for col in row:
                if_total += col
        print("Total inflows of all fundraising: " + str(if_total))
        print()

        of = cursor.execute("SELECT website.date, campaign.cost FROM website JOIN campaign on website.campid=campaign.campid")
        of_table = cursor.fetchall()
        print("  date  |  cost")
        print("----------------")
        for row in of_table:
            for col in row:
                    print(col, end='  ')
            print()

        oft = cursor.execute("SELECT cost FROM campaign")
        oft2 = cursor.fetchall()

        for row in oft2:
            for col in row:
                of_total += col
        print("Total outflows of all campaigns: " + str(of_total))
        print()

        print("Total inflows vs. outflows")
        if_total_b = int(if_total/1000)
        of_total_b = int(of_total/1000)
        print("inflows:  " + if_total_b * '|' + ' ' + str(if_total))
        print("outflows: " + of_total_b * '|' + ' ' + str(of_total))

    elif choice == 4:
        while True:
            print("1: View membership history")
            print("2: Add attributes to campaign")
            ph4_1 = input("Press 1 or 2 to modify:")
            try:
                ph4_2 = int(ph4_1)
                if ph4_2 !=1 and ph4_2 !=2:
                    print("1: View membership history")
                    print("2: Add attributes to campaign")
                    print("Press 1 or 2 to modify")
                    continue
            except ValueError:
                print("1: View membership history")
                print("2: Add attributes to campaign")
                print("Press 1 or 2 to modify:")
                continue
            else:
                ph4_2 = int(ph4_1)
                break
        if ph4_2 == 1:
            emp1 = 1

            while True:
                emp_id = input("Enter an empid of an employee (greater than 0): ")
                try:
                    emp_id2 = int(emp_id)
                    if emp_id2 < 1:
                        print("Invalid input!")
                        continue
                    else:
                        emp_id2 = int(emp_id)
                        break
                except ValueError:
                    continue

              
            his_tb = "SELECT * FROM q16 where empid=%s"
            emp_id3 = (emp_id2,)
            cursor.execute(his_tb, emp_id3)
            his_tb2 = cursor.fetchall()
                
            if not his_tb2:
                print("This empid is not exist.")
            else:
                print("campid  empid  firstname  lastname  city  events  lengweeks  date")
                print("--------------------------------------------------------------------")
                for row in his_tb2:
                    for col in row:
                        print(col, end=' | ')
                    print()


        elif ph4_2 == 2:
            al1 = 1
            count_c = 0

            while al1 != 0:
                tb_cname = input("Enter a column name that you want to add: ")
                tb_al = "ALTER TABLE campaign ADD %s VARCHAR(255)" % (tb_cname)
                cursor.execute(tb_al)
                dbconn.commit()
                count_c += 1
                
                al2 = input("Press 0 to exit. Press anything else to continue: ")
                try:
                    al1 = int(al2)
                    if al1 == 0:
                        break
                    else:
                        continue
                except ValueError:
                    continue

            print(str(count_c) + " attributes have been added successfully")

    elif choice == 5:
        tb = input("Enter a table name: ")
        q1 = "SELECT * FROM %s" % (tb)
        cursor.execute(q1)
        col_name = [desc[0] for desc in cursor.description]
       
        print("The existing attributes from this table are: ")
        for i in range(len(col_name)):
            print(col_name[i])
                    
    cursor.close()
    dbconn.close()

if __name__ == "__main__": main()

