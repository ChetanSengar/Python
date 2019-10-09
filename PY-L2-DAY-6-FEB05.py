 


import random




# define generator to generate a character
def  randomchar(n,m):    
    for i in range(n):
        lst=[]
        for k in range(m):
           c = chr(ord('a')+random.randint(0, 25))
           lst.append(c)
           
        yield lst


def gendemo():
    #use generator
    for seq in randomchar(5,3):       
        print (seq )

#gendemo()


import time

def profile_time(original_function):
	def wrapper_function():
		t1=time.clock()
		original_function()
		t2=time.clock()
		print ("The execution time for the function is,", t2-t1)
	return wrapper_function

def test():
	time.sleep(1)
	print ("Its done")
    
    
t = profile_time(test)   
 
#########################


import xml.etree.ElementTree as ET 

def get_aiportcount():
    tree = ET.parse('airportdata.xml') 
    CA={} 
    root = tree.getroot() 
    for  country in root:     
        countryname = country.attrib['name']     
        CA[countryname] = []      
        count=0
        for  airport  in country:          
            count=count+1
        print (countryname + ':' +str(count) )


get_aiportcount()


      

def dict2XMLfile():
    airportdict = { "India" : { 'BOM' : 'mumbai', 'DEL' : 'Delhi'},
                   "UK" : {'LHR' : 'London - Heathrow', 'STN' : 'Stansted' }}
    
    # 1. create root node
    root = ET.Element('WorldAirports')
    
    for country,aps in airportdict.items():
        print ('-----', country,'-------')
        # step 2 : add <country> node
        node_country = ET.SubElement(root, 'country', name = country)
        for code,city in aps.items():
            """
            # method -1
            node = ET.Element("code")    
            node.text = code
            node_country.append(node)
            node = ET.Element("city")    
            node.text = city
            node_country.append(node)
            """
            # alternate way -- method - 2
            ET.SubElement(node_country, 'code').text = code
            ET.SubElement(node_country, 'city').text = city
    
    tree = ET.ElementTree(root)
    xmlfile = ".\\apdata.xml"
    tree.write(xmlfile)
    
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(open(xmlfile), 'xml')
    print(bs.prettify())
    

dict2XMLfile()















 
 
 
