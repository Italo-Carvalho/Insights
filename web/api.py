import requests
import json


class WebService():
    url = 'http://0.0.0.0:8000/api/v1' 
    refresh = None


    def loginUser(self, username, password):
        login = requests.post(f"{self.url}/token/",
                     data={"username":username,"password":password})
        if login.json()['refresh']:
            return login.json()['refresh']
        return login

    def accessToken(self, refresh):

        if refresh:
            response = requests.post(f"{self.url}/token/refresh/", data={"refresh":refresh})   
            if response.status_code == 200:
                return response.json()['access']
            breakpoint()    
        else:
            
            return 'denied'
