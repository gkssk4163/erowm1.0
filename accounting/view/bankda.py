# -*- coding: utf-8 -*-

import json
import requests
import xml.etree.ElementTree as ET

def account_info_xml(data):
    url = "https://ssl.bankda.com/partnership/partner/account_info_xml.php"
    resMsg = requests.post(url, data=data)
    root = ET.fromstring(resMsg.content.decode('euc-kr'))
    attrib = root.find("account").attrib
    return attrib

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
    print(resMsg.content)
    print(type(resMsg.content))
    # root = ET.fromstring(resMsg.content.decode('utf-8'))
    # print(root)
    # attrib = root.find("account").attrib
    return resMsg