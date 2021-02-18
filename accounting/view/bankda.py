# -*- coding: utf-8 -*-

import json
import logging
import requests
from django.utils import timezone
import xml.etree.ElementTree as ET

with open('/home/ubuntu/erowm/accounting/bankdakey.json', 'r') as f:
    json_data = json.load(f)

def setDefaultValue(data):
    data.setdefault('directAccess', "y")
    data.setdefault('service_type', "basic")
    data.setdefault('partner_id', json_data['id'])
    data.setdefault('partner_pw', json_data['pw'])
    data.setdefault('partner_name', json_data['name'])
    data.setdefault('char_set', "utf-8")
    return data

def bankda_log(result, data, func):
    logging.basicConfig(filename='./accounting/bankda.log', level=logging.INFO)
    if result.upper() == "OK":  # 정상
        logging.info("\n"
            "[" + str(timezone.now()) + "] 뱅크다 " + func + " 완료\n"
            "전송DATA : " + str(data) + "\n"
            "RESULT : " + result + "\n")
    else:
        logging.error("\n"
            "[" + str(timezone.now()) + "] 뱅크다 " + func + " 오류\n"
            "전송DATA : " + str(data) + "\n"
            "RESULT : " + result + "\n")


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

# 이용자(파트너쉽 회원사의 고객) 계좌추가
def account_add(data):
    url = "https://ssl.bankda.com/partnership/user/account_add.php"
    data = setDefaultValue(data)
    data.setdefault('Command', "update")
    data.setdefault('Mjumin_2', "0000000")

    resMsg = requests.post(url, data=data)  # 데이터전송
    result = resMsg.content.decode('utf-8').upper() # 결과
    bankda_log(result, data, "계좌추가")    # 로그기록
    return result

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