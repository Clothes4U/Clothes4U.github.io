f=open('index.txt','w')
for i in range(46):
    i1=46-i
    if i1<10:i1='0'+str(i1)
    else:i1=str(i1)
    f.write('|[\['+i1+'\]](\heartbridge\HB_'+i1+'.pdf)|<img src="/heartbridge/HB_'+i1+'.jpg" width = "300px" />||||\n')
f.close()
