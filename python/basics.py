print("hello harru ji")
print("hello hii kese ho")

# collage_name = "LIET"
# print(collage_name)

# a = 10
# print(a)

# 5 = 10
# ! = 10
# $ = 10

# collage = "liet"
# collage_name = "liet"
collage22_name = "liet"

# print(collage_name)
print(collage22_name)




collage22_name="Liet alwar"
print(collage22_name)
print(type(collage22_name))






#indexing
print(collage22_name[0])
print(collage22_name[2])



#slicing
text = "datascience"

print(text[0:4])   # data
print(text[4:7])   # sci
print(text[:4])    # data
print(text[4:])    # science

#OPERATION of atring 
a = "Data"
b = "Science"

print(a + b)
print(a * 3)
print(a[0:2])
print(a.upper())
print(b.lower())



a = "Straße"
b = "STRASSE"

print(a.lower() )       # ❌ False 😐
print(a.casefold()) # ✅ True 😎


#multiple comment 

"""
🔤 Letters bolein, “humein chhota karo”
🙂 lower() aaya, bola “bas itna hi kaafi hai yaaro”
🌍 Par jab aaye special words, thoda scene bigad gaya
💪 casefold() bola, “chinta mat karo, main hoon na!”

😴 lower() simple kaam kare, English tak hi rahe
😎 casefold() duniya bharke letters ko barabar kahe
🧠 Comparison jab ho serious, rule bas ek yaad rakho
🔥 casefold() use karo, aur tension ko bye-bye kaho!
"""
#list 
lst=[1,32,5,4,3,2,6,7,"hello harru","liet"]
print(lst)
print(lst[0])
lst.append(10)
lst.insert(5, 78)

#pop
lst.pop(10)
print(lst)
#remove 
lst.remove(32)
print(lst)

nums = [1, 2, 3]
nums.clear()
print(nums)



#tupple
tpl=(1234,636,5,454,5, "jump")
print(tpl)


#tupple unpacking
tpl=(1,2,3,"hello","false")
print("this is my tuple",tpl)
print("tuple change into list")
lst=list(tpl)
print(lst)
print("list change into tuple")
tpl1=tuple(lst)
#>>>>>>>>>>>>>>>>>>>dictionary

student= {
    "name": "John",
    "class": "10th",
    "branch" : "science",
    "age": "15", 
    "collage22_name":"liet",
    "address":"loni"
}

#name,class,branch,age,collage22_name,address
print("type of dict",type(student))
print("this is my dict",student)
print ("length of dict",len(student))
print(student["name"])
print(student["collage22_name"])
print(student["age"])
print(student["address"])
print(student["branch"])
print(student["class"])


#update ,copy, deep copy
student.get('namw')
print(tpl1)



#Features of dictionary  
#>>>>>>>>>>>>>>>>>>>dictionary
#Features of dictionary


student= {
    "name": "John",
    "class": "10th",
    "branch" : "science",
    "age": "15", 
    "collage22_name":"liet",
    "address":"loni"
}

#name,class,branch,age,collage22_name,address
print("this is my dict",student)
print("type of dict",type(student))
print ("length of dict",len(student))
print(student["name"])
print(student["age"])
print(student["collage22_name"])
print(student["address"])
print(student["class"])
print(student["branch"])




#set
set={1,2,3,4,5,"harru",}
print(type(set))
print(set)



#conditional statements
age = 18
if age >= 18:
    print("Eligible to vote")



#if else
if age >= 18:
    print("Adult")
else:
    print("Minor")
