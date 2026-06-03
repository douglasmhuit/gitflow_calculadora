def dividir(a: float, b: float) -> float:
    """Retorna la división de dos números."""
    if b == 0:
        raise Exception("No se puede dividir por cero")
    return a / b