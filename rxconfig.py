import reflex as rx

config = rx.Config(
    app_name="App_Reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)