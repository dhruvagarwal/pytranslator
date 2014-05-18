import goslate,sys
gs=goslate.Goslate()
s='\n'
while True:
	try:
		print gs.translate(s,'en')
		s=raw_input()
	except:
		sys.exit()