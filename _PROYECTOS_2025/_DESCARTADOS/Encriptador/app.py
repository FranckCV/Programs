# 


import hashlib
encript = '282b91e08fd50a38f030dbbdee7898d36dd523605d94d9dd6e50b298e47844be'
# password = '1234567890'
# password = 'securepass456'
password = 'eee'




def encstringsha256(cadena_legible):
    h = hashlib.new('sha256')
    h.update(bytes(cadena_legible, encoding='utf-8'))
    epassword = h.hexdigest()
    return epassword

valor = encstringsha256(password)

print(valor)
xdxdxd = valor == encript
print(xdxdxd)