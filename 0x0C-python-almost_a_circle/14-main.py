#!/usr/bin/python3

""" 14-main """
import random
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import turtle
#!/usr/bin/python3
""" Check """


file_path = "Square.json"
if os.path.exists(file_path):
    os.remove(file_path)

list_objs = []
for i in range(0, 5):
    list_objs.append(Square(random.randrange(1, 100, 2),
                     random.randrange(1, 100, 2), random.randrange(1, 100, 2)))

Square.save_to_file(list_objs)

list_objs_res = Square.load_from_file()

if list_objs_res is None:
    print("load_from_file doesn't return a list")
    exit(1)

if len(list_objs_res) != len(list_objs):
    print("load_from_file doesn't return a list")
    exit(1)

for i in range(0, len(list_objs)):
    obj = list_objs[i]
    if i >= len(list_objs_res):
        print("load_from_file doesn't return all objects")
        exit(1)

    obj_res = list_objs_res[i]

    if obj_res.id != obj.id:
        print("Square {} not found".format(obj))
        exit(1)

    if obj_res.size != obj.size:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.x != obj.x:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

    if obj_res.y != obj.y:
        print("Square {} doesn't match with the original: {}".format(obj_res, obj))
        exit(1)

print("OK", end="")
