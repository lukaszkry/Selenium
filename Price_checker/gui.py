import price_checker
from tkinter import *


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.item_list = ['mirror shard', 'headhunter', 'cos']
        self.currency_type_list = ['Exalted Orb', 'chaos orb']
        # Class from price_checker.py
        self.check = price_checker.Price()

        # Labels
        self.space_label = Label(self.master, text=' ', padx=15, pady=20)
        self.space_label.grid(row=0, column=0)
        self.item_label = Label(self.master, text='Choose item from list', padx=30, pady=20)
        self.item_label.grid(row=0, column=1)
        self.currency_type_label = Label(self.master, text='Choose currency type', padx=30, pady=20)
        self.currency_type_label.grid(row=0, column=2)
        self.threshold_label = Label(self.master, text='Threshold', padx=20, pady=20)
        self.threshold_label.grid(row=0, column=4)
        self.sell_label = Label(self.master, text='Sell', padx=20, pady=20)
        self.sell_label.grid(row=1, column=3)
        self.buy_label = Label(self.master, text='Buy', padx=20, pady=20)
        self.buy_label.grid(row=2, column=3)
        self.refresh_rate_label = Label(self.master, text='Refresh rate (s)', padx=20, pady=20)
        self.refresh_rate_label.grid(row=0, column=5)
        self.refresh_repetitions_label = Label(self.master, text='Number of refreshes', padx=20, pady=20)
        self.refresh_repetitions_label.grid(row=2, column=5)

        # Entries
        self.item_entry = Entry(self.master, width=25)
        self.item_entry.grid(row=1, column=1)
        self.currency_type_entry = Entry(self.master, width=25)
        self.currency_type_entry.grid(row=1, column=2)
        self.sell_entry = Entry(self.master, width=20)
        self.sell_entry.grid(row=1, column=4)
        self.buy_entry = Entry(self.master, width=20)
        self.buy_entry.grid(row=2, column=4)
        self.refresh_rate_entry = Entry(self.master, width=20)
        self.refresh_rate_entry.grid(row=0, column=6)
        self.number_of_refreshes_entry = Entry(self.master, width=20)
        self.number_of_refreshes_entry.grid(row=2, column=6)

        # Listbox
        self.item_listbox = Listbox(self.master, width=25)
        self.item_listbox.grid(row=2, column=1)
        self.currency_type_listbox = Listbox(self.master, width=25)
        self.currency_type_listbox.grid(row=2, column=2)

        # Buttons
        self.start_button = Button(self.master, text='START', padx=20, pady=20, command=self.compare)
        self.start_button.grid(row=4, column=6)

    def update_item(self, data):
        self.item_listbox.delete(0, END)
        for item in data:
            self.item_listbox.insert(END, item)

    def update_currency_type(self, data):
        self.currency_type_listbox.delete(0, END)
        for item in data:
            self.currency_type_listbox.insert(END, item)

    def fill_item_entry(self, event):
        self.item_entry.delete(0, END)
        self.item_entry.insert(0, self.item_listbox.get(ANCHOR))

    def fill_currency_type_entry(self, event):
        self.currency_type_entry.delete(0, END)
        self.currency_type_entry.insert(0, self.currency_type_listbox.get(ANCHOR))

    def check_item(self, event):
        typed = self.item_entry.get()
        if typed == '':
            data = self.item_list
        else:
            data = []
            for item in self.item_list:
                if typed.lower() in item.lower():
                    data.append(item)
        self.update_item(data)

    def check_currency_type(self, event):
        typed = self.currency_type_entry.get()
        if typed == '':
            data = self.currency_type_list
        else:
            data = []
            for item in self.currency_type_list:
                if typed.lower() in item.lower():
                    data.append(item)
        self.update_currency_type(data)

    def compare(self):
        buy = self.buy_entry.get()
        sell = self.sell_entry.get()
        item = self.item_entry.get()
        refresh_rate = int(self.refresh_rate_entry.get())
        number_of_refreshes = int(self.number_of_refreshes_entry.get())
        for i in range(number_of_refreshes):
            data = self.check.check(item)
            self.check.compare(data, buy, sell)
            self.check.sleep(refresh_rate)
            print(i)

    def finish(self):
        self.check.finish()

    def execute(self):
        self.update_item(self.item_list)
        self.item_listbox.bind("<<ListboxSelect>>", self.fill_item_entry)
        self.item_entry.bind("<KeyRelease>", self.check_item)
        self.update_currency_type(self.currency_type_list)
        self.currency_type_listbox.bind("<<ListboxSelect>>", self.fill_currency_type_entry)
        self.currency_type_entry.bind("<KeyRelease>", self.check_currency_type)


main_window = Tk()
app = MainWindow(main_window)
app.execute()
main_window.mainloop()
