import tkinter as tk
from tkinter import messagebox

maze = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

cs = 60
p = [1,1]
g = [3,3]

r = tk.Tk()
c = tk.Canvas(r, width=5*cs, height=5*cs)
c.pack()

def draw():
    for i in range(5):
        for j in range(5):
            col = "black" if maze[i][j] else "white"
            c.create_rectangle(j*cs,i*cs,(j+1)*cs,(i+1)*cs,fill=col)
    c.create_rectangle(g[1]*cs,g[0]*cs,(g[1]+1)*cs,(g[0]+1)*cs,fill="green")

def player():
    c.delete("p")
    x,y = p[1]*cs+cs//2, p[0]*cs+cs//2
    c.create_oval(x-15,y-15,x+15,y+15,fill="blue",tags="p")

def move(e):
    d = {"Up":(-1,0),"Down":(1,0),"Left":(0,-1),"Right":(0,1)}
    if e.keysym in d:
        nx,ny = p[0]+d[e.keysym][0], p[1]+d[e.keysym][1]
        if maze[nx][ny]==0:
            p[0],p[1]=nx,ny
            player()
        if p==g:
            messagebox.showinfo("Done","Goal Reached")
            r.destroy()

draw()
player()
r.bind("<Key>", move)
r.mainloop()
