import reflex as rx
import datetime
from link_bio.styles.styles import Talla
from link_bio.styles.colores import TexColor
from link_bio.styles.colores import Color


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/imagen.jpg",width="100px",height="auto"
        ),
        rx.link('Visita mi página de cursos en informática',
                href='http://cursosinformaticos6.wordpress.com',
                is_external=True,trim='both'
        ),
        rx.link(
            rx.image(
                src='/github-logo.png',width="50px",height="auto"
            ),
            href='https://github.com/juantheater/python-reflex',
            is_external=True
        ),
        rx.text(
            {datetime.date.today().year},
              ', Este es el footer de nuestra página hecha totalmente con python'
        ),
        margin_botton=Talla.BIG.value,
        trim='both',
        align_items='center',
        padding_botton=Talla.BIG.value,
        color=TexColor.FOOTER.value,
        bg=Color.CONTENIDO.value
    )