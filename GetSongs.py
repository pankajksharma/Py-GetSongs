import os,re

###Get Latest movies/tracks###
os.system("clear")
link='http://www.songspk.pk/'
print '\nGetting latest Movies Please Wait...'
os.system('wget '+link+' -O temp -o /dev/null')
tempFile = open('temp','r')
tempMovies = tempFile.read()
tempFile.close()
tempMovies = tempMovies.split('Category</font>')[1].split('</TR></TBODY></TABLE></TD></TR></TBODY></TABLE>')[0]
tempLinks=re.findall(r'<a href=[^ ]*_mp3_song[s]*.html">[^<>]*</a>',tempMovies)
urls=[]
names=[]
for link in tempLinks:
	#print link
	urls.append(link.split('href="')[1].split('">')[0])
	names.append(link.split('">')[1].split('</a>')[0].replace('\n','').replace('\t',''))

for i in range(len(names)):
	print ' %2d. %s'%(i+1,names[i])
choice = int(raw_input('\nEnter Your Choice: '))-1

###Get Movie/Track Page###
print '\nPlease wait getting file...'
os.system('wget '+urls[choice]+' -O temp -o /dev/null')
tempFile = open('temp','r')
temp=tempFile.read()
tempFile.close()
links=re.findall(r'<a href=[^ ]*?songid=[0-9]*">[^0-9]*</a>',temp)
urls=[]
names=[]
for link in links:
	urls.append(link.split('href="')[1].split('">')[0])
	names.append(link.split('\t')[-1].split('</a>')[0])

for i in range(len(names)):
	print ' %2d. %s'%(i+1,names[i])

choice=raw_input('\nEnter Choice (* for All): ')

###Download Track(s)###
if choice=='*':
	for i in range(len(urls)):
		os.system('wget '+urls[i]+' -O '+'"'+names[i]+'.mp3"')
else:
	choice = int(choice)-1
	print 'wget '+urls[choice]+' -O '+names[choice]
	os.system('wget '+urls[choice]+' -O '+'"'+names[choice]+'.mp3"')

os.system('rm temp')
