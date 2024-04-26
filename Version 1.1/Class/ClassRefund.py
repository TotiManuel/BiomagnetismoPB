import tkinter as tk
from tkinter import ttk
def prueba():
    pass
def main():
    rootRefund = tk.Tk()
    rootRefund.title("Registro de Reembolsos")
    rootRefund.geometry("800x600+0+0")
    label_products = tk.Label(rootRefund, text="Producto:")
    label_products.place(relx=0.01, rely=0.1)
    ProductExact = prueba()
    combobox_product = ttk.Combobox(rootRefund, values=ProductExact)
    combobox_product.place(relx=0.09, rely=0.1)
    combobox_product.set(ProductExact[0])
    combobox_product.bind("<<ComboboxSelected>>", prueba)
    label_amount = tk.Label(rootRefund, text="Cantidad:")
    label_amount.place(relx=0.01, rely=0.15)
    spinbox_Amount = tk.Spinbox(rootRefund, from_=1, to=100)
    spinbox_Amount.place(relx=0.09, rely=0.15)
    spinbox_Amount.bind("<<SpinboxSelected>>", prueba)
    label_price = tk.Label(rootRefund, text="Precio:")
    label_price.place(relx=0.01, rely=0.20)
    entry_price = tk.Entry(rootRefund)
    entry_price.config(state="readonly")
    entry_price.place(relx=0.09 , rely=0.20, relwidth=0.17)
    label_client = tk.Label(rootRefund, text="Cliente:")
    label_client.place(relx=0.01, rely=0.25)
    rootRefund.mainloop()
if __name__=="__main__":
    main()