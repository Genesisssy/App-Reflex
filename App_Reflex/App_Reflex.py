import reflex as rx


class State(rx.State):
    texto = "Presiona el botón 🌸"
    contador = 0
    color_texto = "#d63384"

    def cambiar_texto(self):
        self.contador += 1

        mensajes = [
            "¡Gracias por visitar mi página! 💖",
            "🌸 Eres increíble 🌸",
            "💐 Reflex es divertido 💐",
            "🌷 Bienvenido a mi página 🌷",
        ]

        colores = [
            "#d63384",
            "#ff1493",
            "#c71585",
            "#ff69b4",
        ]

        self.texto = mensajes[self.contador % len(mensajes)]
        self.color_texto = colores[self.contador % len(colores)]


def index():
    return rx.center(
        rx.vstack(

            rx.text(
                "🌸 🌷 🌸",
                font_size="35px"
            ),

            rx.heading(
                "Mi Página Web",
                size="8",
                color="#ff4fa3"
            ),

            rx.text(
                "Bienvenido a mi proyecto desarrollado con Reflex 💕",
                font_size="20px",
                color="#b03060",
                text_align="center"
            ),

            rx.text(
                State.texto,
                color=State.color_texto,
                font_size="22px",
                text_align="center"
            ),

            rx.text(
                f"Cantidad de clics: {State.contador}",
                color="#c71585",
                font_size="18px"
            ),

            rx.button(
                "Haz clic 💖",
                on_click=State.cambiar_texto,
                background_color="#ff69b4",
                color="white",
                border_radius="15px",
                size="3"
            ),

            rx.text(
                "🌷 💐 🌸 💕 🌷",
                font_size="28px"
            ),

            spacing="5",
            padding="35px",
            background_color="#ffe6f2",
            border_radius="25px",
            box_shadow="0px 0px 15px rgba(255,105,180,0.4)",
            width="450px"
        ),
        height="100vh",
        background_color="#fff0f5",
    )


app = rx.App()
app.add_page(index)