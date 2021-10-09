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
	# TheStudentclassstorestheinformationofastudent(e.g.,name,studentid,D.O.B,etc),programcode(which program he/she is currently at), the academichistory, current enrollments, and a study plan.Assumeastudentcanonlyhaveoneactiveprogram.Theacademichistorystoresalistofcoursesthatastudenthasattemptedbefore,aswellhis/hermarkandgradeoftheattemptedcourse.Currentenrollmentisalistofexistingofferings(coursecode,semester,year)thathe/sheiscurrentlyenrolledin,andastudyplanisalistoftuples(coursecode,semester,year)indicatingthefutureplanforcompletingtheremainingstudiestowardsgraduation(i.e.,thestudyplanexcludesthecoursesthatthestudenthasalreadypassed,andcourses that he is currently enrolled in.).TheStudentclassshouldprovideconstructor,stringmethods,getterandsetters,aswellasmethodstoamend the academic history and study plan.Note:-Oncetheofficialmarksofthecurrentenrollmentsarereleased,theyshouldbemovedtohis/heracademic history.-You might also want to include a status of the studyplan. For instance:-Ifastudentfailedacourse,thestatusofthestudyplanshouldindicatethatitneedstobeadjusted to reflect the updated plan on remainingstudies.Page2of9- Similarly,ifastudentenrolinorunenrollfromacourseoffering,thisstatusshouldalsobeupdated to reflect adjustment is needed on the studyplan.-Whenanewstudyplanisgenerated,thestatusofthestudyplanshouldindicatethatthestudy plan is up-to-date.
	def __init__():
		pass