class Course:
	# The Course class is used to store course related information, this would include: 
	# course code, title, credit points, prerequisites, available semesters 
	# (takes a list of semesters as its value, 
	# e.g., [S1] indicades S1 only, [S2] indicates S2 only, and [S1,S2] means available in both semesters). 
	# For instance, a sample list of courses, their information including 
	# name, course code, pre-requisite and available semesters are available in your enrolment online systems as well as course guides.
	def __init__():
		pass

class Program:
	# This is the class of an academic program, like the Bachelor of Computer Science (BP094) and Bachelor of Software Engineering (BP096). 
	# Each program consists of program code, credit points 
	# (e.g.,BP094 requires completion of 288 credit points upon graduation),
	# a list of core courses (mandatory requirements) and a list of programe lective courses.
	# In this system prototype, to make it simple, we can ignore the possibilities of a university elective, 
	# i.e., a program can only containcore and elective courses.
	def __init__():
		pass

class Semester:
	# The Semester class contains its identity, e.g., S22021, and a list of course offerings in the semester.
	# For each course offering, it also contains the maximum student number 
	# (aka. Cap, assume each course only allows a certain number of students to enrol),
	# and a list of enrolled students
	# (i.e., the list of currently enrolled students). 
	# The Semester class should provide constructor, string methods, getter and setters, as well as methods to add or remove a student from a course offering. 
	# When adding a student into an offering, the system should first check whether the cap has been reached, in which case,the student cannot enrol.
	def __init__():
		pass

class Student:
	# The Student class stores the information of a student 
	# (e.g., name, student id, D.O.B, etc), 
	# program code (which program he/she is currently at), 
	# the academic history, current enrollments, and a study plan. 
	# Assume a student can only have one active program. 
	# The academic history stores a list of courses that a student has attempted before, as well his/her mark and grade of the attempted course. 
	# Current enrollment is a list of existing offerings 
	# (course code, semester, year) that he/she is currently enrolled in, and a study plan is a list of tuples 
	# (course code, semester, year) indicating the future plan for completing the remaining studies towards graduation
	# (i.e.,the study plan excludes the courses that the student has already passed, and courses that he is currently enrolled in.).
	# The Student class should provide constructor, string methods, getter ands etters, as well as methods to amend the academic history and study plan.
	# - Once the official marks of the current enrollments are released, they should be moved to his/her academic history.
	# - You might also want to include a status of the study plan. 
	# For instance:
	# - If a student failed a course, the status of the study plan should indicate that it needs to be adjusted to reflect the updated plan on remainingstudies.
	# - Similarly,if a student enrol in or unenroll from a course offering, this status should also be updated to reflect adjustment is needed on the studyplan.
	# - When a new study plan is generated, the status of the study plan should indicate that the study plan is up-to-date.
	def __init__():
		pass