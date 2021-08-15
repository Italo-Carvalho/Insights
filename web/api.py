import requests
import json


class ApiService:
    url = "http://0.0.0.0:8000/api/v1"
    refresh = None
    email = "test@test.com"
    password = "test123"

    def loginUser(self):
        login = requests.post(
            f"{self.url}/token/obtain/",
            data={"email": self.email, "password": "test123"},
        )
        if login.json()["access"]:
            return login.json()["access"]
        return login

    def accessToken(self, refresh):

        if refresh:
            response = requests.post(
                f"{self.url}/token/refresh/", data={"refresh": refresh}
            )
            if response.status_code == 200:
                return response.json()["access"]
        else:

            return "denied"

    def getData(self, page):
        auth = self.loginUser()
        if auth != "denied":
            data = requests.get(
                f"{self.url}/card/?page={page}",
                headers={"Authorization": f"Bearer {auth}"},
            )

            return json.loads(data.content)
        return "denied"

    def createData(self, texto, tags):
        auth = self.loginUser()
        if auth != "denied":
            return requests.post(
                f"{self.url}/card/",
                data={"texto": texto, "tags": tags},
                headers={"Authorization": f"Bearer {auth}"},
            ).status_code
        return "denied"

    def delData(self, username, password, pk):
        auth = self.loginUser()
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
