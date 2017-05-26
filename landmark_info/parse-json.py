import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'Khách sạn Rex'
data['service'].append({'id':1, 'type':"Thông tin chi tiết", 'content':'http://www.rexhotelvietnam.com/', 'icon_id':1})
data['service'].append({'id':1, 'type':"Đặt bàn", 'content':'http://www.rexhotelvietnam.com/dining/', 'icon_id':3})
data['service'].append({'id':1, 'type':"Đặt phòng", 'content':'https://www.book-secure.com/index.php?s=results&property=vnhoc18828&arrival=2017-06-11&departure=2017-06-12&accommodation=Premium&code=PROMO-EARLY-BIRD-PROMOTION&adults1=1&children1=0&rooms=1&locale=en_GB&currency=USD&stid=1pdh7wuif&Hotelnames=ASIAVNHTLRex&hname=ASIAVNHTLRex&FirstRoomName=Premium&room=Premium&FirstDate=170611%3B1%3B1%3B0&FSTBKNGCode=PROMO-EARLY-BIRD-PROMOTION&accessCode=PROMO-EARLY-BIRD-PROMOTION&style=DIRECT&HTTP_REFERER=http%3A%2F%2Fwww.rexhotelvietnam.com%2Fdining%2F&profil=SESSION%3D57545826996&__utma=1.1453430872.1495820841.1495820841.1495820841.1&__utmb=1.6.10.1495820841&__utmc=1&__utmx=-&__utmz=1.1495820841.1.1.utmcsr%3Dgoogle%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmctr%3D%28not%20provided%29&__utmv=-&__utmk=200602286&redir=BIZ&rt=1495821237&_code=GoogleAnalytics&nbNightsValue=1', 'icon_id':10})
data['service'].append({'id':1, 'type':"Khuyến mãi", 'content':'http://www.rexhotelvietnam.com/special-offers/', 'icon_id':6})
data['rating'] = 4.4
with open('khach_san_rex.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)

'''
data['name'] = 'Nha Hang 3 la chay'
data['service'].append({'type':'Thong tin chi tiet', 'url':'http://3lachay.com/'})
data['service'].append({'type':'event', 'url':'http://3lachay.com/?page_id=122'})
data['address'] = '32A Cao Ba Nha, Nguyen Cu Trinh, Quan 1, Ho Chi Minh'
data['location'] = (10.7626116,106.6899306)
data['phone-number'] = '08 6683 0303'
data['rating'] = 4.1
data['images'].append({'url':''})
data['opening-hour'] = '08:00 to 22:00'
data['landmarktype'] = 'restaurant'
with open('Nha_Hang_3_la_chay.json', 'w') as fp:
    json.dump(data, fp)
'''