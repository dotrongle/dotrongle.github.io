import json
from os import listdir
from os import isfile
from os import join

for adir in listdir('.'):
    data = list()
    if isfile(adir):
        continue
    with open(adir+'.json', 'w') as outfile:
        for im in listdir(join('.',adir))[:5]:
            dim = dict()
            durl = dict()
            durl['medium']='https://dotrongle.github.io/landmark_gallery/'+adir+'/'+im
            dim['url']=durl
            data.append(dim)
        json.dump(data, outfile)

