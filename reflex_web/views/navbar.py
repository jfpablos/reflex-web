import reflex as rx
import reflex_web.constants as constants
from reflex_web.styles.styles import Size, Color
from reflex_web.components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="persona.png",
                alt="imagen de Jesus",
                width=Size.BIG.value,
                height=Size.BIG.value
            ),
            rx.text("Web Personal"),
            rx.spacer(),
            link_icon("youtube", 
                      constants.YOUTUBE_URL
                      ),
            link_icon("twitch", 
                      constants.TWITCH_URL
                      ),
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )