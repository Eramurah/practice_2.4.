import requests
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO


def show_image_from_url(url):
    response = requests.get(url)
    img_data = response.content

    img = Image.open(BytesIO(img_data))
    img = img.resize((200, 200))

    tk_img = ImageTk.PhotoImage(img)

    panel.config(image=tk_img)
    panel.image = tk_img


def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    image_url = data[0]["url"]
    show_image_from_url(image_url)


def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    image_url = data["message"]
    show_image_from_url(image_url)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300+75+75")
    root.title("Коты и собаки")

    btn_cat = ttk.Button(root, text="Получить кота", command=get_cat)
    btn_cat.pack()

    btn_dog = ttk.Button(root, text="Получить собаку", command=get_dog)
    btn_dog.pack()

    panel = Label(root)
    panel.pack()

    root.mainloop()