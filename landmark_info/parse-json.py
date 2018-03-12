import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'Da Nang Cathedral'
data['service'].append({'id':1, 'type':"Detailed Information", 'content':'http://www.giaoxuchinhtoadanang.org', 'icon_id':1})
data['service'].append({'id':1, 'type':"Events", 'content':'http://www.giaoxuchinhtoadanang.org/tin-tuc/giao-xu/', 'icon_id':5})
#data['service'].append({'id':1, 'type':"Tour Registration", 'content':'http://baotangdanang.vn/portal/page/portal/baotang/huong_dan', 'icon_id':1})
data['rating'] = 4.5


with open('CathedralDanang.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)

# {"icon_id": 4, "type": "Tour Registration", "content": "http://www.baotangchungtichchientranh.vn/visit/registration.html", "id": 1}]}
