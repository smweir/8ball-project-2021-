import random, tkinter, time

root = tkinter.Tk()
root.geometry("800x800")
canvas = tkinter.Canvas(root, width = 800, height = 800)
canvas.pack()
img = tkinter.PhotoImage(file = "8ball.png.jpeg")
image = canvas.create_image(400,400,image = img)
entry1 = tkinter.Entry(root)
entry1.place(x = 300, y = 0)

label1 = tkinter.Label(root, text = "")
label1.place(x = 800, y = 0)

def move():
    canvas.move(image,-100,100)
    root.update()
    time.sleep(1)
    canvas.move(image,200,-200)
    root.update()
    time.sleep(1)
    canvas.move(image,-250,150)
    root.update()
    time.sleep(1)
    canvas.move(image, 150, -50)
    answer = random.randint(1,5)
    
    if answer == 1:
        label1.config(text = "yes")
        label1.place(x = 387, y = 387)
    elif answer == 2:
        label1.config(text = "no")
        label1.place(x = 390, y = 387)
    elif answer == 3:
        label1.config(text = "maybe")
        label1.place(x = 377, y = 387)
    elif answer == 4:
        label1.config(text = "ask again later")
        label1.place(x = 353, y = 387)
    elif answer == 5:
        label1.config(text = "i hope not")
        label1.place(x = 365, y = 387)
        
    root.update()
    time.sleep(5)
    label1.config(text = "")
    label1.place(x = 800, y = 0)

button1 = tkinter.Button(root, text = "Go", command = move)
button1.place(x = 495, y = 0)

root.mainloop()