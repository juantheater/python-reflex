import reflex as rx # type: ignore
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.titulo import titulo

def index_links() -> rx.Component:
    return rx.vstack(
        titulo("Entretenimientos"),
        link_button(
            'Twitch',
            'Canal de twitch',
            'twitch.svg',
            'https://www.twitch.tv'
        ),
        link_button(
            'Youtube',
            'Canal de videos',
            'youtube.svg',
            'https://www.youtube.com'
        ),
        link_button(
            'Instagram',
            'Canal de chismes',
            'instagram.svg',
            'https://www.instagram.com'
        ),
        link_button(
            'Tiktok',
            'Canal de idiotas',
            'tiktok.svg',
            'https://www.tiktok.com'
        ),
        
        titulo("Recursos"),
        link_button(
            'Cursos',
            'Páginas Web con Reflex',
            'youtube.svg',
            Route.COURSES.value,
            is_external=False
        ),
        
        width='100%'        
    ) 