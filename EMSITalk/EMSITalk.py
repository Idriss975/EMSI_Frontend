import reflex as rx
from .Components import Header, Footer, Post, Topic
from .Services import Authentication, Feed
from .Services import Post as P


from rxconfig import config
from typing import Dict


class IndexState(rx.State):
    def page_redirect(self):
        return rx.redirect("feed/")


@rx.page(route="/", title="Index", on_load=IndexState.page_redirect)
def index():
    return rx.text("Redirecting ...") 

@rx.page(route="login", title="Log in")
def login():
    return rx.container(
        Header.header(Topicname="Log in"),

        rx.flex(
            rx.input(placeholder="Username" ,on_change=Authentication.LoginState.set_Local_Username),

            rx.input(placeholder="Password", type="password", on_change=Authentication.LoginState.set_Password),

            rx.hover_card.root(
                rx.hover_card.trigger(rx.text("Forgot password ?",size="1", _hover={"font-weight":"var(--font-weight-bold)"})),
                rx.hover_card.content(rx.heading("Not yet implemented", size="2")),
                ),
                
            
            rx.button("Login", on_click=Authentication.LoginState.login),

             
        
        border="1px solid #ededed",
        border_radius="7px",
        align="center",
        justify="center",
        direction="column",
        margin= "2rem",
        padding="1rem",
        row_gap="1rem",
        
        
        ),

        Footer.footer(),

        width="100%",
        padding_top="0",
        padding_right="0",
        padding_left="0",
        
    )




@rx.page(route="signup", title="Sign up")
def signup():
       return rx.container(
        Header.header(Topicname="Sign up"),

        rx.flex(
            rx.input(placeholder="Email", on_change=Authentication.SigninState.set_Email),

            rx.input(placeholder="Username" ,on_change=Authentication.SigninState.set_Username),

            rx.input(placeholder="Password", type="password", on_change=Authentication.SigninState.set_Password),
                
            
            rx.button("Sign up", on_click=Authentication.SigninState.sign_in),

             
        
        border="1px solid #ededed",
        border_radius="7px",
        align="center",
        justify="center",
        direction="column",
        margin= "2rem",
        padding="1rem",
        row_gap="1rem",
        
        ),

        Footer.footer(),

        width="100%",
        padding_top="0",
        padding_right="0",
        padding_left="0",
    )


class FeedPageState(rx.State):

    @rx.var
    def post_id(self) -> str:
        return self.router.page.params.get("id", "no id")
    

    
@rx.page(route="feed", title="Home", on_load=Feed.FeedState.getallfeed)
@rx.page(route="feed/[id]", title="Home",)
def feed():
    return rx.flex(
        Header.header(),
        rx.flex(
            rx.foreach(Feed.FeedState.Topics, lambda x : Topic.Topic(x["name"], x["description"], x["numberOfPosts"])),

            margin_left="2rem",
            margin_right="2rem",
        ),
        Footer.footer(),

        width="100%",
        direction="column",
        align="stretch",

    )

@rx.page(route="verify/", title="Email Verification")
def verify():
     return rx.container(
        Header.header(),
        rx.stack(
            rx.heading("Confirmation email has been sent.", size="4"),
            
            justify="center",
            min_height="85vh",
        ),
        Footer.footer(),


        padding_top="0"
    )

app = rx.App()
