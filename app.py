from validator import *
from tools import *
from trace_logger import TraceLogger

MAX_STEPS = 1


trace = TraceLogger()


def university_agent(question_type, course_code=None):

    trace.log("User Request Received")

    step = 0
    tool = None
    result = None

    while step < MAX_STEPS:

        step += 1
        trace.log(f"Step {step}")

        if step == 1:
            if not validate_question(question_type):
                trace.log("Rejected : Invalid Question")
                return "Sorry, I cannot answer that."

            if question_type == "course_info":
                tool = "get_course_info"
            elif question_type == "schedule":
                tool = "get_course_schedule"
            elif question_type in ("all_course_info", "all_courses"):
                tool = "get_all_course_info"
            else:
                return "Unknown"

            trace.log("Reasoning : Selected Tool -> " + tool)

        elif step == 2:
            if not validate_tool(tool):
                trace.log("Validator Blocked Tool")
                return "Tool Blocked"

            trace.log("Preparing Execution")

        elif step == 3:
            if tool == "get_course_info" and not course_code:
                trace.log("No Course Code Provided")
                return "Please provide a course code."

            trace.log("Validating Inputs")

        elif step == 4:
            trace.log("Executing Tool")
            if tool == "get_course_info":
                result = get_course_info(course_code)
            elif tool == "get_course_schedule":
                result = get_course_schedule(course_code)
            else:
                result = get_all_course_info()

        elif step == 5:
            if tool != "get_all_course_info" and result is None:
                trace.log("Course Not Found")
                return "Course does not exist."

            trace.log("Execution Finished")
            return result

    trace.log("Maximum steps exceeded")
    return "Agent stopped: Maximum step limit reached."

def main():
    import sys

    args = sys.argv[1:]
    if len(args) == 2:
        question_type, course_code = args
    elif len(args) == 1:
        question_type = args[0]
        course_code = None
    else:
        question_type = input("Enter question type (course_info/schedule/all_course_info/all_courses): ").strip()
        if question_type in ("all_course_info", "all_courses"):
            course_code = None
        else:
            course_code = input("Enter course code (AI101/PY201/DB301): ").strip()

    result = university_agent(question_type, course_code)
    print(result)
    trace.save("traces/trace1_success.txt")


if __name__ == "__main__":
    main()