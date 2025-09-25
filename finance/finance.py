"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .ui.mimamba import mimamba
from .ui.mimamba2 import mimamba2
import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.box(
        #* главный блок (сверху вниз)
        rx.vstack(
            #* шапка сайта
            rx.box(
                rx.hstack(
                    #* логотип
                    rx.box(
                        rx.hstack(
                            rx.image("/logo.png",height="60px",width="60px"),
                            rx.text("Finance",weight="bold",size="7"),
                            align="center",
                        ),
                    ),
                    #* кнопки
                    rx.box(
                        rx.hstack(
                            #* кнопка
                            rx.box(
                                rx.hstack(
                                    mimamba('Today'),
                                    mimamba('This Week'),
                                    mimamba('This Month'),
                                    mimamba('Reports'),
                                    mimamba('All Outlets'),
                                    rx.button(
                                        rx.icon(tag = 'grip',

                                        ),
                                        border_radius="50%",
                                        min_width="48px",
                                        min_height="48px",
                                        padding="0",



                                ),
                                        
                                        spacing = '6',                            
                            align = 'center',
                            ),
                            ),
                            #Левая и правая часть

                        ), 
                            ),

                    width="100%",
                    display="flex",
                    justify="between",
                    align="center",
                ),
                rx.box(
                        rx.hstack(
                            rx.box(rx.vstack(
                                mimamba2(),
                                    ),),
                                        rx.box(),
                                ),
                    
                    ),
                
                width="100%"
            ),
        #* конец главного блока
        margin="15px",
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=False,
    ),
    #* font
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Saira:ital,wght@0,100..900;1,100..900&display=swap"
    ],
    #* global styles
    style={
        "font_family": "Saira, sans-serif",
        "height": "100vh",
        "width": "100%",
    }
)
app.add_page(index)