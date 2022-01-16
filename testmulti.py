def main ():
    pass
def sozinumber_checker(file):
    CECK=[3, 7, 9, 5, 8, 4, 2, 1, 6 ]
    input("but your Data into input.txt, press any KEY to continue")
    with open(file) as f:
        patients=[i.strip().split(",")for i in f]

    list_correct=[]
    list_fault=[]
    for i in range (len(patients)):
        test=patients[i][0]
        if len(test)==10:
            to_check_number= int(test[3])
            calc_numbers= test[:3]+test[4:]
            calc_sum=0
            for j in range(len(calc_numbers)):
                calc_sum += int(calc_numbers[j])*CECK[j]
            testnumber=calc_sum%11
            if testnumber==to_check_number and to_check_number !=10:
                list_correct.append(patients[i])
            else: 
                list_fault.append(patients[i])


    with open("Results\correct.txt",'w') as f:
        for b in  range (len(list_correct)):
            f.writelines(str(list_correct[b][0]))
            for t in range(1,len(list_correct[b])):
                f.writelines(","+str(list_correct[b][t]))
            f.writelines("\n")

    with open("Results\wrong.txt",'w') as f:
        for b in  range (len(list_fault)):
            f.writelines(str(list_fault[b][0]))
            for t in range(1,len(list_fault[b])):
                f.writelines(","+str(list_fault[b][t]))
            f.writelines("\n")

    print ("Prozessed Patients Correct:", len(list_correct))    
    print ("Prozessed Patients Faulty:", len(list_fault)) 
    print ("success rate:", (len(list_correct)/len(patients))*100, "%" )   
    input("Correct file: Results\correct.txt\nFaulty file: Results\wrong.txt")

if __name__ == "__main__":
   sozinumber_checker("input.txt")

