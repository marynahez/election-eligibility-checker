# Eligibility Checker if people can or can not participate in a poll of election - Maryna Hez (M.H.)

# Step 1 Creating a new Python file - M.H.

# Step 2 - M.H.
# Step 2.1   # Step 3.1 Asking if a user is a resident of Alberta - M.H.
citizenship = input("Are you a Canadian citizen? ") #Asking if a user is citizen of Canada

# Step 2.2 Checking if the answer about citizenship is valid - M.H.
if citizenship == "no" or citizenship == "No" or citizenship == "yes" or citizenship == "Yes": # Step 2 Only 4 valid answers for a question of citizenship - M.H.
    pass

    # Step 3 - M.H.
    # Step 3.1 Asking if a user is a resident of Alberta - M.H.
    residency_of_Alberta = input("Are you a resident of Alberta? ") # Step 3 Asking a residency of a user

    # Step 3.2 Checking if residency response is valid - M.H.
    if residency_of_Alberta == "no" or residency_of_Alberta == "No" or residency_of_Alberta == "Yes" or residency_of_Alberta == "yes": # Step 3.2 Only 4 valid answers for a question of residency of Alberta - M.H.
        pass

        # Step 4 Asking about a month, day and year of birth of a user and checking if the answers are valid - M.H.

        # Step 4.1 Month - M.H.
        valid_month_of_birth = ["January", "February", "March", "April",
                                "May", "June", "July", "August",
                                "September", "October", "November", "December"] #Listing all valid months, others are not valid - M.H.
        month_of_birth = input(str("What is the month of your birth date? ")) # Asking for a month of birth - M.H.

        if month_of_birth in valid_month_of_birth: #Compare if month of birth is one of the valid ones - M.H.

            # Step 4.2 Day
            day_of_birth = int(input("What is the day of your birth date? ")) #Asking for a day of birth - M.H.

            # Step 5 - M.H.
            # Step 5.1 Check to see the birthdate is indeed valid - M.H.
            if month_of_birth == "February": #Conditions to check if date is valid according to month. The month is February. - M.H.
                if 1<= day_of_birth <= 28: #Because February has 28 days - M.H.
                    pass #If it is true date (day is possible in February(not less than 1 and not bigger than 28, then go to the next questions) - M.H.
                else:
                    print("Invalid birth date.") #Otherwise, it is not possible to have birthday day in this month as there is not such a day,
                                                 # so print that it's an invalid birthdate and exit - M.H.
                    exit() #Exit (stop asking questions and run the programme) - M.H.
            elif month_of_birth in ["April", "June",
            "September", "November"]: #Conditions to check if a date is valid according to month. The months are Apr, June, Sep and Nov. - M.H.
                if 1 <= day_of_birth <= 30: #Because months in this condition have 30 days - M.H.
                    pass #If it is true date (day is possible in that months, then go to the next questions) - M.H.
                else:
                    print("Invalid birth date.") #Otherwise, it is not possible to have birthday day in this month as there is not such a day,
                                                 # so print that it's an invalid birthdate and exit - M.H.
                    exit() #Exit - M.H.
            elif month_of_birth in ["January",
            "March", "May", "July", "August",
            "October", "December"]: #Conditions to check if a date is valid according to month. The months are Jan, March, May, July, Aug, Oct, Dec - M.H.
                if 1 <= day_of_birth <= 31: #Because months in this condition have 31 days - M.H.
                    pass #If it is a true date (day is possible in that months, then go to the next questions) - M.H.
                else:
                    print("Invalid birth date.") #Otherwise, it is not possible to have birthday day in this month as there is not such a day,
                                                 # so print that it's an invalid birthdate and exit - M.H.
                    exit() #Exit - M.H.

            # Step 4.3 Year - M.H.
            year_of_birth = int(input("What is the year of your birth date? ")) #Asking a user their year of birth - M.H.

            if 1900 <= year_of_birth <= 2024:
                pass
            else:
                print("Invalid response.")
                exit()

            # Step 5.2 Check if the date is not in the future (not later than due date of assignment!) - M.H.

            due_year = 2024 #Not later than 2024 year the birthday can be - M.H.
            due_month = "September" #Last month of 2024 when birthday can be but don't forget about day - M.H.
            due_day = 27 #Last day when the birthday can be as it is also the last day of assignment - M.H.

            if year_of_birth > due_year: #It is invalid birthdate in this case as it means that the day of birth is in the future - M.H.
                print("Invalid birth date.") #Print "Invalid birthday" as it is year in the future - M.H.
                exit() #Exit - M.H.
            elif year_of_birth == due_year: #It is possible that a user has a birthday same year as a due year but if the month will be
                                            #again the one which will be after a due month than it means it will be in the future, and it is not possible - M.H.
                if month_of_birth > due_month:
                    print("Invalid birth date.") #Print that text in case of invalid month of birth - M.H.
                    exit() #Exit - M.H.
            elif month_of_birth == due_month: # Same with day, if it is same year and month as a due day (assignment day) then it is not in the future,
                                              # but condition here about a day, if this day will be after a due day, then again it is in the future and not possible - H.M.
                if day_of_birth > due_day:
                    print("Invalid birth date.") #As it is not possible as it is future date, print that it's an invalid birthdate - M.H.
                    exit() #Exit - M.H.
            else: #If month of birth is one of the valid ones and the date of birth is not in the future and is possible according to numbers of days in a months, then fine,
                  #keep running a programme. That's why else is condition and pass (next line) means keep running a programme - M.H.
                pass

            # Step 6 - M.H.
            # Step 6.1 Checking age of a user - M.H.

            age = due_year - year_of_birth #checking how old is person only by checking year at first - M.H.
            if due_month < month_of_birth or (due_month == month_of_birth and due_day < day_of_birth): #Making a condition that in case if
                                            # this year person didn't have birthday we have to minus 1 year to make a proper calculation of age - M.H.
                age = age - 1 # Minus 1 if the birthday wasn't yet in this year by already checking month and day - M.H.
            else:
                pass #If a person already had birthday this year then calculation doesn't need to minus 1 year as it was in previous condition, so it is "else" condition and in this case it says to go to the next stage of code - M.H.

                if age >= 18: #If age is bigger or equal 18 - M.H.
                    print("You are eligible to vote.") #Print the text in brackets as a person has already 18 years old - M.H.
                else: #Otherwise if the person is younger than 18 years old - M.H.
                    print("You are not eligible to vote.") #Print that a user can't participate in a poll - M.H.
                    exit()  # Exit a programme for user


        else: #If a month is invalid (not from the list of months or grammatically not as it has to be) - M.H.
            print("Invalid response.") #Print that this is an invalid response - M.H.
            exit() #Exit a programme for user

    else: #What to do if the answer about residency is not valid - M.H.
        print("Invalid response.") #Print that this is an invalid response - M.H.
        exit() #Exit a programme for user

else: #What to do if the answer about citizenship is not valid - M.H.
    print("Invalid response.") #Exit a programme for user
    exit() #Exit a programme for user

    #Maryna Hez
    #Checked more than a few times the auto-grader
    #Used information "The Python Workbook" - Ben Stephenson, YouTube lecture "Learn Python - Full Course for Beginners[Tutorial] - freeCodeCamp.ord channel