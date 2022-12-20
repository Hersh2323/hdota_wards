# this is to run every day. But only once. 
import logging  # For logging purposes
logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    #logging.info('your text goes here')
    #logging.error('your text goes here')
    #logging.debug('your text goes here')

#import pickle   # For saving persistent variables

from datetime import datetime

# Current date time in local system
today_date = str(datetime.date(datetime.now()))
logging.info('dota_wards has executed on: ' + str(datetime.now()) )

