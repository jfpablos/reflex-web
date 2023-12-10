import reflex as rx
import reflex_web.constants as constants
from reflex_web.styles.styles import Size, TextColor
import reflex_web.styles.styles as styles


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Titulo de la Cabecera",
            size="lg",
            padding_botton=Size.BIG.value
        ),
        rx.flex(
            rx.image(
                src="persona.png",
                alt="descripción de la imagen",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("Este es el Subtitulo1"),
                    rx.text("Este es el Subtitulo2"),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    "Frase de prueba dentro de un span con una plabra al final en otro ",
                    rx.span("color",
                            color=TextColor.ACCENT.value,
                            text_size=Size.DEFAULT.value),
                    "!"
                ),
                rx.span(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nisl magna, pharetra id justo vitae."
                ),
                rx.span(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nisl magna, pharetra id justo vitae."),
                rx.link(
                    "#Hastag",
                    href=constants.HASTAG_URL,
                    is_external=True,
                    color=TextColor.TERTIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                ),
                align_items="start"
            ),
            flex_direction=["column", "column", "column", "row", "row"]
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style,
    )
