import json
from os import listdir
from os.path import isfile
from os.path import join
import os
for adir in ['danang_center']:
    data = list()   
    if isfile(adir):
        continue
    #os.mkdir('../landmark_gallery_info/' + adir)
    with open('../landmark_gallery_info/' + adir+'.json', 'w') as outfile:
        for im in listdir(join('.',adir)):
            dim = dict()
            durl = dict()
            durl['medium']='https://dotrongle.github.io/landmark_gallery/'+adir+'/'+im
            dim['url']=durl
            data.append(dim)



        json.dump(data, outfile)

