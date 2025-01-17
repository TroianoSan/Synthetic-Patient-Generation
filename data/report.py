# List of some characteristics of MESH population groups (NEEDS to be distinguish between age groups)
MESH_population_groups = [
    "de tez blanca", "de ascendencia africana del norte", "de ascendencia asiática", "de ascendencia centroasiática", "de ascendencia asiática oriental",
    "de ascendencia asiática del sudeste", "de ascendencia asiática occidental", "de ascendencia caribeña", "de ascendencia indígena americana",
    "de ascendencia europea oriental", "de ascendencia nórdica o escandinava", "de ascendencia del medio oriente", "de ascendencia norteamericana",
    "de ascendencia oceánica", "de ascendencia australiana", "de ascendencia sudamericana", "de descendencia africana", "de ascendencia árabe",
    "de ascendencia indígena centroamericana", "de ascendencia indígena sudamericana", "de ascendencia gitana", "de comunidades vulnerables", "testigo de Jehová",
    "musulman", "judío", "refugiado", "migrante", "transeúnte", "vegetariano", "vegano", "víctima de desastre", "víctima de violencia de género", "discapacitado",
    "terminal", "sobreviviente de violencia", "fumador", "exfumador", "no fumador", "consumidor de alcohol", "usuario de drogas"
]

# Weights for each MESH population group
MESH_population_weights = [
    25, 5, 10, 5, 10, 5, 5, 3, 4, 8, 7, 6, 15, 2, 2, 12, 8, 6, 3, 4, 
    2, 5, 1, 7, 5, 2, 3, 4, 15, 15, 1, 1, 3, 2, 2, 12, 8, 20, 15, 10
]

# List of some possible relatives of a patient according to their age group
companions_0_to_15 = (
    ["madre"] * 5 + ["padre"] * 3 + ["abuela"] * 3 + ["abuelo"] + ["hermana"] * 2 + ["hermano"] + ["tía"] + ["tío"]
)

companions_16_to_59 = (
    ["madre"] * 5 + ["padre"] * 3 + ["abuela"] * 3 + ["hija"] * 5 + ["hijo"] * 5 + ["abuelo"] + ["hermana"] + ["hermano"] + ["tía"] + ["tío"] + ["prima"] + ["primo"] +
    ["sobrina"] + ["sobrino"] + ["nuera"] + ["yerno"] + ["suegra"] + ["suegro"] + ["marido"] + ["esposa"] + ["pareja"] + ["conviviente"] + ["compañero"] + ["amigo"] +
    ["amiga"] + ["vecino"] + ["vecina"] + ["compañero de trabajo"] + ["compañera de trabajo"] + ["compañero de estudio"]
)

companions_60_to_100 = [
    "madre", "padre", "hermana", "hermano", "hija", "hijo", "nuera", "yerno", "marido", "esposa", "pareja", "conviviente",
]