from data import courses, schedules

def get_course_info(course_code):

    return courses.get(course_code)

def get_course_schedule(course_code):

    return schedules.get(course_code)

def get_all_course_info():

    return courses