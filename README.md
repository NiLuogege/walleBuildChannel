##[首先我们来一片该小工具的原理博客](https://blog.csdn.net/jason_2016/article/details/58137497)

###本文对 [使用Python脚本实现360加固后一键V2签名和Walle打出渠道包](https://blog.csdn.net/finddreams/article/details/78773687)中提供的工具进行了改进，改进和使用方式如下所示

#####改进
1. 对python文件编码格式进行了设置，避免编码方式引起的错误
2. 简化了文件的配置步骤
  之前我们要如下图一一配置
![image.png](https://upload-images.jianshu.io/upload_images/3571184-48fe4cd3377d907b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  而现在通过配合控制台参数输入只需要配置两个地方
![image.png](https://upload-images.jianshu.io/upload_images/3571184-fa7af16c60f1f601.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 替换```CheckAndroidV2Signature.jar```为```CheckAndroidSignature.jar```前者只会输出V2签名的相关信息，后者还会输出V1签名的信息。


#####使用
1. 在build_channle.py中配置自己的```build-tools```路径，和签名文件名称。
2. 打开控制台输入如下命令
```python build_channel.py 1.0.1 app-release.apk```
  1.0.1---》标识app版本号
  app-release.apk---》经过360加固过但未签名的apk
3. 在下图处输入签名文件密码
![image.png](https://upload-images.jianshu.io/upload_images/3571184-a92096a6f672dfef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 顺利的话可以看到控制台输出如下log，到这里渠道包就已经生成了在channles文件夹中，可以看出现在的apk已经支持V1和V2签名。
![image.png](https://upload-images.jianshu.io/upload_images/3571184-d2c69eec121056fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
5. 把渠道包发给市场吧，哈哈。



###最后再次感激[使用Python脚本实现360加固后一键V2签名和Walle打出渠道包](https://blog.csdn.net/finddreams/article/details/78773687)的作者




