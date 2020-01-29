# Alex Emerich, ajemerich21@gmail.com, +353833639401

from tkinter import *
import tkinter.messagebox

fo = open("bmi.csv", "a")


class BMI:

    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        # ====================================================Frame Setup==============================================

        mainFrame = Frame(self.root, bd=20, width=1350, height=700, padx=10, pady=10, bg="Gray", relief=RIDGE)
        mainFrame.grid()

        bodyFrame = Frame(mainFrame, bd=10, width=600, height=600, padx=10, pady=10, relief=RIDGE)
        bodyFrame.pack(side=LEFT)

        bodyFrame0 = Frame(bodyFrame, bd=5, width=712, height=143, padx=5, bg="black", relief=RIDGE)
        bodyFrame0.grid(row=0, column=0)

        bodyFrame1 = Frame(bodyFrame, bd=5, width=712, height=80, padx=5, pady=5, relief=RIDGE)
        bodyFrame1.grid(row=5, column=0)

        bodyFrame2 = Frame(bodyFrame, bd=5, width=712, height=168, padx=5, pady=5, relief=SUNKEN)
        bodyFrame2.grid(row=3, column=0)

        bodyFrame3 = Frame(bodyFrame, bd=5, width=712, height=95, padx=5, pady=5, relief=SUNKEN)
        bodyFrame3.grid(row=4, column=0)

        bodyFrame4 = Frame(bodyFrame, bd=5, width=712, height=168, padx=5, pady=5, relief=SUNKEN)
        bodyFrame4.grid(row=2, column=0)

        bodyFrame5 = Frame(bodyFrame, bd=5, width=712, height=80, padx=5, pady=5, relief=SUNKEN)
        bodyFrame5.grid(row=1, column=0)

        bodyFrame6 = Frame(bodyFrame, bd=5, width=712, height=168, padx=5, pady=5, relief=RIDGE)
        bodyFrame6.grid(row=6, column=0)

        # ====================================================Health Metrics===========================================

        firstName = StringVar()
        lastName = StringVar()
        HeightMetric = StringVar()
        HeightImperialFeet = StringVar()
        HeightImperialInches = StringVar()
        WeightMetric = StringVar()
        WeightImperialStones = StringVar()
        WeightImperialPounds = StringVar()

        # ====================================================Functions================================================

        def close():
            close.set = root.destroy()
            return

        def clear():
            firstName.set("")
            lastName.set("")
            HeightMetric.set("")
            HeightImperialFeet.set("")
            HeightImperialInches.set("")
            WeightMetric.set("")
            WeightImperialStones.set("")
            WeightImperialPounds.set("")
            self.textResult.delete("1.0", END)

        def calculate():
            BMIHeightcm = HeightMetric.get()
            BMIWeightkg = WeightMetric.get()
            BMIHeightfeet = HeightImperialFeet.get()
            BMIHeightinches = HeightImperialInches.get()
            BMIWeightstones = WeightImperialStones.get()
            BMIWeightpounds = WeightImperialPounds.get()
            BMIFirstName = firstName.get()
            BMILastName = lastName.get()
            self.textResult.delete("1.0", END)

            if BMIHeightcm.isdigit() and BMIWeightkg.isdigit():
                BMIHeightcm = float(BMIHeightcm)
                BMIWeightkg = float(BMIWeightkg)
                BMI = float('%.1f' % (BMIWeightkg / ((BMIHeightcm / 100) * (BMIHeightcm / 100))))
                self.textResult.insert(END, BMI)
                fo.write("%s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (BMIFirstName, BMILastName, BMIHeightcm, BMIWeightkg,
                                                                   BMIHeightfeet, BMIHeightinches, BMIWeightstones,
                                                                   BMIWeightpounds, BMI))

            elif BMIHeightfeet.isdigit() and BMIHeightinches.isdigit() and BMIWeightstones.isdigit() \
                    and BMIWeightpounds.isdigit():
                heightconversion = (float(BMIHeightfeet) + (float(BMIHeightinches) / 12)) * 0.3048
                weightconversion = (float(BMIWeightstones) + (0.0714286 * float(BMIWeightpounds))) * 6.35029
                BMI = float('%.1f' % (weightconversion / (heightconversion * heightconversion)))
                self.textResult.insert(END, BMI)
                fo.write("%s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (BMIFirstName, BMILastName, BMIHeightcm, BMIWeightkg,
                                                                   BMIHeightfeet, BMIHeightinches, BMIWeightstones,
                                                                   BMIWeightpounds, BMI))

            elif ValueError:
                tkinter.messagebox.showwarning("BMI Calculator", "Please only enter valid numbers")
                HeightMetric.set("")
                HeightImperialFeet.set("")
                HeightImperialInches.set("")
                WeightMetric.set("")
                WeightImperialStones.set("")
                WeightImperialPounds.set("")
                self.textResult.delete("1.0", END)

        # ====================================================Labels====================================================

        self.labelTitle = Label(bodyFrame0, text="Calculate your BMI!", padx=15, pady=5, bd=1,
                                bg="black", width=20, font=("arial", 20, 'bold'), fg='orange')
        self.labelTitle.pack()

        self.LabelFname = Label(bodyFrame5, width=20, text='Enter your first name', font=('arial', 12, 'bold'),
                                justify=LEFT)
        self.LabelFname.grid(row=0, column=0)

        self.LabelLname = Label(bodyFrame5, text='Enter your last name', font=('arial', 12, 'bold'), justify=LEFT)
        self.LabelLname.grid(row=1, column=0)

        self.TextFname = Entry(bodyFrame5, textvariable=firstName, font=('arial', 12, 'bold'), width=10, justify=LEFT)
        self.TextFname.grid(row=0, column=1)

        self.TextLname = Entry(bodyFrame5, textvariable=lastName, font=('arial', 12, 'bold'), width=10, justify=LEFT)
        self.TextLname.grid(row=1, column=1)

        self.LabelHeightMetric = Label(bodyFrame4, text="Enter Height in centimeters \t \t", font=("arial", 12, 'bold'),
                                       justify=LEFT)
        self.LabelHeightMetric.grid(row=0, column=0, padx=15)

        self.textHeightMetric = Entry(bodyFrame4, textvariable=HeightMetric, font=('arial', 12, 'bold'), width=15,
                                      justify=LEFT)
        self.textHeightMetric.grid(row=0, column=1, pady=10)

        self.LabelHeightImperialFeet = Label(bodyFrame4, text="or enter Height in feet and inches \t",
                                             font=('arial', 12, 'bold'), justify=LEFT)
        self.LabelHeightImperialFeet.grid(row=1, column=0, padx=15)

        self.textHeightImperialFeet = Entry(bodyFrame4, textvariable=HeightImperialFeet, font=('arial', 12, 'bold'),
                                            width=7, justify=LEFT)
        self.textHeightImperialFeet.grid(row=1, column=1)

        self.textHeightImperialInches = Entry(bodyFrame4, textvariable=HeightImperialInches, font=('arial', 12, 'bold'),
                                              width=7, justify=LEFT)
        self.textHeightImperialInches.grid(row=1, column=2, padx=5)

        self.LabelWeightMetric = Label(bodyFrame2, text="Enter Weight in kilograms", font=("arial", 12, 'bold'),
                                       justify=LEFT)
        self.LabelWeightMetric.grid(row=0, column=0, padx=15)

        self.textWeightMetric = Entry(bodyFrame2, textvariable=WeightMetric, font=('arial', 12, 'bold'), width=15,
                                      justify=LEFT)
        self.textWeightMetric.grid(row=0, column=1, pady=10)

        self.LabelWeightImperialStones = Label(bodyFrame2, text="or enter Weight in stone and pounds",
                                               font=('arial', 12, 'bold'), justify=LEFT)
        self.LabelWeightImperialStones.grid(row=1, column=0, padx=15)

        self.textWeightImperialStones = Entry(bodyFrame2, textvariable=WeightImperialStones, font=('arial', 12, 'bold'),
                                              width=7, justify=LEFT)
        self.textWeightImperialStones.grid(row=1, column=1, pady=5)

        self.textWeightImperialPounds = Entry(bodyFrame2, textvariable=WeightImperialPounds, font=('arial', 12, 'bold'),
                                              width=7, justify=LEFT)
        self.textWeightImperialPounds.grid(row=1, column=2, pady=5)

        self.labelResult = Label(bodyFrame3, text='BMI=', font=('arial', 20, 'bold'), justify=LEFT)
        self.labelResult.grid(row=0, column=0)

        self.textResult = Text(bodyFrame3, pady=1, font=('arial', 20, 'bold'), width=13, height=1)
        self.textResult.grid(row=0, column=1)

        self.labelTable = Label(bodyFrame6, font=('arial', 20, 'bold'), text="BMI Meaning")
        self.labelTable.grid(row=0, column=0)

        self.textTable = Text(bodyFrame6, font=('arial', 12, 'bold'), height=4, width=55)
        self.textTable.grid(row=1, column=0)

        self.textTable.insert(END, 'Underweight \t \t \t \t ' + 'less than 18.5 \n')
        self.textTable.insert(END, 'Normal (healthy weight) \t \t \t \t ' + 'between 18.5 and 24.9 \n')
        self.textTable.insert(END, 'Overweight \t \t \t \t ' + 'between 25 and 29.9\n')
        self.textTable.insert(END, 'Obese \t \t \t \t ' + '30 or greater \n')

        # ====================================================Buttons===================================================

        self.buttonCalculate = Button(bodyFrame1, text='Calculate', padx=5, pady=5, bd=5, width=10,
                                      font=('arial', 12, 'bold'), command=calculate)
        self.buttonCalculate.grid(row=1, column=0)

        self.buttonClear = Button(bodyFrame1, text='Clear', padx=5, pady=5, bd=5, width=10, font=('arial', 12, 'bold'),
                                  command=clear)
        self.buttonClear.grid(row=1, column=1)

        self.buttonClose = Button(bodyFrame1, text='Close', padx=5, pady=5, bd=5, width=10, font=('arial', 12, 'bold'),
                                  command=close)
        self.buttonClose.grid(row=1, column=2)


if __name__ == '__main__':
    root = Tk()
    application = BMI(root)
    root.mainloop()
