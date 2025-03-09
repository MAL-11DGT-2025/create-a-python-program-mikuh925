season = input("What is your favorite season: ")

season_list = ["summer" , "winter" , "autumn" , "spring" , "fall"]

if season.lower().strip() in season_list:
    print("That is a valid season")
else:
    print("That is not a valid season")    


book = input("What is the first book of the Bible? ")
print("a)Genesis" , "b)Exodus" , "c)Numbers" , "d)Leviticus")
correct = ["a" , "a)" , "genesis" , "a)genesis"]
incorrect = ["b" , "b)" , "exodus" , "b)exodus" , "c" , "c)" , "numbers" , "c)numbers" , "d" , "d)" , "leviticus" , "d)leviticus" ]

if book.lower().strip() in correct:
    print("Correct")
elif book.lower().strip() in incorrect:
    print("Incorrect")
else:
    print("Invalid")