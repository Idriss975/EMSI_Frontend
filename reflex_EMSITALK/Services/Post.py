import reflex as rx
from requests import get, post
from rxconfig import config

class PostModel:
    def __init__(self, username:str, title:str, text:str):
        self.username = username
        self.title = title
        self.text = text
        

class PostState(rx.State):
    #@rx.var
    def Get_Topic(self):
        ... #return self.router.page.params.get("id", "no id")
    #@rx.var    self.router.page.params.get("pid", "no pid")