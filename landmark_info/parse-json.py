import json

data = {'name':'', 'service':[], 'rating':0}

data['name'] = 'Museum of Cham Sculpture'
data['service'].append({'id':1, 'type':"Detailed Information", 'content':'http://chammuseum.vn/en', 'icon_id':1})
data['service'].append({'id':1, 'type':"Events", 'content':'http://chammuseum.vn/en/news-events/?type=event', 'icon_id':5})
data['service'].append({'id':1, 'type':"Tour Registration", 'content':'http://www.baotangchungtichchientranh.vn/visit/registration.html', 'icon_id':1})
data['rating'] = 4.5


with open('banahills.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)

# {"icon_id": 4, "type": "Tour Registration", "content": "http://www.baotangchungtichchientranh.vn/visit/registration.html", "id": 1}]}
