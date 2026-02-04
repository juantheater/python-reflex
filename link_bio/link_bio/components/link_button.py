import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Talla


def link_button(titulo:str,body:str,image:str,url:str,is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Talla.BIG.value,
                    height=Talla.BIG.value
                ),
                rx.vstack(
                    rx.text(titulo,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    align_items='center',
                    spacing="0"
                )
            )
        ),
        href=url,
        is_external=is_external,
        width='100%'
        )