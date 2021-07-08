import requests
import time
import json

if "__main__" == __name__:
    api_access_token = json.load(open('config.json'))['main-token']
    login = json.load(open('config.json'))['main-number']
    tel = json.load(open('config.json'))['number-client']

    # Баланс QIWI Кошелька
    def balance(login, api_access_token):
        s = requests.Session()
        s.headers['Accept']= 'application/json'
        s.headers['authorization'] = 'Bearer ' + api_access_token  
        b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + login + '/accounts')
        return b.json()

    # Перевод на QIWI Кошелек
    def send_p2p(api_access_token, to_qw, comment, sum_p2p):
        s = requests.Session()
        s.headers = {'content-type': 'application/json'}
        s.headers['authorization'] = 'Bearer ' + api_access_token
        s.headers['User-Agent'] = 'Android v3.2.0 MKT'
        s.headers['Accept'] = 'application/json'
        postjson = {"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"}, "comment": comment ,"fields":{"account":""}}
        postjson['id'] = str(int(time.time() * 1000))
        postjson['sum']['amount'] = sum_p2p
        postjson['sum']['currency'] = '643'
        postjson['fields']['account'] = to_qw
        res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments',json = postjson)
        return res.json()

    # Тарифные комиссии
    def get_commission(api_access_token, to_account, prv_id, sum_pay):
        s = requests.Session()
        s.headers = {'content-type': 'application/json'}
        s.headers['authorization'] = 'Bearer ' + api_access_token  
        postjson = {"account":"","paymentMethod":{"type":"Account","accountId":"643"}, "purchaseTotals":{"total":{"amount":"","currency":"643"}}}
        postjson['account'] = to_account
        postjson['purchaseTotals']['total']['amount'] = sum_pay
        c_online = s.post('https://edge.qiwi.com/sinap/providers/'+prv_id+'/onlineCommission',json = postjson)
        return c_online.json()['qwCommission']['amount']

    def summa():
        summ = balance(login,api_access_token)['accounts'][0]['balance']['amount']
        if(summ > 2):
            print("-----------------------------------------------------------------------------------------------------------")
            print(" ")
            print("Сумма на кошельке: " + str(summ))
            y = round(get_commission(api_access_token,tel,'99',summ) / summ,2)
            print("Комиссия при переводе: " + str(y * 100) + "%")
            x = round(summ / (1 + y),2)
            print("Сумма перевода бyдет составлять: " + str(x))
            responce = send_p2p(api_access_token,tel,'comment',x)
            try:
                print("Ошибка перевода: " + responce['message'])
            except:
                print("Перевод " + str(x) + "руб выполнен успешно")
                print("Сумма на кошельке после перевода состовляет: " + str(balance(login,api_access_token)['accounts'][0]['balance']['amount']))
            print(" ")
            print("-----------------------------------------------------------------------------------------------------------")
        time.sleep(3)
        summa()

    summa()

    

   
    
    

    
    

