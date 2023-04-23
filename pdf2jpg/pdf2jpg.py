#-*- coding:utf-8 -*-

from pdf2image import convert_from_path

file_name = "filename.pdf"

pages = convert_from_path("./source/" + file_name)

for i, page in enumerate(pages):
	page.save("./output/"+file_name+str(i)+".jpg", "JPEG")