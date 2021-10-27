from tkinter import *
import random

root=Tk()
root.title("Lucky friend wheel")
root.geometry("500x500")

input1=Entry(root)
input1.place(relx=0.5,rely=0.2,anchor=CENTER)

friend_list=Label(root)
lucky_number=Label(root)

list1=[]

def friend_list2():
    word=input1.get()
    list1.append(word)
    friend_list['text']="Your list of friends are:"+str(list1)
    


label=Label(root,text="")
label.place(relx=0.5,rely=0.7,anchor=CENTER)


def random():
    length=len(list1)
    random_no=random.randint(0,length-1)
    lucky_number['text']="Your number is:"+str(random_no)
    print(random_no)
    random_lucky_friend=list1(random_no)
    print("Your lucky friend is:"+random_lucky_friend)
    label["text"]="your lucky friend is:"+random_lucky_friend

btn2=Button(root,text="Add to your friend list",command=friend_list2)
btn2.place(relx=0.5,rely=0.3,anchor=CENTER)
friend_list.place(relx=0.5,rely=0.4,anchor=CENTER)
lucky_number.place(relx=0.5,rely=0.6,anchor=CENTER)

btn1=Button(root,text="Who is your luck friend?",command=random)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)


root.mainloop()