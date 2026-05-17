from PIL import Image, ImageTk
import tkinter as tk

MAX_SEL = 3
COLS    = 5
BTN_W   = 80
BTN_H   = 80 #ESTO ES PARA GUARDAR LAS MEDIDASS DE UNA VEZ, LAS DE LOS PERSONAJES 

selected   = []
btn_frames = []
btn_canvas = []
imagenes   = []
ventanas   = []

root = tk.Tk()
root.title("Panel")
root.geometry("1500x700")
root.resizable(False, False)
root.configure(bg="white")

# ── Imágenes de los 15 botones ────────────────────────────────────────────────
RUTAS = [
    "greninja.png", 
    "pikachu.png",     
    "charizard.png",     
    "talonflame.png",     
    "sceptile.png",         
    "aurorus.png",        
    "hawlucha.png",          
    "gardevoir.png",     
    "goodra.png",            
    "noivern.png",          
    "sylveon.png",     
    "gengar.png",         
    "lucario.png",           
    "muk.png",          
    "shiinotic.png", #AQUI LLAMO A LAS IMAGENES DESCARGADAS EN EL MISMO ARCHIVO
]
# ─────────────────────────────────────────────────────────────────────────────

# ── Botón de información ─────────────────────────────────────────────
def abrir_info():
    v = tk.Toplevel(root)
    ventanas.append(v)
    v.title("Información")
    v.geometry("400x500")
    v.resizable(False, False)
    v.configure(bg="white")

    # ── Texto de la ventana emergente — escribe aquí tu contenido ─────────
    texto = (
        "Este juego trata de una manera simple de pokemon, \n"
        "donde elijes a tus primeros 3 acompaniantes y vas de \n"
        "ciudad en ciudad combatiendo otras personas con otros \n"
        "pokemones, que al vencer, podras obtener para ti.\n"
        "\n"
        "PERO CUIDADO\n"
        "\n"
        "porque asi como puedes robar los pokemones de tus \n"
        "contrincantes, ellos podran agarrar los tuyos. \n"
        "\n"
        "Y QUE PASA SI PIERDES TODOS TUS POKEMONES???\n"
        "\n"
        "nada... solo pierdes para siempre\n"
        "MUCHA SUERTEEEEEEE!!!"
    )
    # ──────────────────────────────────────────────────────────────────────

    tk.Label(v, text=texto, bg="white", justify="center",
             wraplength=340, font=("Arial", 12)).pack(expand=True)

ci = tk.Canvas(root, width=40, height=40, bg="white", highlightthickness=0, cursor="hand2")
ci.place(x=16, y=16)
ci.create_oval(2, 2, 38, 38, fill="#cccccc", outline="#aaaaaa")
ci.create_text(20, 20, text="!", font=("Arial", 16, "bold"), fill="white")
ci.bind("<Button-1>", lambda e: abrir_info()) #BOTON DE INFO

# ── Campo de nombre ────────────────────────────────────────────────────────────
tk.Label(root, text="Tu nombre:", bg="white", font=("Arial", 13)).pack(pady=(60, 6))
tk.Entry(root, width=30, font=("Arial", 12)).pack()

# ── Cuadrícula de botones ──────────────────────────────────────────────────────
grid = tk.Frame(root, bg="white")
grid.pack(pady=40)

def toggle(idx):
    if idx in selected:
        selected.remove(idx)
    elif len(selected) < MAX_SEL:
        selected.append(idx)
    actualizar_bordes(0)

def actualizar_bordes(i):     
    if i >= len(btn_frames):
        return
    btn_frames[i].config(bg="#e2c96a" if i in selected else "#aaaaaa")
    actualizar_bordes(i + 1)

def crear_botones(idx):        
    if idx >= 15:
        return

    borde = tk.Frame(grid, bg="#aaaaaa", padx=2, pady=2)
    borde.grid(row=idx // COLS, column=idx % COLS, padx=8, pady=8)

    c = tk.Canvas(borde, width=BTN_W, height=BTN_H,
                  bg="white", highlightthickness=0, cursor="hand2")
    c.pack()

    if RUTAS[idx]:
        img  = Image.open(RUTAS[idx]).resize((BTN_W, BTN_H))
        foto = ImageTk.PhotoImage(img)
        imagenes.append(foto)
        c.create_image(0, 0, anchor="nw", image=foto)
    else:
        c.config(bg="#dddddd")
        c.create_text(BTN_W // 2, BTN_H // 2, text=str(idx + 1),
                      font=("Arial", 14), fill="#888888") #ESTO ERA AL PURO PRINCIPIO, QUE LO OCUPE PARA SABER SI ERA UN FALLO PORQUE NO ESTABA SIENDO CAPAZ DE VER LAS IMAGENES

    c.bind("<Button-1>", lambda e, i=idx: toggle(i))
    btn_frames.append(borde)
    btn_canvas.append(c)
    crear_botones(idx + 1)

crear_botones(0)

# ── Botón INICIAR ─────────────────────────────────────────────────────────────
def iniciar():
    # PARA CERRAR TODAS LAS VENTANAS ANTERIORES
    for v in ventanas:
        try:
            v.destroy()
        except Exception:
            pass

    import importlib
    import ventana_juego
    importlib.reload(ventana_juego)
    ventana_juego.abrir(seleccion=selected, ventana_anterior=root) #AQUI RECIBI MUCHA AYUDA DE AI, YA QUE QUERIA QUE LOS CODIGOS SE ENTRELAZARAN, EN VEZ DE SER UN SOLO CODIGO MUY GRANDE

    root.destroy()                          

tk.Button(
    root, text="INICIAR",
    font=("Arial", 13, "bold"),
    bg="#aaaaaa", fg="white",
    activebackground="#888888",
    relief="flat", padx=24, pady=10,
    cursor="hand2",
    command=iniciar
).pack(pady=(0, 30))
# ─────────────────────────────────────────────────────────────────────────────

root.mainloop()