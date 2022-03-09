#CODE WRITTEN BY FIVEX
from datetime import datetime
from time import sleep
import requests,sys,os
#os.system('cat /dev/location > /dev/null &')
black='\033[1;90m'
white='\033[1;97m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
whitex='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
fivex=white+'['+blue+'FIVEX'+white+']'
fivex_no_pro=whitex+'[FIVEX]'+end
hln=white+"["+blue+"HOÀNG LONG NGŨ"+white+"]"
s=0
block=0
ip=requests.get('https://api.ipify.org/').text
logo="               \033[7;37m\033[1;37m HOÀNG LONG NGŨ [FIVEX] \033[0m \n               \033[4;40;97m\033[1;97m 0  3  0  4  2  0  0  5 \033[0m \n               \033[4;40;96m\033[1;96m MB BANK  :  \033[1;97m8603042005 \033[0m \n               \033[4;40;97m\033[1;97m Z A L O  :  \033[1;96m0979762905 \033[0m \n               \033[4;40;97m\033[1;97m I  P   :  "+ip+" \033[0m \n               \033[7;37m\033[1;37m T O O L  :  TDS PYTHON \033[0m \n";
getkey=requests.get("https://fivextest.000webhostapp.com/fivexkey.php")
getkey1=requests.get("https://fivextest.000webhostapp.com/key5.php")
gettb=requests.get("https://fivextest.000webhostapp.com/thongbao.php")
tb=gettb.text
key=getkey.text
key1=getkey1.text
os.system('clear')
print(logo)
while(True):
	for i in range(3,0,-1):
		print(white+'BẠN CÒN',redz+' '+str(i)+' '+end+white,'LẦN NHẬP KEY, VUI LÒNG NHẬP CHÍNH XÁC!')
		nhapkey=input('NHẬP KEY: '+yellow)
		if (nhapkey==key or nhapkey==key1):break
	if (nhapkey==key or nhapkey==key1):break
	else:print(red+str(tb)),quit()
print('KEY ĐÚNG, ĐANG VÀO TOOL CỦA FIVEX')
for dvt in range(3,0,-1):
	print(blue+'[FIVEX]',white+'['+blue+str(dvt)+white+']',end='\r')
	sleep(0.7)
#FIVEX
os.system('clear')
print(logo)
tokentds=input(white+'NHẬP'+blue+' ACCESS_TOKEN TDS: '+white)
#tokentds='TDS9JSMxIXZ2V2ciojIyVmdlNnIsISNwgXZ2lmZiojIyV2c1Jye'
tokenfb=input(white+'NHẬP'+blue+' TOKEN FACEBOOK: '+white)
#tokenfb='EAAGNO4a7r2wBABQ4ZBph2O7IVnyDrBy1EdZATiwt9lF6aj1dFABfoScG4AXr0XNJJdRrYdFVGitvJVmRC1gFC6jY8uae28cVfLL8tDFuVYtZAaMEjeNV7ZAfuZBrVZCQEA4drfZAxs6gMQY8E73T6arNB6zx0Ugxg2BnNiGZAPoCM0sVaqEQT1CS'
#dlj=int(input(blue+'NHẬP '+white+'DELAY: '+blue))
stop=int(input(blue+'NHẬP '+white+'SỐ NHIỆM VỤ: '+blue))
delay_job=int(input(blue+'NHẬP '+white+'DELAY: '+blue))
#stop_block=int(input(blue+'NHẬP '+white+'SỐ LẦN VƯỢT '+red+'BLOCK'+white+': '+blue))
stop_block=3
os.system('clear')
print(logo)
fb=requests.get('https://graph.facebook.com/me/?access_token='+str(tokenfb))
if 'id' in fb.text and 'name' in fb.text:print(white+'['+blue+'ĐANG'+white+' CẤU HÌNH: '+blue+(fb.json()['name'].upper())+white+' ID: '+blue+str(fb.json()['id'])+white+']')
else:print(red+fb.json()["error"]["message"]),quit()
run=requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+str(tokentds))
if 'success' in run.text:print(fivex,run.json()['data']["msg"].upper())
else:print(red+run.json()['error'].upper()),quit()
s=0
while(True):
	time=datetime.now().strftime("%H:%M:%S")
	#GET_LIST_NHIEM_VU
	while(True):
		listlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+str(tokentds))
		if 'id' in listlike.text:break
	snv=len(listlike.json())
	s=s+snv
	tsnv=s
	#print("LIST LIKE:",listlike.json())
	print(fivex_no_pro,white+'TÌM THẤY',white+'['+blue+str(snv)+white+']'+end,white+'NHIỆM VỤ [',blue+time,white+']')
	for i in range(0,len(listlike.json()),1):
		id=listlike.json()[i]['id']
		dem_so_nv=tsnv-snv+i+1
		print(white+'['+blue+str(dem_so_nv)+white+']',"ĐANG LÀM NHIỆM VỤ ID:",black+id)
		urllike='https://graph.facebook.com/'+str(id)+'/likes'
		datalike='access_token='+str(tokenfb)
		like=requests.post(urllike, data=datalike)
		#print(like.json())
		if like.text=='true':print(hln,white+"LIKE SUCCESS, ĐANG NHẬN XU"+end)
		#if like.text!='true':print(like.text)
		if 'error' in like.text and '368' in like.text:block=block+1
		if block==stop_block:break
		if 'error' in like.text and '190' in like.text:break
#DELAY_NHAN_XU
		for delay_nhan in range(delay_job,0,-1):
			print(fivex,'['+blue+str(delay_nhan)+white+']','     ',end='\r')
			sleep(0.7)
		nhanxu=requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(id)+'&access_token='+str(tokentds))
		xu=nhanxu.json()
		if 'success' in xu:print(yellow+'[NHẬN XU SUCCESS]',white+'[',yellow+str(xu['data']['msg']),white+'] [',yellow+str(xu['data']['xu']),white+']')
		if 'error' in xu:print(red+str(xu['error']).upper())
		if (tsnv-snv+i+1)==stop:break
	if block==stop_block:break
	if (tsnv-snv+i+1)==stop:break
	if 'error'  in like.text and '190' in like.text:break
	for delay in range(3,0,-1):
		print(white+'[FIVEX]',black+'ĐANG GET LIST NHIỆM VỤ, ĐỢI:',delay,'   ' ,end="\r")
		sleep(0.7)
ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(tokentds)).json()
if (tsnv-snv+i+1)==stop:print(white+' CHẠY TOOL SUCCESS, TỔNG XU:',yellow+str(ttacc['data']['xu']))
if block==stop_block:print(red+like.json()['error']['message'])
if 'error'  in like.text and '190' in like.text:print(red+like.json()['error']['message'])
print(white+'THANKS BẠN ĐÃ SỬ DỤNG TOOL CỦA',fivex+' !')
