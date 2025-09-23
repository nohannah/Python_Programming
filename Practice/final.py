x ='hello'
y ='hey'

if x < y:
	if x.islower():
		x = x.upper()
		print('Hey, this program is started.')
elif y.isupper() or x.islower():
	x=x.capitalize()
	print(x)
	if x[0].isupper() and y[-1].islower:
		print('Morning')
	if x[:1] == y[:1]:
		print('Afternoon')
	else:
		print('Evening')
		x = 'hey'
else:
	y.capitalize()
	print('I have no idea what Im doing.')
	
if x == y:
	print('I know what Im doing.')
print ('This program is finished.')


