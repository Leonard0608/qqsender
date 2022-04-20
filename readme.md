## QQsender   一款轻量级的QQ信息发送助手

##### 如何通过QQ假装内卷？

只需定时向同学发送消息即可。

##### 第零步 切换QQ发送消息模式为Enter发送

##### 第一步 安装库

`pip install datetime`

##### 第二步 下载源文件

##### 第三步 引入文件

`import qqsender`

##### 第四步 使用代码

`qqsender.sleep_send(<message>,<name>,<max_time>,<main_time>)`

message:你要发送的信息

name:你要发送的人

max_time:发送消息最大间隔时间，单位秒

min_time:发送消息最小间隔时间，单位秒

`qqsender.clocksend(<time.hour>,<message>,<name>)`

time.hour:发送消息的时间，单位为时

message:发送的信息

name:发送的人