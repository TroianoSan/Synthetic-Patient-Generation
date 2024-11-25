import xml.etree.ElementTree as ET

def match_tag(tag_type, tags):
    """
    Returns the correct tag element based on the tag type.
    """
    match tag_type:
        case "NOMBRE_PERSONAL_SANITARIO":
            return ET.SubElement(tags, "NAME")
        case "ID_SUJETO_ASISTENCIA" | "ID_TITULACION_PERSONAL_SANITARIO" | "ID_ASEGURAMIENTO" | "ID_CONTACTO_ASISTENCIAL" | "IDENTIF_VEHICULOS_NRSERIE_PLACAS" | "ID_EMPLEO_PERSONAL_SANITARIO":
            return ET.SubElement(tags, "ID")
        case "CALLE" | "TERRITORIO" | "PAIS":
            return ET.SubElement(tags, "LOCATION")
        case "FECHAS":
            return ET.SubElement(tags, "DATE")
        case "SEXO_SUJETO_ASISTENCIA" | "FAMILIARES_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "OTHER")
        case "EDAD_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "AGE")
        case "CORREO_ELECTRONICO" | "NUMERO_TELEFONO" | "NUMERO_FAX":
            return ET.SubElement(tags, "CONTACT")
        case "PROFESION":
            return ET.SubElement(tags, "OCCUPATION")
        case "HOSPITAL" | "CENTRO_DE_SALUD" | "INSTITUCION":
            return ET.SubElement(tags, "LOCATION")
        case "EDAD_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "AGE")
        
    return ET.SubElement(tags, "TAG")

def create_tag(tag_type, value, start, end, tags, tag_id):
    tag = match_tag(tag_type, tags)
    tag.set("id", f"T{tag_id}")
    tag.set("start", str(start))
    tag.set("end", str(end))
    tag.set("text", value)
    tag.set("TYPE", tag_type)
    tag.set("comment", "")
    return tag_id + 1

def process_name_subject_assistance_tag(tag_type, full_name, start_pos, tags, tag_id):
    """
    Split the full name into name and surnames, and create the corresponding tags.
    """
    parts = full_name.split()
    name = ""
    surnames = ""

    # If the person has two names and two surnames
    if len(parts) == 4:
        name = " ".join(parts[:2])
        surnames = " ".join(parts[2:])
    else:
        name = parts[0]
        surnames = " ".join(parts[1:])

    # Calculates the start and end positions for the name and surnames
    first_start = start_pos
    first_end = first_start + len(name)
    last_start = first_end + 1 
    last_end = last_start + len(surnames)

    # Create the tag for the name(s) and surnames
    tag_id = create_tag(tag_type, name, first_start, first_end, tags, tag_id)
    tag_id = create_tag(tag_type, surnames, last_start, last_end, tags, tag_id)

    # Return the next tag id
    return tag_id

def process_name_healthcare_personnel_tag(match, tags, tag_id):
    """
    Create the tags for the healthcare roles.
    """
    # Create the tags for the healthcare personnel
    tag_id = create_tag("NOMBRE_PERSONAL_SANITARIO", match.group(1).strip(), match.start(1), match.end(1), tags, tag_id)
    tag_id = create_tag("ID_TITULACION_PERSONAL_SANITARIO", match.group(2).strip(), match.start(2), match.end(2), tags, tag_id)
    tag_id = create_tag("ID_EMPLEO_PERSONAL_SANITARIO", match.group(3).strip(), match.start(3), match.end(3), tags, tag_id)
    tag_id = create_tag("INSTITUCION", match.group(4).strip(), match.start(4), match.end(4), tags, tag_id)
    tag_id = create_tag("CALLE", match.group(5).strip(), match.start(5), match.end(5), tags, tag_id)
    tag_id = create_tag("TERRITORIO", match.group(6).strip(), match.start(6), match.end(6), tags, tag_id)
    tag_id = create_tag("TERRITORIO", match.group(7).strip(), match.start(7), match.end(7), tags, tag_id)
    tag_id = create_tag("PAIS", match.group(8).strip(), match.start(8), match.end(8), tags, tag_id)

    return tag_id

def process_city_tag(full_localitation, start_pos, tags, tag_id):
    """
    Split the full localitation into parts and create the corresponding tags.
    """
    parts = full_localitation.split(", ")
    current_start = start_pos

    for part in parts:
        current_end = current_start + len(part)
        tag_id = create_tag("LOCATION", part, current_start, current_end, tags, tag_id)
        current_start = current_end + 2

def process_patient_report(match, tags, tag_id):
    """
    Split the patient report into parts and create the corresponding tags.
    """
    id_sujeto_asistencia = match.group(1).strip() if match.group(1) else ""
    edad_sujeto_asistencia = match.group(2).strip() if match.group(2) else ""
    familiares_sujeto_asistencia = match.group(4).strip() if match.group(4) else ""

    if id_sujeto_asistencia:
        tag_id = create_tag("ID_SUJETO_ASISTENCIA", id_sujeto_asistencia, match.start(1), match.end(1), tags, tag_id)
    if edad_sujeto_asistencia:
        tag_id = create_tag("EDAD_SUJETO_ASISTENCIA", edad_sujeto_asistencia, match.start(2), match.end(2), tags, tag_id)
    if familiares_sujeto_asistencia:
        tag_id = create_tag("FAMILIARES_SUJETO_ASISTENCIA", familiares_sujeto_asistencia, match.start(4), match.end(4), tags, tag_id)

    return tag_id