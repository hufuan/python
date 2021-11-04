import sys
sys.path.append('..')
from lib import mod2
import mod1
print("haha1")
teacher = mod2.Teacher("laochen", 50)
student = mod1.Student("Lixi", 9)

teacher.detail()
student.detail()
