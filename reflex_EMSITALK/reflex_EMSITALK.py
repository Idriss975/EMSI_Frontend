import reflex as rx
from .Components import Header, Footer, Post
from .Services import Authentication, Feed
from .Services import Post as P

from rxconfig import config


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

@rx.page(route="feed/[id]", title="Home")
def feed():
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in neque nulla. In sit amet facilisis augue, id eleifend dui. Vivamus lobortis commodo iaculis. Morbi a pulvinar massa. Sed sed interdum nulla. Integer non mattis lacus, sed interdum diam. Integer cursus justo purus, at egestas neque sodales quis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In iaculis, nibh eget vestibulum pharetra, diam felis sagittis nisi, eget molestie est purus ac ipsum. Vestibulum rhoncus maximus neque. Suspendisse nec euismod augue. Nullam vel urna sit amet erat rutrum iaculis a vitae ipsum. Aliquam non orci at urna faucibus malesuada nec quis velit. Donec hendrerit, risus non aliquam scelerisque, odio magna egestas ex, id posuere purus dui ac est. Mauris consectetur ut justo at sodales.

Fusce ac felis augue. Nulla ut est nunc. Sed sit amet dolor libero. Phasellus lectus enim, convallis a risus vitae, tempus dictum tortor. Curabitur ornare scelerisque nulla, vitae feugiat felis tristique non. Etiam lorem lorem, accumsan vitae leo rhoncus, aliquam sollicitudin tellus. Morbi quis mi metus. Duis a justo in diam gravida lacinia at ac lorem. Nam ac nisl in dolor viverra commodo ut eu sapien. Etiam ac tortor id eros gravida bibendum a quis massa.
"""
    return rx.flex(
        Header.header(),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
        Post.Post("test","Title", text, 5),
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
