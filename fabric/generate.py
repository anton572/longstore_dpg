def formul(text:str):
    text=str(text)
    indax=0
    sil=[]
    while '[' in text[indax:]:
        try:
            indax=text.index('[',indax)
            indax1=text.index(']',indax+1)+1
            sil.append((indax,indax1))
            indax=indax1
        except:
            indax+=1

    se={}
    for i in sil:
        t=text[i[0]:i[1]]
        se[t]=t[1:-1]
    for i in se:
        t=se[i]
        if '{' in t:
            cl=t.index('}')
            tex=t[t.index('{')+1:cl]
            t=t[cl+1:]
        else:
            tex=t
        se[i]=f"[ref={t}]{tex}[/ref]"
    for k,v in se.items():
        text=text.replace(k,v)
    return text
