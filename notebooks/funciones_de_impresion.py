def imprimir_lineas(datos):
    """
    Imprime CADA OBJETO COMPLETO en una sola línea (sin desglosar).
    """
    if isinstance(datos, dict):
        # Diccionario: cada clave:valor en línea completa
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    elif isinstance(datos, (tuple, list, set)):
        # Lista, set, etc: cada elemento COMPLETO en su línea
        for elemento in datos:
            print(elemento)
    elif isinstance(datos, float):
        print(f"{datos:.2f}" )
    else:
        print(datos)
    print("-" * 50)