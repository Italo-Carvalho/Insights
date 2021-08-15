import requests
import json


class ApiService:
    url = "http://0.0.0.0:8000/api/v1"
    refresh = None

    # def createUser(self, username, password):
    #     response = requests.post(f"{self.url}/user/",
    #          data={"username":username, "password":password})
    #     return response

    def loginUser(self, username, password):
        login = requests.post(
            f"{self.url}/token/obtain/",
            data={"email": "test@test.com", "password": "test123"},
        )
        if login.json()["access"]:
            return login.json()["access"]
        return login

    # def accessToken(self, refresh):

    #     if refresh:
    #         response = requests.post(f"{self.url}/token/refresh/", data={"refresh":refresh})
    #         if response.status_code == 200:
    #             return response.json()['access']
    #     else:

    #         return 'denied'

    def getData(self, username, password, page):
        auth = self.loginUser(username, password)
        if auth != "denied":
            data = requests.get(
                f"{self.url}/card/?page={page}",
                headers={"Authorization": f"Bearer {auth}"},
            )

            return json.loads(data.content)
        return "denied"

    def createData(self, username, password, texto, tags):
        auth = self.loginUser(username, password)
        if auth != "denied":
            return requests.post(
                f"{self.url}/card/",
                data={"texto": texto, "tags": tags},
                headers={"Authorization": f"Bearer {auth}"},
            ).status_code
        return "denied"

    def delData(self, username, password, pk):
        auth = self.loginUser(username, password)
        if auth != "denied":
            return requests.delete(
                f"{self.url}/card/{pk}", headers={"Authorization": f"Bearer {auth}"}
            ).status_code
        return "denied"

    def putData(self, username, password, pk, texto, body):
        auth = self.loginUser(username, password)
        if auth != "denied":
            return requests.put(
                f"{self.url}/card/{pk}",
                data={"texto": texto},
                headers={"Authorization": f"Bearer {auth}"},
            ).status_code
        return "denied"
