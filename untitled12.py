from tkinter import*
root = Tk()
root.title("Fever_survey")
root.geometry("500x500")

#Q1
question1_radioButton=stringVar(value="0")
Question1=Label(root, text="do you have headache and sore throat?")
Question1.pack()
question1_r1=Radiobuttton(root, text = "yes", variable=question1_radiobutton, value="yes")
question1_r1.pack()
question1_r2=Radiobuttton(root, text = "no", variable=question1_radiobutton, value="no")
question1_r2.pack()

#Q2
question2_radioButton=stringVar(value="0")
Question2=Label(root, text="Is your body temperature high?")
Question2.pack()
question2_r1=Radiobuttton(root, text = "yes", variable=question2_radiobutton, value="yes")
question2_r1.pack()
question2_r2=Radiobuttton(root, text = "no", variable=question2_radiobutton, value="no")
question2_r2.pack()

#Q3
question3_radioButton=stringVar(value="0")
Question3=Label(root, text="Are there any symptoms off eyee rashes")
Question3.pack()
question3_r1=Radiobuttton(root, text = "yes", variable=question3_radiobutton, value="yes")
question3_r1.pack()
question3_r2=Radiobuttton(root, text = "no", variable=question3_radiobutton, value="no")
question3_r2.pack()


#defination(if conditional)
def fever_score():
    score=0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
        
     if score <= 20:
         messagebox.showinfo("Report","Visiting a doctor is not required.")
     elif  score > 20 and score <= 40:
         messagebox.showinfo("Report","You may have ti visit a doctor.")
     else :
         messagebox.showinfo("Report","I strongly advis you to visit a doctor.")

btn = Button(root, text="click me", command= fever_score)
btn.pack()
root.mainloop()