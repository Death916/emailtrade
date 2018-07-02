import logging
import time


def tradehist(msg):
    log = open('d:\\code\\emailtrade\\tradehist.txt','a')
    log.write('\n' + time.ctime() + ' ' +  msg)

