def cube():
    result=[]
    for i in range(5):
    #     result.append(i**3)  
    # return result
        yield i**3 # yield bize rastgele değişken atar,degeri bize gonderir ancak sonra kaybolur.
        # bilgi saklanmaz
#print(cube)

# generator=cube()
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in cube(): # yield veri tutmadigindan her seferinde tekrar olusturulur
    print(i)

generator=(i**3 for i in range(5))
print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)
    
