from pyautogui import typewrite
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from generateValue import function1

def generateKey():
    function1()
    with open('data.txt', 'rb') as hwrgnFile:
        key = RSA.generate(1024, hwrgnFile.read)
    return key    

trueMessage = input('Wprowadź wiadomość:')
fakeMessage = trueMessage
if input("Czy zmienić wiadomość? [t/n]") == 't':
    typewrite(trueMessage)
    fakeMessage = input()
    print ("Wiadomość po zmianie",  fakeMessage)
    
trueMessage = trueMessage.encode()
fakeMessage = fakeMessage.encode()
key = generateKey()
privateKey = key.exportKey('PEM')
publicKey = key.publickey().exportKey('PEM')

hasher = SHA256.new(trueMessage)

signer = PKCS1_v1_5.new(RSA.importKey(privateKey))

signature = signer.sign(hasher)


if input("Czy chcesz podmienic klucz publiczny? [t/n]") == 't':
    fakeKey = RSA.generate(1024)
    publicKey = fakeKey.publickey().exportKey('PEM')

hasher2 = SHA256.new(trueMessage)


verifier = PKCS1_v1_5.new(RSA.importKey(publicKey))
if verifier.verify(hasher, signature):
    print('Weryfikacja przebiegła pomyślnie!')
else:
    print ('Błąd weryfikacji!')

 