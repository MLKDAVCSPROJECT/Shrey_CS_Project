from tkinter import *
from tkinter import messagebox
import mysql.connector as mycon

def rel():
    global topic

    topic="'RELATION'"
    root1.destroy()
    quesnumber()


def gen(): 
    global topic

    topic="'Genetics'"
    root1.destroy()
    quesnumber()

def rep():
    global topic

    topic="'Reproduction'"
    root1.destroy()
    quesnumber()

def elect():
    global topic

    topic="'Electrochemistry'"
    root1.destroy()
    quesnumber()

def sur():
    global topic
    root1.destroy()
    topic="'Surface chemistry'"
    quesnumber()

def kine():
    global topic
    root1.destroy()
    topic="'Chemical kinetics'"
    quesnumber()

def pblock():
    global topic
    root1.destroy()
    topic="'P-block'"
    quesnumber()

def charge():
    global topic
    root1.destroy()
    topic="'Electric charges and fields'"
    quesnumber()

def capa():
    global topic
    root1.destroy()
    topic="'Electrostatic Potential and Capacitance'"
    quesnumber()

def reh():
    global topic
    root1.destroy()
    topic="'Reproductive health'"
    quesnumber()

def liv():
    global topic
    root1.destroy()
    topic="'Living world'"
    quesnumber()

def loco():
    global topic
    root1.destroy()
    topic="'Locomotion'"
    quesnumber()

def sol():
    global topic
    root1.destroy()
    topic="'Solutions'"
    quesnumber()

def thermal():
    global topic
    root1.destroy()
    topic="'Thermal properties of Matter'"
    quesnumber()

def kinega():
    global topic
    root1.destroy()
    topic="'Kinetic Theory of Gasses'"
    quesnumber()

def oss():
    global topic
    root1.destroy()
    topic="'Oscillations'"
    quesnumber()

def trigo():
    global topic
    root1.destroy()
    topic="'Trigonometry'"
    quesnumber()

def proba():
    global topic
    root1.destroy()
    topic="'Probability'"
    quesnumber()

def comba():
    global topic
    root1.destroy()
    topic="'Permutations and Combinations'"
    quesnumber()

def ineqa():
    global topic
    root1.destroy()
    topic="'Linear Inequalities'"
    quesnumber()

def update():
    def upb():
        root3.destroy()
        main()
    global root3
    root1.destroy()
    root3 = Tk()
    root3.title("Update Question Bank")
    root3.geometry("600x700")

    Canvas1 = Canvas(root3) 
    Canvas1.config(bg="#03c6fc")
    Canvas1.pack(expand=True,fill=BOTH)
     
    btn1 = Button(root3,text="Add new Question",bg='#0328fc', fg='white', command=add)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
    
    btn2 = Button(root3,text="Update an Existing Question",bg='#0328fc', fg='white', command=updata)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1) 
    
    btn3 = Button(root3,text="Delete a Question",bg='#0328fc', fg='white', command=dele)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1) 
    
    BackBtn = Button(root3,text="BACK",bg='#d1ccc0', fg='black',command=upb)
    BackBtn.place(relx=0.42,rely=0.8, relwidth=0.18,relheight=0.08)
    
    headingFrame1 = Frame(root3,bg="#0328fc",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    headingLabel = Label(headingFrame1, text="Update Question Bank", bg='black', fg='#03c6fc', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

def updata():
    root3.destroy()
    def addb():
        root4.destroy()
        main()
    def upq():
        con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
        cur = con.cursor()

        atopic = itopic.get()
        aquesno = iquesno.get()
        aques = iques.get()
        aopt1 = iopt1.get()
        aopt2 = iopt2.get()
        aopt3 = iopt3.get()
        aopt4 = iopt4.get()
        acorrect = icorrect.get()
    
        query = "UPDATE "+sub+" SET QUES ='"+aques+"', OPT1 = '"+aopt1+"', OPT2 = '"+aopt2+"', OPT3 = '"+aopt3+"', OPT4 = '"+aopt4+"', CORRECT = '"+acorrect+"' WHERE TOPIC = '"+atopic+"' AND QUESNO = '"+aquesno+"';"
        
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo('Success',"Question Has Been Updated successfully")
        except:
            messagebox.showinfo("Error","Check Topic Name And Question NO. Carefully!!!! \n Maybe It is Wrong Or You Have Entered Wrong Data")
        root4.destroy()
        main()

    root4 = Tk()
    root4.title("Add Question in Question Bank")
    root4.geometry("1000x700")

    itopic = StringVar()
    iquesno = StringVar()
    iques = StringVar()
    iopt1 = StringVar()
    iopt2 = StringVar()
    iopt3 = StringVar()
    iopt4 = StringVar()
    icorrect = StringVar()

    labelFrame = Frame(root4,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.75)
        
    lb1 = Label(labelFrame,text="Topic (You want to Update) : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.05)
        
    char1 = Entry(labelFrame,textvariable=itopic)
    char1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.04)
    
    lb2 = Label(labelFrame,text="Question No. (You want to Update) : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.2, relheight=0.05)
    
    char2 = Entry(labelFrame,textvariable=iquesno)
    char2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.04)

    lb3 = Label(labelFrame,text="Question : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.3, relheight=0.05)
        
    char3 = Entry(labelFrame,textvariable=iques)
    char3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.04)

    lb4 = Label(labelFrame,text="Option 1 : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4, relheight=0.05)
    
    char4 = Entry(labelFrame,textvariable=iopt1)
    char4.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.04)

    lb5 = Label(labelFrame,text="Option 2 : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.5, relheight=0.05)

    char5 = Entry(labelFrame,textvariable=iopt2)
    char5.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.04)

    lb6 = Label(labelFrame,text="Option 3 : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.6, relheight=0.05)
         
    char6 = Entry(labelFrame,textvariable=iopt3)
    char6.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.04)

    lb7 = Label(labelFrame,text="Option 4 : ", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.7, relheight=0.05)
         
    char7 = Entry(labelFrame,textvariable=iopt4)
    char7.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.04)

    lb8 = Label(labelFrame,text="Correct Answer : ", bg='black', fg='white')
    lb8.place(relx=0.05,rely=0.8, relheight=0.05)
         
    char8 = Entry(labelFrame,textvariable=icorrect)
    char8.place(relx=0.3,rely=0.8 , relwidth=0.62, relheight=0.04)
    
    SubmitBtn = Button(root4,text="SUBMIT",bg='#d1ccc0', fg='black',command=upq)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    BackBtn = Button(root4,text="BACK",bg='#f7f1e3', fg='black', command=addb)
    BackBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def dele():
    root3.destroy()
    def deb():
        root4.destroy()
        main()
    def deq():
        con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
        cur = con.cursor()

        atopic = itopic.get()
        aquesno = iquesno.get()
        
        query = "DELETE FROM "+sub+" WHERE TOPIC = '"+atopic+"' AND QUESNO = '"+aquesno+"';"
        
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo('Success',"Question Has Been Deleted successfully")
        except:
            messagebox.showinfo("Error","Check Topic Name And Question NO. Carefully!!!! \n Maybe It is Wrong Or You Have Entered Wrong Data")
        root4.destroy()
        main()

    root4 = Tk()
    root4.title("Delete a Question from Question Bank")
    root4.geometry("1000x500")

    itopic = StringVar()
    iquesno = StringVar()

    labelFrame = Frame(root4,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.75)
        
    lb1 = Label(labelFrame,text="Topic (You want to Delete) : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.1)
        
    char1 = Entry(labelFrame,textvariable=itopic)
    char1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.1)
    
    lb2 = Label(labelFrame,text="Question No. (You want to Delete) : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5, relheight=0.1)
    
    char2 = Entry(labelFrame,textvariable=iquesno)
    char2.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.1)

    SubmitBtn = Button(root4,text="SUBMIT",bg='#d1ccc0', fg='black',command=deq)
    SubmitBtn.place(relx=0.28,rely=0.7, relwidth=0.18,relheight=0.08)
    
    BackBtn = Button(root4,text="BACK",bg='#f7f1e3', fg='black', command=deb)
    BackBtn.place(relx=0.53,rely=0.7, relwidth=0.18,relheight=0.08)
  
def add():
    root3.destroy()
    def addb():
        root4.destroy()
        main()
    def addq():
        con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
        cur = con.cursor()

        atopic = itopic.get()
        aquesno = iquesno.get()
        aques = iques.get()
        aopt1 = iopt1.get()
        aopt2 = iopt2.get()
        aopt3 = iopt3.get()
        aopt4 = iopt4.get()
        acorrect = icorrect.get()

        query = "INSERT INTO "+sub+" VALUES('"+atopic+"','"+aquesno+"','"+aques+"','"+aopt1+"','"+aopt2+"','"+aopt3+"','"+aopt4+"','"+acorrect+"')"
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo('Success',"Question added successfully")
        except:
            messagebox.showinfo("Error","Can't add data into Database")
        
        root4.destroy()
        main()

    root4 = Tk()
    root4.title("Add Question in Question Bank")
    root4.geometry("1000x700")

    itopic = StringVar()
    iquesno = StringVar()
    iques = StringVar()
    iopt1 = StringVar()
    iopt2 = StringVar()
    iopt3 = StringVar()
    iopt4 = StringVar()
    icorrect = StringVar()

    labelFrame = Frame(root4,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.75)
        
    lb1 = Label(labelFrame,text="Topic : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.05)
        
    char1 = Entry(labelFrame,textvariable=itopic)
    char1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.04)
    
    lb2 = Label(labelFrame,text="Question Number : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.2, relheight=0.05)
    
    char2 = Entry(labelFrame,textvariable=iquesno)
    char2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.04)

    lb3 = Label(labelFrame,text="Question : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.3, relheight=0.05)
        
    char3 = Entry(labelFrame,textvariable=iques)
    char3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.04)

    lb4 = Label(labelFrame,text="Option 1 : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4, relheight=0.05)
    
    char4 = Entry(labelFrame,textvariable=iopt1)
    char4.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.04)

    lb5 = Label(labelFrame,text="Option 2 : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.5, relheight=0.05)

    char5 = Entry(labelFrame,textvariable=iopt2)
    char5.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.04)

    lb6 = Label(labelFrame,text="Option 3 : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.6, relheight=0.05)
         
    char6 = Entry(labelFrame,textvariable=iopt3)
    char6.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.04)

    lb7 = Label(labelFrame,text="Option 4 : ", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.7, relheight=0.05)
         
    char7 = Entry(labelFrame,textvariable=iopt4)
    char7.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.04)

    lb8 = Label(labelFrame,text="Correct Answer : ", bg='black', fg='white')
    lb8.place(relx=0.05,rely=0.8, relheight=0.05)
         
    char8 = Entry(labelFrame,textvariable=icorrect)
    char8.place(relx=0.3,rely=0.8 , relwidth=0.62, relheight=0.04)
    
    SubmitBtn = Button(root4,text="SUBMIT",bg='#d1ccc0', fg='black',command=addq)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    BackBtn = Button(root4,text="BACK",bg='#f7f1e3', fg='black', command=addb)
    BackBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def maths():
    def mathsb():
        root1.destroy()
        main() 

    global sub,root1
    root.destroy()
    root1 = Tk()
    root1.title("Maths Question Bank")
    root1.geometry("600x700")

    sub="Maths"

    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="#ffff00")
    Canvas1.pack(expand=True,fill=BOTH)
        
    btn1 = Button(root1,text="Topic - Relations",bg='#ffbb00', fg='white', command=rel)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
        
    btn2 = Button(root1,text="Topic - Trigonometry",bg='#ffbb00', fg='white', command=trigo)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1) 
        
    btn3 = Button(root1,text="Topic - Probability",bg='#ffbb00', fg='white', command=proba)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1) 
        
    btn4 = Button(root1,text="Topic - Permutations and Combinations",bg='#ffbb00', fg='white', command=comba)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1) 
        
    btn5 = Button(root1,text="Topic - Linear Inequalities",bg='#ffbb00', fg='white', command=ineqa)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1) 
    
    btn6 = Button(root1,text="Update Question Bank",bg='#03fcf0', fg='#b103fc', command=update)
    btn6.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1) 
    
    BackBtn = Button(root1,text="BACK",bg='#d1ccc0', fg='black',command=mathsb)
    BackBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    headingFrame1 = Frame(root1,bg="#ffbb00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    headingLabel = Label(headingFrame1, text="Maths Question Bank", bg='black', fg='#ffff00', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
def chem():
    def chemb():
        root1.destroy()
        main() 

    global sub,root1
    root.destroy()
    root1 = Tk()
    root1.title("Chemistry Question Bank")
    root1.geometry("600x700")

    sub="Chem"

    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="#62fc03")
    Canvas1.pack(expand=True,fill=BOTH)
        
    btn1 = Button(root1,text="Topic - Solutions",bg='#43d41c', fg='white', command=sol)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
        
    btn2 = Button(root1,text="Topic - Electrochemistry",bg='#43d41c', fg='white', command=elect)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1) 

        
    btn3 = Button(root1,text="Topic - Surface Chemistry",bg='#43d41c', fg='white', command=sur)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1) 

        
    btn4 = Button(root1,text="Topic - Chemical Kinetics",bg='#43d41c', fg='white', command=kine)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1) 
        
    btn5 = Button(root1,text="Topic - P-block",bg='#43d41c', fg='white', command=pblock)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1) 
    
    btn6 = Button(root1,text="Update Question Bank",bg='#03fcf0', fg='#b103fc', command=update)
    btn6.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1) 
    
    BackBtn = Button(root1,text="BACK",bg='#d1ccc0', fg='black',command=chemb)
    BackBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    headingFrame1 = Frame(root1,bg="#43d41c",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    headingLabel = Label(headingFrame1, text="Chemistry Question Bank", bg='black', fg='#62fc03', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

def phy():
    def phyb():
        root1.destroy()
        main() 

    global sub,root1
    root.destroy()
    root1 = Tk()
    root1.title("Physics Question Bank")
    root1.geometry("600x700")

    sub="Phy"

    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="#fc03f0")
    Canvas1.pack(expand=True,fill=BOTH)
        
    btn1 = Button(root1,text="Topic - Electric charges and fields",bg='#b103fc', fg='white', command=charge)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
        
    btn2 = Button(root1,text="Topic - Electrostatic Potential and Capacitance",bg='#b103fc', fg='white', command=capa)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1) 
        
    btn3 = Button(root1,text="Topic - Thermal properties of Matter",bg='#b103fc', fg='white', command=thermal)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1) 

    btn4 = Button(root1,text="Topic - Kinetic Theory of Gases",bg='#b103fc', fg='white', command=kinega)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1) 
        
    btn5 = Button(root1,text="Topic - Oscillations",bg='#b103fc', fg='white', command=oss)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1) 
    
    btn6 = Button(root1,text="Update Question Bank",bg='#03fcf0', fg='#b103fc', command=update)
    btn6.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1) 
    
    BackBtn = Button(root1,text="BACK",bg='#d1ccc0', fg='black',command=phyb)
    BackBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    headingFrame1 = Frame(root1,bg="#b103fc",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    headingLabel = Label(headingFrame1, text="Physics Question Bank", bg='black', fg='#fc03f0', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

def bio():
    def biob():
        root1.destroy()
        main() 

    global sub,root1
    root.destroy()
    root1 = Tk()
    root1.title("Biology Question Bank")
    root1.geometry("600x700")

    sub="Bio"

    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    btn1 = Button(root1,text="Topic - Genetics",bg='#eb4f34', fg='white', command=gen)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 

    btn2 = Button(root1,text="Topic - Reproduction",bg='#eb4f34', fg='white', command=rep)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1) 

    btn3 = Button(root1,text="Topic - Reproductive health",bg='#eb4f34', fg='white', command=reh)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1) 

    btn4 = Button(root1,text="Topic - Living world",bg='#eb4f34', fg='white', command=liv)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1) 
    
    btn5 = Button(root1,text="Topic - Locomotion",bg='#eb4f34', fg='white', command=loco)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1) 
    
    btn6 = Button(root1,text="Update Question Bank",bg='#03fcf0', fg='#b103fc', command=update)
    btn6.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1) 
    
    BackBtn = Button(root1,text="BACK",bg='#d1ccc0', fg='black',command=biob)
    BackBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    headingFrame1 = Frame(root1,bg="#eb4f34",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    headingLabel = Label(headingFrame1, text="Biology Question Bank", bg='black', fg='#ff6e40', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       
def q1():
    global quesno
    root2.destroy()
    quesno="001"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q2():
    global quesno
    root2.destroy()
    quesno="002"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q3():
    global quesno
    root2.destroy()
    quesno="003"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q4():
    global quesno
    root2.destroy()
    quesno="004"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q5():
    global quesno
    root2.destroy()
    quesno="005"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q6():
    global quesno
    root2.destroy()
    quesno="006"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q7():
    global quesno
    root2.destroy()
    quesno="007"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()

def q8():
    global quesno
    root2.destroy()
    quesno="008"
    if sub=="Maths":
        mathsq()
    elif sub=="Phy":
        phyq()
    elif sub=="Chem":
        chemq()
    elif sub=="Bio":
        bioq()


def quesnumber():
    global root2
    def quesnob():
        root2.destroy()
        main()
    root2 = Tk()
    root2.title("Questions")
    root2.geometry("600x700")

    Canvas1 = Canvas(root2)
    Canvas1.config(bg="#34eb99")
    Canvas1.pack(expand=True,fill=BOTH)

    btn1 = Button(root2,text="Question 1",bg='black', fg='white', command=q1)
    btn1.place(relx=0.28,rely=0.1, relwidth=0.45,relheight=0.1)

    btn2 = Button(root2,text="Question 2",bg='black', fg='white', command=q2)
    btn2.place(relx=0.28,rely=0.2, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root2,text="Question 3",bg='black', fg='white', command=q3)
    btn3.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

    btn4 = Button(root2,text="Question 4",bg='black', fg='white', command=q4)
    btn4.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn5 = Button(root2,text="Question 5",bg='black', fg='white', command=q5)
    btn5.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn6 = Button(root2,text="Question 6",bg='black', fg='white', command=q6)
    btn6.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn7 = Button(root2,text="Question 7",bg='black', fg='white', command=q7)
    btn7.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn8 = Button(root2,text="Question 8",bg='black', fg='white', command=q8)
    btn8.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    
    BackBtn = Button(root2,text="BACK",bg='#d1ccc0', fg='black',command=quesnob)
    BackBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
def mathsq():
    def mathsqb():
        root5.destroy()
        main()

    con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
    cur = con.cursor(buffered=True)

    root5=Tk()
    root5.title("Questions")
    root5.geometry('1300x250')

    mathsget = "select ques from maths where topic = "+topic+"and quesno = "+quesno
    cur.execute(mathsget)
    questions=cur.fetchone()
    option= "select opt1,opt2,opt3,opt4,correct from maths where topic ="+topic+"and quesno = "+quesno
    cur.execute(option)
    options=cur.fetchone()
    
    headingLabel = Label(root5, text=questions, bg='orange', fg='white', font=('Courier',11))
    headingLabel.pack()

    lstbox=Listbox(root5,bg="white",fg="black",font=('Courier',11),selectmode=SINGLE,width=70)
    lstbox.pack()
    for i in options:
        lstbox.insert(END,i)
    
    BackBtn = Button(root5,text="BACK",bg='#d1ccc0', fg='black',command=mathsqb)
    BackBtn.place(relx=0.42,rely=0.6, relwidth=0.18,relheight=0.08)
    
def phyq():
    def phyqb():
        root5.destroy()
        main()
    
    con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
    cur = con.cursor(buffered=True)

    root5=Tk()
    root5.title("Questions")
    root5.geometry('1300x250')

    phyget = "select ques from phy where topic = "+topic+"and quesno = "+quesno
    cur.execute(phyget)
    questions=cur.fetchone()
    option= "select opt1,opt2,opt3,opt4,correct from phy where topic ="+topic+"and quesno = "+quesno
    cur.execute(option)
    options=cur.fetchone()
    
    headingLabel = Label(root5, text=questions, bg='orange', fg='white', font=('Courier',11))
    headingLabel.pack()

    lstbox=Listbox(root5,bg="white",fg="black",font=('Courier',11),selectmode=SINGLE,width=70)
    lstbox.pack()
    for i in options:
        lstbox.insert(END,i)
    
    BackBtn = Button(root5,text="BACK",bg='#d1ccc0', fg='black',command=phyqb)
    BackBtn.place(relx=0.42,rely=0.6, relwidth=0.18,relheight=0.08)
    
def chemq():
    def chemqb():
        root5.destroy()
        main()
    
    con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
    cur = con.cursor(buffered=True)

    root5=Tk()
    root5.title("Questions")
    root5.geometry('1300x250')

    chemget = "select ques from chem where topic = "+topic+"and quesno = "+quesno
    cur.execute(chemget)
    questions=cur.fetchone()
    option= "select opt1,opt2,opt3,opt4,correct from chem where topic ="+topic+"and quesno = "+quesno
    cur.execute(option)
    options=cur.fetchone()
    
    headingLabel = Label(root5, text=questions, bg='orange', fg='white', font=('Courier',11))
    headingLabel.pack()

    lstbox=Listbox(root5,bg="white",fg="black",font=('Courier',11),selectmode=SINGLE,width=70)
    lstbox.pack()
    for i in options:
        lstbox.insert(END,i)
    
    BackBtn = Button(root5,text="BACK",bg='#d1ccc0', fg='black',command=chemqb)
    BackBtn.place(relx=0.42,rely=0.6, relwidth=0.18,relheight=0.08)
    
def bioq():
    def bioqb():
        root5.destroy()
        main()
    
    con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
    cur = con.cursor(buffered=True)

    root5=Tk()
    root5.title("Questions")
    root5.geometry('1300x250')

    bioget = "select ques from bio where topic = "+topic+"and quesno = "+quesno
    cur.execute(bioget)
    questions=cur.fetchone()
    option= "select opt1,opt2,opt3,opt4,correct from bio where topic ="+topic+"and quesno = "+quesno
    cur.execute(option)
    options=cur.fetchone()
    
    headingLabel = Label(root5, text=questions, bg='orange', fg='white', font=('Courier',11))
    headingLabel.pack()

    lstbox=Listbox(root5,bg="white",fg="black",font=('Courier',11),selectmode=SINGLE,width=70)
    lstbox.pack()
    for i in options:
        lstbox.insert(END,i)
    
    BackBtn = Button(root5,text="BACK",bg='#d1ccc0', fg='black',command=bioqb)
    BackBtn.place(relx=0.42,rely=0.6, relwidth=0.18,relheight=0.08)
    
con = mycon.connect(host="localhost",user="root",password="1234",database="ques")
cur = con.cursor()

topic=""
quesno=""
sub=""
def main():
    global root
    root = Tk()
    root.title("Question Bank")
    root.geometry("600x700")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#eb8634")
    Canvas1.pack(expand=True,fill=BOTH)
    #ff6e40        
    headingFrame1 = Frame(root,bg="#b1eb34",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    #FFBB00
    headingLabel = Label(headingFrame1, text="Welcome to \n Question Bank", bg='black', fg='#e2eb34', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Maths",bg='#34d9eb', fg='#5934eb',command=maths)
    btn1.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Chemistry",bg='#34d9eb', fg='#5934eb',command=chem)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1,)

    btn3 = Button(root,text="Physics",bg='#34d9eb', fg='#5934eb', command=phy)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Biology",bg='#34d9eb', fg='#5934eb', command=bio)
    btn4.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    root.mainloop()
main()