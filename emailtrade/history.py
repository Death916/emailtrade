import time
import csv
import os




def tradehist(msg):
    log = open("tradehist.txt", 'a')
    log.write('\n' + time.ctime() + ' ' + msg)
    log.close()


def tradecsv(Date,  Exchange, Price, Profit, Type, Pair):
    filename = '/home/death/code/python/emailtrade/emailtrade/bottrades.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        
        format = ['Date',  'Exchange', 'Price', 'Profit', 'Type', 'Pair']
        if not file_exists:
            tradewriter = csv.DictWriter(csvfile, fieldnames=format)
       
        
        tradewriter.writerow({'Date':Date,'Exchange':Exchange,'Price':Price,'Profit':Profit,'Type':Type,'Pair':Pair})

            

        csvfile.close

#tradecsv('4  ','3  ','2  ','1  ','4  ','5  ')
