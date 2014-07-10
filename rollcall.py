from urllib import urlopen
import re
	

f = open('rollcall.csv','w')

print "What's the bill ID number (the number that appears after 'rollcall.asp?ID=' in the URL)?"
billID = raw_input()

print "What chamber (House or Senate)?"
chamber = raw_input()

print "What's the Roll Call serial number (the number that appears after '&serialnumber=' in the URL)?"
serial = raw_input()

print "Getting data from http://www.mainelegislature.org/LawMakerWeb/rollcall.asp?ID=" + billID + "&chamber=" + chamber + "&serialnumber=" + serial


url = 'http://www.mainelegislature.org/LawMakerWeb/rollcall.asp?ID=' + billID + '&chamber=' + chamber + '&serialnumber=' + serial

webpage = urlopen(url).read()

column = re.compile('<td class="rccell" valign="top" >(.*)</td>')

findColumn = re.findall(column,webpage)

length = len(findColumn)

listIterator = []
listIterator[:] = range(0,length)

counter = 0
row = 1

f.write('id,rep,town,party,vote,')
for i in listIterator:
	if (i % 3 == 0):
		repTown = re.split('\s+of\s', findColumn[i])
	 	town = repTown.pop()
	 	rep = repTown.pop()
		id = '{}'.format(row)
		f.write('\n' + id + ',' + rep + ',' + town + ',')
		row += 1
	else:
		f.write((findColumn[i]) + ',')

	

print 'Successfully saved vote data to rollcall.csv.'
