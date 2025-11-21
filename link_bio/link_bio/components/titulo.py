import reflex as rx
import link_bio.styles.styles as styles

def titulo(texto:str) -> rx.Component:
    return rx.heading(
        texto,
        size='5',
        style=styles.title_style
    )