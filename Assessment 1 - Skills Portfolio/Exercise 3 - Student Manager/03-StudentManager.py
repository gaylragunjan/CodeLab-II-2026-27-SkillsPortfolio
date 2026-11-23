import os
import json

# same path helper we've been using

main_directory = os.path.dirname(os.path.abspath(__file__))

def path(filename): 
    return os.path.join(main_directory, "Assets", filename)

# list that will hold every student

students = [] 

# opens .txt file in read-only mode

with open(path("studentMarks.txt"), "r") as f:
    f.readline()
    for line in f:
        v = line.strip().split(",") 
        if len(v) == 6:
            students.append({
                "number": int(v[0]),
                "name": v[1],
                "marks": [int(v[2]), int(v[3]), int(v[4])],
                "exam": int(v[5]),
            })

# creates a .json file in write mode

with open(path("studentMarks.json"), "w") as f:
    json.dump(students, f, indent=2) # puts our student list in the (f)ile with indentation!