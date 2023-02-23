import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está disponível no momento!')
else:
    print('Ele está funcionando normalmente!')
    
'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''