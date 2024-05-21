import reflex as rx
from requests import get, post
import rxconfig
from json import dumps

class PostModel:
    def __init__(self, username:str, title:str, text:str):
        self.username = username
        self.title = title
        self.text = text
        

class PostState(rx.State):
    

    @rx.var
    def Get_Topic(self):
        ...
    #@rx.var    self.router.page.params.get("pid", "no pid")