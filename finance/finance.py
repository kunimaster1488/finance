"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .ui.mimamba import mimamba
from .ui.mimamba2 import nav_bar_button
from .ui.charts import mimamba3
import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
#https://www.behance.net/gallery/190475019/Salesforce-CRM-SaaS-UX-UI-Design?tracking_source=curated_galleries_ui-ux

data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]

def composed():
    return rx.recharts.composed_chart(
        rx.recharts.area(
            data_key="uv", stroke="white", fill="#4c4c4c"
        ),
        rx.recharts.line(
            data_key="pv",
            type_="monotone",
            stroke="#d8ff00",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        data=data,
        height=200,
        width="100%",
    )



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
            #* левая и правая часть
                rx.box(
                    rx.hstack(
                        #* левая сторона с кнопками
                        #? nav_bar.py
                        rx.box(
                            rx.vstack(
                                nav_bar_button("house"),
                                nav_bar_button("database"),
                                nav_bar_button("calendar-range"),
                                nav_bar_button("folder"),
                                nav_bar_button("square-chart-gantt"),
                                nav_bar_button("chart-column-big"),
                                nav_bar_button("users"),
                                nav_bar_button("upload"),
                            ),
                            width="150px",
                            margin_top ='10%',
                        ),    
                        #* правая сторона
                        rx.box(
                            #1 block
                            rx.box(
                                rx.hstack(
                                    
                                    #left block
                                    rx.box(
                                        rx.vstack(
                                        rx.box(
                                            rx.text(('Hi mike '), rx.text.em("here's "), ('whats happening in your store')),
                                            weight = 'bold',
                                            font_size = '35px',
                                            
                                        ),
                                        
                                        rx.box(
                                            rx.hstack(
                                                    mimamba3('may', 20),
                                                    mimamba3('june', 30),
                                                    mimamba3('july', 40),
                                                    mimamba3('aug', 20),
                                                    mimamba3('sep', 60),
                                                    mimamba3('oct', 10),
                                                    
                                                
                                                    
                                                    
                                                
                                                
                                            )
                                            
                                        ),
                                        
                                        rx.box(
                                            rx.vstack(
                                                rx.text('This month your store have sell ALL Outlets',
                                                        font_size = '150%',
                                                        weight = 'light') ,
                                                rx.text('$331,224.74',
                                                        font_size = '200%',
                                                        weight = 'bold'
                                                        ) ,
                                                
                                            ), ),
                                        rx.box(),
                                    
                                    ),
                                        width = '40%',
                                        height  = '400px',
                                        border_radius = '30px',
                                        background = '#527bdd',
                                        
                                        padding = '20px',
                                        ),
                                    
                                    #* правый блок (график)
                                        rx.box(
                                            
                                            #* название блока и ссылка
                                            rx.box(rx.flex(
                                                rx.text('All Autlets'),
                                                rx.button(
                                                    rx.icon(tag = 'a_arrow_down',

                                                    ),
                                                    border_radius="50%",
                                                    min_width="48px",
                                                    min_height="48px",
                                                    padding="0",



                                                    ),
                                                    width="100%",
                                                    display="flex",
                                                    justify="between",
                                                    align="center",
                                                    
                                                    
                                                    
                                                    
                                                )),
                                            
                                            rx.hstack(
                                                #* верхняя сторона
                                                rx.box(
                                                    #текст
                                                    rx.box(
                                                        rx.vstack(
                                                        rx.text('Average items per sale',
                                                                font_size = '25px',
                                                                ),
                                                            rx.hstack(
                                                            rx.text('12.5', font_size = '25px', color = '#d8ff00'),
                                                            rx.text('5.2 more than last month', font_size = '15px', color= '#4c4c4c'),
                                                            ),
                                                            ),
                                                        ),
                                                    #график
                                                    rx.box(),
                                                    
                                                    ),
                                                composed(),
                                                #* правая сторона
                                                rx.box(),
                                                
                                            ),
                                            
                                            
                                            background="#232323",
                                            padding="20px",
                                            border_radius="35px",
                                            width="100%",
                                            height="400px",
                                        ),
                                    
                                ),
                                
                                width = '100%',
                                ),
                            
                            #2 block
                            rx.box(),
                            
                            #3 block
                            rx.box(),
                            
                           
                            
                            
                            
                            
                            width="100%",
                        ),    
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