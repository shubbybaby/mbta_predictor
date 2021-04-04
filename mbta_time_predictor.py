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
    #get api response for routes stopping at stop2
    url = "https://api-v3.mbta.com/routes?filter[stop]=place-north"
    response =''

    print(url)
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("ERROR: Server Error")
            exit()
        
        for x in response.data:
            desArray = x.attributes.direction_destinations
            if desArray[0] ne entry1:
                next
            else

    except :
        print(" Error connecting to API, Please try again")
    

    #

 



time_predictor(stop1, stop2)