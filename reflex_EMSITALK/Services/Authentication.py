import reflex as rx
from requests import get, post
import rxconfig

class SigninState(rx.State):
    Email:str
    Username:str
    Password:str

    def sign_in(self) -> int:
        signin = post(rxconfig._backend_url+"/api/auth/signup", json={
            "email":self.Email,
            "username":self.Username,
            "password":self.Password
        })

        return rx.redirect("verify") if signin.status_code == 200 else rx.redirect("/")
    
class LoginState(rx.State):
    Username:str = rx.LocalStorage()
    Local_Username:str
    Password:str
    Logged_in: str = rx.LocalStorage()
    Auth_token:str = rx.Cookie("Auth_token", same_site="strict")
    JWT_Token:str = rx.Cookie("JWT_Token",same_site="strict")

    def login(self):
        self.Username = self.Local_Username
        login = post(rxconfig._backend_url+"/api/auth/login", json={
            "username":self.Username,
            "password":self.Password
        })
        if login.status_code == 200:
            self.JWT_Token = login.json()["authenticationToken"]
            self.Auth_token = login.json()["refreshToken"]
            self.Logged_in = True
            return rx.redirect("feed")
    
    def logout(self):
        logout = post(rxconfig._backend_url+"/api/auth/logout", json={
            "refreshToken": self.Auth_token,
            "username": self.Username
        })

        if logout.status_code == 200:
            self.Logged_in = False
            self.Local_Username = ""
            self.Auth_token = ""
            return rx.redirect("feed")
