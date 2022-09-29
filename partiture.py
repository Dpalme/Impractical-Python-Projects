from sys import stdout as st
UP = 3
DOWN = 4
LEN = DOWN*UP
FSPACE = ' '*((LEN-(UP*2))//2)
BSPACE = ' '*((LEN-(DOWN*2))//2)
f_str = '|' + (''.join((FSPACE, '.', FSPACE))*UP) + FSPACE + '|'
bar = '|' + (''.join((BSPACE, '°', BSPACE))*DOWN) + BSPACE + '|'
st.write(f_str + '\n')
st.write(bar + '\n')