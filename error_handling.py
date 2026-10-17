#Error handling

#Try and except block

try:
    result = 10/0
except ZeroDivisionError:
    print("oops! Tried to divide by 0")

#######
#key/value

fruits = {
    "apple" : 5,
    "banana" : 7,
    "orange" : 3
}

try:
    print(fruits["cherry"])
except KeyError:
    print("Key does not exist in the directory")


#BaseException

text = "This is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("An error occurred while parsing data", e)

#else block
try:
    result = 10/2
except ZeroDivisionError:
    print("Division by zero occurred")
else:
    print("Division successful. Result: ", result)

def divide_number(a,b):
    try:
        result = a/b
        print("result of devision", result)
    except ZeroDivisionError:
        print("Division by zero occurred") 
    except TypeError:
        print("Invalid type for divison")
    except Exception as e:
        print(f"Unexpected error: {e}")

divide_number(10,2)
divide_number(10,"2")   