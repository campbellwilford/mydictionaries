def encryption(codes):
    
    infosecurity = open('info_security.txt', 'r')
    infosecurity_read = infosecurity.read()

    encrypted = open('encrypted.txt', 'w')

    for i in infosecurity_read:
        if i in codes:
            encrypted.write(codes[i])
        else:
            encrypted.write(i)

    encrypted.close()

def decryption(codes):
    
    encrypted = open('encrypted.txt', 'r')
    encrypted_read = encrypted.read()

    for i in encrypted_read:
        if not i in codes.values() or i == '.' or i == ' ':
            print(i, end='')
        else:
            for k, v in codes.items():
                if i == v:
                    print(k, end='')

def main():
    
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
             'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':'Y', \
             'J':'Z', 'j':'>', 'K':'<', 'k':'/', 'L':'j', 'l':'_', 'M':'"', 'm':'i', 'N':';', \
             'n':'A', 'O':'h', 'o':'-', 'Q':'$', 'q':'V', 'R':'^', 'r':'&', 'S':'^', \
             's':'(','T':')', 't':'~', 'U':'`', 'u':'g', 'V':'\\', 'v':'+', 'W':'=', 'w':'!', \
             'X':'f', 'x':'e', 'Y':'d', 'y':'c', 'Z':'b', 'z':'a'}
  
    encryption(codes)

    decryption(codes)

main()