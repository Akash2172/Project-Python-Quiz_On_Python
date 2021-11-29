from tkinter import *
from tkinter import messagebox
import mysql.connector as sqltor
import random

main = Tk()
db = sqltor.connect(host="localhost", user="root",
                    password="1234", database="project")
cur = db.cursor()
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
global opt, marks, n, username
marks = 0
n = 0
opt = StringVar()
randomlist = random.sample(range(1, 26), 10)


def opener():
    main.iconify()
    root = Toplevel()
    root.geometry("950x500+155+60")
    root.resizable(height=FALSE, width=FALSE)
    root.config(bg="#F0F0F2")
    root.title("Quiz")

    global n, timer, opt, marks

    n = 0
    timer = 30

    questions = {
        1:  " In Python 3, the maximum value for an integer is ?",
        2:  " How do you insert COMMENTS in Python code ?",
        3:  " Which one is NOT a legal variable name ?",
        4:  " What is the correct file extension for Python files ?",
        5:  " What is the correct syntax to output the type of a variable or object in Python ?",
        6:  " What is the correct way to create a function in Python ?",
        7:  " Which built-in function can be used to calculate the\nlength of any iterable object in Python ?",
        8:  " Which method can be used to return a string in upper case letters ?",
        9:  " Which method can be used to replace parts of a string ?",
        10: " Which operator is used to multiply numbers ?",
        11: " Which operator can be used to compare two values ?",
        12: " Which of these collections defines a LIST ?",
        13: " Which of these collections defines a TUPLE ?",
        14: " Which of these collections defines a SET ?",
        15: " Which collection is ordered, changeable, and allows duplicate members ?",
        16: " Which collection does not allow duplicate members ?",
        17: " What is output for − 'raining'. find('z') ?",
        18: " What is output for − 2 * 2 **3 ?",
        19: " What command is used to insert 6 in a list \"L\" at 3rd position ?",
        20: " Which of the following data types is not supported in python?",
        21: " What is the output of print str[0] if str = 'Hello World!'?",
        22: " What is the output of print list if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?",
        23: " Which operator is overloaded by the or() function?",
        24: " Which function overloads the >> operator?",
        25: " What is called when a function is defined inside a class?"

    }

    options = {
        1:
        {
            'A':		"2^63 – 1",
            'B':		"2^63 + 1",
            'C':		"–(2^63 + 1)",
            'D':   	"No limit"

        },
        2:
        {
            'A':		"// this is a comment",
            'B':		"/* this is a comment*/",
            'C':		"#  This is comment",
            'D':		"* This is a comment*"

        },
        3:
        {
            'A': 		"my-var",
            'B':    	"My_var",
            'C':    	"Myvar",
            'D':   	 "_Myvar"

        },
        4:
        {
            'A':		"Python",
            'B':		"Pyh",
            'C':		"Ptx",
            'D':		"Py"

        },
        5:
        {
            "A":	"print(typeof(x))",
            "B":    	"print(type(x))",
            "C":    	"print(typeOf(x))",
            "D":	"none of the above"

        },
        6:
        {
            "A":	"generate myFunction():",
            "B": 	"def myFunction():",
            "C": 	"create myFuntion():",
            "D": 	"function myfucntion():"

        },
        7:
        {
            "A":	"Ptrim()",
            "B":	"trim()",
            "C":	"strip()",
            "D":	"len()"

        },
        8:
        {
            "A": 	"uppercase()",
            "B": 	"upper()",
            "C": 	"touppercase()",
            "D": 	"UpperCase()"

        },
        9:
        {
            "A":	"switch()",
            "B":	"repl()",
            "C":	"replace()",
            "D":	"replacestring()"
        },
        10:
        {
            "A":	"X",
            "B":	"%",
            "C":	"*",
            "D":	"**"

        },
        11:
        {
            "A":	"=",
            "B":	"==",
            "C":	"><",
            "D":	"<>"

        },
        12:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B":	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        13:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B":	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        14:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B": 	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        15:
        {
            "A":	"list",
            "B":	"set",
            "C":	"dictionary",
            "D":	"tuple"

        },
        16:
        {
            "A":	"list",
            "B":	"set",
            "C":	"dictionary",
            "D":	"tuple"
        },
        17:
        {
            "A": 	"Type error",
            "B": 	" ",
            "C": 	"-1",
            "D": 	"Not found"
        },
        18:
        {
            "A": 	"12",
            "B": 	"64",
            "C": 	"16",
            "D": 	"36"

        },
        19:
        {
            "A":	"L.insert(2,6)",
            "B": 	"L.insert(3,6)",
            "C": 	"L.add(3,6)",
            "D": 	"L.append(2,6)"

        },
        20:
        {
            "A": 	"Numbers",
            "B": 	"String",
            "C": 	"List",
            "D": 	"Option A and B"

        },
        21:
        {
            "A": 	"Hello World!",
            "B": 	"H",
            "C": 	"ello World!",
            "D": 	"None of the above."

        },
        22:
        {
            "A":	"( 'abcd', 786 , 2.23, 'john', 70.2 )",
            "B": 	"tuple",
            "C": 	"Error",
            "D": 	"None of the above"

        },
        23:
        {
            "A": 	"||",
            "B": 	"|",
            "C": 	"//",
            "D": 	"/"

        },
        24:
        {
            "A": 	"__more__()",
            "B": 	"__gt__()",
            "C": 	"__ge__()",
            "D": 	"None of the above"

        },
        25:
        {
            "A": 	"Module",
            "B": 	"Class",
            "C": 	"Another Function",
            "D": 	"Method"

        }

    }

    answerkey = {
        1: "D",
        2: "C",
        3: "A",
        4: "D",
        5: "B",
        6: "B",
        7: "D",
        8: "B",
        9: "C",
        10: "C",
        11: "B",
        12: "B",
        13: "C",
        14: "A",
        15: "A",
        16: "B",
        17: "C",
        18: "C",
        19: "A",
        20: "D",
        21: "B",
        22: "A",
        23: "B",
        24: "D",
        25: "D"

    }

    marks = 0
    opt = StringVar()
    randomlist = random.sample(range(1, 26), 10)

    def starting():

        global quelabel, nextbutton, option1, option2, option3, option4, finished_times, optionframe, countdown

        quelabel = Label(root, text="Q"+str(n+1)+"."+questions[randomlist[n]], font=(
            "Open sans", 18, "normal"), fg="black", bg="#F0F0F2", pady=30)
        quelabel.pack(side=TOP)

        optionframe = Frame(root, bg="#F0F0F2")
        optionframe.pack()
        option1 = Radiobutton(optionframe, text="A.    "+options[randomlist[n]]['A'], variable=opt, value="A", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option1.grid(row=0, column=0, sticky=W)

        option2 = Radiobutton(optionframe, text="B.    "+options[randomlist[n]]['B'], variable=opt, value="B", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option2.grid(row=1, column=0, sticky=W)

        option3 = Radiobutton(optionframe, text="C.    "+options[randomlist[n]]['C'], variable=opt, value="C", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option3.grid(row=2, column=0, sticky=W)

        option4 = Radiobutton(optionframe, text="D.    "+options[randomlist[n]]['D'], variable=opt, value="D", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option4.grid(row=3, column=0, sticky=W)
        option_clear = Button(optionframe, border=0, text="Clear Selection", command=clear_option, font=(
            'Open sans', 11, UNDERLINE), bg="#F0F0F2", fg="#3176F2")
        option_clear.grid(pady=(10, 0), row=4, column=0, sticky=W)
        root.config(bg="#F0F0F2")

        nextbutton = Button(root, text="Next", font=("Cinzel", 16, "bold"),
                            bg="#F0F0F2", fg="#194159", border=0, command=nextquestion)
        nextbutton.pack(anchor=E, side=BOTTOM, padx=(10), pady=5)

        countdown = Label(root, text=timer, font=(
            "Open sans", 16, "bold"), fg="#D9BD32", bg="#F0F0F2",)
        countdown.pack(anchor=W, side=BOTTOM, padx=35, pady=0)

        timecount()

        savebutton.destroy()
        x.destroy()
        global savename, password
        savename = name.get()
        password = past.get()
        name.destroy()
        past.destroy()
        y.destroy()

    def clear_option():
        option1.deselect()
        option2.deselect()
        option3.deselect()
        option4.deselect()

    def reseting():
        global timer
        timer = 30

    def timecount():
        global timer
        if (timer > 0):
            timer = timer-1
            countdown.config(text=timer)
            countdown.after(1000, timecount)
        else:
            nextquestion()
            timecount()

    def nextquestion():
        def khtam():
            messagebox.showinfo("Hurray", "Thank You for giving the test")
            root.destroy()
            main.deiconify()
        global quelabel, finished_times, n, option1, option2, option3, option4, marks, markstoshow, namestoshow
        x = opt.get()
        if x == answerkey[randomlist[n]]:
            marks = marks+1
        n = n+1

        if n < 10:
            quelabel.config(text="Q"+str(n+1)+"."+questions[randomlist[n]])

            option1.config(text="A.    "+options[randomlist[n]]['A'])

            option2.config(text="B.    "+options[randomlist[n]]['B'])

            option3.config(text="C.    "+options[randomlist[n]]['C'])

            option4.config(text="D.    "+options[randomlist[n]]['D'])
            clear_option()
            reseting()

        else:
            optionframe.destroy()
            quelabel.destroy()
            nextbutton.destroy()
            countdown.destroy()
            sql = "insert into result(name,id,marks) values('{}',{},{})".format(
                savename, password, marks)
            cur.execute(sql)
            db.commit()
            s = Label(root, text=savename.title()+" Your score is %d.       " %
                      marks, bg="#F0F0F2", font=("Open sans", 20, "bold"))
            s.pack(padx=0, pady=(200, 0))

            savebutton = Button(root, text="Save", font=(
                "Cinzel", 18, "bold"), bg="#F0F0F2", fg="#194159", border=0, command=khtam)
            savebutton.pack(side=BOTTOM, pady=(0, 15))

    x = Label(root, text="Enter your name :", bg=(
        "#F0F0F2"), font=("Open Sans", 14, "bold"))
    x.pack(side=TOP, pady=(100, 0))
    name = Entry(root, width=30, bg="#ADD8E6", font=("Open Sans", 14))
    name.pack(pady=20)
    y = Label(root, text="Enter a unique code: ", bg=(
        "#F0F0F2"), font=("Open Sans", 14, "bold"))
    y.pack()
    past = Entry(root, width=30, bg="#ADD8E6", font=("Open Sans", 14))
    past.pack(pady=20)
    savebutton = Button(root, text="Save", font=(
        "Cinzel", 18, "bold"), bg="#F0F0F2", fg="#194159", border=0, command=starting)
    savebutton.pack(side=BOTTOM, pady=(0, 15))


def extractdata():
    def details():
        def khatam():
            first.destroy()
            main.deiconify()
        username = entt1.get()
        password = entt2.get()
        start.destroy()
        first = Toplevel()
        first.geometry("950x500+155+60")
        first.resizable(height=FALSE, width=FALSE)
        first.config(bg="#ffffff")

        sql = "select marks from result where name='{}' and id = {}".format(
            username, password)
        cur.execute(sql)
        marks = 0
        for x in cur:
            marks = x[0]

        s = Label(first, text=username.title()+" Your score is %d       " %
                  marks, bg="#ffffff", font=("Open sans", 20, "bold"))
        s.pack(padx=0, pady=(200, 0))

        savebutton = Button(first, text="Okay", font=(
            "Cinzel", 18, "bold"), bg="#F0F0F2", fg="#194159", border=0, command=khatam)
        savebutton.pack(side=BOTTOM, pady=(0, 15))

    main.iconify()
    start = Toplevel()
    start.title('Details')
    start.geometry('350x300+500+120')
    start.resizable(False, False)
    fr = Frame(start, bd=7, background='black', relief='raise')
    wel = Label(fr, text='Enter Details', font=(
        'arial', 25, 'bold'), fg='blue')
    wel.grid(row=0, columnspan=2)
    fr.pack(side=TOP)

    fr1 = Frame(start)
    fr1.place(x=10, y=90)

    user = Label(fr1, text='User Name', font=('arial', 15, 'bold'), fg='black')
    passt = Label(fr1, text='Unique Number', font=('arial', 15, 'bold'))

    entt1 = Entry(fr1, font=('arial', 12, 'bold'), bd=4,
                  width=15, bg='#ffffff', justify='right')
    entt2 = Entry(fr1, font=('arial', 12, 'bold'), bd=4,
                  width=15, bg='#ffffff', justify='right')

    user.grid(row=1, sticky=E)
    entt1.grid(row=1, column=1)
    passt.grid(row=2, sticky=E)
    entt2.grid(row=2, column=1)

    b = Button(start, text='Submit', command=details, width=8, bd=5,
               bg='antiquewhite1', font=('arial', 10, 'bold'), fg='green', padx=2, pady=1)
    b.place(x=120, y=180)

    fr2 = Frame(start)
    note = Label(fr2, text='*Use the username and id used to start the quiz.',
                 font=('arial', 10, 'bold')).pack()
    fr2.pack(side=BOTTOM)


def feedback():
    main.iconify()

    def subb():
        messagebox.showinfo("Submitted", 'Feedback Submitted')
        feed.destroy()
        main.deiconify()
    feed = Toplevel()
    feed.title('Feedback')
    feed.resizable(False, False)

    fr = Frame(feed)
    fr.place(x=15, y=80)
    feed.geometry('450x430+500+120')

    fr1 = Frame(feed, bd=7, background='black', relief='raise')
    wel = Label(fr1, text='Feedback', font=('arial', 25, 'bold'), fg='blue')
    wel.grid(row=0, columnspan=2)
    fr1.pack(side=TOP)

    i = StringVar()
    u1 = Label(fr, text='How would you rate your first impression of us?', font=(
        'arial', 12, 'bold'))
    r1 = Radiobutton(fr, text='Excellent', value='Excellent', variable=i)
    r2 = Radiobutton(fr, text='Good', value='Good', variable=i)
    r3 = Radiobutton(fr, text='Satisfactory', value='Satisfactory', variable=i)
    r4 = Radiobutton(fr, text='Poor', value='Poor', variable=i)
    u1.grid(row=2, columnspan=4)
    r1.grid(row=3, column=0, sticky=W)
    r2.grid(row=3, column=1, sticky=W)
    r3.grid(row=3, column=2)
    r4.grid(row=3, column=3, sticky=E)

    l = StringVar()
    u2 = Label(fr, text='Did you feel safe and comfortable?',
               font=('arial', 12, 'bold'))
    c1 = Radiobutton(fr, text='Yes', value='Y', variable=l)
    c2 = Radiobutton(fr, text='No', value='N', variable=l)
    u2.grid(row=4, columnspan=3)
    c1.grid(row=5, column=0, sticky=W)
    c2.grid(row=5, column=1, sticky=W)

    j = StringVar()
    u3 = Label(fr, text='Would you travel with us in the future?',
               font=('arial', 12, 'bold'))
    a1 = Radiobutton(fr, text='Yes', value='Yes', variable=j)
    a2 = Radiobutton(fr, text='No', value='No', variable=j)
    u3.grid(row=6, columnspan=3)
    a1.grid(row=7, column=0, sticky=W)
    a2.grid(row=7, column=1, sticky=W)

    k = StringVar()
    u4 = Label(fr, text='Would you recommend us to others?',
               font=('arial', 12, 'bold'))
    b1 = Radiobutton(fr, text='Yes', value='Yes', variable=k)
    b2 = Radiobutton(fr, text='No', value='No', variable=k)
    u4.grid(row=8, columnspan=3)
    b1.grid(row=9, column=0, sticky=W)
    b2.grid(row=9, column=1, sticky=W)

    u6 = Label(fr, text='Anything More?', font=('arial', 12, 'bold'))
    fdk = StringVar()
    fd = Entry(fr, font=('arial', 16), textvariable=fdk, width=30)
    u6.grid(row=10, columnspan=2)
    fd.grid(row=11, columnspan=4, sticky='s', rowspan=3, ipady=20)

    ub = Button(fr, text='Submit', command=subb, width=8, bd=5, bg='antiquewhite1', font=(
        'arial', 10, 'bold'), fg='green', padx=2, pady=1)
    ub.grid(row=18, column=1, sticky=E)


# -------------------------------------------------EXIT--------------------------------------------------------------
def iexit():
    qExit = messagebox.askyesno("Quit", "Do  you want to quit")
    if qExit > 0:
        main.destroy()

# -------------------------------------------------------------------------------------------------------------------


def rules():
    def subb():
        ruleswindow.destroy()
        main.deiconify()
    main.iconify()
    ruleswindow = Toplevel()
    ruleswindow.geometry('500x150+400+200')
    rt = Frame(ruleswindow)
    rt.pack()
    R = Label(rt, pady=12, justify=LEFT, text="• There are a total of 10 questions.\n• Each question carries 1 mark, for every correct answer.\n• There is no negative marking.\n• There is a 30 sec time limit on every question.", font=("Open sans", 12, 'bold'))
    R.pack()
    sub = Button(rt, text='OK', command=subb, width=8, bd=1, bg='antiquewhite1', font=(
        'Open sans', 10, 'bold'), fg='green', padx=2, pady=1)
    sub.pack()


# -------------------------------------------------------------------------------------------------------------------
main.title('Python Quiz')
fr = Frame(main, bd=0, background='black', relief='raise')
fr.pack(side=TOP, pady=(30, 10))
fr1 = Frame(main)
w = Label(fr, font=('Times New Roman', 25, 'bold'),
          text='PYTHON QUIZ', fg='Navy')
w.grid(row=0, columnspan=2)
fr1.pack()

b = Button(fr1, text='START RANDOM QUIZ', command=opener, width=20, bd=2,
           bg='antiquewhite1', font=('Open Sans', 11, 'bold'), fg='green', padx=3, pady=1)
b1 = Button(fr1, text='SEE SCORES', command=extractdata, width=20, bd=2,
            bg='antiquewhite1', font=('Open Sans', 11, 'bold'), fg='green', padx=3, pady=1)

b3 = Button(fr1, text='RULES', command=rules,  width=20, bd=2, bg='antiquewhite1',
            font=('Open Sans', 11, 'bold'), fg='green', padx=3, pady=1)
b4 = Button(fr1, text='FEEDBACK', command=feedback, width=20, bd=2,
            bg='antiquewhite1', font=('Open Sans', 11, 'bold'), fg='green', padx=3, pady=1)
b5 = Button(fr1, text='EXIT',  command=iexit, width=20, bd=2,
            bg='antiquewhite1', font=('Open Sans', 11, 'bold'), fg='green', padx=3, pady=1)

b.grid(columnspan=2, pady=(15, 0))
b1.grid(columnspan=3)
b3.grid(columnspan=3)
b4.grid(columnspan=3)
b5.grid(columnspan=3)

main.resizable(False, False)
main.geometry('450x325+420+120')
main.mainloop()
