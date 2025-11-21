import reflex as rx
from enum import Enum
from .colores import Color
from .colores import TexColor
from .fuentes import Fuente,FontWeight

#Constantes
MAX_WIDTH='600px'

#Hojas de estilo
STYLESHEETS=[
    "HTTPS://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "HTTPS://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
    ]

#Clase Size
class Talla(Enum):
    SMALL='0.5em'
    MEDIUM='0.8em'
    MIDDLE='1em'
    LARGE='1.5em'
    BIG='2em'

#Estilo base
BASE_STYLE={
    "font_family":Fuente.DEFAULT.value,
    "font_weight":FontWeight.LIGHT.value,
    "background_color":Color.FONDO.value,
    rx.heading:{
        "color":TexColor.HEADER.value,
        "font_family":Fuente.TITLE.value,
        "font_weight":FontWeight.MEDIUM.value
    },

    rx.button:{
        'width':'100%',
        'height':'100%',
        'display':'block',
        'padding':Talla.SMALL.value,
        'border_radius':Talla.MIDDLE.value,
        "background_color":Color.CONTENIDO.value,'color':"black",
        '_hover':{
            "background_color":Color.SECUNDARIO.value
        }
    },
    rx.link:{
        'text_decoration':None,
        '_hover':{}
    }
}

button_title_style=dict(
    font_family=Fuente.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Talla.MIDDLE.value,
    color=TexColor.HEADER.value
)

button_body_style=dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Talla.MEDIUM.value,
    color=TexColor.BODY.value
)

navbar_title_style=dict(
    font_family=Fuente.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Talla.MIDDLE.value
)

title_style=dict(
    color=TexColor.HEADER.value,
    width='100%',
    padding_top=Talla.MIDDLE.value
)