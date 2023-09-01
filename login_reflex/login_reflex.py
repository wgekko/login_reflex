"""Pynecone login UI."""

import pynecone as pc

# return custom text input field


def get_input_field(icon: str, placeholder: str, _type: str):
    return pc.container(
        # I'll be displaying a icon side by side so we need
        # to stack horizontally
        pc.hstack(
            pc.icon(
                tag=icon,  # we pass this in when we call the func.
                color="white",
                fontSize="12px",
            ),
            pc.input(
                placeholder=placeholder,  # pass in when called
                border="0px",
                focus_border_color="None",
                color="white",
                fontWeight="semibold",
                fontSize="12px",
                type=_type,
            ),
        ),
        # container settings
        borderBottom="0.1 solid grey",
        width="300px",
        height="45px",
    )


def index():
    # we ll start by creating the main container where all other UI
    # control are stored
    login_container = pc.container(
        # we'll be going for a vertical stack...
        pc.vstack(
            # we'll store the inputs and buttons in here vetically,
            # some padding at the top
            pc.container(height="65px"),
            pc.container(
                pc.text(
                    "Ingresar",
                    fontSize="28px",
                    color="white",
                    fontWeight="bold",
                    letterSpacing="2px",
                ),
                # text setting
                widht="250px",
                center_content=True,
            ),
            pc.container(
                pc.text(
                    "Conceptos de UI Pynecone con Python",
                    fontSize="12px",
                    color="white",
                    fontWeight="#eeeeee",
                    letterSpacing="0.25px",
                ),
                # text setting
                widht="250px",
                center_content=True,
            ),
            # some more padding
            pc.container(height="50px"),
            # we'll great a function that returns a custom text field in order
            # to minimize code cluttering
            get_input_field("email", "Email", ""),
            pc.container(height="5px"),
            get_input_field("lock", "Password", "password"),
            pc.container(height="5px"),
            pc.container(
                pc.text(
                    "Olvido la clave?",
                    color="white",
                    fontSize="14px",
                    textAlign="end",
                )
            ),
            pc.container(height="55px"),
            # form bottom
            pc.container(
                pc.button(
                    pc.text(
                        "Ingresar",
                        color='white',
                        fontSize="12px",
                        weight="bold",
                    ),
                    # button settings
                    width="350px",
                    height="45px",
                    color_scheme="blue",
                )    
            ),            
        ),
        # container settings
        width="400px",
        height="75vh",
        bg="#1d2330",
        boerderRadius="15px",
        boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",
    )
    # main stack to return
    _main = pc.container(
        login_container,
        # stack settings
        center_content=True,
        justifyContent="center",
        maxWidth="auto",
        height="100vh",
        bg="#1d2330",
    )
    # return main
    return _main


# Add state and page to the app.
app = pc.App()
app.add_page(index)
app.compile()
