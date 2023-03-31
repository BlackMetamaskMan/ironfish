# -*- coding:utf-8 -*-
import logging
import json
import time
import logging
import ironfish.ironfish_api as if_api

class RegisterClient:

    def __init__(self,email_list):

        self.email_list=email_list

    def to_signup(self):

        iApi = if_api.IronfishApi()
        result=[]
        for email in self.email_list:
            rdict=iApi.register(email)
            # result.append(rdict)
            strs='%s,%s' % (email, rdict.get('msg'))
            logging.info(strs)
            result.append(strs)
            time.sleep(2)

        return result

# if __name__=='__main__':
#
#     iApi=IronfishApi()
#     r=iApi.register('volutes.cues_0l@icloud.com')
#     print(r)
#     # iApi.register('corms_fervent0c@icloud.com')
