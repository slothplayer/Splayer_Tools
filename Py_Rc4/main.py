import base64

def rc4_main(key = "init_key", message = "init_message"):
    print("RC4解密主函数调用成功")
    print('')
   
    s_box = rc4_init_sbox(key)
    crypt = rc4_excrypt(message, s_box)
   
    return crypt

def rc4_init_sbox(key):
    s_box = list(range(256))
    
    print("原来的 s 盒：%s" % s_box)
    print('')
    
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    
    print("混乱后的 s 盒：%s"% s_box)
    print('')
    
    return s_box

def rc4_excrypt(plain, box):
    print("调用解密程序成功。")
    print('')

    plain = base64.b64decode(plain.encode('utf-8'))
    plain = bytes.decode(plain)
    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))

    cipher = "".join(res)

    print('res用于解密字符串，解密后是：%s' %res)
    print('')

    print("解密后的字符串是：%s" %cipher)
    print('')

    print("解密后的输出(没经过任何编码):")
    print('')

    return cipher

if __name__ == '__main__':
    # a cipher
    a=[]
    key='123'
    s=''
    for i in a:
        s+=chr(i)  
    s=str(base64.b64encode(s.encode('utf-8')), 'utf-8')

    print(rc4_main(key, s))

