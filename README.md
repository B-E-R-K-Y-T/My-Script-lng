# My-Script-lng

Общие возможности языка:

```
var x = 1;
print x;

try do
    # Нельзя переобъявить переменную. Потом добавлю константы, а переменные сделаю реальными переменными
    var x = 2;
catch ObjectException do
    for i=(1,4) do
        print "ObjectException 1", "i: ", loop_i;
    end_loop
catch SyntaxException do
    print "SyntaxException 2";
end_try

func test(x)
    print "Hello world!", func_x;
end_func

test(12);

Min(1, 2, 3, -1);

# Создает папку
OS_command("mkdir TEST");
```

Вывод:
```
1
ObjectException 1 i:  1
ObjectException 1 i:  2
ObjectException 1 i:  3
ObjectException 1 i:  4
Hello world! 12
-1
```


Пример кода
```
var x = 1;
var y = 1;

print x;
print "Hello world!";

var z = x + y;

print z;

for i=(1,10) do
    print "loop_i", loop_i;
end_loop
```

Вывод: 
```
>>>/home/berkyt/PycharmProjects/MyScriptLanguage/test2.txt
1
Hello world!
2
loop_i 1
loop_i 2
loop_i 3
loop_i 4
loop_i 5
loop_i 6
loop_i 7
loop_i 8
loop_i 9

```

Пример кода2
```
var x = 1;
var y = 1000;

var result = x + y;

print x;
print "RESULT: ", result;

func print_x()
    print "PRINTED: ", x;
end_func

print_x();

for i=(1,5) do
    print loop_i, x;
end_loop
```

Вывод: 
```
1
RESULT:  1001
PRINTED:  1
1 1
2 1
3 1
4 1
5 1
```

Пример try catch:
```
var x = 1;

try do
    var x = 2
catch ObjectException do
    print "ObjectException 1";
catch SyntaxException do
    print "SyntaxException 2";
end_try

print x;
```

Вывод:
```
SyntaxException 2
1
```


общие возможности ЯП 

[https://www.youtube.com/watch?v=b_BpHXJyhHE](https://www.youtube.com/watch?v=b_BpHXJyhHE)

вызов функций python

[https://www.youtube.com/watch?v=sqP7jk1jH-0](https://www.youtube.com/watch?v=sqP7jk1jH-0)
