from itertools import count
import os
import time
from pathlib import Path
import instaloader
from instaloader import Profile, Post
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
pro43=os.getcwd()
def download():
    instance = instaloader.Instaloader()
    
    username = "Eithan__1837_Kamdyn"
    password = "allkosu55dos"
    #instance.login("Eithan__1837_Kamdyn", "allkosu55dos")
    
    instance.login(username,password)
    pwd=os.getcwd()
    
    if os.path.exists("xxx")==False:
        os.mkdir("xxx")
    os.chdir("xxx")
    jjy8=os.getcwd()
    n=0
    for i in open("../acc.txt"):
        os.chdir(jjy8)
        f=i.split(":")
        print(n,"=============================================================>",f[0])
        n+=1
        if os.path.exists(f[0])==False:
            os.mkdir(f[0])
        os.chdir(f[0])
    
        dds=open("page.txt","w")
        if(f[0]=="godofcar_bc"):
            dds.write("mazandarancars\nvinewcar")
            dds.close()
        if(f[0]=="beisyk_bc"):
            dds.write("organik.paylasimlar\n")
            dds.close()
        if(f[0]=="toki_bc"):#geldegulmeee :  clipcartooni  :  discovery.engenharia   :  signal.pedia  :  khande.shw  : 
            dds.write("geldegulmeee\nclipcartooni")
            dds.close()
        if(f[0]=="loverk_bc"):
            dds.write("inzomniatik\n_sadpainn\nloficraze\n")
            dds.close()
        if(f[0]=="sias_bc"):
            dds.write("voice_tori\n")
            dds.close()
        if(f[0]=="drock_bc"):
            dds.write("khande.shw\nvoice_tori\n")
            dds.close()
        if(f[0]=="polesht_"):
            dds.write("discovery.engenharia")
            dds.close()
        if(f[0]=="gogol_bc"):
            dds.write("khande.shw\nfunny_klippp\n")
            dds.close()
    
        if os.path.exists("xxx")==False:
            os.mkdir("xxx")
        os.chdir("xxx")
        sabaz=0
        bk=open("../page.txt").readlines()
        bl=len(bk)
        for kl in range(bl):
            #print(bk[sabaz])
            ty=bk[sabaz].split("\n")
            print(ty)
            try:
                profile = Profile.from_username(instance.context, username=ty[0])
                instance.download_stories(userids=[profile.userid],filename_target='{}'.format(profile.username))
                sabaz+=1
            except:
                continue 
    """
        os.system("touch P-ls-all-mp.txt P-up-in.txt")
        with open('P-up-in.txt','r') as xx:
            b=xx.read().split('\n')#splitlines()
            print(b)
        for oss in os.listdir():
            ott=oss.split(".")
            if ott == "mp4":
                print(oss)
                if oss in b:
                    print('Yes')
                else:
                    print('no')
                    # print("ok")
                    with open("P-ls-all-mp.txt","a") as iner:
                        iner.write(oss+"\n")
                    iner.close()
            os.system("rm *.xz *.jpg")
        os.chdir(pwd+"/xxx")
    """
def write():
    os.chdir(pro43)
    print(os.getcwd())
    v=open("acc.txt","r").readlines()
    m=len(v)
    
    num=0
    pwd=os.getcwd()
    for i in range(m):
        os.chdir(pwd) 
        vv=v[i].split(":")
        os.chdir("xxx")
        if os.path.exists(vv[0])==False:
            os.mkdir(vv[0])
        os.chdir(vv[0])#
        kiokio=0
        #op=open("page.txt","r").readlines()
        
    
        if os.path.exists("xxx")==False:
            os.mkdir("xxx")
        os.chdir("xxx")#
        #print(os.getcwd())
        print(os.getcwd())
        for op in open("../page.txt","r").readlines():
            ko2=op.split("\n")
            try:
                os.chdir(ko2[0])
                ("P-up-in.txt")
            except:
                continue
            print("op------------------------------------------> ",op)
            
            #pwd=os.getcwd()  
            try:
                open("P-up-in.txt","a")
                #os.system("rm -fr P-ls-all-mp.txt ")
                open("P-ls-all-mp.txt","a")
            except:
                continue
            
            os.system("rm -fr P-ls-all-mp.txt")
            os.system("rm -fr *.webp *.xz *.jpg")
            open("P-ls-all-mp.txt","a")
            print(op)
            with open('P-ls-all-mp.txt','r') as xx:
                b=xx.read()#splitlines()
            print(b)
            for oss in os.listdir():
                if "mp4" in oss:
                    print(oss)
                    if oss in b:
                        print('Yes')
                    else:
                        print('no')
                        
                        with open("P-ls-all-mp.txt","a") as iner:
                            iner.write(oss+"\n")
                        iner.close()
           
            kiokio+=1
            
            print(os.getcwd())
            #open("P-UP-in.txt","a+")
            #Path(f'{pwd}/file.txt').touch()
            #g=os.system("ls *.mp4 > P-ls-all-mp.txt")
            #open("touch P-up-in.txt","a")
            #print(g)
            os.chdir("..")
            
            num+=1
def upload():
    os.chdir(pro43)
    cl = Client()
    o=open("acc.txt","r").readlines()
    ol=len(o)
    pwd=os.getcwd()
    for i in range(ol):
        time.sleep(2)

        os.chdir(pro43)
        X=o[i].split(":")
        print(X[0], " " ,X[1])
        username=X[0]
        password=X[1]
        cl.login(username,password)
        
        #time.sleep(2)
        for ig in range(4):
            
            pass
        os.chdir(pro43)
        time.sleep(2)
        os.chdir("xxx")
        os.chdir(X[0])
        print(os.getcwd())
        #pa=open("page.txt","r").readlines()

        os.chdir("xxx")
        pwd2=os.getcwd()
        paf= open("../page.txt","r").readlines()
        paa=len(paf)
        if(paa<1):
            continue
        for pa in range(paa):

            os.chdir(pwd2)
            tyi=paf[pa].split("\n")
            time.sleep(2)
            try: 
                os.chdir(tyi[0])
            except:
                continue
            #time.sleep(2)
            uo=open("P-ls-all-mp.txt","r").readlines()
            tr=len(uo)
            if(tr<1):
                    continue
            lol=tr-1
            sfg434=os.getcwd()
            for d in range(lol):
                os.chdir(sfg434)
                #print("----------------------------> ",os.getcwd())
                with open("P-up-in.txt","r") as xx:
                    yy=xx.read()
                ds=uo[d].split("\n")
                boo=len(yy)
                if tr==boo:
                    break
                if ds[0] in yy :
                    print("up in (OK)")
                else:
                    try:
                        print(os.getcwd())
                        time.sleep(2)
                       # time.sleep(2)
                        ppw=os.getcwd()
                        #print(ppw+"\\"+ds[0])
                        plo=ppw+"\\"+ds[0]
                        print("===========================")
                        print("----------------------------> ",os.getcwd())
                        print(plo)
                        time.sleep(2)
                        cl.video_upload_to_story(plo)
                        print("_-_OK_-_")
                        with open("P-up-in.txt","a")as file:
                            file.write(ds[0] + '\n')
                            time.sleep(6)
                        print("===========================")
                        #time.sleep(2)
                        #pyautogui.press('enter')
                        #time.sleep(16)
                        #os.chdir("..")
                        file.close()
                        time.sleep(2)
                    except:
                        continue
            os.chdir("..")
        os.chdir(pwd)
        cl.logout()

download()
write()
upload()