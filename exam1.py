import re
def function1 ():
    f = open ('C:\\Users\\student\\Desktop\\new.txt', 'r', encoding = 'utf-8')
    string = f.read()
    f.close ()
    return string
def function2 (string):
    regex = '(?:[^А-Я][^.] )([А-Я][.] ?[А-Я][а-я]+)[^а-я]'
    a = re.findall (regex, string)
    line = ''
    for word in a:
        word = str (word)
        line = line + word + '\n'
    print (line)
def function3 (string):
    regex = '((?:(?:[А-Я][а-я]+)|(?:(?:[А-Я]. ?)?[А-Я][.])) ?[А-Я][а-я]+)[^а-я]'
    a = re.findall (regex, string)
    line = ''
    for word in a:
        word = str (word)
        line = line + word + '\n'
    print (line)
    return (a)
def main ():
    f1 = function1 ()
    f2 = function2 (f1)
    f3 = function3 (f1)
    
if __name__ == '__main__':
    main ()
