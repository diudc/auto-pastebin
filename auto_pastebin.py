import os
import requests
import getpass
import sys
import pyperclip

url ="https://pastebin.ubuntu.com/"

def read_file(filename):
	content=""
	with open(filename, 'rt') as filename:
		for lines in filename:
			content+=lines
	filename.close()
	return content

def construct_data(filename,user=getpass.getuser()):
	data= {
	'poster':user,
	'syntax':'text',
	'content': read_file(filename)
	}
	return data

def post_req(data,url):
	res=requests.post(url,data=data)
	return res

def main():
	#construct data
	if len(sys.argv) <2:
		print("please provie the data to upload.")
		exit()
	if len(sys.argv) ==3:
		data=construct_data(sys.argv[1],sys.argv[2])	
	else:
		data=construct_data(sys.argv[1])	
	resp=post_req(data,url)
	if resp.ok:

		print(resp.url)
		pyperclip.copy(resp.url)
	else:
		print(resp.status_code)

	
if __name__ =="__main__":
	main()
