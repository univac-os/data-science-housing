# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:59:48 2020

@author: udayh
"""

import time
import os
import requests
import sys

def retrieve_html():

  for year in range(2015,2019):
    for month in range(1,13):
      if(month <10):
        url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)
      else:
        url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)

    texts=requests.get(url)
    text_utf=texts.text.encode('utf=8')#entire html

    if not os.path.exists("Data/Html_Data/{}".format(year)):
        os.makedirs("Data/Html_data/{}".format(year))  #create folder
    with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
        output.write(text_utf) #with keyword is used when working with unmanaged resources (like file streams).
        #It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown
        #he with statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed
    
    sys.stdout.flush()
    
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("time taken {}".format(stop_time-start_time))
    