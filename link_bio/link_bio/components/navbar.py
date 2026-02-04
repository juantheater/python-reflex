import reflex as rx # type: ignore
import link_bio.styles.styles as styles
from link_bio.styles.styles import Talla
from link_bio.styles.colores import Color
from link_bio.routes import Route


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
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
        href = Route.INDEX.value
        ),
    position="sticky",
    bg=Color.CONTENIDO.value,
    padding_x=Talla.BIG.value,
    padding_y=Talla.MIDDLE.value,
    z_index="999",
    top='0'
    )