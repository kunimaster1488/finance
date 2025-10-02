import reflex as rx

def nav_bar_button(icon="circle-dot"):
    return rx.button(
        rx.icon(
            tag=icon,
            color="#d5d6d1",
            _hover={
                "color":"black",
            }
        ),
        border_radius="50%",
        min_width="48px",
        min_height="48px",
        padding="0",
        background="#4c4c4c",
        _hover={
            "background":"white",
        }
    )  