import tkinter as tk
from tkinter import messagebox

from digiKala import get_price_digikala
from torob import get_price_torob


def run_scraping():
    keyword = keyword_entry.get()
    if not keyword:
        messagebox.showerror("Error", "Please enter a keyword")
        return

    # Get prices
    price_digi = get_price_digikala(keyword)
    price_torob = get_price_torob(keyword)

    # Show results in a message box
    result = f"Digikala Price: {price_digi}\nTorob Price: {price_torob}"
    messagebox.showinfo("Prices", result)

if __name__ == '__main__':

    # GUI setup
    root = tk.Tk()
    root.title("Price Scraping App")

    tk.Label(root, text="Enter a keyword:").pack()
    keyword_entry = tk.Entry(root)
    keyword_entry.pack()

    tk.Button(root, text="Get Prices", command=run_scraping).pack()

    root.mainloop()
