# print(
# '''   _~_    
#   (o o)   
#  /  V  \  
# /(  _  )\ 
#   ^^ ^^
# ''' * 2, end='')

penguins_count = int(input())

if penguins_count > 9:
    print('не бывает столько пэнгвинсов')
    exit()

for i in range(0, penguins_count):
    print('   _~_    ' * penguins_count)
    print('  (o o)   ' * penguins_count)
    print(' /  V  \  ' * penguins_count)
    print('/(  _  )\ ' * penguins_count)
    print('  ^^ ^^   ' * penguins_count)