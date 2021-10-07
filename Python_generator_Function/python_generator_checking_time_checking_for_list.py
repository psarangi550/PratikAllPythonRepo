import random
import time
names=["pratik","rika","papali","pupuli","puja","Rohith","priya"]
subjects=["django","flask","heroku","postgres","git"]
# num=int(input("Enter the Number of student list"))
def student_list(num):
    students=[]
    for x in range(num):
        student={"id":x,"name":random.choice(names),"subj":random.choice(subjects)}
        time.sleep(1)
        students.append(student)
    return students
t1=time.time()
for x in student_list(100):
    print(x)
t2=time.time()
# print(l1)

print(t2-t1)