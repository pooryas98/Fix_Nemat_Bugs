bord= float(input('win percentage ro bede'))
zarib_w= float(input('up margin*100 ro bede'))
zarib_l= float(input('low margin*100 ro bede'))

a=100/((bord*zarib_w)+((100-bord)*zarib_l))
print(a*(bord*zarib_w))

