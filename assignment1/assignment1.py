#task1
def hello():
    return 'Hello!'
print(hello())

#task2
def greet(name):
    return 'Hello'+', '+ name+'!'
print(greet('Jesvika'))

#task3
def calc(arg1,arg2,op = 'multiply'):
    try:
        if op == 'add':
            return arg1 + arg2    
        elif op == 'divide':
            return arg1 / arg2
        elif op == 'multiply':
            return arg1 * arg2
        elif op == 'subtract':
            return arg1 - arg2
        elif op == 'modulo':
            return arg1 % arg2
        elif op == "int_divide":
            return arg1 // arg2
        elif op == "power":
            return arg1 ** arg2
        else:
            return "Not an Operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"     
print(calc(5,6))
print(calc(5,6,"add")) 
print(calc(20,5,"divide"))
print(calc(14,2.0,"multiply"))
print(calc(12.6, 4.4, "subtract"))
print(calc(9,5, "modulo"))
print(calc(10,0,"divide"))
print(calc("first", "second", "multiply"))

#task4
def data_type_conversion(value, type):
    try:
        if type == 'int':
            return int(value)
        elif type == 'float':
            return float(value)
        elif type == 'str':
            return str(value)
        else:
            return 'Unknown datatype'
    except (TypeError, ValueError):
        return f"You can't convert {value} into a {type}."
print(data_type_conversion("110", "int"))
print(data_type_conversion("5.5", "float"))
print(data_type_conversion(7,"float"))
print(data_type_conversion(91.1,"str"))
print(data_type_conversion("banana", "int"))

#task5
def grade(*args):
    try:
        avg = sum(args)/len(args)
        if avg >= 90:
            return 'A'
        elif avg >=80 and avg<=89 :
            return 'B'
        elif avg >=70 and avg<=79 :
            return 'C'
        elif avg >=60 and avg<=69 :
            return 'D'
        elif avg < 60:
            return 'F'
        else:
            return 'Invalid data'
    except (TypeError, ValueError, ZeroDivisionError):
        return 'Invalid data was provided.'
print(grade(75,85,95))
print(grade("three", "blind", "mice"))

#task6
def repeat(stringVal, count):
    result = ""
    for i in range(count):
        result += stringVal
    return result
print(repeat("up,", 4))
        
#task7
def student_scores(cls, **kwargs):
    try:
        if cls == "best":
            return max(kwargs, key=kwargs.get)
        elif cls == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid"
    except (TypeError, ValueError, ZeroDivisionError):
        return "Invalid data was provided."
print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))

#task8
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        else:
            if word.lower() in little_words:
                words[i] = word.lower()         
            else:
                words[i] = word.capitalize()   
    return " ".join(words)
print(titleize("war and peace"))
print(titleize("a separate peace")) 
print(titleize("after on"))
  
#task9      
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
print(hangman("difficulty","ic"))

#task10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result_words = []
    for word in words:
        if word[0] in vowels:
            result_words.append(word + "ay")
            continue
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i:i+2] == "qu":
                i += 2
            elif word[i] in vowels:
                break
            else:
                i += 1
        result_words.append(word[i:] + word[:i] + "ay")
    return " ".join(result_words)
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))

        