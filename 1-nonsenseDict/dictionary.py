# usage of the file:
# input: subword list (dict_subwords_final.txt)
# output: normalized dict grapheme with prob (normal_dict_prob.txt), dict of word to phone (dict_word_phone.txt)
# please be informed:
# created and edited by Wenda Chen
# code upload to github, data uploaded to server
# make the code file-runable to make phone dict in server

import numpy as np

#print grapheme pronunciations
def pmethod(word, psofar, index):
    global flag
    if(index<len(word)):
      nomatch=0
      for x in range(0,len(i1)):
        if(i1[x]-1==index):
           nomatch=1
           if(flag==1):
             print (' '+wlist[x], end='', flush=True,file=f)
             pmethod(word, psofar+' '+wlist[x],i2[x])
           else:
             print (psofar+' '+wlist[x],end='', flush=True,file=f)
             flag=1
             pmethod(word, psofar+' '+wlist[x],i2[x])
      if(nomatch==0):
        flag=1
        pmethod(word, psofar, index+1)
    else:
      print('',file=f)
      flag=0


#generate dict_grapheme
f = open('dict_subwords_final.txt', 'r')
doc=f.read()
cdo=doc.split('\n')
f.close()
f = open('new_dict_grapheme.txt', 'w')
for sam in cdo:
    if(sam!=''):
        ki=0
        i1=[0 for x in range(100)]
        i2=[0 for x in range(100)]
        wlist=['' for x in range(100)]
        for j in range(1,len(sam)+1):
            for i in range(j-1,-1,-1):
              if (sam[i:j] in le2):
                  wlist[ki]=sam[i:j]
                  i1[ki]=i+1
                  i2[ki]=j
                  ki=ki+1
        flag=0
        pmethod(sam,sam,0)
        if(flag==1):
            print('',file=f)
            flag = 0
f.close()


#assign probability to each pronunciation
f = open('new_dict_grapheme.txt', 'r')
cdl=f.read()
cdo=cdl.split('\n')
f.close()
f = open('new_dict_prob.txt', 'w')
for co in cdo:
    x=co.split(' ')
    print(x[0],np.exp(-len(x)+1),co[len(x[0])+1:len(co)],file=f)

#normalized probability for each grapheme pronunciation

f = open('new_dict_prob.txt', 'r')
cdl=f.read()
cpo=cdl.split('\n')
f.close()
f = open('normal_dict_prob.txt', 'w')
ba=cpo[0].split(' ')
rec=ba[0]
tot=0
p=''
q=''
sum1=0
for cf in cpo:
    ti = cf.split(' ')
    if (ti[0] == rec):
        sum1 = sum1 + float(ti[1])
        tot=tot+1
        t2 = cf.split(ti[1])
        q=q+'*'+ti[1]
        p = p + '*' + t2[1]
    else:
        pc=p.split('*')
        qc = q.split('*')
        for i in range(tot):
            if(qc[i]!=''):
                print (rec, float(qc[i])/sum1,pc[i],file=f)
        tot=1
        rec=ti[0]
        sum1=float(ti[1])
        t2 = cf.split(ti[1])
        q=ti[1]
        p = t2[1]
pc=p.split('*')
qc = q.split('*')
for i in range(tot):
    print (rec, float(qc[i])/sum1,pc[i],file=f)
f.close()



#print phone pronunciation from graphemes
def pme(ind,x,sofar,le4,phone):
    if(ind<len(x)):
        for j in range(len(le4)):
            if(le4[j]==x[ind]):
                sofar1 = sofar
                sofar=sofar+' '+phone[j]
                pme(ind+1,x, sofar,le4,phone)
                sofar=sofar1
    else:
        print(sofar,file=f)

#prepare grapheme and phone list
f=open('g2p2.txt','r')
lis=f.read()
ps=lis.split('\n')
phone=['' for x in range(len(ps))]
for k in range(len(ps)):
    kl=ps[k].split(' ')
    km=ps[k].split(kl[0])
    ps[k]=kl[0]
    phone[k]=km[1]
le2=set(ps)
le4=ps
f.close()

#grapheme to phone

f = open('new_dict_grapheme.txt', 'r')
cdl=f.read()
cdo=cdl.split('\n')
f.close()
f = open('dict_word_phone.txt', 'w')
for co in cdo:
    x=co.split(' ')
    sofar=x[0]
    pme(1,x,sofar,le4,phone)





















