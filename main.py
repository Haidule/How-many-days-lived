import tkinter as tk
from datetime import datetime

def calculate():
    try:
        # få inndatadatoen i formatet DD/MM/ÅÅÅÅ
        birth_date = inputdate_entry.get()
        # del opp datoen i dag, måned og år
        birth_day, birth_month, birth_year = birth_date.split('/')
        # beregn tidsforskjellen fra inndatadatoen til nå
        actual = datetime.now() - datetime(year=int(birth_year), month=int(birth_month), day=int(birth_day))
        # vis antall beregnede dager
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

# datooppføring (skriv inn datoen din)
inputdate_entry = tk.Entry(width=11)
inputdate_entry.place(x=90, y=60)

inputdate = tk.Label(text="Days! lived")
inputdate.place(x=110, y=230)

# beregner hvor mange dager du har levd, ved å trykke på beregn-knappen
enter_btn = tk.Button(text='Calculate', width=8, command=calculate) # kall calculate()
enter_btn.place(x=90, y=100)

# her kommer utdata og viser hvor mange dager du har levd
output_entry = tk.Entry(width=11)
output_entry.place(x=90, y=200)

root.mainloop()
