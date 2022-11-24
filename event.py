from api import *

import requests
import json

import time

import craverify


def on_group_message(m):
    pass


def on_private_message(m):
    pass


def on_group_manager_change(m):
    pass





def on_group_users_add(m):
    pass


def on_group_users_delete(m):
    pass


def on_group_ban(m):
    pass


def on_group_document_upload(m):
    pass


def on_request_friend_add(m):
    pass


#申请或邀请
def on_request_group_invite(m):
    print(m)
    comment = m["comment"]
    groupid = m["group_id"]
    flag = m["flag"]
    sub_type =  m["sub_type"]

    if (sub_type == "invite"):
        set_group_add_request(flag, sub_type, False, reason = "禁止邀请加群");
        print("禁止邀请加群");
        return

    comment = comment.split('\n')[1];
    comment = comment[3:];
    print(comment)
    if (craverify.verify(comment, m["user_id"])):
       set_group_add_request(flag, sub_type, True);
       print("放人成功");
       return   
        
    set_group_add_request(flag, sub_type, False, reason = "无法识别加群验证");
    print("拒绝加群");
    pass


def on_group_message_recall(m):
    pass


def on_private_message_recall(m):
    pass






def on_heartbeat(m):
    pass


