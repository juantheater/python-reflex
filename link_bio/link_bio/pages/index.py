import reflex as rx # type: ignore
import link_bio.utils as utils
from link_bio.utils import lang
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
from link_bio.styles.styles import Talla

@rx.page(
        title=utils.index_titulo,
        description=utils.index_descripcion)

def index() -> rx.Component:
    return rx.box(
        lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width='600px',
                width='100%',
                margin_y=Talla.BIG.value,
                padding=Talla.BIG.value
            )
        ),
        footer()
    )