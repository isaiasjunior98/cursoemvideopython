medida = float(input('Digite a medida: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida {}m tem {}cm {}mm {}dm {}dam {}hm e {}km'.format(medida, cm, mm, dm, dam, hm, km))
