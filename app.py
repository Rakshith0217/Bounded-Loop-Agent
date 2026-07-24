from validator import *
from tools import *
from trace_logger import TraceLogger

trace = TraceLogger()


def university_agent(question_type, course_code):

    trace.log("User Request Received")

    if not validate_question(question_type):

        trace.log("Rejected : Invalid Question")

        return "Sorry, I cannot answer that."

    if question_type == "course_info":

        tool = "get_course_info"

    elif question_type == "schedule":

        tool = "get_course_schedule"

    else:

        return "Unknown"

    trace.log("Reasoning : Selected Tool -> " + tool)

    if not validate_tool(tool):

        trace.log("Validator Blocked Tool")

        return "Tool Blocked"

    trace.log("Executing Tool")

    if tool == "get_course_info":

        result = get_course_info(course_code)

    else:

        result = get_course_schedule(course_code)

    if result is None:

        trace.log("Course Not Found")

        return "Course does not exist."

    trace.log("Execution Finished")

    return result


print(university_agent("course_info", "AI101"))
print(university_agent("schedule", "PY201"))
print(university_agent("schedule", "DB301"))
print(university_agent("course_info", "PY201"))
print(university_agent("course_info", "DB301"))

trace.save("traces/trace1_success.txt")