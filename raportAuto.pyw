#! python3

import pyautogui
import time
import pyperclip
import re
import os
import datetime


class Koltelefon:

	def __init__(self):
		self.polozenie = self.inicjowanieMenu()	
		if self.polozenie == (0,0,0,0) or self.polozenie == None:
			self.szukajMenu()
			time.sleep(1)
			self.polozenie = self.inicjowanieMenu()
			
		self.przerwa = 0	
		self.BtnPodsumowanie = self.findInside('podsumowanie.png')
		self.BtnLogowanie = self.findInside('logowanie.png')
		self.BtnPrzerwa = self.findInside('przerwa.png')
		if self.BtnPrzerwa != None:
			self.przerwa = 1

	def inicjowanieMenu(self):
		if  pyautogui.locateOnScreen('pasek.png', grayscale=True) != None:
			x = pyautogui.locateOnScreen('pasek.png', grayscale=True)
			x = list(x)
			x[3] = x[3]+75
			x = tuple(x)
		else:
			x = (0,0,0,0)
			
		return x
		
	def findInside(self, png):
		try:
			if pyautogui.locateCenterOnScreen(png, region=self.polozenie, grayscale=True) != None:
				return pyautogui.locateCenterOnScreen(png, region=self.polozenie, grayscale=True)
				
		except TypeError:
			print('nie znaleziono koltelefonu')
			exit()
	
	def podsumowanie(self):
		print('podsumowanie')
		pyautogui.click(self.BtnPodsumowanie)
		time.sleep(1)
		pyautogui.press('tab')
		pyautogui.press('enter')
		time.sleep(0.3)
		pyautogui.press('right')
		time.sleep(0.3)
		pyautogui.typewrite('.txt')
		pyautogui.hotkey('ctrl', 'a')
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.2)
		pyautogui.press('enter')
		time.sleep(0.2)
		pyautogui.press('left')
		time.sleep(0.2)
		pyautogui.press('enter')
		time.sleep(0.2)
		pyautogui.press('tab')
		time.sleep(0.2)
		pyautogui.press('enter')
		
	def wyloguj(self):
		if self.przerwa == 1 and pyautogui.locateCenterOnScreen('jeden.png', region=(self.polozenie)) == None:
			pyautogui.click(self.BtnPrzerwa)
		
		print('wylogowywanie')
		pyautogui.click(self.BtnLogowanie)
		time.sleep(0.5)
		pyautogui.click(self.BtnLogowanie[0], self.BtnLogowanie[1]+45)
		
		
	def przygotujMail(self):
		print('otwiranie skrzynki')
		os.startfile("C:/Program Files (x86)/Mozilla Thunderbird/thunderbird.exe")
		time.sleep(2)
		self.szukajSzkicy()
		time.sleep(1)
		pyautogui.doubleClick(340,170)
		time.sleep(1)
		pyautogui.press('pagedown')
		time.sleep(1)
		try:
			print('szukanie podsumowania')
			time.sleep(1)
			x, y = pyautogui.locateCenterOnScreen('podsumowaniemail.png', region=(0,245,400,600), grayscale=True)
			pyautogui.click(x, y)
		except TypeError:
			print('nie znaleziono podsumowaniemail.png')
			exit()
			
		print('klik w miejscu pod podsumowaniem')
		pyautogui.click(x, y+20, button='left')
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'v')
		time.sleep(1)
		pyautogui.hotkey('ctrl', 'enter')
		print('wysylka raportu')
	
	def szukajMenu(self):
		print('nie znaleziono menu, szukam w zminimalizowanych')
		try:
			if pyautogui.locateCenterOnScreen('kolmini.png', region=(108, 870, 968, 30), grayscale=True ) != None:
				x, y = pyautogui.locateCenterOnScreen('kolmini.png', region=(108, 870, 968, 30), grayscale=True)
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('kolukryty.png', region=(1076, 870, 240, 30), grayscale=True) != None:
				x, y = pyautogui.locateCenterOnScreen('kolukryty.png', region=(1076, 870, 240, 30), grayscale=True)
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('kolukrytyprzerwa.png', region=(1076, 870, 240, 30), grayscale=True) != None:
				x, y = pyautogui.locateCenterOnScreen('kolukrytyprzerwa.png', region=(1076, 870, 240, 30), grayscale=True)
				pyautogui.click(x, y)
	
		except TypeError:
			print('nie znaleziono schowanej ikonki')
			exit()
	
	def zapisRaportu(self):
		print('zapis raportu')
		os.startfile("C:/Users/helpdesk/Desktop/RAPORT/"+pyperclip.paste())
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'a')
		time.sleep(0.2)
		pyautogui.hotkey('ctrl', 'c')
		
		
	def zakonczenieDnia(self):
		self.podsumowanie()
		self.wyloguj()
		self.zapisRaportu()
		self.przygotujMail()
	
	def szukajSzkicy(self):
		try:
			print('szukam szkicy')
			if pyautogui.locateCenterOnScreen('szkice1.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkice1.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('szkice2.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkice2.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('szkice3.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkice3.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('szkiceb1.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkiceb1.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('szkiceb2.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkiceb2.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			elif pyautogui.locateCenterOnScreen('szkiceb3.png', region=(0, 0, 260, 845)) != None:
				x, y = pyautogui.locateCenterOnScreen('szkiceb3.png', region=(0, 0, 260, 845))
				pyautogui.click(x, y)
			else:
				pyautogui.click(0,840)
				pyautogui.hotkey('shift', 'g')
				pyautogui.typewrite('Szkice')
				time.sleep(3)
				pyautogui.press('enter')
		except TypeError:
			print('nie znaleziono szkicy')
			
	

print('Podaj godzine startu.. ')
hh = int(input())
print('Podaj minute startu.. ')	
mm = int(input())
print('Podaj sekunde startu.. ')
ss = int(input())
	
now = datetime.datetime.now()
start_time = datetime.datetime(now.year, now.month, now.day, hh, mm, ss)

while(True):
	now = datetime.datetime.now()
	pozostalo = start_time - now
	if now  > start_time: 
		test = Koltelefon()
		test.zakonczenieDnia()
		exit()
	else:
		time.sleep(1)
		#print(datetime.datetime.now())	
		print('pozostalo: ', pozostalo)
		
		

