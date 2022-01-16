from datetime import datetime
import pandas as pd

def main ():
    pass
def texttocsv(file,num):
    if num ==1:
        input("but your Data into input.txt, press any KEY to continue")
    now = datetime.now()
    date_time = now.strftime("%d.%m.%Y %H:%M")

    with open(file) as f:
            patients=[i.strip().split(",")for i in f]

    infolist=[]
    for i in range(len(patients)):
        if patients[i][-1]=='pcr' or patients[i][-1]==' pcr':
            test="Covid-19 PCR"
            infolist.append([date_time,patients[i][0],test])
        elif patients[i][-1]=='ag'or patients[i][-1]==' ag' :
            test="Covid-19 Antigen Schnelltest"
            infolist.append([date_time,patients[i][0],test])
        elif patients[i][-1]=='pcr+ag' or patients[i][-1]==' pcr+ag':
            test="Covid-19 PCR"
            infolist.append([date_time,patients[i][0],test])
            test="Covid-19 Antigen Schnelltest"
            infolist.append([date_time,patients[i][0],test])


    data=pd.DataFrame(infolist, columns=['Datum', 'SVNR','Testtyp'])
    data.to_csv("Results\\results.csv",sep=';',index=False)
    input('csv file: Results\\results.csv')

if __name__ == "__main__":
    texttocsv("input.txt",1)

