CECK=[3, 7, 9, 5, 8, 4, 2, 1, 6 ]

def main ():
    pass
def testone():
    so_number =input("Socialsecuritynumber: ")
    if so_number =="5":
        return
    if len(so_number)==10:
        to_check_number= int(so_number[3])
        calc_numbers= so_number[:3]+so_number[4:]
        calc_sum=0
        for j in range(len(calc_numbers)):
            calc_sum += int(calc_numbers[j])*CECK[j]
        testnumber=calc_sum%11
        if testnumber==to_check_number and to_check_number !=10:
            print ("Okey")
        else: 
            print ("Wrong")
    else: 
            print ("Wrong Size")
    testone()

if __name__ == "__main__":
   testone()


