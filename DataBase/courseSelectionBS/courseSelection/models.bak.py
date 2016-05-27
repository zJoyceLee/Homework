from .inspectdb import *

del Colleges._meta.managed
Colleges.__str__= lambda self: str(self.name)

Courses.college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name', blank=True, null=True)

del Opencourses._meta.managed
Opencourses.course = models.ForeignKey(Courses, models.CASCADE)
Opencourses.teacher = models.ForeignKey('Teachers', models.CASCADE)

del Sc._meta.managed
del Sc.sc_semester
del Sc.sc_course
del Sc.sc_teacher
del Sc.sc_class_time
Sc.SCsemester = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_semester')
Sc.SCcourse = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_courses')
Sc.SCteacher = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_teacher')
Sc.SCclass_time = models.ForeignKey(Opencourses, models.CASCADE, related_name='sc_class_time')
Sc.student = models.ForeignKey('Students', models.CASCADE)
print(dir(Sc))

Sc._meta.unique_together = ['SCsemester', 'SCcourse', 'SCteacher', 'SCclass_time', 'student']

del Students._meta.managed
Students.college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name', blank=True, null=True)

del Teachers._meta.managed
Teachers.college_name = models.ForeignKey(Colleges, models.CASCADE, db_column='college_name')

