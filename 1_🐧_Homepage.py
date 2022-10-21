import lista_demo as llb
from info import (
    config_page as cfp,
)

cfp.config_page()

# Llamada a la clase con los proyectos(Carpeta projects)
page = llb.proyectos()
page.__lista__()