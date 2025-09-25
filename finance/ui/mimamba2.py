import reflex as rx

def mimamba2(icon = 'ampersands'):
    return rx.button(
            tag = icon ,
            padding = '20px',   
            max_height = '48px',
            max_width = '48px',
            color="white", 
            _hover= {
            'background':'white',
            'color':'black',
            
            }),