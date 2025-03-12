def convert(number, choice):
    if choice == "f":
        result = number 32 * (5/9)
    elif choice == "c":
        result = number * (9/5) + 32
        print(result)


temperature = input("Do you want to convert?\na) Farenheit to Celcius\nb) Celcius to Farenheit\n>>")

number = input("What is the temperature you would like to convert?\n>>")

f_to_c = ["farenheit to celcius", "a", "a)"]
c_to_f = ["celciues to farenheit", "b", "b)"]

if temperature in f_to_c:
    convert(number, "f")
elif temperature in c_to_f:
    convert(number, "c")''