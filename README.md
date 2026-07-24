# Bounded-Loop-Agent
# University FAQ Agent (Bounded Agent)

## Overview

The University FAQ Agent is a simple bounded AI agent developed for the PGDAIML203 Agentic AI & Autonomous Systems assignment.

The agent answers frequently asked questions about university courses using synthetic data. It is a bounded agent because it only allows predefined questions and predefined tools. Any invalid request is rejected before execution.

---

## Features

- Uses synthetic university data (no real student data).
- Two read-only tools:
  - Get course information
  - Get course schedule
- Input validation before tool execution.
- Trace logging for every request.
- Demonstrates successful and failure cases.
- Includes a deliberately invalid tool call.

---

## Project Structure

```
University-FAQ-Agent/
│
├── app.py
├── data.py
├── tools.py
├── validator.py
├── trace_logger.py
├── README.md
├── requirements.txt
│
└── traces/
      trace1_success.txt
      trace2_unknown_course.txt
      trace3_invalid_question.txt
      trace4_schedule.txt
      trace5_invalid_tool.txt
```

---

## Synthetic Data

The project uses two dictionaries as a fake university database.

- Course information
- Course schedules

No real student or university data is used.

---

## Read-Only Tools

The agent provides two tools.

### Tool 1

```
get_course_info(course_code)
```

Returns course details.

### Tool 2

```
get_course_schedule(course_code)
```

Returns course schedule.

These tools only read data and never modify it.

---

## Bounded Agent

The validator only allows:

### Allowed Questions

- course_info
- schedule

### Allowed Tools

- get_course_info
- get_course_schedule

Any other request is rejected before execution.

---

## Trace Files

The project generates the following traces.

| Trace | Description |
|--------|-------------|
| trace1_success.txt | Successful course information lookup |
| trace2_unknown_course.txt | Course not found |
| trace3_invalid_question.txt | Invalid question rejected |
| trace4_schedule.txt | Successful schedule lookup |
| trace5_invalid_tool.txt | Invalid tool blocked by validator |

---

## Layer Mapping

### Control Layer

Receives the user request and controls the workflow.

File:

```
app.py
```

---

### Reasoning Layer

Chooses which tool should be executed.

File:

```
app.py
```

---

### Execution Layer

Executes the selected read-only tool.

File:

```
tools.py
```

---

### State Layer

Stores the synthetic university data.

File:

```
data.py
```

---

## How to Run

1. Install Python 3.10 or above.

2. Clone or download the project.

3. Open the project folder.

4. Run:

```
python app.py
```

5. Check the generated trace files inside the `traces` folder.

---

## Example

Input

```
course_info AI101
```

Output

```
{
    "name": "Introduction to Artificial Intelligence",
    "credits": 4,
    "faculty": "Dr. Smith"
}
```

---

## Technologies Used

- Python 3
- Dictionaries (Synthetic Database)
- Functions
- Input Validation
- Trace Logging

---

## Assignment Requirements Covered

- Synthetic data
- Two read-only tools
- Bounded agent
- Input validation
- Trace analysis
- Invalid tool handling
- Layer mapping