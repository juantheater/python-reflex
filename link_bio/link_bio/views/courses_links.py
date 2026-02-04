import reflex as rx # type: ignore
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.titulo import titulo

def courses_links() -> rx.Component:
    return rx.vstack(
        titulo("Cursos:"),
        link_button(
            'Django',
            'Framework para paginas web',
            'twitch.svg',
            'https://www.twitch.tv'
        ),
        link_button(
            'Python',
            'Lenguaje de programacion',
            'youtube.svg',
            'https://www.youtube.com'
        ),
        link_button(
            'Reflex',
            'Paginas web con solo python',
            'youtube.svg',
            'https://www.youtube.com'
        ),        
        width='100%',
    )
        
