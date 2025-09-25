import reflex as rx

config = rx.Config(
    app_name="finance",
    frontend_port=3001,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],

)