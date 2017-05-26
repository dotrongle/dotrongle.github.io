import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'Lotte cinema Nowzone'
data['service'].append({'id':1, 'type':"Thông tin chi tiết", 'content':'https://lottecinemavn.com/vi-vn/rap-phim/ho-chi-minh/nowzone.aspx', 'icon_id':1})
data['service'].append({'id':1, 'type':"Đặt vé", 'content':'https://lottecinemavn.com/vi-vn/buoc-1.aspx', 'icon_id':2})
data['service'].append({'id':1, 'type':"Khuyến mãi", 'content':'https://lottecinemavn.com/vi-vn/su-kien/all.aspx', 'icon_id':6})
data['rating'] = 4.2
with open('lotte_cinema_nowzone.json', 'w') as fp:
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