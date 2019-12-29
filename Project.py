# Python code for Phenoix Integrators 3.0

# Done by Enfa Rose George,Neeraj T.K

# Under the guidance of Ms.Mary John (Dept. of. Information Technology)

# Special Thanks to Mr.Jairam Raj( Dept of.Computer Science)

# Mr. Felix Xavier (Quantum Lab Assistant)

from googlemaps import googlemaps

def locator(location):

    gmaps = googlemaps.Client('Enter Secret pass key here')

    response1 = gmaps.places('Hospital', location)
    i=1
    hospitalresponse='n'

    if response1['status'] == 'OK':

        hospitals = response1['results']
	for hospital in hospitals:
            i+=1
	    if hospitalresponse=='n':
				print "Send All possible details to ",hospital['name']
				print "Waiting for Response from hospital..."
				hospitalresponse=raw_input("Enter Response(n/y):")
				hospitalresponse=hospitalresponse.lower()
				if hospitalresponse=='y':
					hospositive=hospital['name']
				
	    else:
		print "Accident occured at lat,long,destination. Charge :",hospositive,"to",hospital['name']
	
    response2 = gmaps.places('Police Station', location)
    if response2['status'] == 'OK':

        Policestations = response2['results']
		
	for policestation in Policestations:
		
		print "Send  Accident details including Latitude and Longitude,geocode_result,hospital in charge, Impact Quotient etc to",policestation['name']
		break   

# 1.Accepting Input



# a.Locator accepting Address as input - defintion{Geocoding}





def get_location(point):

    return point['geometry']['location']

# b.Locator_latloninput - definition {Reverse Geocoding}



def locator_latloninput():



    gmaps = googlemaps.Client('AIzaSyCdyV5Olz8kyrCTlgnvNF-Mud9Mp3jtBMU')

    lat = input("Enter the Latitude:")

    lon = input("Enter the longitude:")

    destination = gmaps.reverse_geocode((40.714224, -73.961452))
    
    locator(get_location(destination[0]))
#The help module

def help():

	print "Input current locarion from GPS system:"	
	locator_latloninput()
	contact_authories()
	print "Then contact the emergency contacts and give details. If possible collect date pertaining to driver's conditions from smartwatch/fitness band and send to authorities."
	
# Main Program

print "Welcome to Phenoix Integrators 3.0".center(100)

impact=0
threshold=50
cond=1

while (cond==1):

   impact=input("Enter Impact parameter from crash sensor")
   if impact> threshold:
	help()
	cond = input("Enter 1 to continue,0 to exit")
	
	
print "Glad to be of service.".center(60)

