import sys
import os
import time
import module1

def main():
    print("pls use python 3.6!\n youre version: "+str(sys.version_info[:2]))
    error=0
    errorl=[]
    quelle=None
    maxFileSize=10000000000#10GB
    while quelle==None:
        quelle=module1.setquelle()
    print("QUELLE: "+quelle)
    dateien=[]
    #dateienex=[]
    d,o=module1.getFilesNFolder(quelle)
    for i in range(0,len(d)):
        fn,fx=os.path.splitext(quelle+d[i])
        dateien.append(fn+fx)
        #dateienex.append(fx)
    del d
    oebenen=0
    d,dx,e,el=module1.getFilesNUnterordner(o,quelle,oebenen)
    error+=e
    errorl+=el
    for j in range(0,len(d)):
        dateien.append(d[j]+dx[j])
        #dateienex.append(dx[j])
    
    print("\nAuswertung:\n")
    print("ANZ Dateien: "+str(len(dateien)))
    time.sleep(1)
    """
    for i in range(len(dateien)):
        print(str(i)+"\t"+dateien[i])
    """
    ziel=None
    while ziel==None:
        ziel=module1.setZiel()
        try:
            if ziel.lower()==quelle.lower():
                print("SAME DIR!")
                ziel=None
        except:
            continue
    print(ziel)
    #ziel="F:\\Roman\\Anime\\"
    print("START COPYING!")    
    do=True
    sco=""
    txt=quelle.split("\\")[:-1]
    for i in range(len(txt)):
        sco+=txt[i]+"\\"    
    print("sco: "+sco)
    co=""
    lco=""
    cp=10000
    jump=False
    for i in range(len(dateien)):        
        #txt=ziel#+dateien[i].split("\\")[-1]
        #print(str(os.path.isdir(txt))+" "+txt)
        txt=dateien[i].split(sco)[1].split("\\")[:-1]
        #print("txt: "+str(txt))
        co=""
        for j in range(len(txt)):
            co+=txt[j]+"\\"        
        #print("co: "+co)        
        if co!=lco:
            #print("NEW DIR!")
            lco=co
            if not os.path.isdir(ziel+co):
                try:
                    os.makedirs(ziel+co)
                    print("DIR CREATED! "+ziel+co)
                    jump=False
                except:
                    print("make dir error SKIP DIR")
                    jump=True
        if jump:
            continue
        txt=ziel+co+dateien[i].split("\\")[-1]
        #print("Ziel: "+txt)
        do=module1.b_write(str(dateien[i]),txt,maxFileSize)                
        if do==True:
            try:
                f=open(dateien[i],"rb")           #Datei zum kopieren
            except:
                error+=1
                txt="coudn't read "+dateien[i]
                print(txt)
                errorl.append(txt)
                continue
            txt=ziel+co+dateien[i].split("\\")[-1]
            #print(str(i)+" "+txt)
            try:
                z=open(txt,"wb")      #Datei erstellen
            except:
                error+=1
                txt="coudn't write "+txt
                print(txt)
                errorl.append(txt)
                f.close()
                continue
            fsize=os.path.getsize(dateien[i])
            zsize=0
            buff=bytearray()
            while fsize-zsize>1023:
                buff=f.read(1024)
                z.write(buff)
                zsize+=1024
            if zsize<fsize:
                buff=f.read(fsize-zsize)
                z.write(buff)
            z.close()
            f.close()
            proz=(int)(i/len(dateien)*100)
            print("wrote file "+str(i)+" / "+str(proz)+"% "+dateien[i].split("\\")[-1])
        else:
            #txt=ziel+co+dateien[i].split("\\")[-1]
            #print(str(i)+" "+txt)
            #print(str(i)+" "+str(do)+" "+ziel+dateien[i].split("\\")[-1])
            if i>cp:
                proz=(int)(i/len(dateien)*100)
                print(". "+str(proz)+"%")                
                cp+=10000
            pass
    print("Es sind "+str(error)+" Fehler aufgetreten\n")
    for i in range(0,len(errorl)):
        print(errorl[i])
    print("ENDE")
    input("")

if __name__=="__main__":
    main()
