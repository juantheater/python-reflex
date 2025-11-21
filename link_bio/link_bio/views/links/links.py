import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.titulo import titulo

def links() -> rx.Component:
    return rx.vstack(
        titulo("Entretenimientos"),
        link_button('Twitch',
                    'Canal de twitch',
                    'twitch.svg',
                    'https://www.twitch.tv'
                    ),
        link_button('Youtube',
                    'Canal de videos',
                    'youtube.svg',
                    'https://www.youtube.com'
                    ),
        link_button('Instagram',
                    'Canal de chismes',
                    'instagram.svg',
                    'https://www.instagram.com'
                    ),
        link_button('Tiktok',
                    'Canal de idiotas',
                    'tiktok.svg',
                    'https://www.tiktok.com'
                    ),
        
        titulo("Recursos"),
        link_button('Twitch',
                    'Canal de twitch',
                    'youtube.svg',
                    'https://www.twitch.tv'
                    ),
        link_button('Youtube',
                    'Canal de videos',
                    'youtube.svg',
                    'https://www.youtube.com'
                    ),
        link_button('Instagram',
                    'Canal de chismes',
                    'youtube.svg',
                    'https://www.instagram.com'
                    ),
        link_button('Tiktok',
                    'Canal de idiotas',
                    'youtube.svg',
                    'https://www.tiktok.com'
                    ),
        width='100%'        
    ) 