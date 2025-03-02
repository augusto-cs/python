#medida = float(input('Uma distancia em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))

#medida = float(input('Uma distancia em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

medida = float(input("Uma distância em metros: "))
km = medida / 1000      
hm = medida / 100       
dam = medida / 10      
dm = medida * 10       
cm = medida * 100       
mm = medida * 1000      

print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm  \n{}mm'.format(medida, km, hm, dam, dm, cm, mm))
