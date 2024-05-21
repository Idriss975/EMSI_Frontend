import reflex as rx
from rxconfig import config
from reflex.style import color_mode
from ..Services.Authentication import *




def header(Topicname:str="Feed") -> rx.Component :
    return rx.container(
            rx.hstack(
                rx.heading("EMSITalk"),

                rx.spacer(),
                rx.heading(Topicname,size="5"),
                rx.spacer(),
                rx.cond(LoginState.Logged_in=="true",
                        rx.flex(
                            rx.heading(LoginState.Username, size="4"),
                            rx.button("Log out", on_click=LoginState.logout),
                            spacing="3",
                        ),
                        rx.flex(
                            rx.button("Login", on_click=rx.redirect("login/")),
                            rx.button("Sign up",on_click=rx.redirect("signup/")),
                            spacing="3",
                        )
                ),
                
                rx.color_mode.button(position="right"),
            ),
        padding="0.5rem 2rem 1rem 2rem",
        margin_bottom="1rem",
        top="0",
        position="sticky",
        z_index="1",
        background_color=rx.cond(color_mode == "light", "#f9f9f9", "#5b5bd6"),
        border_radius="0px 0px 40px 40px",
        border_bottom="1px solid",
        border_color=rx.cond(color_mode == "light","black","white"),
    )