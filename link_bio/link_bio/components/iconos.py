import reflex as rx
from link_bio.styles.styles import Talla

def link_icon(imagen:str,url:str,alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            alt=alt,
            height=Talla.BIG.value,
            width=Talla.BIG.value
        ),
        href=url,
        is_external=True,
        width='100%',
    )