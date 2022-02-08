import requests
import secret

class Refresh:

    def __init__(self):
        self.refresh_token=secret.refresh_token
        self.base_64=secret.base_64

    def refresh(self):
        query="https://accounts.spotify.com/api/token"
        response = requests.post(query,
        data={"grant_type":"refresh_token","refresh_token":secret.refresh_token},
        headers={"Authorization":"Basic "+ secret.base_64})
        return(response.json()["access_token"])

