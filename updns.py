#!/usr/bin/python
import hashlib
import os,sys
 
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
         


def update_rpz():
	os.system('rm -rf root.z.new')
	os.system('wget -O rpz.zone.new "https://raw.githubusercontent.com/WyattShao/DNS/master-rpz/root.z"')

	old = CalcMD5("/root/dnspod-sr/root.z")
	new = CalcMD5("root.z.new")

	if old == new:
		print('nothing can update')

	else:
		os.system('')	
		os.system('mv /root/dnspod-sr/root.z /root/dnspod-sr/root.z.bak')
		os.system('mv root.z.new /root/dnspod-sr/root.z')
		os.system('sudo rndc reload')	
		print('update have done,thanks!')


def check_exist(path):
	if os.path.exists(path):
		print 'Find old rpz.zone'
	else:
		os.system('touch /root/dnspod-sr/root.z')


if __name__ == '__main__':

	check_exist('/root/dnspod-sr/root.z')
	update_rpz()
