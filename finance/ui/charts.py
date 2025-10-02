import reflex as rx

def mimamba3(text = 'September', height_top = 20):
    return rx.box(
        rx.text((text), color = '#d56d1',
        padding = f'{height_top}px 20px' ,      
                
        ),
        border_radius = '30px',
        border = '1px solid #a4b5c1',
        
        
        
    )