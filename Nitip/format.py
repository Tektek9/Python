#!/usr/bin/env python3
# -*- coding: utf-8 -*
from re import search, MULTILINE


def __(content, export):
	try:
		r   = search(r"URL\s*[:=]\s*(?P<_url_>(.*))\s*[:,]\s*USER\s*[:=]\s*(?P<_user_>(.*)),\s*PASS\s*[:=]\s*(?P<_pass_>(.*))", str(content), MULTILINE).group("_url_", "_user_","_pass_")
		if len(r)==3:
			if login.lower()=="y": url = f"{r[0].strip()}wp-login.php"
			else: url = r[0].strip()
			for _ in (("url", url), ("user", r[1].strip()), ("pass", r[2].strip())): export = export.replace(*_)
			print(f"[ NEW FORMAT ]>> {export}")
			open("_new_format_.txt",'a').write(f'{export}\n')
		else: print(f"[ ERROR FORMAT ]>> {content}")
	except Exception as e: print(f"[ ERROR ]>> {str(e)}")

if __name__ == '__main__':
	print("""

	 __ _  ____  __ _    ____  __  ____  _  _   __  ____  
	(  / )(_  _)(  ( $  (  __)/  $(  _ $( $/ ) / _$(_  _) 
	 )  (   )(  /    /   ) _)(  O ))   // $/ $/    $ )(   
	(__$_) (__) $_)__)  (__)  $__/(__$_)$_)(_/$_/$_/(__)  
	   ____  _  _  ____  ____   __    ___  ____  __  ____ 
	  (  __)( $/ )(_  _)(  _ $ / _$  / __)(_  _)/  $(  _ $
	   ) _)  )  (   )(   )   //    $( (__   )( (  O ))   /
	  (____)(_/$_) (__) (__$_)$_/$_/ $___) (__) $__/(__$_)

			""")
	try:
		urls = input("Please enter ktn urls file >> ")
		print("Please enter the format that you like to export (EXEMPLE : url#user@pass or url|user|pass).")
		format_ = input(">> ")
		print("you want to add wp-login.php at the end of the url ?")
		login = input("Y for yes / N for no>> ")
		for url in open(urls, 'r').read().splitlines(): __(url, format_)
	except Exception as e: print(f"[ ERROR ]>> {str(e)}")