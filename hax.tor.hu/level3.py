# hax.tor.hu: level3
# woanmeo11

from base64 import b64decode

c = 'V m 0 w d 2 Q y U X l V W G x X Y T F w T 1 Z s Z G 9 W R m x 0 Z U V 0 W F J t e F Z V M j A 1 V j A x V 2 J E T l h h M k 0 x V j B a S 2 M y S k V U b G h o T W s w e F Z t c E d T M k 1 5 U 2 t W V W J H a G 9 U V 3 N 3 Z U Z a d G N F Z F R N b E p J V m 1 0 c 2 F W S n R h R z l V V m 1 o R F Z W W m F k R 0 5 G Z E Z S T l Z U V k p W b T E w Y T F k S F N r Z G p T R U p Y W V R G d 2 F G W k Z S U Q'

c = c.replace(' ', '')

while True:
    print(c)
    success = False
    for i in range(4):
        try:
            m = b64decode(c + i*'=').decode()
            success = True
            break
        except:
            continue
    if not success:
        break
    c = m
