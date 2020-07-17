def myfunc():
    text = input("Введите текст: ")
    upper_ = 0
    lower_ = 0
    for i in text:
        if i.isupper():
            upper_ += 1
        else:
            lower_ += 1
    result = upper_ + lower_
    b = (upper_ / result) * 100
    c = (lower_ / result) * 100
    print(round(b, 2), "%", "Upper")
    print(round(c, 2), "%", "lower")
myfunc()