# EnterpriseWeChatPushMessage
**利用企业微信搭建自己的应用推送文本、图文、模板等消息。**

下面开始教程（非常容易）：

1. 首先注册企业微信，这就不用我多说了吧，自己百度一下就知道了。
2. 然后如下图所示创建自己的应用。

![image-20220911185906292](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911185906292.png)

3. 创建完之后记住图中标注的信息，后面脚本里需要填写对应信息。

![image-20220911190331127](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911190331127.png)

![image-20220911190458162](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911190458162.png)

4. 在微信插件里找到企业微信二维码，发给需要推送的人，让他扫码关注即可。然后找到通讯录记录自己想要推送对象的ID，一般为成员名的英文名，不会就写@all。

   ![image-20220911191158405](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911191158405.png)

5. 下载我仓库里的对应推送脚本，一个是推送纯文本信息的，另一个是推送图文消息的，按照自己需求下载，下载完之后打开python文件，修改里面的刚刚前面要求记录的信息（包括企业ID，应用ID，应用Secret和用户ID）。

   ![image-20220911191539478](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911191539478.png)

6. 修改完成后将该脚本上传至服务器等平台，设置宝塔定时任务定时执行推送任务即可完成推送。
    ![image-20220911191440342](https://raw.githubusercontent.com/Alleyf/PictureMap/main/web_icons/image-20220911191440342.png)
    **[AlleyfBlog](https://alleyf.github.io)**
[注]: 感谢支持，可以关注我的博客，随时更新对你有用的文章。



