import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colores import TexColor
from link_bio.styles.colores import Color


def info_text(titulo:str,body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                titulo,
                font_weight='bold',
                color=Color.PRIMARIO.value
            ),
            rx.text(
                body,
                font_size=styles.Talla.MEDIUM.value,
                color=TexColor.BODY.value
            ),
            align_items='center'
    )
    )