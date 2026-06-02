from operations import sumar,restar

def ejecutar_demo() -> None:
    print("=== Calculadora App ===\n")
    print(f"  Suma: 2 + 3 = {sumar(2, 3)}")
    print(f"  Resta: 5 - 2 = {restar(5, 2)}")
if __name__ == "__main__":
    ejecutar_demo()