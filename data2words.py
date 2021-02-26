#!\usr\bin\python
# -*- coding:utf-8 -*-
#www.philiphacker.in
import os
import time
import platform
from datetime import datetime
def cls():
    pf=platform.system()
    pf=pf.lower()
    pfsys=str(pf)
    if pfsys=="linux":
        os.system("clear")
    else:
        os.system("cls")
def reset():
    input("press any key to retry..")
    start()
def help():
    print("\n\n This is a tool to encode and decode 4 types of data which are name, age, date of birth and mobile number.\n\n Type 1 or en or encode to encode\n Type 2 or de or decode to decode\n Type 3 or x or exit to close\n Type hackerzx for easter egg\n Type help or ? or about for this menu\n\nFor more info visit, www.philiphacker.in\n\n")
    input("press any key to go back..")
    start()
def terminate():
    print("\n\n    Thank you :)\nwww.philiphacker.in\n\n")
    exit()
def encode():
    name=input("What is your name ?  : ")
    age=input("What is your age ?   : ")
    dob=input("What is your dob ?   : ")
    mob=input("Your Mobile number ? : ")
    if len(name)<3:
        print("\n\nError !!!\n\nName can't be below 3 characters\n\n")
        reset()
    elif len(name)>32:
        print("\n\nError !!!\n\nName can't be above 32 characters\n\n")
        reset()
    if name=="" or age=="" or dob=="" or mob=="" or name==" " or age==" " or dob==" " or mob==" ":
        print("\n\nError !!!\n\nField can't be empty !\n\n")
        reset()
    for i in name:
        if i.isalpha()==False:
            print("\n\nError !!!\n\nUse only English letters in name !\nName shouldn't contains numbers  !\nName shouldn't contains symbols  !\nName shouldn't contains space    !\n\n")
            reset()
    if len(mob)==10:
        pass
    else:
        print("\n\nError !!!\n\nMobile number have to be 10 digit\n\nyou entered :",len(mob),"digit")
        print("\n")
        reset()
    for i in mob:
        if i.isdigit()==True:
            pass
        else:
            print("\n\nError !!!\n\nMobile number must be numeric\n\nyou entered :",str(mob),"\n\n")
            reset()
    try:
        if len(dob)==10:
            if dob.isdigit()==True:
                print("\n\nError !!!\n\nRecheck Date of Birth !\n\n")
                reset()
        else:
            print("\n\nError !!!\n\nDob must be in following format,\n(dd/mm/yyyy)\n\nExample : 21/05/1996 \n\n")
            reset()
    except ValueError:
        print("\n\nError !!!\n\nRecheck Date of Birth !\n\n")
        reset()
    if age.isdigit()==False:
        print("\n\nError !!! \n\nAge must be numeric value !\n\n ")
        reset()
    if len(age)<2:
        age="0"+age
    elif len(age)>3 or int(age)>150:
        print("\n\nError !!! \n\nAge you entered is impossible !\n\nTry to google : JEANNE LOUISE CALMENT\n\n")
        reset()
    elif len(age)>2:
        age=age+"legend "
    aaa=age
    age=age.replace("0","gold ").replace("1","is ").replace("2","apple ").replace("3","god ").replace("4","what ").replace("5","on ").replace("6","car ").replace("7","draw ").replace("8","will ").replace("9","then ")
    s=""
    for r in dob:
        if r.isdigit():
            s=s+r
        else:
            continue
    if s.isdigit()==False:
        print("\n\nError !!!\n\nDob must be in following format,\n(dd/mm/yyyy)\n\nExample : 21/05/1996 \n\n")
        reset()
    ab=dob[0:2]
    cd=dob[3:5]
    ef=dob[6:10]
    yyyy=datetime.now().strftime("%Y")
    if int(ab)>31 or int(ab)<1:
        print("\n\nError : Invalid Date in Dob !!!\n\n")
        reset()
    elif int(cd)>12 or int(cd)<1:
        print("\n\nError : Invalid Month in Dob !!!\n\n")
        reset()
    elif int(ef)>int(yyyy) or int(ef)<1900:
        print("\n\nError : Invalid Year in Dob !!!\n\n")
        reset()
    if int(cd)==2:
        if int(ab)>29:
            print("\n\nError : Feb doesn't have 30 or 31 !!!\n\n")
        reset()
    hhh=int(cd)
    if hhh==4 or hhh==6 or hhh==9 or hhh==11:
        print("\n\nError : Month you typed contains only 30 days!!!\n\n")
        reset()
    ans=int(yyyy)-int(ef)
    if int(ans)==int(aaa) or (int(ans)-1)==int(aaa):
        pass
    else:
        print("\n\nError !!!\n\nDob and Age doesn't match !\n\nAs per your dob, (",dob,")\nyour age is :",int(ans)-1,"or",ans,"\n\n")
        reset()
    dob=s.replace("0","fire ").replace("1","pig ").replace("2","ghost ").replace("3","from ").replace("4","arrow ").replace("5","up ").replace("6","life ").replace("7","world ").replace("8","because ").replace("9","which ")
    x=mob
    y=["0","1","2","3","4","5","6","7","8","9"]
    z=[]
    for i in y:
        for j in y:
            z.append(i+j)
    a=""
    s=[]
    for k in x:
        a=a+k
        if len(a)==2:
            s.append(a)
            a=""
    n=["kite ","hit ","solar ","magic ","dog ","of ","soft ","and ","cold ","on ","queen ","maths ","dice ","kill ","did ","pop ","soap ","dry ","sky ","how ","be ","bold ","would ","still ","time ","can ","sold ","fox ","jump ","mad ","pan ","make ","drill ","swing ","love ","six ","gems ","fix ","mix ","tax ","soil ","pen ","we ","both ","man ","torch ","as ","win ","rose ","bot ","ping ","zip ","tip ","saw ","nose ","under ","run ","cry ","black ","him ","you ","bomb ","got ","jet ","come ","end ","game ","lip ","beach ","way ","give ","dot ","are ","pure ","drink ","there ","dark ","dose ","pick ","final ","boss ","mouse ","four ","digit ","word ","see ","bye ",'boy ',"mint ","bulb ","me ","tick ","simple ","put ","sit ","dive ","lion ","like ","am ","out "]
    b=""
    for o in s:
        m=(z.index(o))
        p=n[m]
        b=b+p
    mob=b
    name=name.lower().replace("a","00").replace("b","01").replace("c","02").replace("d","03").replace("e","47").replace("f","05").replace("g","06").replace("h","07").replace("i","08").replace("j","09").replace("k","27").replace("l","11").replace("m","12").replace("n","13").replace("o","14").replace("p","15").replace("q","16").replace("r","17").replace("s","18").replace("t","19").replace("u","92").replace("v","21").replace("w","22").replace("x","23").replace("y","24").replace("z","25")
    name=name.replace("00","umbrella ").replace("01","light ").replace("02","down ").replace("03","aim ").replace("47","or ").replace("05","male ").replace("06","kiss ").replace("07","best ").replace("08","fear ").replace("09","grace ").replace("27","oreo ").replace("11","head ").replace("12","lemon ").replace("13","form ").replace("14","owl ").replace("15","alien ").replace("16","when ").replace("17","fresh ").replace("18","thumb ").replace("19","thief ").replace("92","sing ").replace("21","water ").replace("22","bingo ").replace("23","slim ").replace("24","egg ").replace("25","ocean ")
    x=age+dob+mob+name
    print("\n")
    print("Encryted text,\n\n",x)
    print("\n")
    input("press any key to continue..")
    start()
def magic():
    ani=["w","ww","www","www.","www.p","www.ph","www.phi","www.phil","www.phili","www.philip","www.philiph","www.philipha","www.philiphac","www.philiphack","www.philiphacke","www.philiphacker","www.philiphacker.","www.philiphacker.i","www.philiphacker.in","www.philiphacker.in ","www.philiphacker.in «","www.philiphacker.in ««","www.philiphacker.in «««","www.philiphacker.in ««","www.philiphacker.in «","www.philiphacker.in ","www.philiphacker.in","www.philiphacker.i","www.philiphacker.","www.philiphacker","www.philiphacke","www.philiphack","www.philiphac","www.philipha","www.philiph","www.philip","www.phili","www.phil","www.phi","www.ph","www.p","www.","www","ww","w"]
    i=0
    az=0
    while True:
        print(ani[i])
        time.sleep(0.1)
        cls()
        az=az+1
        if az==110:
            pf=platform.system()
            pf=pf.lower()
            pfsys=str(pf)
            if pfsys=="linux":
                os.system("xdg-open https://www.philiphacker.in")
                cls()
                print("Opening Webpage...")
                time.sleep(2)
                start()
            else:
                os.system("start www.philiphacker.in")
                cls()
                print("Opening Webpage...")
                time.sleep(2)
                start()
        else:
            pass
        if i==44:
            i=0
        else:
            i=i+1
def decode():
    try:
        y=input("Decode : ")
        y=y.lower().strip()
        y=y+" "
        noob=["kite","hit","solar","magic","dog","of","soft","and","cold","on","queen","maths","dice","kill","did","pop","soap","dry","sky","how","be","bold","would","still","time","can","sold","fox","jump","mad","pan","make","drill","swing","love","six","gems","fix","mix","tax","soil","pen","we","both","man","torch","as","win","rose","bot","ping","zip","tip","saw","nose","under","run","cry","black","him ","you","bomb","got","jet","come","end","game","lip","beach","way","give","dot","are","pure","drink","there","dark","dose","pick","final","boss","mouse","four","digit","word","see","bye",'boy',"mint","bulb","me","tick","simple","put","sit","dive","lion","like","am","out"]
        nip=""
        for i in y.split():
            if i in noob:
                m=noob.index(i)
                if len(str(m))==2:
                    nip=nip+str(m)
                else:
                    m="0"+str(m)
                    nip=nip+str(m)
        mo=nip[-10:-1]
        bo=nip[-1]
        mob=mo+bo
        g=y.replace("gold ","0").replace("is ","1").replace("apple ","2").replace("god ","3").replace("what ","4").replace("on ","5").replace("car ","6").replace("draw ","7").replace("will ","8").replace("then ","9")
        if "legend" in y:
            age=g[0:3]
        else:
            age=g[0:2]
        h=y.replace("fire ","0").replace("pig ","1").replace("ghost ","2").replace("from ","3").replace("arrow ","4").replace("up ","5").replace("life ","6").replace("world ","7").replace("because ","8").replace("which ","9")
        dob=""
        for i in list(h):
            if i.isdigit()==True:
                dob=dob+i
        dd=dob[0:2]
        mm=dob[2:4]
        yy=dob[4:8]
        dob=dd+"/"+mm+"/"+yy
        y=y.lower().replace("umbrella ","a").replace("light ","b").replace("down ","c").replace("aim ","d").replace("or ","e").replace("male ","f").replace("kiss ","g").replace("best ","h").replace("fear ","i").replace("grace ","j").replace("oreo ","k").replace("head ","l").replace("lemon ","m").replace("form ","n").replace("owl ","o").replace("alien ","p").replace("when ","q").replace("fresh ","r").replace("thumb ","s").replace("thief ","t").replace("sing ","u").replace("water ","v").replace("bingo ","w").replace("slim ","x").replace("egg ","y").replace("ocean ","z")
        name=y.split()
        name=name[-1]
        print("\n")
        print("Name   :",name)
        print("Age    :",age)
        print("Dob    :",dob)
        print("Mobile :",mob)
        print("\n")
        input("press any key to continue..")
        start()
    except IndexError:
        print("\n\nError !!!\n\nText you used to decode is invalid !\nIts not a valid cipher sentence !\n\n")
        reset()
def start():
    cls()
    print("\n")
    print("    Data ★ Cipher \n\n www.philiphacker.in")
    print("\n")
    print("1 - encode")
    print("2 - decode")
    print("3 - exit")
    print("\n")
    ui=input("Enter your choice : ")
    if ui=="1" or ui=="encode" or ui=="en":
        cls()
        encode()
    elif ui=="2" or ui=="decode" or ui=="de":
        cls()
        decode()
    elif ui=="hackerzx" or ui=="3.14159265":
        cls()
        magic()
    elif ui=="3" or ui=="exit" or ui=="x":
        cls()
        terminate()
    elif ui=="?" or ui=="help" or ui=="about":
        cls()
        help()
    else:
        print("Invalid Choice !")
        time.sleep(1)
        start()
start()