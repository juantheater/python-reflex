import reflex as rx

from link_bio.components.iconos import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colores import Color
from link_bio.styles.colores import TexColor
from link_bio.styles.styles import Talla

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="Juan-Teran.webp",
                size="5",
                radius="full",
                border="14px",
                border_color="blue-light",
                alt='imagen de juan teran'
            ),
            rx.vstack(
                rx.heading(
                    'Juan Terán',
                    trim='both',
                    color=TexColor.HEADER.value
                ),
                rx.text(
                    'jctpicon@gmail.com',
                    trim='both',
                    color=TexColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        'x-twitter.svg',
                        'https://www.x.com',
                        alt='twitter'
                    ),
                    link_icon(
                        'instagram.svg',
                        'https://www.instagram.com',
                        alt='instagram'
                    ),
                    link_icon(
                        'youtube.svg',
                        'https://www.youtube.com',
                        alt='youtube'
                    ),
                    link_icon(
                        'facebook.svg',
                        'https://www.facebook.com',
                        alt='facebook'
                    )
                ),
                    spacing='3',
                    align_items='center'
            )
        ),
        rx.flex(
            info_text('+10','Años de experiencia'),
            rx.spacer(),
            info_text('+10','Años de experiencia'),
            rx.spacer(),
            info_text('+10','Años de experiencia'),
            width='100%'
        ),
        rx.text(
            """Soy ingeniero electrónico, con doctorado en ingeniería de sistemas, 
                y estoy probando esta nueva plataforma para hacer páginas web, 
                exclusivamente con python""",
                color=TexColor.BODY.value,
                font_size='15px',
                align="center"
                ),
                align_items='center'        
    )