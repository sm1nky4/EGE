print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x == (y <= z)) and (y == (not(z <= w)))):
                    print(x, y, z, w)








answer = 'wzxy'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 205, answer, 'c5e4e768af58cf865c4006af69319e62'))