
import time

def tradehist(msg):
    log = open("tradehist.txt", 'a')
    log.write('\n' + time.ctime() + ' ' +  msg)
    log.close()
