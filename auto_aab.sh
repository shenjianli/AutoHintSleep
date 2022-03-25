# --bundle为输入文件的全路径（当前目录直接使用文件名） --output为输出文件全路径
bundletool build-apks --bundle=my.aab --output=my.apks

# 安装命令： install-apks
java -jar bundletool-xxx.jar install-apks --apks=myapp.apks