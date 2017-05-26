import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'Bảo Tàng Chứng Tích Chiến Tranh'
data['service'].append({'id':1, 'type':"Thông tin chi tiết", 'content':'http://www.baotangchungtichchientranh.vn/', 'icon_id':1})
data['service'].append({'id':1, 'type':"Đăng ký tour", 'content':'http://www.baotangchungtichchientranh.vn/visit/registration.html', 'icon_id':4})
data['service'].append({'id':2, 'type':'phone number', 'content':'0839305587', 'icon_id':7})
data['rating'] = 4.3
with open('bao_tang_chung_tich_chien_tranh.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)

'''
data['name'] = 'Bao Tang Chung Tich Chien Tranh'
data['service'].append({'type':'Thong tin chi tiet', 'url':'http://www.baotangchungtichchientranh.vn/'})
data['service'].append({'type':'Dang ky tour', 'url':'http://www.baotangchungtichchientranh.vn/visit/registration.html'})
data['address'] = '28 Vo Van Tan, quan 3, Thanh pho Ho Chi Minh, Viet Nam'
data['location'] = (10.7794658,106.692127)
data['phone-number'] = '08 3930 5587'
data['rating'] = 4.3
data['images'].append({'url':''})
data['opening-hour'] = '07:30 to 12:00, 13:30 to 17:00'
data['landmarktype'] = 'museum'
with open('Bao_Tang_Chung_Tich_Chien_Tranh.json', 'w') as fp:
    json.dump(data, fp)
'''

'''
data['name'] = 'Khu Du Lich Suoi Tien'
data['service'].append({'type':'Thong tin chi tiet', 'url':'http://suoitien.com'})
data['service'].append({'type':'Dat ve', 'url':'http://suoitien.com/online'})
data['service'].append({'type':'event', 'url':'http://suoitien.com/le-hoi/'})
data['address'] = '120 AH1, Tan Phu, Ho Chi Minh, Viet Nam'
data['location'] = (10.865742,106.8022934)
data['phone-number'] = '08 3896 0260'
data['rating'] = 4.2
data['images'].append({'url':'http://file.vforum.vn/hinh/2016/05/suoi-tien(1).jpg'})
data['opening-hour'] = '07:00 to 17:00'
data['landmarktype'] = 'amusement'
with open('Khu_Du_Lich_Suoi_Tien.json', 'w') as fp:
    json.dump(data, fp)
'''
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