# cryptopals: Convert hex to base64
# huycon

from base64 import b64encode

hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(b64encode(bytes.fromhex(hexstr)).decode())