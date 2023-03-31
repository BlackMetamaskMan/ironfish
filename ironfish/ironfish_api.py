# -*- coding:utf-8 -*-
import logging
import time
import requests
import random

class IronfishApi:

    def check_points(self,id):

        check_points_url='https://api.ironfish.network/users/%s'%(id)
        try:
            with requests.get(url=check_points_url,timeout=10,stream=True) as r:
                '''{"id":67056,"country_code":"AND",
                "graffiti":"byte","total_points":60,
                "created_at":"2022-06-12T08:23:18.917Z","rank":14768}'''
                rt= r.json()
                if 'total_points' in rt:
                    points=rt['total_points']
                    return points
        except Exception as ex:
            logging.error('check_points,Error:%s'%(ex))

        return None


    def register(self,register_email):
        '''{
            "statusCode": 422,
            "message": "User already exists for 'dddd212dddd'",
            "error": "Unprocessable Entity"
        }
        {
            "id": 208259,
            "created_at": "2022-06-16T09:54:38.166Z",
            "updated_at": "2022-06-16T09:54:38.166Z",
            "email": "asdf33@test.com",
            "graffiti": "dddd212dddd2",
            "country_code": "ALB",
            "email_notifications": false,
            "last_login_at": null,
            "discord": null,
            "telegram": "dddd",
            "github": "dfdf1"
        }
        '''
        rurl='https://testnet.ironfish.network/users/'
        register_url='https://api.ironfish.network/users'
        emails=register_email.split('@')
        name=emails[0]
        countries=['KHM','TWN','TCA','SDN','SJM','SYR','TJK','THA','UMI','ARE','VEN','VNM','ZWE','URY','VGB','UKR','TCA']
        cty=random.choice(countries)
        post_data={"github": name,
                   "email": register_email,
                   "graffiti": name,
                   "discord": name,
                   "country_code": cty}

        r={'mail_name':register_email,'result':False,'msg':''}

        for i in range(3):
            try:
                with requests.post(url=register_url,data=post_data,timeout=10,stream=True) as rt:
                    jdata=rt.json()
                    if 'id' in jdata:
                        r['result']=True
                        r['msg']='%s%s'%(rurl,jdata['id'])
                    elif 'statusCode' in jdata:
                        r['result']=False
                        r['msg']=jdata['message']
                    break
            except Exception as ex:
                logging.error('login,Error:%s'%(ex))
                time.sleep(2)

        return r

