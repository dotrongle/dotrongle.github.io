import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'DA NANG ADMINISTRATIVE CENTER'
data['service'].append({'id':1, 'type':"Detailed Information", 'content':'http://trungtamhanhchinhdanang.vn/?lang=en', 'icon_id':1})
data['service'].append({'id':1, 'type':"Events", 'content':'http://trungtamhanhchinhdanang.vn/category/tin-tuc?lang=en', 'icon_id':5})
data['service'].append({'id':1, 'type':"Tour Registration", 'content':'http://trungtamhanhchinhdanang.vn/du-khach?lang=en', 'icon_id':1})
data['rating'] = 4.5


with open('danang_admin.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)

# {"icon_id": 4, "type": "Tour Registration", "content": "http://www.baotangchungtichchientranh.vn/visit/registration.html", "id": 1}]}
