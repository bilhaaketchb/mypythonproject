def mitmorning():
    print("This is MIT Morning class")


mitmorning()
mitmorning()
mitmorning()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(x - y)
    print(x / y)


calculate()


def majina(myfirstname, mylastname):
    print(myfirstname + " " + mylastname)


majina("Bilha", "Aketch")
majina("Jairus", "Otieno")
majina("Bryton", "Ouma")
majina("Bryna", "Mercy")
majina("Mary", "Wanjiku")


def majina(myfirstname, mylastname, myage):
    print("my name is", myfirstname, " " + mylastname, "and my age is" + " ", myage)


majina("Bilha", "Aketch", 18)
majina("Jairus", "Otieno", 30)
majina("Bryton", "Ouma", 9)
majina("Bryna", "Mercy", 4)
majina("Mary", "Wanjiku", 25)
#create a fuction that give the average of [2.5,6,3,5]
#create a funtion that gives you the longest string in a list
def calculate_average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average
data =[2,6,8,9,2,1,8]
result=calculate_average(data)
print("The average is",result)

