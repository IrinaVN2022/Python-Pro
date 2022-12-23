#Натисненням кнопки малюємо хрестик або нолик.
from tkinter import*
from random import randint
def clik(event,index):
    global znak,list_used,wind
    #print('!')
    if index not in list_used:
        list_used.append(index)
        
        if znak==0:
            znak=1
            list_zero.append(index)
            print(list_zero,'list_zero')
            list_canvas[index].create_oval(20,20,180,180,width=3)
            for i in win_list:                
                if i.issubset(set(list_zero)):
                    print('ZERO WINNER')
                    for y in i:
                        list_canvas[y]['bg']='red'
                    wind=Tk()
                    wind.geometry('600x300+400+50')
                    wind.title('WINNER')
                    lab_1 =Label(wind,text="ZERO WINNER",fg="red",font="Tahoma 16 bold" )
                    lab_1.pack(pady=50)
                    button_1=Button(wind,width=15,height=5,text='NEW GAME',font="Tahoma 16 bold",fg="red",command=new_game)
                    button_1.pack()
        else:
            znak=0
            list_cross.append(index)
            print(list_cross,'list_cross')
            list_canvas[index].create_line(20,20,180,180,width=3)
            list_canvas[index].create_line(180,20,20,180,width=3)
            for i in win_list:
                if i.issubset(set(list_cross)):
                    print('CROSS WINNER')
                    for y in i:
                        list_canvas[y]['bg']='red'
                        
                    wind=Tk()
                    wind.geometry('600x300+400+50')
                    wind.title('WINNER')
                    lab_2=Label(wind,text="CROSS WINNER",fg="red",font="Tahoma 16 bold" )
                    lab_2.pack(pady=50)
                    button_2=Button(wind,width=15,height=5,text='NEW GAME',font="Tahoma 16 bold",fg="red",command=new_game)
                    button_2.pack()
def game():
    global list_canvas,list_used,list_zero,list_cross,win_list,znak,windows
    znak=randint(0,1)
    print('znak',znak)
    windows=Tk()
    windows.geometry('600x600+400+50')
    windows.title('Хрестики/Нолики')
    list_canvas=[0]*9
    list_used=[]
    list_zero=[]
    list_cross=[]
    win_list=[{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
    for x in range(3):   
        for i in range(3):
            list_canvas[i+3*x]=Canvas(bg='#E9967A',width=200,height=200)
            list_canvas[i+3*x].grid(row=x+1,column=i)
            print(i+3*x)
            list_canvas[i+3*x].bind('<Button-1>',lambda event,z=i+3*x: clik(event,z))
    mainloop()
def new_game():
    windows.destroy()
    wind.destroy()
    game()


if __name__=='__main__':
    game()

#Доробити кольорову гаму, виділити кольором переможну комбінацію 

