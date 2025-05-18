def main():
    print("🚀 Bienvenido al Forex Bot")
    print("Este es el punto de entrada del sistema de trading.")
    print("Aquí podrías iniciar tus microservicios, lanzar el bot o ejecutar análisis.")

    # Ejemplo de flujo inicial
    menu()

def menu():
    print("\nSeleccione una opción:")
    print("1. Descargar datos históricos")
    print("2. Ejecutar estrategia simple")
    print("3. Entrenar modelo de IA")
    print("4. Salir")

    choice = input("Opción: ")

    if choice == "1":
        descargar_datos()
    elif choice == "2":
        ejecutar_estrategia()
    elif choice == "3":
        entrenar_modelo()
    elif choice == "4":
        print("Saliendo...")
    else:
        print("Opción no válida.")
        menu()

def descargar_datos():
    print("📈 Descargando datos... (simulado)")
    # Aquí irá el código real de descarga desde yfinance o API
    menu()

def ejecutar_estrategia():
    print("🤖 Ejecutando estrategia simple... (simulado)")
    # Aquí se puede llamar a una función de src/strategies
    menu()

def entrenar_modelo():
    print("🧠 Entrenando modelo IA... (simulado)")
    # Aquí se integrará con modelos en src/models
    menu()

if __name__ == "__main__":
    main()
