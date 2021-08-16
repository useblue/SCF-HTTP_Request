import requests
import sys
import codecs
from t import payload


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


SESSIONDATA = ''

class wx(object):
    def __init__(self, SESSIONDATA):

        self.SESSIONDATA = SESSIONDATA

        self.headers = {
		    'Host':' ',
			'Connection':' ',
			'X-Tag':' ',
			'Content-Length':' ',
			'content-type':' ',
			'Accept-Encoding':' ',
            'user-agent':' ',
            'Referer':' ',
            'cookie':' '
        }

    def prt_err_msg(self, res, expectation):
        if res['code'] != expectation:
            print('ERROR:', res['message'])
        else:
            print('SUCCESS')

    def sign(self):

        url = " "

        res = requests.post(url, headers=self.headers, data=payload.encode('utf-8')).json()
        self.prt_err_msg(res, 0)

    def run(self):

        print('ck')
        self.sign()


if __name__ == '__main__':
    wx(SESSIONDATA).run()