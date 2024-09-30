from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image
from tkinter import ttk
import ttkthemes
import random , os
from tkinter import messagebox
import tempfile
from time import strftime



splash = Tk()
splash.title("Gowiseth")
splash.iconbitmap('agry.ico')
splash.config(bg='#FFFFFF')
height = 1080
width = 1920
x = (splash.winfo_screenwidth() // 2) - (width // 2)
y = (splash.winfo_screenheight() // 2) - (height // 2)
splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# backgroundImage = ImageTk.PhotoImage(file="pradarlogo.png")

# bgLabel=Label(splash,image=backgroundImage)
# bgLabel.place(x=500,y=200)
# bgLabel.pack()


img = ImageTk.PhotoImage(Image.open("pradarlogo.png").resize((712, 323)))
l = Label(splash, image=img)
l.img = img
l.place(height=323, width=712, x=550, y=300)

splash.overrideredirect(True)


def menu():
    splash.destroy()  # like a destroy
    root = Tk()
    # root.overrideredirect(True)
    # root.geometry('1920x1080+0+0')
    # root.config(bg='blue')
    root.configure(bg="#ffffff")  # colour code task bar same #ECF5F5 #ECF5F5
    root.title(" ")
    root.iconbitmap('Screenshot_(334)2.ICO')

    height = 1080
    width = 1920
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # ==========variable========

    global qty
    global prices
    global bill_no
    global c_name
    global c_phone
    global z
    global c_email
    global search_bill
    global product
    global sub_total
    global tax_input
    global total

    c_name = StringVar()
    c_phone = StringVar()
    bill_no = StringVar()
    z = random.randint(1000, 9999)
    bill_no.set(z)
    c_email = StringVar()
    search_bill = StringVar()
    product = StringVar()
    prices = StringVar()
    qty = IntVar()
    sub_total = StringVar()
    tax_input = StringVar()
    total = StringVar()

    global cat_entry
    global subcat_entry
    global subcategoryclothing
    global subcategorylifeStyle
    global subcategorymobile
    global prod_entry
    global pant
    global tshirt
    global shirt
    global soap
    global face_cream
    global hair_oil
    global price_entry
    global price_levis
    global price_mufti
    global price_spykar
    global price_polo
    global price_moose
    global price_jk
    global price_peter
    global price_louise
    global price_park

    # product Catagary
    category = ['Select Option', "Clothing", "LifeStyle", "Mobile"]
    subcategoryclothing = ["Pant", "Tshirt", "Shirt"]
    pant = ["Levis", "Mufti", "Spykar"]
    price_levis = 5000
    price_mufti = 4500
    price_spykar = 8200

    tshirt = ["Polo", "Moose", "Jack&Jones"]
    price_polo = 2000
    price_moose = 1900
    price_jk = 2200

    shirt = ["Peter England", "Louise Phillipe", "Park Avenue"]
    price_peter = 3000
    price_louise = 3500
    price_park = 3200

    subcategorylifeStyle = ["Bath Soap", "Face Creame", "Hair Oil"]
    soap = ["Rani Sadun", "Lux", "Lifeboy", "Detol", "Pearl"]
    price_rani = 200
    price_lux = 200
    price_lifeboy = 150
    price_detol = 200
    price_pearl = 250

    face_cream = ["Fair&Lovely", "Ponds", "Olay", "Garnier"]
    price_fair = 300
    price_ponds = 300
    price_olay = 350
    price_garnier = 420

    hair_oil = ["Parachute", "Jasmin", "Detol Cool", "Pearl"]
    price_parachute = 380
    price_jasmin = 350
    price_detolcool = 260
    price_pearlhair = 425

    subcategorymobile = ["Iphone", "Sumsung", "Xiome", "RealMe", "One+"]

    img = ImageTk.PhotoImage(Image.open("pradarlogo.png").resize((300, 150)))
    l = Label(root, image=img)
    l.img = img
    l.place(height=150, width=300, x=0, y=0)

    title_l1 = Label(root, text="PRADAR BILLING SYSTEM", fg='blue', bg='#ffffff', font=('SimSun', 45, 'bold'))
    title_l1.place(x=650, y=45)

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text= string)
        lbl.after(1000, time)

    lbl = Label(root,font=('SimSun', 16, 'bold'), fg='blue', bg='#ffffff')
    lbl.place(x=1694, y=53,width=250,height=50)
    time()

    main_frame = Frame(root, bd=5, relief=GROOVE, bg='#ffffff')
    main_frame.place(x=10, y=150, width=1895, height=850)

    cust_frame = LabelFrame(main_frame, text='Customer', fg='blue', bg='#ffffff', font=('SimSun', 15, 'bold'))
    cust_frame.place(x=10, y=5, width=450, height=170)

    mob_lbl = Label(cust_frame, text='Mobile No', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    mob_lbl.place(x=5, y=10)
    mob_entry = ttk.Entry(cust_frame, font=('arial', 14, 'bold'), textvariable=c_phone, width=24)
    mob_entry.place(x=160, y=10)

    name_lbl = Label(cust_frame, text='Customer Name', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    name_lbl.place(x=5, y=50)
    name_entry = ttk.Entry(cust_frame, font=('arial', 14, 'bold'), textvariable=c_name, width=24)
    name_entry.place(x=160, y=50)

    em_lbl = Label(cust_frame, text='Email', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    em_lbl.place(x=5, y=90)
    em_entry = ttk.Entry(cust_frame, font=('arial', 14, 'bold'), textvariable=c_email, width=24)
    em_entry.place(x=160, y=90)

    product_frame = LabelFrame(main_frame, text='Product', fg='blue', bg='#ffffff', font=('SimSun', 15, 'bold'))
    product_frame.place(x=500, y=5, width=500, height=250)

    cat_lbl = Label(product_frame, text='Select Categories', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    cat_lbl.place(x=5, y=10)
    cat_entry = ttk.Combobox(product_frame, values=category, font=('arial', 12, 'bold'), width=24, state="readonly")
    cat_entry.current(0)
    cat_entry.place(x=200, y=10)
    cat_entry.bind("<<ComboboxSelected>>", categories)

    subcat_lbl = Label(product_frame, text='Subcategory', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    subcat_lbl.place(x=5, y=50)
    subcat_entry = ttk.Combobox(product_frame, value=[""], font=('arial', 12, 'bold'), width=24, state="readonly")
    subcat_entry.place(x=200, y=50)
    subcat_entry.bind("<<ComboboxSelected>>", product_add)

    prod_lbl = Label(product_frame, text='Product Name', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    prod_lbl.place(x=5, y=90)
    prod_entry = ttk.Combobox(product_frame, font=('arial', 12, 'bold'), width=24, textvariable=product,
                              state="readonly")
    prod_entry.place(x=200, y=90)
    prod_entry.bind("<<ComboboxSelected>>", price)

    price_lbl = Label(product_frame, text='Price', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    price_lbl.place(x=5, y=130)
    price_entry = ttk.Combobox(product_frame, font=('arial', 12, 'bold'), width=24, textvariable=prices,
                               state="readonly")
    price_entry.place(x=200, y=130)

    qty_lbl = Label(product_frame, text='Qty', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    qty_lbl.place(x=5, y=170)
    qty_entry = ttk.Entry(product_frame, font=('arial', 14, 'bold'), textvariable=qty, width=25)
    qty_entry.place(x=203, y=170)

    # search frame
    search_frame = Frame(main_frame, bd=2, bg='#ffffff')
    search_frame.place(x=1100, y=10, width=780, height=440)

    search_lbl = Label(main_frame, text='Bill Number', fg='white', bg='blue', font=('SimSun', 14, 'bold'))
    search_lbl.place(x=1100, y=40)

    search_entry = ttk.Entry(main_frame, font=('arial', 14, 'bold'), textvariable=search_bill, width=35)
    search_entry.place(x=1240, y=40)

    Button(main_frame, text='Search', command=find_bill, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 14, 'bold')).place(x=1650, y=40, height=28, width=230)

    # rigght fram bill area

    global textarea

    right_frame = LabelFrame(main_frame, text='BILL Aria', fg='blue', bg='#ffffff', font=('SimSun', 15, 'bold'))
    right_frame.place(x=1100, y=100, width=780, height=540)

    scroll_y = Scrollbar(right_frame, orient=VERTICAL)
    textarea = Text(right_frame, yscrollcommand=scroll_y.set, fg='#052D73', bg='#ffffff', font=('SimSun', 15, 'bold'))
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=textarea.yview)
    textarea.pack(fill=BOTH, expand=1)

    billcounter_frame = LabelFrame(main_frame, text='Bill Counter', fg='blue', bg='#ffffff',
                                   font=('SimSun', 15, 'bold'))
    billcounter_frame.place(x=10, y=200, width=450, height=170)

    global subt_entry

    subt_lbl = Label(billcounter_frame, text='Sub Total', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    subt_lbl.place(x=5, y=10)
    subt_entry = ttk.Entry(billcounter_frame, font=('arial', 14, 'bold'), textvariable=sub_total, width=24)
    subt_entry.place(x=160, y=10)

    govt_lbl = Label(billcounter_frame, text='Gov Tax', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    govt_lbl.place(x=5, y=50)
    govt_entry = ttk.Entry(billcounter_frame, font=('arial', 14, 'bold'), textvariable=tax_input, width=24)
    govt_entry.place(x=160, y=50)

    total_lbl = Label(billcounter_frame, text='Total', fg='#373535', bg='#ffffff', font=('SimSun', 14, 'bold'))
    total_lbl.place(x=5, y=90)
    total_entry = ttk.Entry(billcounter_frame, font=('arial', 14, 'bold'), textvariable=total, width=24)
    total_entry.place(x=160, y=90)

    global i

    Button(main_frame, command=AddItem, text='Add To Cart', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=50, y=700, height=50, width=250)
    Button(main_frame, command=gen_bil, text='Genarate Bill', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=360, y=700, height=50, width=250)
    Button(main_frame, command=save_bill, text='Save Bill', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=660, y=700, height=50, width=250)
    Button(main_frame, command=iprint, text='Print', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=960, y=700, height=50, width=250)
    Button(main_frame, command=clear, text='Clear', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1260, y=700, height=50, width=250)
    Button(main_frame, command=root.destroy, text='Exit', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1560, y=700, height=50, width=250)

    welcome()

    i = int(1)
    i = []


# ==================function declaration================
def AddItem():
    Tax = 2
    n = prices.get()
    m = n*qty.get()
    i.append(m)
    if product.get() == "":
        messagebox.showerror("Error", "Please Select the Product Name")

    else:
        textarea.insert(END,f"\n {product.get()}\t\t\t{qty.get()}\t\t\t{m}")
        sub_total.set(str('Rs.%.2f'%(sum(i))))
        tax_input.set(str('Rs.%.2f'%((((sum(i)) - (prices.get()))*Tax)/100)))
        total.set(str('Rs.%.2f'%(((sum(i)) + ((((sum(i)) - (prices.get()))*Tax)/100)))))


def iprint():
    q = textarea.get(1.0,"end-1c")
    filename = tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,"Print")


def find_bill():
    found = "no"
    for i in os.listdir("bills/"):
        if i.split('.')[0] == search_bill.get():
            f1 = open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for d in f1:
                textarea.insert(END,d)
            f1.close()
            found = "yes"

    if found == 'no':
        messagebox.showerror("Error","Invalid Bill No")



def clear():
    textarea.delete(1.0,END)
    c_name.set("")
    c_phone.set("")
    c_email.set("")
    x = random.randint(1000,9999)
    bill_no.set(str(x))
    search_bill.set("")
    product.set("")
    prices.set(0)
    qty.set(0)
    i = [0]
    total.set("")
    sub_total.set("")
    tax_input.set('')
    welcome()




def save_bill():
    op = messagebox.askyesno("Save Bill","Do you Want to Save the Bill")
    if op>0:
        bill_data = textarea.get(1.0,END)
        f1 = open('bills/'+str(bill_no.get())+".txt",'w')
        f1.write(bill_data)
        op = messagebox.showinfo("Saved", f"Bill No : {bill_no.get()} Saved Successfully.")
        f1.close()


def gen_bil():
    if product.get() == "":
        messagebox.showerror("Error", "Please Add To Cart Product")

    else:
        text = textarea.get(10.0,(10.0+float(len(i))))
        welcome()
        textarea.insert(END,text)
        textarea.insert(END,"\n====================================================================")
        textarea.insert(END,f"\n Sub Amount: \t\t\t{sub_total.get()}")
        textarea.insert(END, f"\n Tax Amount: \t\t\t{tax_input.get()}")
        textarea.insert(END, f"\n Total Amount: \t\t\t{total.get()}")
        textarea.insert(END, "\n====================================================================")


def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t\t Welcome PARDAR Market Place")
    textarea.insert(END, "\n")
    textarea.insert(END, f"\n BILL Number :{bill_no.get()}")
    textarea.insert(END, f"\n Customer Name :{c_name.get()}")
    textarea.insert(END, f"\n Phone Number :{c_phone.get()}")
    textarea.insert(END, f"\n Customer Email :{c_email.get()}")

    textarea.insert(END, "\n====================================================================")
    textarea.insert(END, f"\n Products\t\t\tQTY\t\t\tPrice")
    textarea.insert(END, "\n====================================================================")


def categories(event=""):
    if cat_entry.get() == "Clothing":
        subcat_entry.config(value=subcategoryclothing)
        subcat_entry.current(0)

    if cat_entry.get() == "LifeStyle":
        subcat_entry.config(value=subcategorylifeStyle)
        subcat_entry.current(0)

    if cat_entry.get() == "Mobile":
        subcat_entry.config(value=subcategorymobile)
        subcat_entry.current(0)


def product_add(event=""):
    if subcat_entry.get() == "Pant":
        prod_entry.config(value=pant)
        prod_entry.current(0)

    if subcat_entry.get() == "Tshirt":
        prod_entry.config(value=tshirt)
        prod_entry.current(0)

    if subcat_entry.get() == "Shirt":
        prod_entry.config(value=shirt)
        prod_entry.current(0)

    # life style
    if subcat_entry.get() == "Bath Soap":
        prod_entry.config(value=soap)
        prod_entry.current(0)

    if subcat_entry.get() == "Face Creame":
        prod_entry.config(value=face_cream)
        prod_entry.current(0)

    if subcat_entry.get() == "Hair Oil":
        prod_entry.config(value=hair_oil)
        prod_entry.current(0)


def price(event=""):
    # pant

    if prod_entry.get() == "Levis":
        price_entry.config(value=price_levis)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Mufti":
        price_entry.config(value=price_mufti)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Spykar":
        price_entry.config(value=price_spykar)
        price_entry.current(0)
        qty.set(1)

        # tshirt
    if prod_entry.get() == "Polo":
        price_entry.config(value=price_polo)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Moose":
        price_entry.config(value=price_moose)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Jack&Jones":
        price_entry.config(value=price_jk)
        price_entry.current(0)
        qty.set(1)

        # shirt
    if prod_entry.get() == "Peter England":
        price_entry.config(value=price_peter)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Louis Phillipe":
        price_entry.config(value=price_louis)
        price_entry.current(0)
        qty.set(1)

    if prod_entry.get() == "Park Avenue":
        price_entry.config(value=price_park)
        price_entry.current(0)
        qty.set(1)

    # img=PhotoImage('icon.jpg')
    # root.iconphoto(False,img)


# splash screen timer
splash.after(1500, menu)

splash.mainloop()
