import goslate,sys
gs=goslate.Goslate()
if len(sys.argv)==1:
	s=raw_input('Enter the text to be translated: ')
else:
	s='\n'.join(sys.argv[1:])
print gs.translate(s,'en') #set your default language here
