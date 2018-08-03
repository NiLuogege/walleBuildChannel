#coding=utf-8
import os
import sys

version = sys.argv[1]  # 版本号
unSignApkName = sys.argv[2]  # 360加固之后没有签名的apk

#keyStoreName = "andmodule.jks"  # 签名文件的名称
channelOutFile = "channels"  # 输出的渠道文件名
buildToolFile = "D:/soft/AndroidSDK/build-tools/26.0.2"  #sdk 编译环境的位置
apkName = "App_" + version + "_sign.apk"  # 签名之后的名称
apkFile = os.path.dirname(os.path.realpath(__file__))+"/"  # 获取到当前py文件的父目录

os.chdir(buildToolFile)

zipResult = os.system("zipalign -v -f 4 "+apkFile+unSignApkName+" " + apkFile+apkName)
print(zipResult)

if zipResult == 0:
    print("zipalign success")
else:
    print("zipalign failed")
    exit(1)
signPath=  "apksigner sign --ks " +apkFile+"andmodule.jks " + apkFile+apkName
print(signPath)
signResult = os.system(signPath)
print(signResult)

if signResult == 0:
    print("sign success")
else:
    print("sign failed")
    exit(1)

os.chdir(apkFile)
checkResult = os.system("java -jar CheckAndroidSignature.jar " + apkName)
print(checkResult)
if checkResult == 0:
    print("sign success")
else:
    print("sign failed")
    exit(1)

channelResult = os.system("java -jar walle.jar batch -f channel  " + apkName + " " + channelOutFile)
print(checkResult)

if channelResult == 0:
    print("build channel success")
else:
    print("build channel failed")
    exit(1)
