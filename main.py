import testone
import testmulti
import texttocsv

def printer():
    print ("This is a toolbox for handling Data regarding Austrian Social Security Numbers!")
    print ("-------------------------------------------------------------------------------")
    print ("-Type 1 for testing a single SSN\n-Type 2 for testing a .txt file of SSNs\n-Type 3 for generating a csv file standart format(Österreich testet) out of .txt file with SSNs Ns\n-Type 4 for 3 only with correct numbers\n-Type 5 to EXIT\n")
printer()

while True:
    desition =input()
    if desition =="1":
        testone.testone()
        break
    elif desition =="2":
        testmulti.sozinumber_checker("input.txt")
        break
        
    elif desition =="3":
        texttocsv.texttocsv("input.txt",1)
        break
    elif desition =="4":
        testmulti.sozinumber_checker("input.txt")
        texttocsv.texttocsv("Results\correct.txt",2)
        break
    elif desition =="5":break
    else: 
        print ("Wrong input, pls use 1-5") 
