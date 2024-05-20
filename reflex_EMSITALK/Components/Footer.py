import reflex as rx
from rxconfig import config


def footer() -> rx.Component :
    return rx.flex(
        rx.text("Created by ", 
                rx.link("Idriss BERCHIL",
                    href="https://github.com/Idriss975",
                    weight="bold",
                    margin_right="1rem",)
            ),
        

        justify="end",
        align="end",
        margin_top="1rem",
        position="absolute",
        bottom="0",
        right= "0",
    )