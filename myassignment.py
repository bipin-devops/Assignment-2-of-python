from aifc import Error

import matplotlib.pyplot as plt


def welcome_message():
    print("--------------------Tooth Fairy- ATO Case--------------------")
    print("-----------------Bipin Raj Sitoula-30377216------------------")


welcome_message()


def myMenu():
    print("""
1. Statistics
2. Export children details who haven't lost any teeth
3. Display number of claims per state
4. Compare 2 States
5. Exit""")
    print("-" * 61)


file = open("addresses.csv", "r")
lines = file.readlines()
num_of_children = (len(lines) - 1)
total_num = 0
no_teeth_lost = 0
average_teeth = 0
all_teeth_lost = 0
expenditure_amount = 0

for l in lines[1:]:
    total_num += int(l.split(",")[6])
    average_teeth = total_num / num_of_children
    if int(l.split(",")[6]) == 0:
        no_teeth_lost += 1
    elif int(l.split(",")[6]) == 20:
        all_teeth_lost += 1
    elif int(l.split(",")[6]) == 1:
        expenditure_amount += 1
    elif int(l.split(",")[6]) > 1:
        expenditure_amount += 0.50


def choice_one():
    print("Total number of children on the list: {}".format(num_of_children))
    print("Average number of teeth claims over the years: {}".format(average_teeth))
    print("Number of children who have never lost a tooth: {}".format(no_teeth_lost))
    print("Number of children who have lost all their baby teeth: {}".format(all_teeth_lost))
    print("Total Expenditure for this year: ${}".format(expenditure_amount))


def choice_two():
    num = 0
    export_file = input("Enter new file name: ")
    new_file = open(export_file, "w")
    for li in lines[1:]:
        if int(li.split(",")[6]) == 0:
            num += 1

            new_file.write(li.split(",")[0] + " " + li.split(",")[1] + "\n")
    print(str(num) + " children have been saved in " + export_file)
    new_file.close()


def choice_three(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars + 1)

    plt.bar(positions, data, align='center')

    plt.xticks(positions, labels)
    plt.xlabel('State')
    plt.ylabel('Number of children')
    plt.title('Number of children per state')

    plt.grid()
    plt.show()


count_tas = 0
count_qld = 0
count_wa = 0
count_nsw = 0
count_sa = 0
count_vic = 0
count_nt = 0
for all in lines[1:]:
    if (all.split(",")[4]) == "TAS":
        count_tas += 1
    elif (all.split(",")[4]) == "QLD":
        count_qld += 1
    elif (all.split(",")[4]) == "WA":
        count_wa += 1
    elif (all.split(",")[4]) == "NSW":
        count_nsw += 1
    elif (all.split(",")[4]) == "SA":
        count_sa += 1
    elif (all.split(",")[4]) == "VIC":
        count_vic += 1
    elif (all.split(",")[4]) == "NT":
        count_nt += 1


steps = [count_tas, count_qld, count_wa, count_nsw, count_sa, count_vic, count_nt]

labels = ['TAS', 'QLD', 'WA', 'NSW', 'SA', 'VIC', 'NT']


def choice_four(data2, labels2):

    num_bars = len(data2)
    positions = range(1, num_bars + 1)

    plt.bar(positions, data2, align='center')

    plt.xticks(positions, labels2)
    plt.xlabel('State')
    plt.ylabel('Average Number of Teeth')
    plt.title('Average number of teeth lost across 2 states')

    plt.grid()
    plt.show()





while True:
    myMenu()
    user_choice = input("Enter your choice[1-5] ")
    if user_choice == '1':
        choice_one()

    elif user_choice == '2':
        choice_two()

    elif user_choice == '3':
        choice_three(steps, labels)

    elif user_choice == '4':
        first_state = input("Enter first state (TAS/QLD/WA/NSW/SA/VIC/NT): ").upper()
        second_state = input("Enter second state (TAS/QLD/WA/NSW/SA/VIC/NT): ").upper()

        average_teeth_one = 0
        average_teeth_two = 0
        item1 = 0
        item2 = 0
        for all in lines[1:]:
            if (all.split(",")[4]) == first_state:
                average_teeth_one += int(all.split(",")[6])
                item1 += 1

            elif (all.split(",")[4]) == second_state:
                average_teeth_two += int(all.split(",")[6])
                item2 += 1
        try:
            final_avg1 = average_teeth_one / item1
            final_avg2 = average_teeth_two / item2

            steps2 = [final_avg1, final_avg2]
            labels2 = [first_state, second_state]
            choice_four(steps2, labels2)

        except ZeroDivisionError:
            print("\n Please enter valid state name")

    elif user_choice == '5':
        quit()
        break
    else:
        print("Please enter valid choice [1-5]")

file.close()
