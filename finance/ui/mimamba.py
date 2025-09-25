import reflex as rx

def mimamba(text = 'Text'):
    return rx.text(
            text ,
            padding = '20px',   
            color="white", 
            _hover= {
            'background':'white',
            'border-radius':'30px',
            'font-weight':'bold',
            'color':'black',
            
            }),
        