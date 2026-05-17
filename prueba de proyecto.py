from PIL import Image, ImageTk
import tkinter as tk

MAX_SEL = 3
COLS    = 5
BTN_W   = 80
BTN_H   = 80

selected   = []
btn_frames = []
btn_canvas = []
imagenes   = []

root = tk.Tk()
root.title("Panel")
root.geometry("1500x700")
root.resizable(False, False)
root.configure(bg="white")

# ── Imágenes de los 15 botones ────────────────────────────────────────────────
# Pon el nombre de tu imagen PNG en el botón que quieras
# Si no quieres imagen en un botón, deja None
RUTAS = [
    "greninja.png",  # botón 1  ← aquí va tu imagen
    "pikachu.png",            # botón 2
    "charizard.png",            # botón 3
    "talonflame.png",            # botón 4
    "sceptile.png",            # botón 5
    "aurorus.png",            # botón 6
    "hawlucha.png",            # botón 7
    "gardevoir.png",            # botón 8
    "goodra.png",            # botón 9
    "noivern.png",            # botón 10
    "sylveon.png",            # botón 11
    "gengar.png",            # botón 12
    "lucario.png",            # botón 13
    "muk.png",            # botón 14
    "shiinotic.png",            # botón 15
]
# ─────────────────────────────────────────────────────────────────────────────

# ── Botón circular de información ─────────────────────────────────────────────
def abrir_info():
    v = tk.Toplevel(root)
    v.title("Información")
    v.geometry("400x300")
    v.resizable(False, False)
    v.configure(bg="white")

    # ── Texto de la ventana emergente — escribe aquí tu contenido ─────────
    texto = (
        "Escribe aquí el texto que quieres\n"
        "que aparezca en esta ventana de información."
    )
    # ──────────────────────────────────────────────────────────────────────

    tk.Label(v, text=texto, bg="white", justify="center",
             wraplength=340, font=("Arial", 12)).pack(expand=True)
    tk.Button(v, text="✕", command=v.destroy,
              bg="#dddddd", relief="flat", font=("Arial", 10),
              padx=8, pady=4).pack(pady=(0, 16))

ci = tk.Canvas(root, width=40, height=40, bg="white", highlightthickness=0, cursor="hand2")
ci.place(x=16, y=16)
ci.create_oval(2, 2, 38, 38, fill="#cccccc", outline="#aaaaaa")
ci.create_text(20, 20, text="!", font=("Arial", 16, "bold"), fill="white")
ci.bind("<Button-1>", lambda e: abrir_info())

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

def actualizar_bordes(i):           # recursiva
    if i >= len(btn_frames):
        return
    btn_frames[i].config(bg="#e2c96a" if i in selected else "#aaaaaa")
    actualizar_bordes(i + 1)

def crear_botones(idx):             # recursiva
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
                      font=("Arial", 14), fill="#888888")

    c.bind("<Button-1>", lambda e, i=idx: toggle(i))
    btn_frames.append(borde)
    btn_canvas.append(c)
    crear_botones(idx + 1)

crear_botones(0)
root.mainloop()