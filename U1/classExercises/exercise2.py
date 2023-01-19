h= 0
m= 1
d= 2939  

fm= (m+d)%60
fh= ((m+d)//60)+h

if fh>24:
    fh= fh%24
if fm<10:
    fm= fm + '0'
    
print(fh, ':', fm)