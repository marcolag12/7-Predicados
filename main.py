universo = {
    "estudiantes": {
        "Mariana": {"materia": "SistemasOperativos", "carrera": "Ing. Sistemas"},
        "Marco":   {"materia": "BasesDatos",         "carrera": "Ing. Sistemas"},
        "Arturo":  {"materia": "Calculo",            "carrera": "Ing. Industrial"},
        "Eric":    {"materia": "SistemasOperativos", "carrera": "Ing. Industrial"}
    },

    "maestros": {
        "Mendoza":   {"SistemasOperativos"},
        "Rivas":     {"BasesDatos"},
        "Hernandez": {"Calculo"}
    },

    "reprobados": {"Mariana", "Arturo"},
    "recursan":   {"Eric", "Marco"}
}


def cursa(x, y):
    for alumno, datos in universo["estudiantes"].items():
        if alumno == x:
            return datos["materia"] == y
    return False

def estudia(x, y):
    for alumno, datos in universo["estudiantes"].items():
        if alumno == x:
            return datos["carrera"] == y
    return False

def enseña(x, y):
    for maestro_nombre, materias in universo["maestros"].items():
        if maestro_nombre == x:
            return y in materias
    return False

def estudiante(x):
    return x in universo["estudiantes"]

def reprobó(x):
    return x in universo["reprobados"]

def recurso(x):
    return x in universo["recursan"]

def maestro(x):
    return x in universo["maestros"]


print("cursa('Marco', 'BasesDatos'):                ", cursa("Marco", "BasesDatos"))               # True
print("cursa('Mendoza', 'Calculo'):                 ", cursa("Mendoza", "Calculo"))               # False

print("estudia('Eric', 'Ing. Industrial'):          ", estudia("Eric", "Ing. Industrial"))        # True
print("estudia('Hernandez', 'Ing. Sistemas'):       ", estudia("Hernandez", "Ing. Sistemas"))     # False

print("enseña('Mendoza', 'SistemasOperativos'):    ", enseña("Mendoza", "SistemasOperativos"))    # True
print("enseña('Mendoza', 'Calculo'):              ", enseña("Mendoza", "Calculo"))              # False

print("estudiante('Eric'):                       ", estudiante("Eric"))                       # True
print("estudiante('Rivas'):                      ", estudiante("Rivas"))                      # False

print("reprobó('Mariana'):                       ", reprobó("Mariana"))                       # True
print("reprobó('Carlos'):                        ", reprobó("Carlos"))                        # False

print("recurso('Marco'):                         ", recurso("Marco"))                         # True
print("recurso('Hernandez'):                     ", recurso("Hernandez"))                     # False

print("maestro('Hernandez'):                     ", maestro("Hernandez"))                     # True
print("maestro('Mariana'):                       ", maestro("Mariana"))                       # False
