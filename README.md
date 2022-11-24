# CRAQQBot

QQBot的应用层实现. 通讯层兼容gocqhttp或任何OneBot. 使用正向websocket(ws://localhost:6701/)触发事件, 使用http协议(http://localhost:5701/)调用api. 

暂时通讯地址是硬编码, 后期可以改为读配置文件. 

使用时应配置cmac_secret.txt.

获取token的代码位于https://github.com/SUSTech-CRA/qq-add-group-verify
