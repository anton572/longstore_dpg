import math as _math
import re
import gmpy2
import time

class Random():
    def __init__(self,seed=None,):
        if seed==None:
            seed=time.time()
        self.maxSeed=gmpy2.mpz("78892568484")
        self.__seed=gmpy2.mpz(seed)
    def randint(self,min,max):
        diap=(max-min)
        value= self.__seed%diap+min
        self.__ReSeed()
        return int(value)
    def __ReSeed(self):
        #да случайные формулы если хошь можешь ещо чтото накинуть
        s5=self.__seed*(2**5)
        kr=-int(self.__seed**1.5)
        s3=(s5-self.__seed*3)/17
        dc=(-kr*2-s3)%self.maxSeed
        sc=_math.log(dc,s5)

        li=self.__seed
        self.__seed=li+s5-kr-s3+sc*li

        self.__seed=self.__seed%self.maxSeed

def _split_with_delimiters(s, delimiters):
    delimiters_pattern = '|'.join(map(re.escape, delimiters))
    parentheses_content = re.findall(r'\(.*?\)', s)
    temp_string = re.sub(r'\(.*?\)', '{}', s)
    parts = re.split(f"({delimiters_pattern})", temp_string)
    result_parts = []
    index = 0
    for part in parts:
        while '{}' in part:
            part=part.replace("{}", parentheses_content[index], 1)
            index += 1
        result_parts.append(part)
    elements = [x for x in result_parts if not re.match(delimiters_pattern, x)]
    delimiters_list = [x for x in result_parts if re.match(delimiters_pattern, x)]
    return elements, delimiters_list
class math():
    def __init__(self):
        self.random=Random()
    def __lew(self,form,dilator,F):
        sp,div=_split_with_delimiters(form,dilator)

        div=[None]+div
        value=None
        der=''
        for i,v in enumerate(sp):
            ch=div[i]

            value,derso=F(v,ch,value)

            if ch==None:
                ch=''
            der+=ch+derso
        return value,der
    def colculate(self,formul)->float:
        return self.__lew(formul,r"+-",self.sum)
    def sum(self,form,ch,value):
        if value==None:
            value=0
        vl,dv=self.mul_colculate(form)
        value+=vl*(-(ch=='-')*2+1)
        return value,dv
    def mul_colculate(self,form)->float:

        return self.__lew(form,r"*/",self.mul)
    def mul(self,form,ch,value):
        if value==None:
            value=1

        ve,dv=self.to_colculate(form)
        if ch==None:
            value=ve
        elif ch=='*':
            value*=ve
        else:
            value/=ve
        return value,dv
    def to_colculate(self,form):
        sp,div=_split_with_delimiters(form,['раз'])
        return self.to_colculate_recurs(div,sp)
    def to_colculate_recurs(self,div,formls):
        velue,dve=self.ndm_colculate(formls[-1])

        if len(formls)==1:
            return velue,dve
        ch=div[-1]
        de=ch[3:]
        if de=='':de='+'
        mul=de == '*'
        value1=int(mul)
        der=[]
        for i in range(velue):
            vl,der1=self.to_colculate_recurs(div[:-1],formls[:-1])
            if mul:
                value1*=vl
            else:
                value1+=vl
            der.append(der1)
        dern='['
        for i in der:
            dern+=i+de
        der =dern[:-1]+']'
        return value1,der
    def ndm_colculate(self,form):
        sp,div=_split_with_delimiters(form,r'dк')
        div=[None]+div
        value=None
        der=''
        for i,v in enumerate(sp):
            ch=div[i]

            value,derso=self.ndm(v,value)

            if ch==None:
                ch=''
            der+=ch+derso
        if len(div)!=1:
            return value,f'{value}'
        return value,f'{der}'
    def ndm(self,form,value):
        vl,der=self.scob(form)
        if value==None:
            return vl,der
        else:
            vle=0
            for i in range(value):
                vle+=self.random.randint(1,vl)
            return vle,der
    def scob(self,formul):
        if '(' in formul:
            val,dv=self.colculate(formul[1:-1])
            return val,f'({dv})'
        else:
            return int(formul),formul


