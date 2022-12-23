from tkinter import*
def leng():
    if radio.get()==True:
        windows.title('Конвертер')
        Label_1['text']='Конвертер десяткових чисел\n в бінарний код'
        Label_Frame_1['text']='Опції'
        check_button_1['text']='Копіювати результати в буфер обміну'
        check_button_2['text']='Очищувати попередні результати'
        Label_2['text']='Десяткове число'
        button['text']='Конвертувати'
    else:     
        windows.title('Converter')
        Label_1['text']='Converter decimal numbers\n into binar numbers '
        Label_Frame_1['text']='Optoins'
        check_button_1['text']='Copy resalts clipbord'
        check_button_2['text']='Clear fome resalts '
        Label_2['text']='Decimal number'
        button['text']='Convert'
def binary():
    Entry.get()
    val=bin(int(Entry.get()))
    if clear.get()==True:
        text.delete(0.0,END)
        text.insert(END,'\n'+val)
    else:
        text.insert(END,'\n'+val)
    if copy.get()==True:
        windows.clipboard_clear()
        windows.clipboard_append(val)     
    
windows=Tk()
windows.geometry('400x500+400+50')
windows.title('Конвертер')
radio=BooleanVar()
radio.set(True)
copy=BooleanVar()
clear=BooleanVar()
img_UA=PhotoImage(file='UA.png')
img_USA=PhotoImage(file='USA.png')
radio_button_1=Radiobutton(image=img_UA,text='UA',variable=radio,command=leng,value=True)
radio_button_1.pack()      #text='Ukraine'
radio_button_2=Radiobutton(image=img_USA,variable=radio,command=leng,value=False)
radio_button_2.pack()      #text='English' 
Label_1=Label(text='Конвертер десяткових чисел\n в бінарний код',font='arial 12')
Label_1.pack()
Label_Frame_1=LabelFrame(windows,text='Опції',font='arial 8')
Label_Frame_1.pack()
check_button_1=Checkbutton(Label_Frame_1,variable=copy,onvalue=True,offvalue=False,text='Копіювати результати в буфер обміну',font='arial 8')
check_button_1.pack(pady=5,anchor=W)
check_button_2=Checkbutton(Label_Frame_1,variable=clear,onvalue=True,offvalue=False,text='Очищувати попередні результати',font='arial 8')
check_button_2.pack(anchor=W)
Frame_2=Frame(windows)
Frame_2.pack()
Label_2=Label(Frame_2,text='Десяткове число',font='arial 10')
Label_2.grid(row=0,column=0)
Entry=Entry(Frame_2,bg='white',width=7,font='arial 10',fg='black')
Entry.grid(row=0,column=1)
button=Button(Frame_2,text='Конвертувати',font='arial 10',command=binary)
button.grid(row=1,column=0,columnspan=2,pady=5)
text=Text(Frame_2,font='arial 10',fg='black',width=30,height=10,wrap=NONE)
text.grid(row=2,column=0,columnspan=2)
sc=Scrollbar(Frame_2,orient=HORIZONTAL)
sc.grid(row=3,column=0,columnspan=2,sticky=EW) #sticky=EW-приклеїти Scrollbar до лівого і правого краю
sc.config(command=text.xview)           #text.xview-прокрутка текстового віджиту по х
mainloop()
