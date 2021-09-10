import  requests
length=0

#headers required and bearer is authorization token

head={
    "Host": "search5-noneu.truecaller.com",
    "authorization": "Bearer a1i0j--SzcjdRk4kWGdR84ri9ct_XKaOYlQ3tNnS1SmJfIX30whjJaJPS5yl5blt",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/11.66.7 (Android;10)"
 } 
  
def main(num):
    global length
    info=[]
    url='https://search5-noneu.truecaller.com/v2/search?countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&adId=1af646b1-8cdf-4e8a-b9d4-349f546890c5&encoding=json&q='+str(num)
    req=requests.get(url,headers=head)
    data=req.json()
    try:        
        name=data['data'][0]['name']
        info.append(name)     
    except : pass              
    try:                
        carrier=data['data'][0]['phones'][0]['carrier']  
        info.append(carrier)              
    except : pass
    try:                
        email=data['data'][0]['internetAddresses'][0]['id']  
        info.append(email)              
    except : pass 
    try:                
        address=data['data'][0]['addresses'][0]['city']  
        info.append(address)              
    except : pass
         
    length=len(info)
    
    return info



