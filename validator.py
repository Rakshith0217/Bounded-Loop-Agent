ALLOWED_TOOLS = [
    "get_course_info",
    "get_course_schedule"
]

ALLOWED_QUESTIONS = [
    "course_info",
    "schedule"
]


def validate_tool(tool_name):

    if tool_name not in ALLOWED_TOOLS:
        return False

    return True


def validate_question(question_type):

    if question_type not in ALLOWED_QUESTIONS:
        return False

    return True