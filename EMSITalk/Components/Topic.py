import reflex as rx
from rxconfig import config
from reflex.style import color_mode



def Topic(topicname:str,
         description:str,
         numofPosts:str)-> rx.Component:


    return rx.card(
        rx.link(
            rx.inset(
                rx.avatar(variant="soft",
                    size="9",
                    fallback=topicname[0],
                    width="100%",
                    high_contrast=True,
                    color_scheme="lime",
                ),
                side="top",
                pb="current",
                padding_bottom="3vw",
            ),
            rx.heading(topicname, size="5"),
            rx.text(description, size="2"),
        ),
            rx.hstack(
                rx.text(numofPosts,size="4"),
                rx.icon("inbox"),

                spacing="1",
                justify="end",
                margin_top="5vw",
                align="center",
            ),

        

        max_width="32vw",
        min_width="30vw",
        size="5",
        padding_bottom="2vw",
        margin="1vw 1vw 1vw 1vw",
    )