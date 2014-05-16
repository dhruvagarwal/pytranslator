import goslate

gs=goslate.Goslate()
s=raw_input('Enter the korean text to be translated: ')
print gs.translate(s,'kr')

