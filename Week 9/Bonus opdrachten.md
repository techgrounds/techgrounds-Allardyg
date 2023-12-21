# Opdracht

Bekijk de code snippets en pas ze aan zodat ze het gewenste resultaat laten zien:

## 1
    '''
    The output should be:
    hello Casper
    hello Floris
    hello Esther
    '''
    foo = 'hello'
    ls = ['Casper', 'Floris', 'Esther']
    for name in ls:
    	print(loo,name)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/d498fd55-2a3f-4064-8f34-0bf5ea0126e9)

## 2
    '''
    The output should be:
    100
    '''
    foo = 20
    bar = '80'
    print(foo + bar)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/f02a6c3c-06f5-4363-b686-6d497703109f)

## 3
    '''
    The output should be:
    30
    '''
    foo = 20
    for i in range(10):
    	foo -= 1
    
    print(foo)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/dea3dbd6-3017-4343-9d80-78e62344a4af)

## 4
    '''
    The output should be:
    there are 0 kids on the street
    there are 1 kids on the street
    there are 2 kids on the street
    there are 3 kids on the street
    there are 4 kids on the street
    '''
    foo = 0
    while foo <= 5:
    	print('there are', foo, 'kids on the street')
    	foo += 1

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/022654e1-bf72-469a-8f57-58d7990b2c4a)


## 5
    '''
    The output should be:
    Star Wars
    '''
    ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
    print(ls[4])

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/4f7a6008-8110-4cbf-ba1a-0b8a7a477ca0)

## 6
    '''
    The output should be:
    80
    '''
    foo = 80
    if foo < 30:
    	print(foo)
    else:
    	print('big number wow')
    elif foo < 100:
    	print(foo)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/b63780be-d18f-4c4e-ba48-4b768c84082e)

## 7
    '''
    The output should be:
    ['Dog', 'Cat', 'Fly']
    '''
    ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
    short_names = []
    
    for animal in ln:
    	if len(animal) == 3:
    		short_names.append(animal)
    	short_names = []

    print(short_names)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/4ee17c5b-1391-4f0a-82a2-be8a910dac9a)

## 8
    '''
    The output should be:
    20
    '''
    foo = 10
    bar = 2
    print(foo**bar)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/62e205fa-f2e0-47b0-a761-cb9916d8fede)

## 9
    '''
    The output should be:
    0
    1
    2
    3
    4
    8
    9
    '''
    for i in range(10):
    	if i < 5:
    		print(i)
    	elif i < 8:
    		break
    	else:
    		print(i)

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/a0225a43-ef48-496a-8966-7a60dab65c96)

## 10
    '''
    The output should be:
    the number is 20
    '''
    print('the number is' + 20)
    

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/a1f96ecd-0c9b-4f63-b721-6de39fa929be)

## 11
    '''
    The output should be:
    IT LIVES!
    '''
    dev monster():
    	print('IT LIVES!')
    
    monster()


#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/365b58dd-9ad6-46b9-9959-1cf3ef50acbf)


## 12
    '''
    The output should be:
    4
    16129
    '''
    def square(x):
    	return x**2
    
    nr = square(2)
    print(nr)
    
    big = square(foo)
    print(big)
    
    foo = 127


#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/e6a2f673-b794-4a3a-893d-2915dbb6da15)

## 13
    '''
    The output should be:
    Your random number is: <insert random number here>
    '''
    import random
    
    number = "12"
    
    print("Your random number is:"+number)
    

#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/69891399-1817-44dd-8438-eef0f810b0a1)

## 14
    '''
    The output should be:
    True
    '''
    def rtn(x):
    	return(x)
    
    foo = rtn(3)
    
    if foo > rtn(4):
    	print(True)
    else:
    	print(False)
    
     
#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/c86170bf-193c-4e15-b608-468ee3eb4565)

## 15
    '''
    The output should be:
    a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
    '''
    foo = ''
    for i in range(3):
    	foo += 'a'
    	for j in range(3):
    		foo += '5'
    		for k in range(3):
    			foo += '|'
    
    print(foo)


#### Uitwerking:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/1ddbf0f3-eb8f-4969-ab84-873131bb396a)
