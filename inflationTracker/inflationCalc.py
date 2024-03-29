from tkinter import *
import linearModel

window = Tk()
label = Label(
    text="Please choose a month and year to compare buying power\n\n\n\n\n in Janurary 2000\n has the same buying power as",
    fg="black",
    bg="white",
    width=100,
    height=30,
    anchor='n'
)
label2 = Label(text="$", fg="black", bg= "white")
label2.place(x=310, y=50)
label3 = Label(text="$", fg="black", bg= "white")
label3.place(x=310, y=120)
label4 = Label(text="in", fg="black", bg="white")
label4.place(x=250, y=150)
inputtxt1 = Entry(width = 10, bg = "cyan")
inputtxt1.place(x=325, y=50)
inputtxt2 = Entry(width= 10, bg= "cyan")
inputtxt2.place(x= 325, y= 120)

def OptionMenu_CheckButton(event):
    month = variable.get()
    valueYear = int(variable2.get())
    if month == 'January':
        valueMonth = 0
    elif month == 'February':
        valueMonth = 1
    elif month == 'March':
        valueMonth = 2
    elif month == 'April':
        valueMonth = 3
    elif month == 'May':
        valueMonth = 4
    elif month == 'June':
        valueMonth = 5
    elif month == 'July':
        valueMonth = 6
    elif month == 'August':
        valueMonth = 7
    elif month == 'September':
        valueMonth = 8
    elif month == 'October':
        valueMonth = 9
    elif month == 'November':
        valueMonth = 10
    elif month == 'December':
        valueMonth = 11
    if valueYear - 2000 < 23:
        originalResult = linearModel.y[(valueYear - 2000) * 12 + valueMonth]
        finalResult = float(inputtxt1.get()) * originalResult
        finalResult = round(finalResult, 2)
        inputtxt2.delete(0, END)
        inputtxt2.insert(0, str(finalResult))
    elif valueYear - 2000 == 23 and valueMonth != 11:
        originalResult = linearModel.y[(valueYear - 2000) * 12 + valueMonth]
        finalResult = float(inputtxt1.get()) * originalResult
        finalResult = round(finalResult, 2)
        inputtxt2.delete(0, END)
        inputtxt2.insert(0, str(finalResult))
    else:
        remodelVariable = (valueYear - 2000) + (valueMonth / 12)
        multiplicationFactor = (linearModel.model.coef_[0] * remodelVariable) + linearModel.model.intercept_
        finalResult = float(inputtxt1.get()) * multiplicationFactor
        finalResult = round(finalResult + 20, 2)
        inputtxt2.delete(0, END)
        inputtxt2.insert(0, str(finalResult))
    pass

optionsMonth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
optionsYear = [
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025",
    "2026",
    "2027",
    "2028",
    "2029",
    "2030",
    "2031",
    "2032",
    "2033",
    "2034",
    "2035",
    "2036",
    "2037",
    "2038",
    "2039",
    "2040",
    "2041",
    "2042",
    "2043",
    "2044",
    "2045",
    "2046",
    "2047",
    "2048",
    "2049",
    "2050",
]
variable = StringVar(window)
variable.set("January")
variable2 = StringVar(window)
variable2.set("2000")
v = OptionMenu(window, variable, *optionsMonth, command= OptionMenu_CheckButton)
w = OptionMenu(window, variable2, *optionsYear, command= OptionMenu_CheckButton)
v.pack()
w.pack()
v.place(x= 280, y= 150)
w.place(x=340, y= 150)
#drop = OptionsMenu(window, )
if (variable.get() == "January"):
    print(1)
label.pack()
#inputtxt.pack()

mainloop()