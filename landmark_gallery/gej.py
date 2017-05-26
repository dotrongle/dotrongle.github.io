import json
from os import listdir
from os.path import isfile
from os.path import join

for adir in listdir('.'):
    data = list()
    if isfile(adir):
        continue
    with open('../landmark_gallery_info/' + adir+'.json', 'w') as outfile:
        for im in listdir(join('.',adir)):
            dim = dict()
            durl = dict()
            durl['medium']='https://dotrongle.github.io/landmark_gallery/'+adir+'/'+im
            dim['url']=durl
            data.append(dim)
        json.dump(data, outfile)

