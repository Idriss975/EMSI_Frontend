import reflex as rx
from rxconfig import config
from reflex.style import color_mode


def Post(username:str='Null', 
         PostTitle:str="", 
         description:str="", 
         upVote:int=0,
         voteCount:int=0,
         downVote: int=0,
         commentCount: int=0)-> rx.Component:
    return rx.grid(
            rx.avatar(variant="soft",fallback=username[0].upper()),

        rx.box(
            rx.vstack(
                
                rx.hstack(
                    rx.text("@" + username, font_weight="bold"),
                    rx.text(f"[{PostTitle}]"),
                    
                ),
                rx.text(description, width="100%"),
                align_items="left",
            )
            
        ),
        grid_template_columns="1fr 5fr",
        padding="1.5rem",
        spacing="1",
        border="1px solid #ededed",
        border_radius="7px",
        margin_bottom="2rem",
        margin_right="1rem",
        margin_left="1rem",
        box_shadow=rx.cond(color_mode == "light", "rgba(0, 0, 0, 0.8) 10px 15px 15px -14px", ""),
        )