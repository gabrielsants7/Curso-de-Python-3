dm = int(input('Uma distância em metros:'))
print('A medida de {}m corresponde a:'.format(dm))
km  = dm /1000
hm = dm  /100
dam = dm /10
dm = dm * 10
cm = dm * 100
mm = dm * 10000
print('{}km'.format(km))
print('{}hm'.format(hm))
print ('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))


