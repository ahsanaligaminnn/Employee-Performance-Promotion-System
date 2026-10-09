#Employee Performance & Promotion System

print("---------------------------------------------")
print("|  Employee Performance & Promotion System  |")
print("---------------------------------------------\n")

employee_name = input("Enter Employee Name : ")
experience = input("Enter Experience : ")
salary = input("Enter Salary : ")
perform_score = input("Enter Performance score : ")
project = input("Enter Total completed Projects : ")
late = input("Enter Late : ")

print()

if experience.isdigit() and salary.isdigit() and perform_score.isdigit() and project.isdigit() and late.isdigit():
    experience = int(experience)
    salary = int(salary)
    perform_score = int(perform_score)
    project = int(project)
    late = int(late)

    if experience >= 2:
        pass
    else:
        print(f"Dear {employee_name}, Minium Experience required at least 2 years.\n")

    if perform_score >= 70:
        pass
    else:
        print(f"Dear {employee_name}, Minium Performance Score required at least 70.\n")

    if project >= 3:
        pass
    else:
        print(f"Dear {employee_name}, Minium Project Completed required at 3.\n")

    if late <= 10:
        pass
    else:
        print(f"Dear {employee_name}, Minium Late at least 10 Days.\n") 

    if experience >= 2 and perform_score >= 70 and project >= 3 and late <= 10:
        pass

        #Senior Promotion
        if perform_score >= 90 and perform_score <= 100 and experience >= 5:
            Promotion_Level = "Senior"
            promotion_status = "Eligible"
            Bonus_category = 20

            print("---------------------------")
            print("|  Final Employee Report  |")
            print("---------------------------\n")

            print(f"Employee name = {employee_name}")
            print(f"Experience = {experience}")
            print(f"Performance = {perform_score}")
            print(f"Projects = {project}")
            print(f"Late days = {late}")
            print(f"Promotion status = {promotion_status}")
            print(f"Promotion Level = {Promotion_Level} Years")
            print(f"Bonus = {Bonus_category}%")

        #Mid-Level Promotion
        elif perform_score >= 80 and perform_score <= 89 and experience >= 3 and experience < 5:
            Promotion_Level = "Mid-Level"
            promotion_status = "Eligible"
            Bonus_category = 15

            print("---------------------------")
            print("|  Final Employee Report  |")
            print("---------------------------\n")

            print(f"Employee name = {employee_name}")
            print(f"Experience = {experience}")
            print(f"Performance = {perform_score}")
            print(f"Projects = {project}")
            print(f"Late days = {late}")
            print(f"Promotion status = {promotion_status}")
            print(f"Promotion Level = {Promotion_Level} Years")
            print(f"Bonus = {Bonus_category}%")

        #Junio-Level Promotion
        elif perform_score >= 70 and perform_score <= 79:
            Promotion_Level = "Junior"
            promotion_status = "Eligible"
            Bonus_category = 10

            print("---------------------------")
            print("|  Final Employee Report  |")
            print("---------------------------\n")

            print(f"Employee name = {employee_name}")
            print(f"Experience = {experience}")
            print(f"Performance = {perform_score}")
            print(f"Projects = {project}")
            print(f"Late days = {late}")
            print(f"Promotion status = {promotion_status}")
            print(f"Promotion Level = {Promotion_Level}")
            print(f"Bonus = {Bonus_category}%")            
    else:
            Promotion_Level = None
            promotion_status = "Not Eligible"
            Bonus_category = 0

            print("---------------------------")
            print("|  Final Employee Report  |")
            print("---------------------------\n")

            print(f"Employee name = {employee_name}")
            print(f"Experience = {experience}")
            print(f"Performance = {perform_score}")
            print(f"Projects = {project}")
            print(f"Late days = {late}")
            print(f"Promotion status = {promotion_status}")
            print(f"Promotion Level = {Promotion_Level}")
            print(f"Bonus = {Bonus_category}%")       
else:
    print("Invalid Command.")    
