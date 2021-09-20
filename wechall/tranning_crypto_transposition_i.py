# Wechall: Training: Crypto - Transposition I
# woanmeo11

def decode(cipher):
    for i in range(0, len(cipher), 2):
        print(cipher[i + 1] + cipher[i], end='')

cipher = 'oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wr bbmdmshhmi.l'

decode(cipher)
