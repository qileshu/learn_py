#coding:utf-8
import requests


#活动人数
pal_num = 4
#原始地址
str_from_1 = u"北京市朝阳区德胜门外北沙滩1号院"
str_from_2 = u"北京市东城区朝阳门北大街8号富华大厦b座8/9层"
str_to = u"北京市东城区北京INN8号楼"
'''
str_from_3
str_from_4
str_to
'''

def geocoder(place):
    #地址转坐标
    url_geocoder = "http://restapi.amap.com/v3/geocode/geo?address=" + place + "&key=804fb620e1898068abda8429a2cca2be"
    r_geocoder = requests.get(url_geocoder, verify = False)

    if r_geocoder.json()['status'] != '1' :
        print "error:" + r_geocoder.json()['message']
        return -1
    else:
        location = str(r_geocoder.json()['geocodes'][0]['location'])
        return location


def distance_time(str_from, str_to):

    lac_from
    lng_from = geocoder(str_from)[1]
    lat_to = geocoder(str_to)[0]
    lng_to = geocoder(str_to)[1]
   
    url = "http://restapi.amap.com/v3/direction/transit/integrated?key=804fb620e1898068abda8429a2cca2be&origin=" + loc_from + "&destination=" + loc_to + "&city=北京&cityd=北京&strategy=0&nightflag=0&date=2014-3-19&time=22:34"
    r_distance = requests.get(url, verify = False)

    if r_distance.json()['status'] != '1' :
        print  "error:" + r_distance.json()['info']
    else:
        distance = r_distance.json()['route']['distance']
        duration = r_distance.json()['route']['transits'][0]['duration']
    
    return distance, duration

print distance_time(str_from_1, str_to)
'''
print "max:" + str(max(distance_total))
print "min:" + str(min(distance_total))
print "avg:" + str(reduce(lambda x,y:x+y, distance_total))
'''
#print url
#print r_distance.json()['result']['elements'][0]['distance']
#print r_distance.json()['result']['elements'][0]['duration']
