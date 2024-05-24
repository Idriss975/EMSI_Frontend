import reflex as rx
from requests import get,post
import rxconfig
from ..Services import Authentication

class FeedState(Authentication.LoginState):
    Topics: list[dict[str,str]]

    Topicname:str
    Topicdesc:str

    def getallfeed(self):
        Tget = get(rxconfig._backend_url+"/api/topic/")

        self.Topics = Tget.json()
    
    def createTopic(self):
        cTopic = post(rxconfig._backend_url+"/api/topic/",
            headers={"Authorization": "Bearer "+self.JWT_Token},
            json={
            "name": self.Topicname,
            "description":self.Topicdesc
        })
        if cTopic.status_code == 201:
            return rx.redirect("feed")