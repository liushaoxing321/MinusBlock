#!/usr/bin/env python
from os import listdir
import string
import random
import os
import sys
xmString=""
outPath="./Hooks/"
if(len(sys.argv)<4):
	print "generate.py ModuleType ModuleName ObjcClassName"
	sys.exit(-1)
if(sys.argv[1]!="SDK" and sys.argv[1]!="API" and sys.argv[1]!="AdWall"):
	print "Wrong Argument"
else:
	if(sys.argv[1]=="SDK"):
		outPath=outPath+"SDKSpecific/"+sys.argv[2]+".xm"
	elif(sys.argv[1]=="API"):
		outPath=outPath+"APIHooks/"+sys.argv[2]+".xm"
	elif(sys.argv[1]=="AdWall"):
		outPath=outPath+"AdWall/"+sys.argv[2]+".xm"
	else:
		print "Unknown Module Type"
		sys.exit(-1)
	xmString+="#import \"../SharedDefine.pch\"\n"
	xmString=xmString+"%group"+" "+sys.argv[2]+"\n"
	xmString+="//Insert Your Hook Here\n"
	xmString+="%end\n"
	xmString+="extern void init_"+sys.argv[2]+"_hook(){\n"
	xmString+="if objc_getClass(\""+sys.argv[3]+"\")!=NULL{"
	xmString+="%init("+sys.argv[2]+");\n"
	xmString+="}\n"
	xmString+="}\n"
	if(os.path.isfile(outPath)==False):
		os.system("touch "+outPath)
		fileHandle=open(outPath,"w")
		fileHandle.write(xmString)
		fileHandle.close() 
		print "Generated At"+outPath
	else:
		print "File Already Exists At "+outPath+"!\nFor Safety Reasons,Generating Was Cancelled\nPlease Manually Remove That File"







