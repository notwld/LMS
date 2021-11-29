import os
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime


class LibraryFunctions:
    def __init__(self):
        pass

 
    def addsession(self):
        book=str(self.book.get())
        writer=str(self.writer.get())
        year=str(self.year.get())

        if book=='' or writer=='' or year=='':
            self.notFound.config(text='Fill the fields*',fg='red')


        with open('books.txt','r') as booksLi:
            for books in str(booksLi).split('\n'):
                if book!=books and writer!=books:
                    file=open('books.txt','a')
                    file.write(f"\n{book} by {writer} ({year})")
                    self.notFound.config(text='Book Added!',fg='green')
                    file.close()
                    break

                else:
                    self.notFound.config(text='Book already exists in the list!',fg='green')
                    
        for widgets in self.added.winfo_children():
            widgets.destroy()
        
        
        scrollbarY = Scrollbar(self.added)
        scrollbarY.pack(side = RIGHT, fill = Y )
        

        li=[]
        li.append(f"{book} by {writer} ({year})")
        
        for i in range(len(li)):
            self.added.insert(i,li[i])
        

    

    def clearFieldsofIssueBooks(self):
        self.nameEn.delete(0,'end')
        self.bookEn.delete(0,'end')
        self.returnEn.delete(0,'end')
        self.error.config(text='')

    def clearFieldsofAddBooks(self):
        self.book.delete(0,'end')
        self.writer.delete(0,'end')
        self.year.delete(0,'end')
        self.notFound.config(text='')

    def clearFieldsofDelBooks(self):
        self.booktoDel.delete(0,'end')
        self.notDel.config(text='')

    def clearFieldsofReBooks(self):
        self.borrower.delete(0,'end')
        self.borrowedbook.delete(0,'end')
        self.fine.delete(0,'end')
        self.notReturn.config(text='')
        

    def issuesession(self):
        name=str(self.nameEn.get())
        book=str(self.bookEn.get())
        returnDate=str(self.returnEn.get())
        
        allBooks=os.listdir(f'{os.getcwd()}/Issued Books')
        

        if name=="" or book=="" or returnDate=="":
            self.error.config(text='Fill all Field*')
            return

        for names in allBooks:
            if names==name:
                self.error.config(text=f'{name} already issued a book*',fg='red')
                return
            else:
                with open('books.txt','r') as file:
                    for books in file:
                        if book not in books:
                            self.error.config(text=f'Book does not exists!',fg='red')
                                          
                        else:
                            self.error.config(text=f'Book issued!',fg='green')
                            newFile=open(f"{os.getcwd()}/Issued Books/{name}",'w')
                            newFile.write(f"Name : {name}   Book : {book}       \nReturn Date : {returnDate}\n")
                            
                    
                            newFile.close()

    def delsession(self):
        count = 1
        book = str(self.booktoDel.get())
        path = f"{os.getcwd()}/Logs/logs.txt"
        date = datetime.now()
        owo = open(f"{os.getcwd()}/books.txt", "r+")
        fileData=owo.read()
        details=fileData.split("\n")
        
        if book == '':
            self.notDel.config(text='Please Enter the book name!',fg='red')

        else: 
            with open(path,'w+') as file:
                self.notDel.config(text='Book Deleted!',fg='green')
                for books in details:
                    if book in books:
                        file.write(f"{count}.Deleted {book} on {date.strftime('%d/ %m/ %y : %I : %M %p')}\n")
                        fileData = fileData.replace(book, "")
                        owo.seek(0)
                        owo.truncate(0)
                        owo.write(fileData)
                        owo.close()
                        self.deleted.insert('end',f"{count}.Deleted {book}\n on {date.strftime('%d/ %m/ %y : %I : %M %p')}\n")
                        owo.close()
                        count+=1
                    else:
                        self.notDel.config(text=r"Book donot Exist!",fg='red')

        
    def returnsession(self):
        index = 1
        borrower=str(self.borrower.get())
        book=str(self.borrowedbook.get())
        fine = str(self.fine.get())
        path =f"{os.getcwd()}/Returned Books"
        date = datetime.now().strftime('%d %m/ %y : %I : %M %p')
        if self.borrower=='' or self.fine=='':
            self.notReturn.config(text='fill all fields*',fg='red')
        
        else:
            with open(f"{path}/returned.txt",'a+') as file: 
                self.notReturn.config(text='Book returned successfully',fg='green')
                if borrower in os.listdir(f'{os.getcwd()}/Issued Books'):
                    os.remove(f"{os.getcwd()}/Issued Books/{borrower}")
                    file.write(f'{index} : {borrower} Returned {book} \n Dated : {date}\n')
                    finefile = open(f'{os.getcwd()}/fines.txt','a+')
                    finefile.write(f'{borrower} : {fine}$\n')
                    finefile.close()
                    self.Returned.insert('end',f'{index} : {borrower}Returned {book} \n Dated : {date}\n')
                    index+=1
                else:
                    self.notReturn.config(text='Book was not returned successfully',fg='red')
            
            

    def showfines(self):
        win = Tk()
        win.title('Fines')
        win.geometry('250x250')
        win.config(bg='black')
        owo = Listbox(win,bg='black',fg='green',height=250,width=250,font='hack 13')
        owo.pack()
        with open(f'{os.getcwd()}/Returned Books/fines.txt','r') as file:
            for fines in file:
                owo.insert('end',fines)
        win.mainloop() 

class BackEnd:

    def __init__(self):
        pass
    def register(self):
    
        f_name=self.first_name.get()
        l_name=self.last_name.get()
        age_=self.age.get()
        u_name=self.user.get()
        email_=self.email.get()
        cpwd=self.passwConf.get()
        pwd=self.password.get()

        allAccounts= os.listdir(f'{os.getcwd()}/Accounts')

        if f_name == "" or age_ == "" or email_ == "" or pwd == "":
            self.notif.config(fg="red", text="Fill All Fields*",font='hack 10')
            return
            
        if cpwd==pwd:
            for i in allAccounts:
                if i == u_name:
                    self.notif.config(fg="red", text="Name Taken")
                    return
                else:
                    newFile=open(f"{os.getcwd()}/Accounts/{u_name}","w")
                    newFile.write(f_name+"\n")
                    newFile.write(l_name+"\n")
                    newFile.write(u_name+"\n")
                    newFile.write(age_+"\n")
                    newFile.write(email_+"\n")
                    newFile.write(pwd+"\n")
                    newFile.close()
                    self.notif.config(fg="green", text="Account has successfully been created!",font='hack 10')
        
        else:
            self.notif.config(fg="red", text="Password doesnt matched!",font='hack 10')


    def login(self):

        p = self.passw.get()
        u = self.user_name.get()
        allAcc=os.listdir(f'{os.getcwd()}/Accounts')

        if p == "": 
            self.error.config(fg='red',text='Fill Password!')
        if u == "": 
            self.error.config(fg='red',text='Fill Username!')

        try: 

            for names in allAcc:
                if names!=u:
                    self.error.config(fg='red',text='Invalid Account')
                if names == u:
                    acc = open(f"{os.getcwd()}/Accounts/{names}",'r').read()
                    pwd = acc.split('\n')
                    pwd_from_list=pwd[5]

                    if pwd_from_list==p:
                        self.LibraryScreen()

        except:
            pass

class LoginSys(BackEnd):

    def loginSession(self):
        self.loginwin=Toplevel(self.mainWin)
        self.loginwin.title('LMS - Login')
        self.loginwin.geometry('400x220')
        self.loginwin.config(bg='black')
        self.loginwin.resizable(width=False,height=False)
        self.photo = PhotoImage(file = "title_icon.png")
        self.loginwin.iconphoto(False, self.photo)

        Label(self.loginwin,text="Login",font="hack 20").grid(row=0,column=2,pady=10,padx=10)
        Label(self.loginwin,text='User Name ',font="hack 10").grid(row=1,column=1,pady=10,padx=10)
        self.user_name=Entry(self.loginwin,borderwidth=3)
        self.user_name.grid(row=1,column=2,pady=10,padx=10,sticky=E)
        Label(self.loginwin,text='Password ',font="hack 10").grid(row=2,column=1,pady=10,padx=10)
        self.passw=Entry(self.loginwin,show='*',borderwidth=3)
        self.passw.grid(row=2,column=2,pady=10,padx=10,sticky=E)

        Button(self.loginwin,text="Login" ,bg='black',fg='white', font='hack 10',command=self.login).grid(row=3,column=2,pady=10,padx=10)
        self.error=Label(self.loginwin,font="hack 10",fg='red',bg='black')
        self.error.grid(row=4,column=2)
        self.loginwin.mainloop()

class RegisterSys(BackEnd):

    def registerSession(self):

        self.registerwin=Toplevel(self.mainWin)
        self.registerwin.title('LMS - Register')
        self.registerwin.geometry('650x450')
        self.registerwin.config(bg='black')
        self.registerwin.resizable(width=False,height=False)

        Label(self.registerwin,text="Register",font="hack 20").grid(row=0,column=5,pady=10,padx=10)
        Label(self.registerwin,text='First Name ',font="hack 10").grid(row=1,column=0,pady=10,padx=10,sticky=E)
        self.first_name=Entry(self.registerwin,borderwidth=3)
        self.first_name.grid(row=1,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Last Name ',font="hack 10").grid(row=2,column=0,pady=10,padx=10,sticky=E)
        self.last_name=Entry(self.registerwin,borderwidth=3)
        self.last_name.grid(row=2,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Username ',font="hack 10").grid(row=3,column=0,pady=10,padx=10,sticky=E)
        self.user=Entry(self.registerwin,borderwidth=3)
        self.user.grid(row=3,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Age ',font="hack 10").grid(row=4,column=0,pady=10,padx=10,sticky=E)
        self.age=Entry(self.registerwin,borderwidth=3)
        self.age.grid(row=4,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Email ',font="hack 10").grid(row=5,column=0,pady=10,padx=10,sticky=E)
        self.email=Entry(self.registerwin,borderwidth=3)
        self.email.grid(row=5,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Password ',font="hack 10").grid(row=6,column=0,pady=10,padx=10,sticky=E)
        self.password=Entry(self.registerwin,show='*',borderwidth=3)
        self.password.grid(row=6,column=1,pady=10,padx=10)
        Label(self.registerwin,text='Confirm Password ',font="hack 10").grid(row=7,column=0,pady=10,padx=10,sticky=E)
        self.passwConf=Entry(self.registerwin,show='*',borderwidth=3)
        self.passwConf.grid(row=7,column=1,pady=10,padx=10)

        Button(self.registerwin,text="Register" ,fg='white',bg='black', font='hack 10',command=self.register).grid(row=9,column=1,pady=10,padx=10)
        self.notif=Label(self.registerwin,font='hack 10',bg='black')
        self.notif.grid(row=3,column=5,pady=10,padx=10)

        self.registerwin.mainloop()

class LibraryModels(LibraryFunctions,LoginSys,RegisterSys):

    def __init__(self,win,img):

        super().__init__()

        self.mainWin=win
        self.mainWin.geometry('650x550')
        self.mainWin.title('LMS')
        self.mainWin.config(bg='black')
        self.mainWin.resizable(width=False,height=False)
        self.photo = PhotoImage(file = "title_icon.png")
        self.mainWin.iconphoto(False, self.photo)

        Label(self.mainWin,text='Welcome to Uit Library' ,font="hack 20").pack(pady=50)
        Label(self.mainWin, image=img).pack(pady=30)

        Button(self.mainWin,text="Login" ,width=15,fg = 'white',bg='black',font="hack 10 " ,command=self.loginSession).pack(pady=5)

        Button(self.mainWin,text="Register",width=15 ,fg = 'white',bg='black',font="hack 10" , command=self.registerSession).pack()

        Label(self.mainWin,text='@blurryface' ,font="hack 10",bg='black',fg='green').pack(pady=25)
        
        self.loginwin=None
        self.registerwin=None
        self.lib=None
        self.error=None
        self.notif=None
        
        self.user_name=None
        self.passw=None
        self.passwConf=None
        self.password=None
        self.last_name=None
        self.first_name=None
        self.user=None
        self.age=None
        self.email=None

      

    def LibraryScreen(self):

        self.mainWin.withdraw()  
        self.loginwin.withdraw()
        un=self.user_name.get()

        self.lib = Tk()
        self.lib.title('LMS - Dashborad')
        self.lib.config(bg='black')
        self.lib.geometry('1300x650')

        winHead = Label(self.lib,text="Library - Dashborad",fg='black',font="hack 28")
        winHead.pack(side=TOP,padx=5,pady=80)


        Button(self.lib,text=f"Log Out",fg='white',bg='black',font='hack 8',command=lambda:[self.mainWin.deiconify(),self.lib.destroy()]).pack(pady=5,side=BOTTOM)

        Label(self.lib,text=f"Logged in as {un}",fg='green',bg='black',font='hack 10').pack(pady=10,side=BOTTOM)

        btn1 = Button(self.lib,text="View Books",bg='black', fg='white',font="hack 9",command=self.ViewBooks)
        btn1.place(relx=0.37,rely=0.3, relwidth=0.25,relheight=0.1)
                        
        btn2 = Button(self.lib,text="Issue Book",bg='black', fg='white',font="hack 9",command=self.IssueBooks)
        btn2.place(relx=0.37,rely=0.4, relwidth=0.25,relheight=0.1)
                        
        btn3 = Button(self.lib,text="Add Book",bg='black', fg='white',font="hack 9",command=self.AddBook)
        btn3.place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.1)
                        
        btn4 = Button(self.lib,text="Delete Book",bg='black', fg='white',font="hack 9",command=self.DeleteBooks)
        btn4.place(relx=0.37,rely=0.6, relwidth=0.25,relheight=0.1)
                        
        btn5 = Button(self.lib,text="Return Book",bg='black', fg='white',font="hack 9",command=self.ReturnBooks)
        btn5.place(relx=0.37,rely=0.7, relwidth=0.25,relheight=0.1)

        self.lib.mainloop()


    def AddBook(self):
    
        self.addbook=Tk()
        self.addbook.title('LMS - Add Books')
        self.addbook.geometry('900x600')
        self.addbook.config(bg='black')
        # self.photo = PhotoImage(file = "title_icon.png")
        # self.addbook.iconphoto(False, self.photo)
        Label(self.addbook,text="Add Books",font='hack 20').place(relheight=0.05,relwidth=0.5,relx=0.26,rely=0.02)
        self.bookFrame=Frame(self.addbook,borderwidth=2,bg='black',height=400,width=500)
        self.bookFrame.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)

        name=Label(self.addbook,text='Book Name',font='hack 10')
        name.place(rely=0.75,relx=0.35,anchor=NE)
        book=Label(self.addbook,text='Writer',font='hack 10')
        book.place(rely=0.80,relx=0.35,anchor=NE)
        year=Label(self.addbook,text='Year',font='hack 10')
        year.place(rely=0.85,relx=0.35,anchor=NE)
        
        self.book=Entry(self.addbook,borderwidth=3)
        self.book.place(rely=0.75,relx=0.56,anchor=NE,relwidth=0.2)

        self.writer=Entry(self.addbook,borderwidth=3)
        self.writer.place(rely=0.80,relx=0.56,anchor=NE,relwidth=0.2)

        self.year=Entry(self.addbook,borderwidth=3)
        self.year.place(rely=0.85,relx=0.56,anchor=NE,relwidth=0.2)

        submit=Button(self.addbook,text='Submit',fg='white',bg='black',font="hack 8 ",command=self.addsession)
        submit.place(rely=0.91,relx=0.44)
        clear=Button(self.addbook,text='Clear',fg='white',bg='black',font="hack 8 ",command=self.clearFieldsofAddBooks)
        clear.place(rely=0.91,relx=0.38)
        
        self.notFound = Label(self.addbook,font='hack 10',bg='black')
        self.notFound.place(rely=0.80,relx=0.6,anchor=NW)

        self.added=Listbox(self.addbook,fg='green',bg='black',font='hack 12')

        
        scrollbarY = Scrollbar(self.added)
        scrollbarY.pack(side = RIGHT, fill = Y )
        
        self.added.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)
            

        self.addbook.mainloop()


    def IssueBooks(self):
    
        self.issueBooks=Tk()
        self.issueBooks.title('LMS - Issue Books')
        self.issueBooks.geometry('900x600')
        self.issueBooks.config(bg='black')
        self.issueBooks.resizable(width=False,height=False)

        Label(self.issueBooks,text="Issued Books",font='hack 15').place(relheight=0.05,relwidth=0.5,relx=0.26,rely=0.02)

        self.issuedBooks=Frame(self.issueBooks,background='black',borderwidth=2,height=400,width=500)
        self.issuedBooks.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)
        
    
        

        name=Label(self.issueBooks,text='Name',font='hack 10')
        name.place(rely=0.75,relx=0.35,anchor=NE)

        book=Label(self.issueBooks,text='Book',font='hack 10')
        book.place(rely=0.80,relx=0.35,anchor=NE)

        returnDate=Label(self.issueBooks,text='Return Date',font='hack 10')
        returnDate.place(rely=0.85,relx=0.35,anchor=NE)

        self.nameEn=Entry(self.issueBooks,borderwidth=3)
        self.nameEn.place(rely=0.75,relx=0.56,anchor=NE,relwidth=0.2)

        self.bookEn=Entry(self.issueBooks,borderwidth=3)
        self.bookEn.place(rely=0.80,relx=0.56,anchor=NE,relwidth=0.2)

        self.returnEn=Entry(self.issueBooks,borderwidth=3)
        self.returnEn.place(rely=0.85,relx=0.56,anchor=NE,relwidth=0.2)



        submit=Button(self.issueBooks,text='Submit',fg="white",bg="black",font="hack 8 ",command=self.issuesession)
        submit.place(rely=0.91,relx=0.40)
        clear=Button(self.issueBooks,text='Clear',fg="white",bg="black",font="hack 8 ",command=self.clearFieldsofIssueBooks)
        clear.place(rely=0.91,relx=0.33)


        self.error = Label(self.issueBooks,font='hack 10',bg='black')
        self.error.place(rely=0.85,relx=0.6,anchor=NW)

        self.li=[]

        folder=os.listdir(f"{os.getcwd()}/Issued Books")
    
        for file in range(len(folder)):
            self.li.append(open(f'{os.getcwd()}/Issued Books/{folder[file]}','r').read().split('\n'))
            

        self.listbox=Listbox(self.issuedBooks,fg='green',background='black',font='hack 12')

        scrollbarY = Scrollbar(self.listbox)
        scrollbarX= Scrollbar(self.listbox,orient=HORIZONTAL)
        scrollbarY.pack(side = RIGHT, fill = Y )
        scrollbarX.pack(side = BOTTOM,fill = X )


        self.listbox.place(relheight=1,relwidth=1,relx=0,rely=0)
        for lables in self.li:
            self.listbox.insert('end',f'{"".join(lables)}')
            self.listbox.insert('end','\n')

        self.listbox.config(yscrollcommand=scrollbarY.set)
        self.listbox.config(yscrollcommand=scrollbarX.set)
        scrollbarY.config(command = self.listbox.yview )
        scrollbarX.config(command = self.listbox.xview )
        

        self.issueBooks.mainloop()  


    def ViewBooks(self):
        viewBooks=Tk()
        viewBooks.title('LMS - View Books')
        viewBooks.geometry('700x600')
        viewBooks.config(bg='black')
        
        Label(viewBooks,text="All Available Books",font='hack 25').pack(side=TOP,pady=25)
        scrollbar = Scrollbar(viewBooks)
        scrollbar.pack( side = RIGHT, fill = Y )
        li=Listbox(viewBooks,yscrollcommand=scrollbar.set,height=400,width=400,bg='black',fg='green',font='hack 15')
        with open("books.txt",'r') as file:
            for i in file:
                li.insert('end',i)

        li.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = li.yview )
        viewBooks.mainloop()

    def ReturnBooks(self):

        returnBook=Tk()
        returnBook.title('LMS - Return Books')
        returnBook.config(bg='black')
        returnBook.geometry('750x600')

        Label(returnBook,text="Return Books",font='hack 15').place(relheight=0.05,relwidth=0.5,relx=0.26,rely=0.05)
        self.returnFrame = Frame(returnBook,background='black',borderwidth=2,height=400,width=500)
        self.returnFrame.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)


        name=Label(returnBook,text='Borrower ',font='hack 10')
        name.place(rely=0.75,relx=0.35,anchor=NE)
        
        self.borrower=Entry(returnBook,borderwidth=3)
        self.borrower.place(rely=0.75,relx=0.56,anchor=NE,relwidth=0.2)

        book=Label(returnBook,text='Book ',font='hack 10')
        book.place(rely=0.80,relx=0.35,anchor=NE)
        
        self.borrowedbook=Entry(returnBook,borderwidth=3)
        self.borrowedbook.place(rely=0.80,relx=0.56,anchor=NE,relwidth=0.2)
 
        fine=Label(returnBook,text='Fine ',font='hack 10')
        fine.place(rely=0.85,relx=0.35,anchor=NE)
    
        self.fine=Entry(returnBook,borderwidth=3)
        self.fine.place(rely=0.85,relx=0.56,anchor=NE,relwidth=0.2)

        self.fine.insert('end',str(0))

        returning=Button(returnBook,text='Return',fg='white',bg='black',font="hack 8 ",command=self.returnsession)
        returning.place(rely=0.90,relx=0.40)

        clear=Button(returnBook,text='Clear',fg='white',bg='black',font="hack 8 ",command=self.clearFieldsofReBooks)
        clear.place(rely=0.90,relx=0.33)

        showfine=Button(returnBook,text='Fines',fg='white',bg='black',font="hack 8 ",command=self.showfines)
        showfine.place(rely=0.90,relx=0.48)
        
        self.notReturn = Label(returnBook,font='hack 10',bg='black')
        self.notReturn.place(rely=0.95,relx=0.3,anchor=NW)

        self.Returned=Listbox(self.returnFrame,fg='green',bg='black',font='hack 12')
        self.Returned.place(relheight=0.9,relwidth=0.89,relx=0.05,rely=0.1)

        
        scrollbarY = Scrollbar(self.Returned)
        scrollbarY.pack(side = RIGHT, fill = Y )
        scrollbarX = Scrollbar(self.Returned,orient=HORIZONTAL)
        scrollbarX.pack(side = BOTTOM, fill = X )

        self.Returned.config(yscrollcommand=scrollbarY.set)
        self.Returned.config(yscrollcommand=scrollbarX.set)
        scrollbarY.config(command = self.Returned.yview() )
        scrollbarX.config(command = self.Returned.xview() )

        for details in open(f"{os.getcwd()}/Returned Books/returned.txt").read().split('\n'):
            self.Returned.insert('end',details)

        returnBook.mainloop()


    def DeleteBooks(self):

        deleteBook=Tk()
        deleteBook.title('LMS - Delete Books')
        deleteBook.geometry('700x600')
        deleteBook.config(bg='black')
        Label(deleteBook,text="Delete Books",font='hack 15').place(relheight=0.05,relwidth=0.5,relx=0.26,rely=0.02)
        self.delFrame = Frame(deleteBook,background='black',borderwidth=2,height=400,width=500)
        self.delFrame.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)


        name=Label(deleteBook,text='Book Name',font='hack 10')
        name.place(rely=0.75,relx=0.35,anchor=NE)
        
        self.booktoDel=Entry(deleteBook,borderwidth=3)
        self.booktoDel.place(rely=0.75,relx=0.56,anchor=NE,relwidth=0.2)

        submit=Button(deleteBook,text='Delete',fg='white',bg='black',font="hack 8 ",command=self.delsession)
        submit.place(rely=0.81,relx=0.45)
        clear=Button(deleteBook,text='Clear',fg='white',bg='black',font="hack 8 ",command=self.clearFieldsofDelBooks)
        clear.place(rely=0.81,relx=0.38)
        
        self.notDel = Label(deleteBook,font='hack 10',bg='black')
        self.notDel.place(rely=0.88,relx=0.3,anchor=NW)

        self.deleted=Listbox(deleteBook,fg='green',bg='black',font='hack 12')
        self.deleted.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)

        
        scrollbarY = Scrollbar(self.deleted)
        scrollbarY.pack(side = RIGHT, fill = Y )



        
        self.deleted.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.1)
        
        for logs in open(f"{os.getcwd()}/Logs/logs.txt").read().split('\n'):
            self.deleted.insert('end',logs)



        deleteBook.mainloop()



Win = Tk()
img =  Image.open("uit.jpg")
img = img.resize((200,180))
img = ImageTk.PhotoImage(img)

library=LibraryModels(Win,img)

Win.mainloop()
