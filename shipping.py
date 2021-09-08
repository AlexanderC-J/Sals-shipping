weight = 2
# Ground shipping
if weight <= 2:
  cost = str(weight*1.50 + 20)
  print('Cost of Ground shipping: $' + cost)
elif weight <= 6:
  cost = str(weight*3 + 20)
  print('Cost of Ground shipping: $' + cost)
elif weight <= 10:
  cost = str(weight*4 + 20)
  print('Cost of Ground shipping: $' + cost)
else:
  cost = str(weight*4.75 + 20)
  print('Cost of Ground shipping: $' + cost)

# Ground shipping premium
GSpcost = str(125)
print('Cost of Ground shipping premium: $' + GSpcost)

# Drone shipping
if weight <= 2:
  Dcost = str(weight*4.50)
  print('Cost of Drone shipping: $' + Dcost)
elif weight <= 6:
  Dcost = str(weight*9)
  print('Cost of Drone shipping: $' + Dcost)
elif weight <= 10:
  Dcost = str(weight*12)
  print('Cost of Drone shipping: $' + Dcost)
else:
  Dcost = str(weight*14.25)
  print('Cost of Drone shipping: $' + Dcost)

cost = float(cost)
GSpcost = float(GSpcost)
Dcost = float(Dcost)

if cost <= GSpcost:
  ncost = cost
else:
  ncost = GSpcost

if ncost <= Dcost:
  fcost = ncost
  print('Best price: $' + str(fcost))
else:
  fcost = Dcost
  print('Best price: $' + str(fcost))

if cost <= GSpcost <= Dcost:
  print('Ground shipping is the cheapest option!')
elif cost <= Dcost <= GSpcost:
  print('Ground shipping is the cheapest option!')
elif Dcost <= cost <= GSpcost:
  print('Drone shipping is the cheapest option!')
elif Dcost <= GSpcost <= cost:
  print('Drone shipping is the cheapest option!')
elif GSpcost <= cost <= Dcost:
  print('Ground shipping premium is the cheapest option!')
elif GSpcost <= Dcost <= cost:
  print('Ground shipping premium is the cheapest option!')

