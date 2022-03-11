import tkinter as tk
from datetime import datetime

def calculate():
    try:
        # get the input date in DD/MM/YYYY format
        birth_date = inputdate_entry.get()
        # split the date into day, month and year
        birth_day, birth_month, birth_year = birth_date.split('/')
        # calculate the time difference from the input date to now
        actual = datetime.now() - datetime(year=int(birth_year), month=int(birth_month), day=int(birth_day))
        # show the number of days calculated
        output_entry.delete(0, tk.END)
        output_entry.insert(0, f'{actual.days} days')
    except Exception as ex:
        print(ex)


root = tk.Tk()
root.geometry('300x300')
root.title('How many days ?')
root.resizable(False, False)

inputdate = tk.Label(text="Type in your date (dd/mm/yyyy)")
inputdate.place(x=50, y=30)

# date entry (type your date)
inputdate_entry = tk.Entry(width=11)
inputdate_entry.place(x=90, y=60)

inputdate = tk.Label(text="Days! lived")
inputdate.place(x=110, y=230)

# calculates how many days you have lived , by pressing the calculate button
enter_btn = tk.Button(text='Calculate', width=8, command=calculate) # call calculate()
enter_btn.place(x=90, y=100)

# here comes output and shows how many days you have lived
output_entry = tk.Entry(width=11)
output_entry.place(x=90, y=200)

root.mainloop()