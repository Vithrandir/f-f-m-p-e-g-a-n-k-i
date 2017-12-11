#coding:utf-8
import string
import re
import os
import os.path
import stat
import codecs
import sys
import traceback

# def is_ascii_blank(c):
# 		#ascii前32位都是控制字符,空格 32 换行 10 制表 9 回车 13
# 		if ord(c) < 33 and c != " " and c != "\t" and c != "\n":
# 			return 1
# 		else:
# 			return 0


def caculate_duration(start_time,end_time):


	start_time_split = start_time.split(":")
	end_time_split = end_time.split(":")

	# print(str(start_time_split[2]))
	# print(int(start_time_split[2]))
	# print(end_time_split)


	total1 = float(start_time_split[2])*1000+float(start_time_split[1])*60*1000+float(start_time_split[0])*60*60*1000
	total2 = float(end_time_split[2])*1000+float(end_time_split[1])*60*1000+float(end_time_split[0])*60*60*1000

	duration = (total2 - total1)/1000

	return duration


def tidyDoc():
	#需要遍历的原始ass文件夹
	root_dir = "assRawfiles"
	#处理完成后文件存放的文件夹
	done_dir = "step1Done"
	#用于判定对白的时间字符串，即时间的开头两位，如视频时长超过大于等于1小时，修改该参数
	is_dialogue = "00:"

	#stringNeedReaplace = ""
	# linecout = 0

	#遍历文件夹
	for parent,dirnames,filenames in os.walk(root_dir):
		for filename in filenames:
			#处理Mac中的隐藏文件，或者以下代码更好
			#if filename.startswith("."):
			if filename.startswith("."):
				# print("is b best")
				continue


			#暂存处理结果的中间文件
			temp_file = open(done_dir + "/" + "temp_file","w")
			#当前打开的原始字幕文件

			#python 能不能直接更改文件assFilebeingProcess的编码为utf-8？
			#如果可以，在此处添加代码

			assfile_being_process = open(root_dir + "/" + filename,"r")


			for sourceline in assfile_being_process.readlines():

				#替换字幕文件中的无关内容，将字幕对白写入文件
				print(sourceline)
				newline2 = re.sub("\{.[^{}]*\}","",sourceline)
				print(newline2)
				newline3 = re.sub("\\\N","\t",newline2)
				print(newline3)
				# newline4 = re.sub(",\*?Default.*,0,0,0,,","\t",newline3)
				# newline4 = re.sub(",\*?Default.*,0000,0000,0000,,","\t",newline3)
				if "0,0,0," in newline3:
						
					newline4 = re.sub(",\*?Default.*,0,0,0,,","\t",newline3)
				
				else:

					newline4 = re.sub(",\*?Default.*,0000,0000,0000,,","\t",newline3)

				
				print(newline4)
				newline5 = re.sub("Dialogue: 0,","0",newline4)
				print(newline5)
				newline6 = re.sub(",0","\t00",newline5)
				print(newline6)

				#如果该行不包含英语

				if len(newline6.split("\t")) != 4:

					continue

				if newline6.startswith(is_dialogue):
					temp_file.write(newline6)

			assfile_being_process.close()
			temp_file.close()

			#按源文件名称将处理好的内容存到文件
			os.rename(done_dir + "/" + "temp_file",done_dir + "/" + filename)
				
				# sourceline2 = sourceline.decode("utf_16_le").encode("utf-8")
				# print(sourceline)
				# be le
				# for c in sourceline:
					# if is_ascii_blank(c) == 1:
					# 	# print("get") 
					# 	continue
					# else:
					# 	# temp_file.write(c.decode("utf-8","ignore").encode("utf-8"))
					# 	print(c)

				# linecout += 1
				# print(filename)
				# sourceline = sourceline.decode("gb2312","ignore").encode("utf-8")
				






				# newline6 = re.sub(",0","\t00",newline5)
				# newline7 = re.sub("Dialogue:0\t","",newline6)
				# newline8 = re.sub("\\\N{\\\\方正综艺_GBK}{\\\\fs\d\d}{\\\\b\d}{\\\c&HFFFFFF&}{\\\\3c&H2F2F2F&}{\\\\4c&H000000&}","\t",newline7)
				# temp_file.write(newline8)
				# print(newline8)
				# rightline = sourceline.split("\t")
				# print(rightline)
				# temp_file.write(sourceline)





# 			file3 = open(done_dir + "/" + "file3","a")
# 			temp_file = open(done_dir + "/" + "temp_file")
# # 			count = 0

# 			for sourceline in temp_file.readlines():

# 				if len(sourceline.split("\t")) > 2:
# 					if "this" in sourceline:
# 						print("sourceline")


# 				# if "Dialogue:" in sourceline:
# 				# 	count = 1
# 				# if count == 1:
# 				file3.write(sourceline)
# # 				# else:
# # 					# continue

# 			temp_file.close()
# 			file3.close()	

tidyDoc()

def caculate():
	root_dir = "step1Done"
	done_dir = "step2Done"
	for parents,dirname,filenames in os.walk(root_dir):
		for filename in filenames:
			if filename.startswith("."):
				continue
			# print("into another file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			#打开文件为对象
			assfile = open(root_dir + "/" + filename)
			#用来接收内容的文件
			another_ass = open(done_dir + "/" + "another_ass","w")
			#对于打开文件的每一行
			for line in assfile.readlines():
				#如果是空行则转到下一行
				if line == "\r\n" :
					continue
				temp_line = line
				#用制表符分隔字符串
				line_split = line.split("\t")

				# start_time = line_split[0]
				# # print(filename)
				# end_time = line_split[1]


				# start_time_split = start_time.split(":")
				# end_time_split = end_time.split(":")

				# # print(str(start_time_split[2]))
				# # print(int(start_time_split[2]))
				# # print(end_time_split)


				# total1 = float(start_time_split[2])*1000+float(start_time_split[1])*60*1000+float(start_time_split[0])*60*60*1000
				# total2 = float(end_time_split[2])*1000+float(end_time_split[1])*60*1000+float(end_time_split[0])*60*60*1000

				# duration = (total2 - total1)/1000

				duration = caculate_duration(line_split[0],line_split[1])

				newline = re.sub('(?<=^\d\d:\d\d:\d\d\.\d\d\t).[^\t]*(?=\t)',str(duration),temp_line)

				another_ass.write(newline)





			assfile.close()
			another_ass.close()
			os.rename(done_dir + "/" + "another_ass",done_dir + "/" + filename)


caculate()
# 	# 打开计算好的文档



# #这里应该有一个循环，一个单词遍历所有文档，遍历到一个就记录不再遍历
# # @patch

def get_video_type(filename_without_extend):
	root_dir = "processVideo"
	file_dic = {}
	for parents,dirname,filenames in os.walk(root_dir):
		for filename in filenames:
			filename_split = filename.split(".")
			file_dic[filename_split[0]] = filename_split[1]
	
	return file_dic[filename_without_extend]


# def fix_sentense(line,file_line_list):

	# line = line.split("\t")

	# if line[3].endswith(".") == 1 or line[3].strip().endswith("!") == 0 or line[3].strip().endswith("?") == 0 or line[3].strip().endswith(",") == 0:

		# return line
	# else:

		# return fix_sentense()

	# half = line_list[line_list.index(line) - 1].strip().split("\t")





def PickAWord():

	# print("IN")
	need_download = [""]
	word_found_list = [""]
	file_count = 0
	root_dir = "step2Done"
	words_file = open("words","r")
	get = open("get","w")
	file_num = sum([len(x) for _,_,x in os.walk("step2Done")])
	append_to_anki = open("anki","a")

	# assfile = open(done_dir + "/" + filename,"r")
	#打开单词列表

	# #打开接收匹配的文档
	# get = open("24get","a")
	# #打开未找到的单词文档
	notfound = open("wordnotfound","w")
	# #对于单词文档的每一行
	# item = open("item","a")

	#写入脚本文件运行所需语句
	get.write("#!/bin/bash" + "\n" + "cd Downloads/seven/processVideo" + "\n")

	# for item in words_file.readlines():
		# print(item.strip())

	for word in words_file.readlines():
		# print("IN")
		for parents,dirname,filenames in os.walk(root_dir):
			file_count += 1
			for filename in filenames:
				if filename.startswith("."):
					continue
				assfile_being_process = open(root_dir + "/" + filename,"r")
				# print("assfile_being_process open")

				line_list = assfile_being_process.readlines()

				assfile_being_process.close()

				assfile_being_process = open(root_dir + "/" + filename,"r")








				for line in assfile_being_process.readlines():
					# print(line)

					# print(line)
					if line == "\r\n":
						continue
					if str(" " + word.strip() + " ") in line:#这里需要添加判定，前后都要带空格,因为不带空格可能前后都会
						# print("word in line")
						if str(word.strip()) in word_found_list:
							continue
						# print("find")
						#写入接收匹配的文档
						start_time = line.strip().split("\t")[0]
						end_time = line.strip().split("\t")[1]

						split_line = line.strip().split("\t")
						# chinese = line.strip().split("\t")[2]
						# print(chinese)
						# english = line.strip().split("\t")[3]
						# print(english)
						# item.write(word.strip() + "\t" + chinese + "\t" + english + "\n")
						# get.write(word.strip() + "\t" + line.strip() + "\n")
						# get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + start_time + " -t " + end_time  + " output/" + word.strip() +".mp4" + "\n")
						#ffmpeg -y -i 01.mp4 -vcodec mpeg4 -copyinkf  -ss 00:18:46.41 -t 3.14 output/guy.mp4
						# ffmpeg -y -i 01.mp4 -codec copy -copyinkf -ss 00:02:48.98 -t 2.79 output/upset.mp4
						#ffmpeg -y -i 01.mp4 -c copy -copyinkf -vcodec copy -acodec copy -ss 00:02:48.98 -t 2.79 output/upset.mkv

						#加一个split只有三段的判定，先不加

						# print(line)

						
						
						if split_line[3].strip()[0].isupper() == 0:

							#如果开头是小写，就要匹配上一行

							##这里变成匹配下一行了x
							#没有匹配，执行了if的语句
							# print("into elif")
							# print(line[3])
							# print(line[3][0])


							# 将这些变量都改成参数
							

							half = line_list[line_list.index(line) - 1].strip().split("\t")


							if half[3].strip()[0].isupper() == 0:

								half2 = line_list[line_list.index(line) - 2].strip().split("\t")

								append_to_anki.write(word.strip() + "\t" + half2[2] + " " + half[2] + " " + line.strip().split("\t")[2] + "\t" + half2[3] + " " + half[3] + " " + line.strip().split("\t")[3] + "\n")
								get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + half2[0] + " -t " + str((caculate_duration(half2[0],start_time)+float(end_time)))  + " output/" + word.strip() +".mp4" + "\n")

							else:
								
								append_to_anki.write(word.strip() + "\t" + half[2] + " " +line.strip().split("\t")[2] + "\t" + half[3] + " " + line.strip().split("\t")[3] +  "\n")

								get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + half[0] + " -t " + str((caculate_duration(half[0],start_time)+float(end_time)))  + " output/" + word.strip() +".mp4" + "\n")


						elif split_line[3].strip().endswith(".") == 0 and split_line[3].strip().endswith("!") == 0 and split_line[3].strip().endswith("?") == 0:

							# print("The last string is : ")
							# print(line[3][-1])


							#half为下一行
							# print(line[3])

							half = line_list[line_list.index(line) + 1].strip().split("\t")


							if half[3].endswith(".") == 0 and half[3].strip().endswith("!") == 0 and half[3].strip().endswith("?") == 0 :

								try:
									half2 = line_list[line_list.index(line) + 2].strip().split("\t")
								except:
									continue

								append_to_anki.write(word.strip() + "\t"  + line.strip().split("\t")[2] + " " + half[2] + " " + half2[2] + "\t" +line.strip().split("\t")[3] + " " + half[3] + " " + half2[3] + "\n")
								get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + start_time + " -t " + str((caculate_duration(start_time,half2[0]) + float(half2[1])))  + " output/" + word.strip() +".mp4" + "\n")

							#append_to_anki.write(word.strip() + "\t" + line.strip().split("\t")[2] + " " + half[2] + "\t" +line.strip().split("\t")[3] + " " + half[3] + "\n")
							#get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + start_time + " -t " + str((caculate_duration(start_time,half[0]) + float(half[1])))  + " output/" + word.strip() +".mp4" + "\n")

								# 从第一句开始，到最后一句结束

								# 句子相加，

							# print(line.strip().split("\t")[3])

							else:

								append_to_anki.write(word.strip() + "\t" + line.strip().split("\t")[2] + " " + half[2] + "\t" +line.strip().split("\t")[3] + " " + half[3] + "\n")
								get.write("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + start_time + " -t " + str((caculate_duration(start_time,half[0]) + float(half[1])))  + " output/" + word.strip() +".mp4" + "\n")
								# traceback.print_exc()


							
							#start_time = start_time + line.strip().split("\t")[0]
							#end_time = line.strip().split("\t")[1]
							## !记得连时间间隔也要写进去，所以整个判定上移
							## 写一个计算时间间隔的函数



						else:

							append_to_anki.write(word.strip() + "\t" + line.strip().split("\t")[2] + "\t" +line.strip().split("\t")[3] + "\n")
							get.write(("ffmpeg -y -i " + filename.replace(".ass","") + "." + get_video_type(filename.replace(".ass","")) + " -vcodec mpeg4 -copyinkf  " + "-ss " + start_time + " -t " + end_time  + " output/" + word.strip() +".mp4" + "\n"))

						word_found_list.append(str(word).strip())

						if filename.replace(".ass","") not in need_download:
							need_download.append(filename.replace(".ass",""))
						# print("get!!!")


						#这里加入split filename 以添加上级文件路径


						#转入下一行
						#这里用goto跳转到wordbreak

						assfile_being_process.close()
						# print("break")
						break
					else:
						if file_count == file_num :
							notfound.write(word)
							file_count = 0
						assfile_being_process.close()
				# break
	word_have_found = open("wordhavefound","w")
	for word in word_found_list:
		word_have_found.write(word.strip() + "\n")
	word_have_found.close()

	print("you should download : \n")
	need_download_sorted = sorted(need_download)
	print(need_download_sorted)


	get.close()
	append_to_anki.close()
	os.rename("get","get"+".command")
#有空就写一个接收地址参数的函数
#notfoundword 应该在所有文件中都没有找到才运行
PickAWord()

def aNewWordList():
	old_word_list = open("words")
	recently_word_list = open("wordhavefound","r")
	new = open("newwords","a")
	# print(old_word_list)
	list1 = [""]
	list2 = [""]

	for item in recently_word_list:
		list1.append(item.strip())
	# print(list1)
	for item in old_word_list:
		list2.append(item.strip())

	# print(list2)

	for item in list2:
		if item in list1:
			continue
		else:
			new.write(item + "\n")




	# for word in old_word_list:
	# 	if word.strip() in recently_word_list:
	# 		print("True")
	# 	else:
	# 		new.write(word)

	new.close()
	old_word_list.close()
	os.remove("words")
	os.rename("newwords","words")
	recently_word_list.close()

aNewWordList()

#看有没有0 K的文件

# os.system("chmod 777 get.command")
# os.system("open get.command")


#python 如何chmod
#chmod后os.sys("get.command")

































# os.chmod("get.command",stat.S_IRWXU)
# os.system("open get.command")





		# print(word.strip())
	# 	assfile.close()
	# 	assfile = open("another_ass","r")
	# 	count = 0
	# # 	#检索计算好的文档的每一行
	# 	for line in assfile.readlines():
	# 		# print(line)
	# # 	# 	#如果单词在行中,语法不对
	# 		if word.strip() in line.strip():
	# 			# print("find")
	# 			#写入接收匹配的文档
	# 			start_time = line.strip().split("\t")[0]
	# 			end_time = line.strip().split("\t")[1]
	# 			chinese = line.strip().split("\t")[2]
	# 			print(chinese)
	# 			english = line.strip().split("\t")[3]
	# 			print(english)
	# 			item.write(word.strip() + "\t" + chinese + "\t" + english + "\n")
	# 			# get.write(word.strip() + "\t" + line.strip() + "\n")
	# 			get.write("ffmpeg -ss " + start_time + " -i 1.mkv -t " + end_time + " -c copy output/" + str(word.strip()) +".mp4" + "\n")
	# 			#转入下一行
	# 			break
	# # 		#否则
	# 		else:
	# 			continue
	# 			#计数器加一
	# 			count += 1
	# 			if count == len(assfilelines):
	# 				notfound.write(word)
	# 			#当计数器和行相等
	# assfile.close()
	# words_file.close()
	# get.close()
	# item.close()
	# notfound.close()

	# os.remove("words")
	# os.rename("wordnotfound","words")
	# os.rename("another_ass",filename)
