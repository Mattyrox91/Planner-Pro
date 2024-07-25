#***************************************************************************************************************************************
#Program Name                                   PlannerPro
#Programmer                                     Matthew Dalton
#print("The oldest person is", name[maxindex])
#Purpose                                        Program Allows User To Record Their Daily Schedule And View It
#Modules Used                                   operator library
#Input Variables                                tasks_entered, time_of_day, see_schedule, see_schedule2
#Output                                         sorted_schedule, tasks
#***************************************************************************************************************************************


"""def main():
    import operator
    see_schedule = "Y"
    tasks = {}

    #Starts Program
    tasks_entered = input("Please Enter A Task You'd Like To Add To Your Schedule Or Enter 'stop' to stop ")

    #while loop keeps program functioning until the user types stop
    while (tasks_entered != 'stop'):
        try:
            time_of_day = int(input("Please Enter A Time In Military Time "))
        except ValueError:
            print("Oops! I Need A Time...Try Again ")
            continue
        tasks[tasks_entered] = time_of_day
        tasks_entered = input("Please Enter A Task You'd Like To Add To Your Schedule Or Enter 'stop' to stop ")

    #allows user to view their daily schedule in it's entirety or view a specific topic on the schedule they've entered
    see_schedule = input("Would You Like To View A (T)opic or (E)ntire Schedule? ")
    if see_schedule == "E" or see_schedule == "Entire Schedule":
        sorted_schedule = sorted(tasks.items(), key=operator.itemgetter(1))
        print(sorted_schedule)
    else:
        see_schedule2 = input("What Topic Would You Like To View On Your Schedule? ")
        for tasks_entered in tasks:
            if see_schedule2 == tasks_entered:
                print("Remember It's At", tasks[tasks_entered])

main()"""



def ReadAssoc():
    file = open ("c:/Users/Matt Dalton/OneDrive/Coding Project and Notes/School Projects/SchoolAssignment.txt", "r")
    for record in file:
        fields = record.split(' ')
        field1 = fields[0]
        print(record)
    file.close()


def main():

    dict = {}

    print("Pick Five Words ")

    word, association = input("Pick Word And Association ").split()
    dict[word] = association

    word2, association2 = input("Pick Word And Association ").split()
    dict[word2] = association2

    word3, association3 = input("Pick Word And Association ").split()
    dict[word3] = association3

    word4, association4 = input("Pick Word And Association ").split()
    dict[word4] = association4

    word5, association5 = input("Pick Word And Association ").split()
    dict[word5] = association5


    try:
        file = open('SchoolAssignment2.txt', 'w')
        file.write(str(dict))
        file.close()

    except:
        print("Unable to write to file")

    print(dict)

ReadAssoc()
main()
