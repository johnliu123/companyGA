# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:26:27 2019

@author: johnliu
"""

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from allData import Alldata
import contentutil

def my_job():

    contentutil.printlog('..........start scan ga..........')

    ISOTIMEFORMAT = '%Y-%m-%d'
    start_date = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    end_date = start_date
    start_date = '2019-09-10'
    end_date = '2019-09-10'
    result = Alldata()

    result.outputData(start_date, end_date)

    contentutil.printlog('..........finish scan ga..........')


if __name__ == '__main__': 

    # 直接執行 
    # my_job()

    # Daemon 執行
    sched = BlockingScheduler()
    # 設定時間間隔 (每天執行一次，基底時間為12點)
    sched.add_job(my_job,'interval', days=1, start_date='2019-06-01 12:00:00')
    sched.start()