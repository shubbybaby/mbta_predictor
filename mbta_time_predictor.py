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
    url = "https://api-v3.mbta.com/routes?filter[stop]=%s" %(entry2)
    response =''
    print("URL: " +url)

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("ERROR: Server Error")
            exit()
        
        #if both stops are found, use the predictor api to get arrival time
        for x in response.data:
            desArray = x.attributes.direction_destinations
            if desArray[0] == entry1 and desArray[1] == entry2:
                #get arrival time from api
                try:
                    url_p = "https://api-v3.mbta.com/predictions?filter%5Bstop%5D=%s&filter%5Bdirection_id%5D=0&include=stop" %(entry1)
                    response_p = requests.get(url_p)
                    arrivalTime = response_p.data[0].attributes.arrival_times
                except: 
                    print(" Error getting predicted arrival time from API, Please try again")
                next
        
    except:
        print("Error connecting to API, Please try again")
    
    return 0
time_predictor(stop1, stop2)