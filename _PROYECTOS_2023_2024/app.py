# 


import hashlib
encript = '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'
password = '1234567890'
password = 'securepass456'
password = '1234567890'




def encstringsha256(cadena_legible):
    h = hashlib.new('sha256')
    h.update(bytes(cadena_legible, encoding='utf-8'))
    epassword = h.hexdigest()
    return epassword

valor = encstringsha256(password)

print(valor)
xdxdxd = valor == encript
print(xdxdxd)