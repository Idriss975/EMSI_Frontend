import reflex as rx
from requests import get,post
import rxconfig

class FeedState(rx.State):
    Topics: list[dict[str,str]]

    def getallfeed(self):
        Tget = get(rxconfig._backend_url+"/api/topic/")

        self.Topics = {k: str(v) for k, v in Tget.json().items()}