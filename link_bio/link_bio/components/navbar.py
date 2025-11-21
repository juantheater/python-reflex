import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Talla
from link_bio.styles.colores import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("juan",
                rx.text.strong("dev - Linux",
                    color=Color.SECUNDARIO.value,
                    style=styles.navbar_title_style
                ),
                color=Color.PRIMARIO.value
            ),
            style=styles.navbar_title_style
        ),
    position="sticky",
    bg=Color.CONTENIDO.value,
    padding_x=Talla.BIG.value,
    padding_y=Talla.MIDDLE.value,
    z_index="999",
    top='0'
    )