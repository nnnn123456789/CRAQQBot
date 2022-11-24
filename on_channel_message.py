import api;
import craverify;
import lib; 

class ChannelMsgCommand:

    def __init__(self, handle):
        self.execute = handle


    def __call__(self, args, guild_id, channel_id, user_id):
        try:
            ret = self.execute(args, guild_id, channel_id, user_id)
        except Exception as e:
            print(e)
            ret = "执行出现错误"
        return ret


channel_ans_pool = {}


# def get_ID(args, channel_id, user_id):
#     ID_s = str(user_id)[-8:]
#     return "您的本频道ID为%s, 请访问https://github.com/SUSTech-CRA/qq-add-group-verify, 填写本频道ID"
#     pass



def SUSTech_auth(args, guild_id, channel_id, user_id):
    ID_s = str(user_id)[-8:]
    if len(args) == 1:
        return "[CQ:at,qq=%s] 您的本频道ID为%s, 请访问https://mirrors.sustech.edu.cn/qqverify , 填写本频道ID, 获得验证Token. 使用\"#南科认证 Token\"认证南科身份, 访问频道内容. " % (str(user_id), ID_s)
    elif len(args) == 2:
        if(craverify.verify(args[1], ID_s)):
            l = api.get_guild_roles(str(guild_id))
            aim_role_id_s = 0;
            for i in l:
                if i["role_name"] == "已认证":
                    aim_role_id_s = (i["role_id"])
                    print(i)
            api.set_guild_member_role(str(guild_id), True, aim_role_id_s, str(user_id))
            return "已获得认证用户权限"
        else:
            return "[CQ:at,qq=%s] 无法验证您的南科身份, 请重试. \n您的本频道ID为%s, 访问https://mirrors.sustech.edu.cn/qqverify , 填写本频道ID, 获得验证Token. 使用\"#南科认证 Token\"认证南科身份, 访问频道内容. " % (str(user_id), ID_s)
    pass


def role_list(args, guild_id, channel_id, user_id):
    l = api.get_guild_roles(str(guild_id))
    print(l)
    ret_list = [];
    for i in l:
        #if not i["disabled"]:
            ret_list.append("name: %s, color: %x, id = %s, enable = %s" % (i["role_name"], i["argb_color"], i["role_id"],  str(not i["disabled"])))
    ret = "\n".join(ret_list)
    return ret;


channel_ans_pool["#南科认证"] = ChannelMsgCommand(SUSTech_auth)
channel_ans_pool["#成员组列表"] = ChannelMsgCommand(role_list)
# group_ans_pool["#获取ID"] = ChannelMsgCommand(get_ID)

def main(m):
    rawmsg = m["message"]
    args = lib.div_args(rawmsg)
    cmd = channel_ans_pool.get(args[0])

    if not cmd == None:
        ans = cmd(args, m["guild_id"], m["channel_id"], m["user_id"])
        if not ans == "":
            api.send_guild_channel_msg(m["guild_id"], m["channel_id"],ans)
    pass
    pass



