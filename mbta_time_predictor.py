import sys
import getopt
import requests

argv=sys.argv[1:]
stop1=''
stop2=''

#validate only 2 stops are entered
try: 
    options, args = getopt.getopt(argv, "f:s:", ["first =","second ="])
except :
    print("An Error has occured, Please enter 2 stops to proceed.")


for name, value in options:
    if name in ['-f', '--first']:
        stop1 = value
    elif name in ['-s', '--second']:
        stop2 = value

if not stop1 or not stop2:
    print("An Error has occured, Please enter 2 stops to proceed.")
    exit()

def time_predictor(entry1, entry2):
    print("Stop 1: " + entry1)
    print("stop 2: " + entry2)
    #get api response
    #response = requests.get("https://www.mbta.com/developers/v3-api/stops")
    url = "https://api-v3-mbta.com/routes?filter[stop]=%s" %entry2
    response = requests.get(url)

    if response.status_code != 200:
        print("ERROR: Server Error")
        exit()



time_predictor(stop1, stop2)