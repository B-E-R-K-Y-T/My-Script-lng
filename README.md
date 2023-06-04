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

Более сложный код:

```
var arr = {1,2,3,4};
         # 0 1 2 3
try do
    print arr[0];
    print arr[1];
    print arr[2];
    print arr[3];
    print arr[4];
catch IndexException do
    print "IndexException!!!";
end_try


func test(x, y, z)
    for i=(1,5) do
        try do
            var x = 2;
        catch ObjectException do
            try do
                #Тут намеренная ошибка синтаксиса
                print "ObjectException 1", x
            catch SyntaxException do
                print "SyntaxException 2";
            end_try
        end_try
        print "Hello!", x, loop_i;

        print "x: ", func_x, "y: ", func_y, "z: ", func_z;
    end_loop

    print "END_LOOP";

    try do
        print loop_i;
    catch ObjectException do
        print "ObjectException 3";
    end_try

    print "END_TRY1";

    print "x: ", func_x, "y: ", func_y, "z: ", func_z, "END";
    print "END FUNC";
end_func

test(1, 2, 3);


try do
    print "test";

    # Ошибка, попытка переопределить переменной
    var x = 2;
catch ObjectException do
    try do
        print "ObjectException 4", x
    catch SyntaxException do
        print "SyntaxException 5";
    end_try
end_try


print "END_TRY2";

try do
    try do
        # Ошибка, обращение к неизвестной переменной
        print loop_i;
    catch ObjectException do
        print "ObjectException 6";
    end_try
catch ObjectExcepti2on do
    print "ObjectException 7";
end_try

Add(1, 2);
OS_command("echo 123");
Len("aaaqweqe");
Print(1,2,3);

print "test 2";

test(1, 2, 3);

for _=(1,20) do
    print "FINAL_FOR";
end_loop


Add(1, 2);
OS_command("echo 123");
Len("aaaqweqe");
Print(1,2,3);
Sum(1,2,3,4);

func test_wrapper_loops()
    for i=(1,4) do
        for j=(1,2) do
            for z=(1,23) do
                for k=(1,2) do
                    print loop_i, loop_j, loop_z, loop_k;

                    for tim=(-1,2) do
                        print "Tim: ", loop_tim;
                    end_loop

                    try do
                        :LSDKFH;lkh
                    catch SyntaxException do
                        print "SyntaxException 1";
                    end_try
                end_loop
            end_loop
        end_loop
    end_loop
end_func


test_wrapper_loops();


```

Вывод: 
```
1
2
3
4
IndexException!!!
SyntaxException 2
Hello! 2 1
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 2
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 3
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 4
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 5
x:  1 y:  2 z:  3
END_LOOP
ObjectException 3
END_TRY1
x:  1 y:  2 z:  3 END
END FUNC
test
SyntaxException 5
END_TRY2
ObjectException 6
3
123
8
1 2 3
test 2
SyntaxException 2
Hello! 2 1
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 2
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 3
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 4
x:  1 y:  2 z:  3
SyntaxException 2
Hello! 2 5
x:  1 y:  2 z:  3
END_LOOP
ObjectException 3
END_TRY1
x:  1 y:  2 z:  3 END
END FUNC
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
FINAL_FOR
3
123
8
1 2 3
10
1 1 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 1 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
1 2 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 1 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
2 2 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 1 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
3 2 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 1 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 1 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 1 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 2 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 2 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 3 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 3 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 4 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 4 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 5 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 5 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 6 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 6 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 7 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 7 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 8 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 8 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 9 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 9 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 10 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 10 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 11 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 11 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 12 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 12 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 13 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 13 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 14 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 14 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 15 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 15 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 16 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 16 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 17 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 17 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 18 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 18 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 19 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 19 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 20 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 20 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 21 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 21 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 22 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 22 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 23 1
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
4 2 23 2
Tim:  -1
Tim:  0
Tim:  1
Tim:  2
```




общие возможности ЯП 

[https://www.youtube.com/watch?v=b_BpHXJyhHE](https://www.youtube.com/watch?v=b_BpHXJyhHE)

вызов функций python

[https://www.youtube.com/watch?v=sqP7jk1jH-0](https://www.youtube.com/watch?v=sqP7jk1jH-0)
