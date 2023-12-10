import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.views.navbar import navbar
from reflex_web.views.header import header



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                width="100%"
            )
        )
    )

# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Mi titulo",
    description="pasdfasf sdfsdf asdfsf asdfsf sadfasf asdfsd sdfsdf asdfsdf asdfsdf asdfasf gdfgd ertert ertert ertet ertert"
    )
app.compile()
