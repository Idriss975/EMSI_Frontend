import reflex as rx
from ..Services import Feed


def AddTopic():
    return rx.dialog.root(
            rx.dialog.trigger(rx.button(rx.icon("plus"), size="2")),
                rx.dialog.content(
                    rx.dialog.title("Create Topic"),
                        rx.flex(
                            rx.text(
                                "Name",
                                as_="div",
                                size="2",
                                margin_bottom="1px",
                                weight="bold",
                            ),
                            rx.input(
                                placeholder="Topic name.", on_change=Feed.FeedState.set_Topicname
                            ),
                            rx.text(
                                "Descrition",
                                as_="div",
                                size="2",
                                margin_bottom="1px",
                                weight="bold",
                            ),
                            rx.text_area(
                                placeholder="Type your description here.", on_change=Feed.FeedState.set_Topicdesc
                            ),
                            direction="column",
                            spacing="3",
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button(
                                    "Cancel",
                                    color_scheme="gray",
                                    variant="soft",
                                ),
                            ),
                            rx.dialog.close(
                            rx.button("Create", on_click=Feed.FeedState.createTopic), # TODO: Create Topic
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                    ),
                ),
            )