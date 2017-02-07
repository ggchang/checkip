#*-*coding:utf-8*-*

import urllib
import json
import argparse

def check_ip(ip):
	url="http://apis.juhe.cn/ip/ip2addr?ip="+ip+"&key=0e2c3133ce91bb8854b2a13fb4ebb07e"
	resp=urllib.urlopen(url)
	content=resp.read()
	res=json.loads(content)
	if res:
		error_code=res["error_code"]
		if error_code==0:
			#print "request secusses"
			print res["result"]["area"]+":"+res["result"]["location"]
		else:
			print "error_code:%s,reason:%s"%(res["error_code"],res["reason"])

if __name__=="__main__":
	using="""Using:python chaip.py --ip 8.8.8.8
		      --ip    +ip address
		      --list  +ip address list
	                                	 author:ggchang
						  data:2017/2/7	"""
	#print using
	parser=argparse.ArgumentParser()
	parser.add_argument("--ip",dest="p1")
	parser.add_argument("--list",dest="p2")
	args=parser.parse_args()
	ip=args.p1
	list=args.p2
	if ip:
		check_ip(ip)
	elif list:
		list=open(list,'r')
		for ip in list:
			check_ip(ip)
	else:
		print using
