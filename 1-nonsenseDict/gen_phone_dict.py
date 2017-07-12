#usage: nohup python3 gen_phone_dict.py
#it generates the word-to-phone dictionary normal_dict_word_phone.txt with normalized probabilities
#choose to ignore the non-english words first, there are not much of them, those oov is suggested to use g2p

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

f = open('normal_dict_prob.txt', 'r')
cdl=f.read()
cdo=cdl.split('\n')
f.close()
f = open('dict_word_phone.txt', 'w')
for co in cdo:
    x=co.split(' ')
    sofar=x[0]+' '+x[1]
    pme(2,x,sofar,le4,phone)
f.close()

#normalized probability for each phone pronunciation

f = open('dict_word_phone.txt', 'r')
cdl=f.read()
cpo=cdl.split('\n')
f.close()
f = open('normal_dict_word_phone.txt', 'w')
ba=cpo[0].split(' ')
rec=ba[0]
tot=1
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
