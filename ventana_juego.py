from PIL import Image, ImageTk
import tkinter as tk

BTN_W = 140
BTN_H = 200

# ── Imágenes de los 3 botones ─────────────────────────────────────────────────
RUTAS = [
    "ash.png",      # botón 1
    "serena.png",   # botón 2
    "red.png",      # botón 3
]
# ─────────────────────────────────────────────────────────────────────────────

def abrir(seleccion=None, ventana_anterior=None, nombre=""):
    if ventana_anterior:
        ventana_anterior.destroy()

    selected   = [None]
    btn_frames = []
    imagenes   = []

    root = tk.Tk()
    root.title("Juego")
    root.geometry("1500x700")
    root.resizable(False, False)
    root.configure(bg="white")

    def toggle(idx):
        selected[0] = idx
        actualizar_bordes(0)

    def actualizar_bordes(i):           # recursiva
        if i >= len(btn_frames):
            return
        btn_frames[i].config(bg="#e2c96a" if i == selected[0] else "#aaaaaa")
        actualizar_bordes(i + 1)

    def crear_botones(idx):             # recursiva
        if idx >= len(RUTAS):
            return

        borde = tk.Frame(grid, bg="#aaaaaa", padx=2, pady=2)
        borde.pack(side="left", padx=15)

        c = tk.Canvas(borde, width=BTN_W, height=BTN_H,
                      bg="white", highlightthickness=0, cursor="hand2")
        c.pack()

        try:
            img  = Image.open(RUTAS[idx]).resize((BTN_W, BTN_H))
            foto = ImageTk.PhotoImage(img)
            imagenes.append(foto)
            c.create_image(0, 0, anchor="nw", image=foto)
        except Exception:
            c.config(bg="#dddddd")
            c.create_text(BTN_W // 2, BTN_H // 2, text=str(idx + 1),
                          font=("Arial", 14), fill="#888888")

        c.bind("<Button-1>", lambda e, i=idx: toggle(i))
        btn_frames.append(borde)
        crear_botones(idx + 1)

    # ── Label de bienvenida ───────────────────────────────────────────────────
    tk.Label(root, text=f"BIENVENIDO {nombre.upper()}",
             bg="white", font=("Arial", 18, "bold")).pack(pady=(60, 30))
    # ─────────────────────────────────────────────────────────────────────────

    # ── Botones horizontales ──────────────────────────────────────────────────
    grid = tk.Frame(root, bg="white")
    grid.pack()
    crear_botones(0)

    root.mainloop()