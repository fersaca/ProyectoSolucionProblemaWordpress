# iniciador.py
import detector_de_problemas

def iniciar_analisis():
    # Solicitar al usuario el mensaje de error de WordPress
    user_input = input("Por favor, ingrese el mensaje de error de WordPress que detecta: ")

    # Llamar a la función analizar del archivo detector_de_problemas.py
    resultado_analisis = detector_de_problemas.detect_known_problems(user_input)

    # Devolver el resultado al usuario
    print(f"Respuesta: {resultado_analisis}")

if __name__ == "__main__":
    iniciar_analisis()
