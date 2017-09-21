import json
from os import listdir
from os.path import isfile
from os.path import join

for adir in listdir('.'):
    data = list()
    if isfile(adir):
        continue
    with open('../maykha_gallery/' + adir+'.json', 'w') as outfile:
        for im in listdir(join('.',adir)):
            dim = dict()
            durl = dict()
            durl['medium']='https://dotrongle.github.io/maykha_gallery_image/'+adir+'/'+im
            dim['url']=durl
            data.append(dim)
        json.dump(data, outfile)
