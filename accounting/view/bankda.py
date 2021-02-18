# -*- coding: utf-8 -*-

import json
import requests
import xml.etree.ElementTree as ET

# =============== 계정관련 ===============

# 이용자(파트너쉽 회원사의 고객) 회원가입
def user_join_prs(data):
    url = "https://ssl.bankda.com/partnership/user/user_join_prs.php"
    resMsg = requests.post(url, data=data)
    content = resMsg.content.decode('euc-kr')
    return content

# 이용자(파트너쉽 회원사의 고객) 회원정보수정
def user_info_edit(data):
    url = "https://ssl.bankda.com/partnership/user/user_info_edit.php"
    resMsg = requests.post(url, data=data)
    content = resMsg.content.decode('euc-kr')
    return content

# 이용자(파트너쉽 회원사의 고객) 회원탈퇴(서비스해지)
def user_withdraw(data):
    url = "https://ssl.bankda.com/partnership/user/user_withdraw.php"
    resMsg = requests.post(url, data=data)
    content = resMsg.content.decode('euc-kr')
    return content

# =============== 계정관련 ===============


# =============== 계좌관련 ===============

# 특정계좌의 상태정보 조회(HTML)
def account_info_xml(data):
    url = "https://ssl.bankda.com/partnership/partner/account_info_xml.php"
    resMsg = requests.post(url, data=data)
    root = ET.fromstring(resMsg.content.decode('euc-kr'))
    attrib = root.find("account").attrib
    return attrib

# 파트너회원의 전체계좌 리스트조회
def account_list_partnerid_xml():
    with open('/home/ubuntu/erowm/accounting/bankdakey.json', 'r') as f:
        json_data = json.load(f)

    url = "https://ssl.bankda.com/partnership/partner/account_list_partnerid_xml.php"
    data = {
        'service_type': "basic"
        , 'partner_id': json_data['id']
        , 'partner_pw': json_data['pw']
    }
    resMsg = requests.post(url, data=data)

    root = ET.fromstring(resMsg.content.decode('euc-kr'))
    account_info = root.find("account").findall("account_info")
    accounts = []
    for account in account_info:
        accounts.append(account.attrib)
    return accounts

def account_del(data):
    url = "https://ssl.bankda.com/partnership/user/account_del.php"
    resMsg = requests.post(url, data=data)
    print(resMsg.content)
    # root = ET.fromstring(resMsg.content.decode('euc-kr'))
    # attrib = root.find("account").attrib
    return resMsg.content

# =============== 계좌관련 ===============