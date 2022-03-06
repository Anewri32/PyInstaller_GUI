from tkinter import Tk, Frame, StringVar, Label, Entry

root2 = Tk()
root2.iconbitmap('lib/icon.ico')
root2.title("PyInstaller GUI v1.1 / Archivo de version")
root2.resizable(0, 0)
frame2 = Frame(root2).grid(row=0, column=0)

CompanyName = StringVar()
FileDescription = StringVar()
FileVersion = StringVar()
InternalName = StringVar()
LegalCopyright = StringVar()
OriginalFilename = StringVar()
ProductName = StringVar()
ProductVersion = StringVar()

def VS(op):
	if op:
		label1.grid(row=0, column=0, pady=2.5)
		entry1.grid(row=0, column=1, pady=2.5, columnspan=5)
		label2.grid(row=1, column=0, pady=2.5)
		entry2.grid(row=1, column=1, pady=2.5, columnspan=5)
		label3.grid(row=2, column=0, pady=2.5)
		entry3.grid(row=2, column=1, pady=2.5, columnspan=5)
		label4.grid(row=3, column=0, pady=2.5)
		entry4.grid(row=3, column=1, pady=2.5, columnspan=5)
		label5.grid(row=4, column=0, pady=2.5)
		entry5.grid(row=4, column=1, pady=2.5, columnspan=5)
		label6.grid(row=5, column=0, pady=2.5)
		entry6.grid(row=5, column=1, pady=2.5, columnspan=5)
		label7.grid(row=6, column=0, pady=2.5)
		entry7.grid(row=6, column=1, pady=2.5, columnspan=5)
		label8.grid(row=7, column=0, pady=2.5)
		entry8.grid(row=7, column=1, pady=2.5, columnspan=5)
	else:
		"""label1.grid_remove()
		entry1.grid_remove()
		label2.grid_remove()
		entry2.grid_remove()
		label3.grid_remove()
		entry3.grid_remove()
		label4.grid_remove()
		entry4.grid_remove()
		label5.grid_remove()
		entry5.grid_remove()
		label6.grid_remove()
		entry6.grid_remove()
		label7.grid_remove()
		entry7.grid_remove()
		label8.grid_remove()
		entry8.grid_remove()"""
		root2.destroy()




def archivo_version():
	CompanyName = CompanyName.get()
	FileDescription = FileDescription.get()
	FileVersion = FileVersion.get()
	InternalName = InternalName.get()
	LegalCopyright = LegalCopyright.get()
	OriginalFilename = OriginalFilename.get()
	ProductName = ProductName.get()
	ProductVersion = ProductVersion.get()


	file_version = """VSVersionInfo(
	  ffi=FixedFileInfo(
	    filevers=(6, 1, 7601, 17514),
	    prodvers=(6, 1, 7601, 17514),
	    mask=0x3f,
	    flags=0x0,
	    OS=0x40004,
	    fileType=0x1,
	    subtype=0x0,
	    date=(0, 0)
	    ),
	  kids=[
	    StringFileInfo(
	      [
	      StringTable(
	        u'040904B0',
	        [StringStruct(u'CompanyName', u'"""+CompanyName+"""'),
	        StringStruct(u'FileDescription', u'"""+FileDescription+"""'),
	        StringStruct(u'FileVersion', u'"""+FileVersion+""" (win7sp1_rtm.101119-1850)'), 
	        StringStruct(u'InternalName', u'"""+InternalName+"""'),
	        StringStruct(u'LegalCopyright', u'\xa9"""+LegalCopyright+"""'),
	        StringStruct(u'OriginalFilename', u'"""+OriginalFilename+"""'),
	        StringStruct(u'ProductName', u'"""+ProductName+"""\xae'),
	        StringStruct(u'ProductVersion', u'"""+ProductVersion+"""')])
	      ]), 
	    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
	  ]
	)"""

	archivo = open(file_version_name, "w")
	archivo.write(file_version)
	archivo.close()
	    

#Interfasz de las opciones avanzadas

label1 = Label(frame2, text="CompanyName:")

entry1 = Entry(frame2, width=66, textvariable=CompanyName)


label2 = Label(frame2, text="FileDescription:")

entry2 = Entry(frame2, width=66, textvariable=FileDescription)


label3 = Label(frame2, text="FileVersion:")

entry3 = Entry(frame2, width=66, textvariable=FileVersion)


label4 = Label(frame2, text="InternalName:")

entry4 = Entry(frame2, width=66, textvariable=InternalName)


label5 = Label(frame2, text="LegalCopyright:")

entry5 = Entry(frame2, width=66, textvariable=LegalCopyright)



label6 = Label(frame2, text="OriginalFilename:")

entry6 = Entry(frame2, width=66, textvariable=OriginalFilename)


label7 = Label(frame2, text="ProductName:")

entry7 = Entry(frame2, width=66, textvariable=ProductName)


label8 = Label(frame2, text="ProductVersion:")

entry8 = Entry(frame2, width=66, textvariable=ProductVersion)



root2.mainloop()