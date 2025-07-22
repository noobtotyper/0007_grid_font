import pyperclip

indent=4
tabs=" "*4*indent
while inp:=input():
    sp=inp.split()
    li=[]
    if (len(sp)%2)==0:
        for i in range(0,len(sp)-2,2):
            aux=tabs+"self."+sp[i]+"_"+sp[i+1]+"(cr)\n"
            li.append(aux)
        aux=tabs+"self."+sp[-2]+"_"+sp[-1]+"(cr)"
        li.append(aux)
        out="".join(li)
        pyperclip.copy(out)
        print(out)