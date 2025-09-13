from tkinter import *
from tkinter import messagebox
from Database_Form import *
# ====================================================
#=====================================================
win = Tk()
win.title('فرم ثبت نام')
width = 500
height = 390
screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()
x = (screen_w // 2) - (width // 2)
y = (screen_h // 2) - (height // 2)
win.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
color = 'grey'
win.iconbitmap('d:\Programing\Mix Icon Pack\Sci-Fi\open-folder.ico')
win.configure(bg=color)
win.resizable(0,0)
#=====================================================
# zero  = 0
data = Database('d:/form')
def insert_record():
    global data
    name = ent_name.get()
    lname = ent_lname.get()
    tel = ent_tel.get()
    py = i_py.get()
    c = i_c.get()
    net = i_net.get()
    gender = gender_var.get()
    course = ''
    if py == 1:
        course += ',پایتون'
    if c == 1:
        course += ',سی شارپ'
    if net == 1:
        course += ',شبکه'
    data.insert(name,lname,course,gender,tel)
    messagebox.showinfo('پیام بانک اطلاعات',
                        'مقادیر درون بانک اطلاعاتی ذخیره شدند')
    clear()

def selected_records(event):
    clear()
    index = lst_all.curselection()
    global selected_record
    selected_record = lst_all.get(index)
    ent_name.insert(0,selected_record[1])
    ent_lname.insert(0,selected_record[2])
    ent_tel.insert(0,selected_record[5])
    gender_var.set(selected_record[4])
       
def delete():
    index = lst_all.curselection()
    selected_record = lst_all.get(index)
    q = messagebox.askquestion('هشدار حذف آیتم',
                               'آیا از حذف کردن آیتم مورد نظر در بانک اطلاعاتی اطمینان دارید؟ ')
    if q == 'yes':
        data.delete(selected_record[0])
        clear()    
        show()    

def update():
    global selected_record
    name = ent_name.get()
    lname = ent_lname.get()
    tel = ent_tel.get()
    gender = gender_var.get()
    data.update(selected_record[0],name,lname,tel,gender)
    messagebox.showinfo('بروزرسانی',
                        '.اطالاعات کاربر در بانک اطلاعاتی با موفقیت تغییر کرد')
    show()    
    clear()        

def show():
    lst_all.delete(0,END)
    records =data.select()
    for rec in records:
        lst_all.insert(END,rec)

def exit():
    q =messagebox.askquestion('خروج',
                              'آیا واقعا قصد خروج از برنامه را دارید؟\nتمامی اطلاعات در دیتابیس ذخیره میشوند.') 
    if q == 'yes':
        win.destroy()
        data.end()
        
def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_tel.delete(0,END)
    i_py.set(0)
    i_c.set(0)
    i_net.set(0)
    gender_var.set('مرد')

def insert():
    global zero
    name = ent_name.get()
    lname = ent_lname.get()
    tel = ent_tel.get()
    python = i_py.get()
    c = i_c.get()
    network = i_net.get()
    # gender = gender_var.get()
    course = ''        
    if not name or not lname or not tel:
        messagebox.showwarning('هشدار',
                               'لطفا تمام فیلد ها را پر کنید')
        # clear()
        return
        
    if not tel.isdigit():
        messagebox.showerror('خطا',
                             'شماره تماس باید مقدار عددی داشته باشد')
        ent_tel.delete(0,END)
        return
    
    if len(tel) != 11:
        messagebox.showerror('خطا',
                             'شماره تماس باید 11 عددی باشد')
        # ent_tel.delete(0,END)
        return
    
    if python == 0 and c == 0 and network == 0:
        messagebox.showerror('خطا',
                             'حداقل باید یکی از دوره ها را گذرانده باشید') 
        return
    if python == 1:
        course += 'پایتون'
    if c == 1:
        course += 'سی شارپ'
    if network == 1:
        course += 'شبکه' 
    # zero += 1         
    # lst_all.insert(END,f'{zero}-{name},{lname}{course},{gender},{tel}\n') 
    insert_record()   

#=====================================================
lbl_name = Label(win,
                 text=': نام',
                 font='Bnazanin 18 bold',
                 bg=color)
lbl_name.place(x=375,y=10)

lbl_lname = Label(win,
                  text=': نام خانوادگی',
                  font='Bnazanin 18 bold',
                  bg=color)
lbl_lname.place(x=375 , y=60)

lbl_tel = Label(win,
                text=': شماره تماس',
                font='Bnazanin 18 bold',
                bg=color)
lbl_tel.place(x=375 , y=110)
#=====================================================
ent_name = Entry(win,
                 width=11,
                 font='arial 16',
                 justify=RIGHT)
ent_name.place(x=236 , y=15)

ent_lname = Entry(win,
                  width=11,
                  font='arial 16',
                  justify=RIGHT)
ent_lname.place(x=236 , y=65)

ent_tel = Entry(win,
                width=11,
                font='arial 16',
                justify=RIGHT)
ent_tel.place(x=236 , y=115)
#=====================================================
lbf_sx = LabelFrame(win,
                    text='جنسیت',
                    font='Bnazain 15 bold',
                    labelanchor='ne',
                    bg=color,
                    width=200,
                    height=100)
lbf_sx.pack(padx=15 , pady=4 , anchor='nw')
lbf_sx.pack_propagate(False)

gender_var = StringVar(value='مرد')
gender_var.set('مرد')

male = Radiobutton(lbf_sx,
                   text='مرد',
                   variable=gender_var,
                   value='مرد',
                   font='arial 12',
                   bg=color)
male.pack(anchor='e',pady=3)

female = Radiobutton(lbf_sx,
                     text='زن',
                     variable=gender_var,
                     value='زن',
                     font='arial 12',
                     bg=color)
female.pack(anchor='e',padx=3)
#=====================================================

scb_y = Scrollbar(win)
scb_y.place(x=212 , y=116 , height=154)

scb_x = Scrollbar(win , orient=HORIZONTAL)
scb_x.place(x=16 , y=270 , width=213)


#=====================================================

lst_all = Listbox(win,
                 width=32,
                 height=10,
                 font='Bnazanin 8 bold',
                 yscrollcommand= scb_y.set,
                 xscrollcommand= scb_x.set,
                 justify=LEFT)
lst_all.place(x=16 , y=116)

lst_all.bind('<<ListboxSelect>>',selected_records)
#=====================================================

scb_y.configure(command= lst_all.yview)
scb_x.configure(command=lst_all.xview)

#=====================================================
lbf_course = LabelFrame(win,
                          text='نام دوره',
                          font=('Bnazanin',15,'bold'),
                          labelanchor='n',
                          width=243,
                          height=130,
                          bg=color)
lbf_course.pack(anchor='se',padx=10 , pady=60)
lbf_course.pack_propagate(False)

i_py = IntVar()
i_c = IntVar()
i_net = IntVar()

chk_c = Checkbutton(lbf_course,
                     text='سی شارپ',
                     font='arial 12',
                     bg=color,
                     variable=i_c)
chk_c.pack(anchor='e',padx=5)

chk_py = Checkbutton(lbf_course,
                     text='پایتون',
                     font='arial 12',
                     bg=color,
                     variable=i_py)
chk_py.pack(anchor='e',padx=28)


chk_net = Checkbutton(lbf_course,
                     text='شبکه',
                     font='arial 12',
                     bg=color,
                     variable=i_net)
chk_net.pack(anchor='e',padx=32)
#=====================================================

btn_insert = Button(win,
                    text='ثبت نام',
                    width=12,
                    bg='black',
                    fg='white',
                    command=insert)
btn_insert.place(x=118 , y=290)

btn_clear = Button(win,
                    text='خالی کردن',
                    width=12,
                    bg='black',
                    fg='white',
                    command=clear)
btn_clear.place(x=15, y=290)

btn_show = Button(win,
                    text='نمایش رکوردها',
                    width=12,
                    bg='black',
                    fg='white',
                    command=show)
btn_show.place(x=118 , y=325)

btn_update = Button(win,
                    text='بروزکردن رکورد',
                    width=12,
                    bg='black',
                    fg='white',
                    command=update)
btn_update.place(x=15 , y=325)

btn_delete = Button(win,
                    text='حذف رکورد',
                    width=12,
                    bg='black',
                    fg='white',
                    command=delete)
btn_delete.place(x=220 , y=325)


btn_exit = Button(win,
                  text='خروج',
                  width=66,
                  bg='black',
                  fg='white',
                  command=exit)
btn_exit.place(x=15,y=358)



win.mainloop()