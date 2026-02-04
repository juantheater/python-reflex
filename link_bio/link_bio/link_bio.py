"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx # type: ignore
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses


class State(rx.State):
    pass

app=rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

#class State(rx.State):
#    pass



