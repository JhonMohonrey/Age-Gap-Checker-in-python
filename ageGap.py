#  created by Mohonrey 2023 oct 29
print("--------(Age Gap Checker)-------- Developer:Mohonrey")

checking = "False"
isExit = "False"

while checking == "False":
    while isExit == "False" :
        HerAge = input("How old she is? ")
        userAge = input("How old are you? ")

        try :
            HerAgeCon = int(HerAge)
            userAgeCon = int(userAge)
            checking = "True"
            isExit = "True"
            younger = userAgeCon - HerAgeCon
            older = userAgeCon + HerAgeCon - userAgeCon - userAgeCon

            HerPas = "Checking"
            YouPas = "Checking"
            Both = "True"

            if HerAgeCon <= 17 and userAgeCon <= 17 :
                print("You are both too young")
                Both = "True"
            else :
                Both = "False"
            
            if HerAgeCon >= 90 and userAgeCon >= 90 :
                print("No way you both older")
                Both = "True"
            else :
                Both = "False"

            if HerAgeCon <= 89 and userAgeCon >= 90 :
                print("Your Above 90 years now my friend and she is not")
                Both = "True"

            if HerAgeCon >= 90 and userAgeCon <= 89 :
                print("She above 90 years old now and your not")
                Both = "True"


            if Both == "False" :
                if HerAgeCon <= 17 :
                    print("She is too young wait until she is 18")
                    HerPas = "Not"
                else :
                    HerPas = "pass"

                if userAgeCon <= 17 :
                    print("You are too young wait until your 18")
                    YouPas = "Not"
                else :
                    YouPas = "pass"

                if HerPas == "pass" and YouPas == "pass" :
                    if HerAgeCon <= userAgeCon :
                        if younger <= 8 :
                            print("It's all good you have", younger, "years age gap")
                        else :
                            print("Not good you have", younger, "years age gap")
                    else :
                        if older <= 2 :
                            print("It's all good she is", older, "years older than you")
                        else :
                            print("Not good she is", older, "years older than you")
        except :
            checking = "False"
            print("Type error please enter number only")

    enterError = "False"

    while enterError == "False":
        print("Do you want to exit? y/n")
        userExit = input("")

        if userExit == "N" :
            userExit = "n"
        if userExit == "Y" :
            userExit = "y"
        
        if userExit == "yes" or userExit == "Yes" or userExit == "YES" :
            userExit = "y"
        if userExit == "no" or userExit == "No" or userExit == "NO" :
            userExit = "n"

        if userExit != "n" and userExit != "y":
            enterError = "False"
        if userExit != "y" and userExit != "n":
            enterError = "False"

        if userExit == "n" :
            isExit = "False"
            checking = "False"
            enterError = "True"

        if userExit == "y" :
            isExit = "True"
            checking = "True"
            enterError = "True"