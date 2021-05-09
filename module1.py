
import os


def fileexists(p="path"):
    return os.path.exists(p)


def getFilesNFolder(p="path"):
    try:
        dateien=[]
        ordner=[]
        for found in os.listdir(p):            
            if os.path.isdir(p+found):
                found=found.lower()
                ordner.append(found)
                #print("Ordner: "+found)
            else:
                dateien.append(found)
                #print("Datei : "+found)
        return dateien,ordner
    except:
        print("ERROR TRY OTHER DIRECTORY")
        return

def getFilesNUnterordner(o=[],q="quelle",e="Ebenen"):
    o2=[]
    error=0
    errorl=[]
    dateien=[]
    dateienex=[]
    for i in range(0,len(o)):#o sind die Unterordner des quellenverzeichnis
        print("Unterordner: "+o[i])
        if o[i][-1]!="\\":
            o[i]+="\\"
        try:
            d,o1=getFilesNFolder(q+o[i])#o1 sind die unterordner eines unterordners des quellenverzeichnisses
        except:
            print("ERROR: "+q+o[i])
            errorl.append("coudn't read Directory "+q+o[i])
            error+=1
            continue
        for j in range(0,len(d)):
            fn,fx=os.path.splitext(q+o[i]+d[j])
            dateien.append(fn)
            dateienex.append(fx)        
        for j in range(0,len(o1)):
            o2.append(o[i]+o1[j])#o2 hat alle unterordner der unterordner des quellenverzeichnisses
        del d,o1
    if e!=0:
            if e==1:
                e=-1
            else:
                e-=1
    #print("en(o2): "+str(len(o2)))
    #print("e: "+str(e)) #works until here

    while(len(o2)!=0 and e==0 or len(o2)!=0 and e!=-1):
        o3=[]
        if e!=0:
            if e==1:
                e=-1
            else:
                e-=1
        for i in range(0,len(o2)):
            print("Unterordner: "+o2[i])
            if o2[i][-1]!="\\":
                o2[i]+="\\"
            try:
                d,o1=getFilesNFolder(q+o2[i])#01 unterordner von o1
            except:
                print("ERROR: "+q+o2[i])
                errorl.append("coudn't read Directory "+q+o2[i])
                error+=1
                continue
            for j in range(0,len(d)):
                fn,fx=os.path.splitext(q+o2[i]+d[j])
                dateien.append(fn)
                dateienex.append(fx)
            for j in range(0,len(o1)):
                o3.append(o2[i]+o1[j])
            del d,o1
        o2=o3
    return dateien,dateienex,error,errorl


def setquelle():
    translation_table = dict.fromkeys(map(ord, '/'), '\\')#:->nichts
    quelle=input("Quellenverzeichnis: ")
    if not quelle:
        print("You typed nothing")
        return None
    elif quelle[-1] != "\\":
        quelle+="\\"
    
    if not os.path.isdir(quelle):   #checkt ob das Quellenverzeichnis existiert
        print("Quellenverzeichnis "+quelle+ " konnte nicht gefunden werden")
        return None
    else:
        #quelle=quelle.lower()
        quelle=quelle.translate(translation_table)
        return quelle

def setZiel():
    translation_table = dict.fromkeys(map(ord, '/'), '\\')#:->nichts
    default=os.path.dirname(os.path.realpath(__file__))+"\\TARGETFOLDER\\"
    ziel=input("Zielverzeichnis (ENTER = Standartverzeichnis): ")
    if not ziel:
        print("DEFAULT TARGETFOLDER")
        ziel=default
    else:
        if ziel[-1]!="\\":
            ziel=ziel+"\\"
    ziel=ziel.translate(translation_table)
    if not os.path.isdir(ziel):
        if ziel==default:
            os.makedirs(ziel)
            return ziel
        else:
            check=input("Das Zielverzeichnis: "+ziel+"\nkonnte nicht gefunden werden\nmöchten Sie es erstellen? (y/n): ")
            if check=="y" or check=="Y":
                try:
                    os.makedirs(ziel)
                    ziel=os.path.realpath(ziel)
                    if ziel[-1]!="\\":
                        ziel=ziel+"\\"
                    return ziel
                except:
                    print("Das Zielverzeichnis "+ziel+"\n konnte nicht erstellt werden")
                    return None
    else:
        ziel=os.path.realpath(ziel)
        if ziel[-1]!="\\":
            ziel=ziel+"\\"
        return ziel


def setfextenion():
    endung=input("Dateiendung die du Filtern möchtest: ")
    if not endung:
        print("You typed nothing")
        return None
    elif endung[0]!=".":
        endung="."+endung
    return endung

def setfextenions():    
    endungen=[]
    endung=None
    while endung==None:
        endung=setfextenion()
    endungen.append(endung)
    check=input("Nach einer weiteren Dateiendung suchen? (y/n): ")
    while check=="y" or check=="Y":
        endung=None
        while endung==None:
            endung=setfextenion()
        endungen.append(endung)
        check=input("Nach einer weiteren Dateiendung suchen? (y/n): ")
    return endungen
    
def filenamecheck(f="datei"):
    zwischen=f
    flen=len(f)
    j=-1
    while f[j]!=")"and j>-flen:
        j-=1
    if f[j]==")":
        i=j-2
        while f[i]!="(" and i>-flen:
            i-=1
        if i==-flen:
            pass#ganz normal (1) anhängen
        else:
            #zahl rausholen!
            try:            
                zahl=int(f[i+1:j])
                zahl+=1            
                f=zwischen[:i]+"("+str(zahl)+")"+zwischen[j+1:]
                return f
            except:
                #print("hey")
                pass
    fname,fex=os.path.splitext(zwischen)
    fname+="(1)"
    f=fname+fex
    return f

def test():
    i=0
    p="a.mp3"
    print(p)
    while i!=99999999:
        i+=1
        p=filenamecheck(p)
        print(p)

def getsize(p):
    return os.path.getsize(p)

class Count1:
    i=0

dC= Count1()
def b_write(s,p,maxSize=0):
    #print(str(dC.i)+" "+p)
    dC.i+=1
    ok=False
    size=os.path.getsize(s)
    if maxSize!=0 and size > maxSize:
        print("FILE SIZE BIGGER MAX SIZE")
        return False
    
    if os.path.isfile(p):
        #print(str(dC.i-1)+" exists")        
        if size !=os.path.getsize(p):
            print(str(dC.i-1)+" different size")            
            return True
        else:
            #print("IS fine: "+p)
            return False
    else:
        #print("M1 does not exists!")
        return True        
    
    return ok
if __name__=='__main__':

    test()
    os.system("pause")
