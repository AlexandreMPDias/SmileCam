import ctypes

def PopUp(header, text):
	"""
	@Created by Padawan Alexandre

	Generates a PopUp Window on Windows based Systems
	@param: header	- Is the title on the Window
	@param: text	- Is the text content displayed inside the Window
	"""
	ctypes.windll.user32.MessageBoxW(0, text, header, 0)
