import reflex as rx


class State(rx.State):
    texto = "Haz clic en el botón"

    def cambiar_texto(self):
        self.texto = "¡Gracias por visitar mi página!"


def index():
    return rx.center(
        rx.vstack(
            rx.heading(
                "Mi Página Web",
                size="7",
                color="blue"
            ),

            rx.text(
                "Bienvenido a mi proyecto en Reflex.",
                font_size="20px"
            ),

            rx.text(
                State.texto,
                color="gray"
            ),

            rx.button(
                "Presionar",
                on_click=State.cambiar_texto,
                color_scheme="blue"
            ),

            spacing="5",
            padding="20px",
            border="1px solid #ccc",
            border_radius="10px",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)