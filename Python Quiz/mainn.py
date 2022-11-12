from PIL import Image , ImageTk
from tkinter import*
import random

def main():
    root = Tk()
    quiz = questions(root)
    root.mainloop()


class questions:
    def __init__(self , root):
        global txtlabel ,labelinst ,labelinstr ,E_button ,M_button ,H_button
        # this is for a single window program in which we are going to destroy the previous things and create new things
        # in multi window whole previous window is destroyed and new window is created
        self.root = root
        self.root.title("Quiz")
        self.root.geometry('700x600')
        self.root.config(bg="#7876FD")
        self.root.resizable(0, 0)
        self.root.configure(bg='#7876FD')
        # img1 = PhotoImage(file="terentula nebula.png")
        # img1label = Label(self.root, image=img1, bg="#7876FD")
        # img1label.pack(paddy = (40,0))

        labelinst1 = Label(
            self.root,
            text='Hello',
            font=("impact",20,"bold"),
            bg='#20b2aa', #7876FD
            # fg='#4DB1FF',
        )
        labelinst1.pack(fill="both")


        txtlabel = Label(
            self.root,
            text="Python Quiz",
            font=("montserrat", 40  , "bold"),
            bg="#7876FD",
            fg='#191835',
        )
        txtlabel.pack(pady=(15,25))
        

        # img2 = PhotoImage(file="file name")

        labelinst = Label(
            self.root,
            text="Instructions",
            font=("calibri", 25,"bold"),
            bg="#7876FD",
            justify="center",
            foreground="#fbfd76"
        )
        labelinst.pack()

        labelinstr = Label(
            self.root,
            text="1.Can not jump to previous question\n2.",
            width=100,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            foreground="#fbfd76"
        )
        labelinstr.pack(pady=(0, 10))

        # a = questions()
        # use image=img1 in place of text in button
        # Eimg = Image.open("EASYimg.png")
        # EEimg = ImageTk.PhotoImage(Eimg)
        E_button = Button(
            self.root,
            text="Easy",
            # image=EEimg,
            bg='#7876FD',
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Easy
        )
        # E_button.img = EEimg
        E_button.pack(pady=(0, 30))

        # Mimg = Image.open("MEDimg.png")
        # MMimg = ImageTk.PhotoImage(Mimg)
        M_button = Button(
            self.root,
            text="Medium",
            # image=MMimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Medium
        )
        # M_button.img = MMimg
        M_button.pack(pady=(0, 30))


        # Himg = Image.open("HARDimg.png")
        # HHimg = ImageTk.PhotoImage(Himg)
        H_button = Button(
            self.root,
            text="HARD",
            # image=HHimg,
            bg="#7876FD",
            relief=FLAT,
            activebackground="#7876FD",
            command=self.Hard
        )
        # H_button.img = HHimg
        H_button.pack(pady=(0, 30))
        
    #EASY QUESTIONS 1-10
    questionsEASY = [
        "Who developed Python Programming Language?",
        "Which type of Programming does Python support?",
        "Which of the following is the correct extension of the Python file?",
        "All keywords in Python are in _________",
        "Which of the following character is used to give single-line comments in Python?",
        "Which of the following functions is a built-in function in python?",
        "Which of the following is not a core data type in Python programming?",
        "What is the maximum length of a Python identifier?",
        "What is output of print(math.pow(3, 2))?",
        "Which of the following is a Python tuple?",
    ]
    #EASY QUESTIONS OPTIONS
    choice_ansEASY = [
        ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        ["object-oriented program", "structured program", "functional program", "all of the mentioned"],
        [".python", ".pl", ".py", ".p"],
        ["Capitalized", "lower case", "UPPER CASE", "None of the mentioned"],
        ["//", "#", "!", "/*"],
        ["factorial()", "print()", "seed()", "sqrt()"],
        ["Tuples", "Lists", "Class", "Dictionary"],
        ["32", "16", "128", "No fixed length is specified"],
        ["9", "Error", "9.0", "None of the mentioned"],
        ["{1, 2, 3}", "{}", "[1, 2, 3]", "(1, 2, 3)"],
    ]
    #MEDIUM QUESTIONS 1-10
    questionsMED = [
        "What is the maximum length of a Python identifier?",
        "Which of the following concepts is not a part of Python?",
        "As what datatype are the *args stored, when passed into a function?",
        "As what datatype are the *kwargs stored, when passed into a function?",
        "What keyword is used in Python to raise exceptions?",
        "Which of the following is not a valid set operation in python?",
        "Which of the following modules need to be imported to handle date time computations in Python?",
        "In which language is Python written?",
        "What will be the result of the following expression in Python “2 ** 3 + 5 ** 2”?",
        "Which of the following are valid string manipulation functions in Python?",
    ]
    #MEDIUM QUESTIONS OPTIONS
    choice_ansMED = [
        ["32", "16", "128", "No fixed length is specified"],
        ["Pointers", "Loops", "Dynamic Typing", "All of the above"],
        ["List", "Tuple", "Dictionary", "None of the above"],
        ["Lists", "Tuples", "Dictionary", "None of the above"],
        ["raise", "try", "goto", "except"],
        ["Union", "Intersection", "Difference", "None of the above"],
        ["datetime", "date", "time", "timedate"],
        ["C++", "C", "Java", "None of these"],
        ["65536", "33", "169", "None of these"],
        ["count()", "upper()", "strip()", "All of the above"],
    ]
    #HARD QUESTIONS 1-10
    questionsHARD = [
        "What will be the output of the following code : 'print type(type(int))'",
        "What is the output of the following segment : 'chr(ord('A'))'",
        "What is the output of the following program : \ny = 8\nz = lambda x : x * y\nprint (z(6))",
        "What is called when a function is defined inside a class?",
        "Which of the following concepts is not a part of Python?",
        "Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?",
        "Which of the following are valid string manipulation functions in Python?",
        "Which function overloads the >> operator?",
        "Given a function that does not return any value, what value is shown when executed at the shell?",
        "In which language is Python written?",
    ]
    #HARD QUESTIONS OPTIONS
    choice_ansHARD = [
        ["type 'int'", "type 'type'", "Error", "0"],
        ["A", "B", "a", "Error"],
        ["48", "14", "64", "None of the above"],
        ["Module", "Class", "Another Fuction", "Method"],
        ["Pointers", "Loops", "Dynamic Typing", "All of the above"],
        ["[3, 4, 5, 20, 5, 25, 1, 3]", "[1, 3, 3, 4, 5, 5, 20, 25]", "[3, 5, 20, 5, 25, 1, 3]", "[1, 3, 4, 5, 20, 5, 25]"],
        ["count()", "upper()", "strip()", "All of the above"],
        ["more()", "gt()", "ge()", "None of the above"],
        ["int", "bool", "void", "None"],
        ["C++", "C", "Java", "None of these"],
    ]
    # will contain the correct answers of questions
    answersE = [2, 3, 2, 3, 1, 1, 2, 3, 2, 3]
    answersMED = [3, 0, 1, 2, 0, 3, 0, 1, 1, 3]
    answersHARD = [1, 0, 0, 3, 1, 2, 3, 3, 3, 2]
    user_ans = []
    indexes = []
    count = 1

    def gen(self):
        while(len(self.indexes) < 10):
            x = random.randint(0, 9)
            # if x not in indexes:
            #     indexes.append(x)
            if x in self.indexes:
                continue
            else:
                self.indexes.append(x)

    def showresult(self,score):
        global questionlabel, labelinst1,r1 ,r2 , r3 , r4
        questionlabel.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()


        labelimg = Label(
            self.root,
            bg="#7876FD",
            border=0
        )
        labelimg.pack()

        labelresulttext = Label(
            self.root,
            font=("impact", 20),
            bg="#7876FD",
            justify=CENTER,
        )
        labelresulttext.pack(pady=200)

        if score >= 15:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You did excellent !!!!!\n you got " + str(score)
            )

        elif score < 10 or score >= 8:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="You can do better !!!!!\n you got " + str(score)
            )

        elif score < 8:
            # img = PhotoImage(file="image.png")
            # labelimg.configure(image=img)
            # labelimage.image = img
            labelresulttext.configure(
                text="you should work hard !!!!!\n you got " + str(score)
            )

        Button(
            self.root,
            text="Leaderboard",
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            # relief=FLAT,  
            activebackground="#7876FD",
            #command =
        ).place(x=500,y=500)
        return score

    def calc_E(self):
        # global indexes, user_ans, answers
        x1 = 0
        score = 0
        for i in self.indexes:
            # print("temp = ", x1)
            if self.user_ans[x1] == self.answersE[i]:
                score += 2
            x1 += 1
        # print("score = ", score)
        self.showresult(score)
    def calc_M(self):
        # global indexes, user_ans, answers
        x1 = 0
        score = 0
        for i in self.indexes:
            # print("temp = ", x1)
            if self.user_ans[x1] == self.answersMED[i]:
                score += 2
            x1 += 1
        # print("score = ", score)
        self.showresult(score)
    def calc_H(self):
        # global indexes, user_ans, answers
        x1 = 0
        score = 0
        for i in self.indexes:
            # print("temp = ", x1)
            if self.user_ans[x1] == self.answersHARD[i]:
                score += 2
            x1 += 1
        # print("score = ", score)
        self.showresult(score)
    def selectedE(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        
        # here x will get the value which user choose as input
        # print(x)
        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsEASY[self.indexes[self.count]])
            r1['text'] = self.choice_ansEASY[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansEASY[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansEASY[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansEASY[self.indexes[self.count]][3]
            self.count += 1
        else:
            # print(self.indexes)
            # print(self.user_ans)
            self.calc_E()
    def selectedM(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        
        # here x will get the value which user choose as input
        # print(x)
        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsMED[self.indexes[self.count]])
            r1['text'] = self.choice_ansMED[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansMED[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansMED[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansMED[self.indexes[self.count]][3]
            self.count += 1
        else:
            # print(self.indexes)
            # print(self.user_ans)
            self.calc_M()
    def selectedH(self):
        global questionlabel ,labelinst1,r1 ,r2 , r3 , r4
        x = self.radiovar.get()
        
        # here x will get the value which user choose as input
        # print(x)
        self.user_ans.append(x)
        self.radiovar.set(-1)
        if self.count < 10:
            questionlabel.config(text=self.questionsHARD[self.indexes[self.count]])
            r1['text'] = self.choice_ansHARD[self.indexes[self.count]][0]
            r2['text'] = self.choice_ansHARD[self.indexes[self.count]][1]
            r3['text'] = self.choice_ansHARD[self.indexes[self.count]][2]
            r4['text'] = self.choice_ansHARD[self.indexes[self.count]][3]
            self.count += 1
        else:
            # print(self.indexes)
            # print(self.user_ans)
            self.calc_H()
    def start_QE(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questionsEASY[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
            justify=LEFT,
        )
        r1.place(x=150, y=300)
        # r1.pack()

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)
        # r2.pack(padx=(400,0),pady=0)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)
        # r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansEASY[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)
        # r4.pack(pady=5)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedE,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    def start_QM(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questionsMED[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
            justify=LEFT,
        )
        r1.place(x=150, y=300)
        # r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)
        # r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)
        # r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansMED[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)
        # r4.pack(pady=5)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedM,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    def start_QH(self):
        global questionlabel ,r1,r2,r3,r4
        questionlabel = Label(
            self.root,
            # text="Sample Question which can be too long it will be in next line due to wrap length",
            text=self.questionsHARD[self.indexes[0]],
            font=("Times", 20, "bold"),
            width=500,
            justify="center",
            wraplength=400,
            bg="#7876FD",
        )
        questionlabel.pack(pady=(100, 30))

    
        self.radiovar = IntVar()
        self.radiovar.set(-1)
        # by setting radio var -1 it will not check any option automatically

        r1 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][0],
            font=("Times", 16),
            value=0,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
            justify=LEFT,
        )
        r1.place(x=150, y=300)
        # r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][1],
            font=("Times", 16),
            value=1,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r2.place(x=150, y=400)
        # r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][2],
            font=("Times", 16),
            value=2,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r3.place(x=400, y=300)
        # r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=self.choice_ansHARD[self.indexes[0]][3],
            font=("Times", 16),
            value=3,
            variable=self.radiovar,
            # command=self.selected,
            bg="#7876FD",
            activebackground="#7876FD",
        )
        r4.place(x=400, y=400)
        # r4.pack(pady=5)

        Button(
            self.root,
            text="NEXT",
            command=self.selectedH,
            font=("calibri", 20,"bold"),
            bg="#7876FD",
            activebackground="#7876FD",

        ).place(x=550,y=500)
    def Easy(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QE()

    def Medium(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QM()

    def Hard(self):
        labelinst.destroy()
        labelinstr.destroy()
        # img1label.destroy()
        txtlabel.destroy()
        E_button.destroy()
        M_button.destroy()
        H_button.destroy()
        self.gen()
        self.start_QH()


if __name__ == '__main__':
    main()
