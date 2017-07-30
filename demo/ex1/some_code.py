import nutslib
import some_module

def alphafunc():
    #;print('Before x=1 in alphafunc..')
    x = 1

    #;print('Before printing alphafunc...')
    x = x + 1

#; print('Before x = 2...')
x = 2

#;print('Before calling alphafunc.')
alphafunc()

some_module.foo()
