import tkinter as tk

class CaiApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Care Assesment Instrument Helper")
        self.wm_attributes('-zoomed', 1)        

if __name__ == "__main__":
    app = CaiApp()
    app.mainloop()
