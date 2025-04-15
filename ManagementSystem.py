import tkinter as tk
from tkinter import END, PhotoImage, ANCHOR
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 

def nextWindow():
    un = "admin"
    passWord = "admin123"
    connection = sqlite3.connect('test1.db')
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS TEST(FullName TEXT, DOB TEXT, DayofBirth TEXT, occupation TEXT, status TEXT, department TEXT, position TEXT, PhoneNo INTEGER)"""
    cursor.execute(command1)
    if user_entry.get()==un and pass_entry.get()==passWord:
        root.destroy()

        def dashPage():
            cursor.execute("SELECT * FROM TEST")
            res = cursor.fetchall()
            print(res)
            #No. of members
            cursor.execute("SELECT COUNT(name) FROM TEST")
            result = cursor.fetchone()
            print(result[0])

            #No. of Leaders
            data = ["null"]
            cursor.execute("SELECT COUNT(name) FROM TEST WHERE position != ?", data)
            result1 = cursor.fetchone()
            print(result1[0])

            header = tk.Frame(mainFrame, bg="blue")
            header.place(x= 0, y= 0, width=1070, height= 60)

            bodyFrame1 = tk.Frame(mainFrame, bg="white")
            bodyFrame1.place(x=10, y=110, width=1030, height=300)

            title1 = tk.Label(bodyFrame1, text= "No. of Members", font= ("bold", 30), bg= "white")
            title1.place(x= 20, y= 25)

            title1_1 = tk.Label(bodyFrame1, text= f"{result[0]}", font= ("bold", 42), bg= "white")
            title1_1.place(x= 140, y= 125)

            title2 = tk.Label(bodyFrame1, text= "No. of Departments", font= ("bold", 30), bg= "white")
            title2.place(x= 355, y= 30)

            title2_1 = tk.Label(bodyFrame1, text= "6", font= ("bold", 42), bg= "white")
            title2_1.place(x= 470, y= 130)

            title3 = tk.Label(bodyFrame1, text= "No. of Leaders", font= ("bold", 30), bg= "white")
            title3.place(x= 760, y= 30)

            title2_1 = tk.Label(bodyFrame1, text= f"{result1[0]}", font= ("bold", 42), bg= "white")
            title2_1.place(x= 850, y= 130)

            lb = tk.Label(header, text="Management System", font=("bold", 30), bg= "blue", fg= "white")
            lb.place(x= 300, y= 0)

        def managePage():
            def adding():
                name = name_entry.get()
                DOB = DOB_entry.get()
                day = day_entry.get()
                occupation = occ_entry.get()
                status = status_entry.get()
                dept = dept_entry.get()
                position = pos_entry.get()
                phoneNo = phoneNo_entry.get()

                data = [name, DOB, day, occupation, status, dept, position, phoneNo]
                print(data)
                cursor.execute("INSERT INTO TEST VALUES (?, ?, ?, ?, ?, ?, ?, ?)",data)
                connection.commit()
                messagebox.showinfo(title= "Added", message= "Successfully Added")

            def updating():
                username = uname_entry.get()
                id = ident.get()
                update_info = info.get()

                data = [update_info, username]

                cursor.execute(f"UPDATE TEST SET {id} = ? WHERE name = ?", data)
                connection.commit()
                messagebox.showinfo(title= "Updated", message= "Successfully Updated")

            def deleting():
                del_info = del_entry.get()
                data = [del_info]

                cursor.execute(f"DELETE FROM TEST WHERE name = ?", data)
                connection.commit()
                messagebox.showinfo(title= "Deleted", message= "Successfully Deleted")

            header = tk.Frame(mainFrame, bg="blue")
            header.place(x= 0, y= 0, width=1070, height= 60)

            lb = tk.Label(header, text="Management System", font=("bold", 30), fg= "white", bg= "blue")
            lb.place(x= 300, y= 0)
            #adding info
            add_frame = tk.Frame(mainFrame, bg= "white")
            add_frame.place(x= 30, y= 100, width= 450, height= 580)

            add_text = tk.Label(add_frame, text= "ADD INFO")
            add_text.place(x= 10, y= 0)

            name_text = tk.Label(add_frame, text= "Full Name", font= ("bold", 16), bg= "white")
            name_text.place(x= 40, y= 22)
            name_entry = tk.Entry(add_frame, font= (15))
            name_entry.place(x= 40, y= 50, width= 250, height= 30)

            DOB_text = tk.Label(add_frame, text= "Date of Birth", font= ("bold", 16), bg= "white")
            DOB_text.place(x= 40, y= 75)
            DOB_entry = tk.Entry(add_frame, font= (15))
            DOB_entry.place(x= 40, y= 103, width= 250, height= 30)

            day_text = tk.Label(add_frame, text= "Day of Birth", font= ("bold", 16), bg= "white")
            day_text.place(x= 40, y= 131)
            day_entry = tk.Entry(add_frame, font= (15))
            day_entry.place(x= 40, y= 165, width= 250, height= 30)

            occ_text = tk.Label(add_frame, text= "Occupation", font= ("bold", 16), bg= "white")
            occ_text.place(x= 40, y= 190)
            occ_entry = tk.Entry(add_frame, font= (15))
            occ_entry.place(x= 40, y= 218, width= 250, height= 30)

            status_text = tk.Label(add_frame, text= "Status", font= ("bold", 16), bg= "white")
            status_text.place(x= 40, y= 243)
            status_entry = ttk.Combobox(add_frame, font= (15), values=["Active", "Suspended", "On-Hiatus"])
            status_entry.place(x= 40, y= 271, width= 250, height= 30)

            dept_text = tk.Label(add_frame, text= "Department", font= ("bold", 16), bg= "white")
            dept_text.place(x= 40, y= 310)
            dept_entry = ttk.Combobox(add_frame, font= (15), values=["Chior", "Glory Band", "Women at the Gate", "Intercessor", "Media", "Security", "Usher", "Administration", "Elders"])
            dept_entry.place(x= 40, y= 338, width= 250, height= 30)

            pos_text = tk.Label(add_frame, text= "Position", font= ("bold", 16), bg= "white")
            pos_text.place(x= 40, y= 369)
            pos_entry = tk.Entry(add_frame, font= (15))
            pos_entry.place(x= 40, y= 399, width= 250, height= 30)

            phoneNo_text = tk.Label(add_frame, text="Phone Number", font= ("bold", 16), bg= "white")
            phoneNo_text.place(x= 40, y= 490)
            phoneNo_entry = tk.Entry(add_frame, font= (15))
            phoneNo_entry.place(x= 40, y= 518, width= 250, height= 30)

            add_button = tk.Button(add_frame, text= "ADD", fg= "white", bg= "blue", font= ("bold"), command= adding)
            add_button.place(x= 350, y= 540, width= 60, height= 30)

            #updating info
            update_frame = tk.Frame(mainFrame, bg= "white")
            update_frame.place(x= 520, y= 100, width= 500, height= 300)

            update_text = tk.Label(update_frame, text= "UPDATE")
            update_text.place(x= 10, y= 0)

            uname_text = tk.Label(update_frame, text= "Full Name", font= ("bold", 16), bg= "white")
            uname_text.place(x= 30, y= 30)
            uname_entry = tk.Entry(update_frame, font= (15))
            uname_entry.place(x= 30, y= 65, width= 250, height= 30)
            note = tk.Label(update_frame, text= "Enter the data you wish to update", font= ("bold", 16), bg= "white")
            note.place(x= 30, y= 110)
            ident = ttk.Combobox(update_frame, values=["Full Name", "DOB", "Day of Birth", "Occupation", "Status", "Department", "Position", "Phone Number"], font= (15))
            ident.place(x= 30, y= 150, width= 170, height= 30)
            info = tk.Entry(update_frame, font= (15))
            info.place(x= 210, y= 150, width= 250, height= 30)
            update_button = tk.Button(update_frame, text= "UPDATE", fg= "white", bg= "blue", font= ("bold", 14), command= updating)
            update_button.place(x= 30, y= 190, width= 90, height= 30)

            #deleting info
            del_frame = tk.Frame(mainFrame, bg= "white")
            del_frame.place(x= 520, y= 450, width= 500, height= 231)

            del_text = tk.Label(del_frame, text= "DELETE")
            del_text.place(x= 10, y= 0)

            del_text = tk.Label(del_frame, text= "Full Name", font= ("bold", 16), bg= "white")
            del_text.place(x= 30, y= 100)
            del_entry = tk.Entry(del_frame, font= (15))
            del_entry.place(x= 30, y= 150, width= 250, height= 30)

            del_button = tk.Button(del_frame, text= "DELETE", fg= "white", bg= "red", font= ("bold", 14), command= deleting)
            del_button.place(x= 290, y= 150, width= 90, height= 30)

        def searchPage():

            def listing():
                def select():

                    def genPDF():
                        fileName = 'MS export.pdf'
                        documentTitle = 'Management System Exported PDF'
                        title = 'Management System'
                        subTitle = 'PROFILE INFORMATION'
                        textLines = [ 
                            f'Full Name: {res[0]}', 
                            f'Date of Birth: {res[1]}',
                            f'Day of Birth: {res[2]}',
                            f'Occupation: {res[3]}',
                            f'Status: {res[4]}',
                            f'Department: {res[5]}',
                            f'Position: {res[6]}',
                            f'Phone Number: 0{res[7]}', 
                        ] 

                        # creating a pdf object 
                        pdf = canvas.Canvas(fileName) 

                        # setting the title of the document 
                        pdf.setTitle(documentTitle) 

                        # registering a external font in python 
                        pdfmetrics.registerFont( 
                            TTFont('TNR', 'times.ttf') 
                        ) 

                        # creating the title by setting it's font 
                        # and putting it on the canvas 
                        pdf.setFont('TNR', 36) 
                        pdf.drawCentredString(300, 770, title) 

                        # creating the subtitle by setting it's font, 
                        # colour and putting it on the canvas 
                        pdf.setFillColorRGB(0, 0, 255) 
                        pdf.setFont("Courier-Bold", 24) 
                        pdf.drawCentredString(290, 720, subTitle) 

                        # drawing a line 
                        pdf.line(30, 710, 550, 710) 

                        # creating a multiline text using 
                        # textline and for loop 
                        text = pdf.beginText(40, 680) 
                        text.setFont("Courier", 18) 
                        text.setFillColor(colors.red) 
                        for line in textLines: 
                            text.textLine(line) 
                        pdf.drawText(text) 

                        # drawing a image at the 
                        # specified (x.y) position 
                        #pdf.drawInlineImage(image, 130, 400) 

                        # saving the pdf 
                        pdf.save() 
                        messagebox.showinfo(title= "Pdf Download", message= "Successfully Downloaded PDF")

                    name = [my_list.get(ANCHOR)]
                    cursor.execute("SELECT * FROM TEST WHERE name = ?", name)
                    res = cursor.fetchone()
                    print(f"this is the item: {name}")

                    profile = Image.open('user.png')
                    resize_pic = profile.resize((100, 100))
                    pro_photo = ImageTk.PhotoImage(resize_pic)
                    pro_logo = tk.Label(view_frame, image = pro_photo, bg= "#e5dfcf")
                    pro_logo.image = pro_photo
                    pro_logo.place(x= 335, y= 10)

                    title1 = tk.Label(view_frame, text="Management System", font=("bold", 20), bg= "white", fg= "black")
                    title1.place(x= 10, y= 90)

                    #Details
                    titleName = tk.Label(view_frame, text="Full Name: ", font=("bold", 16), bg= "white", fg= "black")
                    titleName.place(x= 10, y= 140)
                    DBName = tk.Label(view_frame, text=f"{res[0]}", font=("bold", 16), bg= "white", fg= "black")
                    DBName.place(x= 150, y= 140, width= 125)

                    titleDOB = tk.Label(view_frame, text="Date Of Birth: ", font=("bold", 16), bg= "white", fg= "black")
                    titleDOB.place(x= 10, y= 166)
                    dbDOB = tk.Label(view_frame, text=f"{res[1]}", font=("bold", 16), bg= "white", fg= "black")
                    dbDOB.place(x= 150, y= 166,)
                    #---------------------------------------------------------
                    titleDay = tk.Label(view_frame, text="Day Of Birth:", font=("bold", 16), bg= "white", fg= "black")
                    titleDay.place(x= 10, y= 192)
                    dbDay = tk.Label(view_frame, text=f"{res[2]}", font=("bold", 16), bg= "white", fg= "black")
                    dbDay.place(x= 150, y= 192, width= 120)

                    titleOcc = tk.Label(view_frame, text="Occupation:", font=("bold", 16), bg= "white", fg= "black")
                    titleOcc.place(x= 10, y= 218)
                    dbOcc = tk.Label(view_frame, text=f"{res[3]}", font=("bold", 16), bg= "white", fg= "black")
                    dbOcc.place(x= 150, y= 218, width= 120)

                    titleStatus = tk.Label(view_frame, text="Status:", font=("bold", 16), bg= "white", fg= "black")
                    titleStatus.place(x= 10, y= 244)
                    dbStatus = tk.Label(view_frame, text=f"{res[4]}", font=("bold", 16), bg= "white", fg= "black")
                    dbStatus.place(x= 150, y= 244, width= 120)

                    titleDept = tk.Label(view_frame, text="Department:", font=("bold", 16), bg= "white", fg= "black")
                    titleDept.place(x= 10, y= 270)
                    dbDept = tk.Label(view_frame, text=f"{res[5]}", font=("bold", 16), bg= "white", fg= "black")
                    dbDept.place(x= 150, y= 270, width= 120)

                    titlePos = tk.Label(view_frame, text="Position:", font=("bold", 16), bg= "white", fg= "black")
                    titlePos.place(x= 10, y= 296)
                    dbPos = tk.Label(view_frame, text=f"{res[6]}", font=("bold", 16), bg= "white", fg= "black")
                    dbPos.place(x= 150, y= 296, width= 120)

                    titlePhone = tk.Label(view_frame, text="Phone No:", font=("bold", 16), bg= "white", fg= "black")
                    titlePhone.place(x= 10, y= 348)
                    dbPhone = tk.Label(view_frame, text=f"0{res[7]}", font=("bold", 16), bg= "white", fg= "black")
                    dbPhone.place(x= 150, y= 348, width= 130)

                    pdf_btn = tk.Button(display_frame, text= "Save PDF", bg= "blue", fg= "white", font= ("bold", 14), command= genPDF)
                    pdf_btn.place(x= 390, y= 532)
                    

                data = [search_input.get()]
                id_tag = search_id.get()
                cursor.execute(f"SELECT * FROM TEST WHERE {id_tag} = ?", data)
                results = cursor.fetchall()   
                print(results) 
                my_list = tk.Listbox(list_frame, font=("bold", 20), height= 50)
                my_list.place(x= 25, y= 20, width= 400, height= 300)
                for i in results:
                    my_list.insert(END, i[0])
                
                view_btn = tk.Button(list_frame, text= "View Details", bg= "white", command= select)
                view_btn.place(x= 350, y= 325)
                

            header = tk.Frame(mainFrame, bg="blue")
            header.place(x= 0, y= 0, width=1070, height= 60)

            search_frame = tk.Frame(mainFrame, bg= "white")
            search_frame.place(x= 30, y= 100, width= 450, height= 200)

            search_text = tk.Label(search_frame, text="SEARCH FOR INFORMATION", bg= "white", font= ("bold"))
            search_text.place(x= 30, y= 40)

            search_id = ttk.Combobox(search_frame, values=["FullName", "DOB", "DayofBirth", "Occupation", "Status", "Department", "Position", "PhoneNo"], font= (15))
            search_id.place(x= 30, y= 70, width= 105, height= 30)

            search_input = tk.Entry(search_frame, font= (15))
            search_input.place(x= 139, y= 70, width= 200, height= 30)

            Sbtn = tk.Button(search_frame, text= "SEARCH", cursor= 'hand2', font= ("bold"), command= listing)
            Sbtn.place(x= 340, y= 72)
            hint = tk.Label(search_frame, text= "N.B: Search for names, department, occupation", font= ("", 10), bg= "white", fg= "#158aff")
            hint.place(x= 30, y= 120)


            list_frame = tk.Frame(mainFrame, bg= "blue")
            list_frame.place(x= 30, y= 320, width= 450, height= 352)
                

            display_frame = tk.Frame(mainFrame, bg= "grey")
            display_frame.place(x= 520, y= 100, width= 500, height= 570)

            view_frame = tk.Frame(display_frame, bg= "white")
            view_frame.place(x= 30, y= 30, width= 445, height= 500)

            lb = tk.Label(header, text="Management System", font=("bold", 30), bg= "blue", fg= "white")
            lb.place(x= 300, y= 0)

        def delete_page():
            for frame in mainFrame.winfo_children():
                frame.destroy()

        def hideIndicator():
            home_indicate.config(bg="#ffffff")
            manage_indicate.config(bg="#ffffff")
            search_indicate.config(bg="#ffffff")

        def indicate(lb, page):
            hideIndicator()
            lb.config(bg= "#158aff")
            delete_page()
            page()

        def logout():
            mainWindow.destroy()

        mainWindow = tk.Tk()
        mainWindow.title("Management System")
        mainWindow.geometry('3366x768')
        mainWindow.config(background="#eff5f6")

        sideBar = tk.Frame(mainWindow, bg="#ffffff")

        home_btn = tk.Button(sideBar, text="Dashboard", font=('Bold', 20), fg="#158aff", bd=0, cursor= 'hand2',bg="#ffffff", activebackground="#ffffff", command= lambda: indicate(home_indicate, dashPage))
        home_btn.place(x=60, y=300)

        home_indicate = tk.Label(sideBar, text="", bg="#ffffff")
        home_indicate.place(x= 50, y= 300, width= 5, height=40)

        manage_btn = tk.Button(sideBar, text="Add/Modify", font=('Bold', 20), fg="#158aff", bd=0, cursor= 'hand2', bg="#ffffff", activebackground="#ffffff",command= lambda: indicate(manage_indicate, managePage))
        manage_btn.place(x=60, y=370)

        manage_indicate = tk.Label(sideBar, text="", bg="#ffffff")
        manage_indicate.place(x= 50, y= 370, width= 5, height=40)

        search_btn = tk.Button(sideBar, text="Search", font=('Bold', 20), fg="#158aff", bd=0, cursor= 'hand2',bg="#ffffff", activebackground="#ffffff",command= lambda: indicate(search_indicate, searchPage))
        search_btn.place(x=60, y=440)

        search_indicate = tk.Label(sideBar, text="", bg="#ffffff")
        search_indicate.place(x= 50, y= 440, width= 5, height=40)

        log_btn = tk.Button(sideBar, text="Logout", font=('Bold', 20), fg="#158aff", bd=0, cursor= 'hand2', bg="#ffffff", activebackground="#ffffff", command= logout)
        log_btn.place(x=60, y=510)


        sideBar.pack(side=tk.LEFT)
        sideBar.pack_propagate(False)
        sideBar.configure(width= 300, height= 750)

        mainFrame = tk.Frame(mainWindow, highlightbackground="black", highlightthickness= 2, bg= "#e5dfcf")
        mainFrame_text = tk.Label(mainFrame, text= "Welcome Administrator", font= ("bold", 30), bg= "#e5dfcf")
        mainFrame_text.pack()
        mainFrame_text.place(x= 200, y= 350)
        welImage = Image.open('welcome-back.png')
        wel_photo = ImageTk.PhotoImage(welImage)
        wel_logo = tk.Label(mainFrame, image = wel_photo, bg= "#e5dfcf")
        wel_logo.image = wel_photo
        wel_logo.place(x= 650, y= 310)


        mainFrame.pack(side=tk.LEFT)
        mainFrame.pack_propagate(False)
        mainFrame.configure(height= 1070, width= 1059)
    else:
        messagebox.showerror(title="Error", message="Invalid credential")

root = tk.Tk()
root.title("Management System")
app_width = 640
app_height = 440
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')



mainFrame = tk.Frame(root, bg="white")
sideBar = tk.Frame(root, bg="white")

login_label = tk.Label(mainFrame, text='Login', font=["Aria", 20], bg= "white")
login_label.pack()
login_label.place(x= 150, y= 60)

username = tk.Label(mainFrame, text="Username", font=["Aria", 16], bg= "white")
username.pack()
username.place(x= 70, y= 105)

password = tk.Label(mainFrame, text="Password", font=["Aria", 16], bg= "white")
password.pack()
password.place(x= 70, y= 160)

user_entry = tk.Entry(mainFrame, font=["Aria", 16])
user_entry.pack()
user_entry.place(x= 70, y= 130)

pass_entry = tk.Entry(mainFrame, show="*", font=["Aria", 16])
pass_entry.pack()
pass_entry.place(x= 70, y= 190)

login_button = tk.Button(mainFrame, text="Login", bg="blue", fg="#FFFFFF", font=["Aria", 16], command= nextWindow)
login_button.pack()
login_button.place(x= 245, y= 220)

welImage = Image.open('login.png')
wel_photo = ImageTk.PhotoImage(welImage)
wel_logo = tk.Label(sideBar, image = wel_photo)
wel_logo.image = wel_photo
wel_logo.pack(expand= True)


sideBar.pack(side=tk.LEFT)
sideBar.pack_propagate(False)
sideBar.configure(width= 300, height= 750)

mainFrame.pack(side=tk.LEFT)
mainFrame.pack_propagate(False)
mainFrame.configure(width= 400, height= 750)

root.mainloop()