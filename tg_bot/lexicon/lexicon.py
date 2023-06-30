from typing import Optional
import logging

lexicon = {
    "en": {
        "first_hello": "Hello, I am scheduler bot that will help "
        + "you gain healthy based productivity. "
        + "Please enter your start and end of the day"
        + "time in the following format:\n"
        + "\t```[start_time]-[end_time]```"
        + "\nFor example, 13:00-2:00 or 1:00PM-2:00AM",
        "hello": "Hello, how can I help you?",
        "retry_first_hello": "Please enter correctly in the following format:"
        + "\t```[start_time]-[end_time]```"
        + "\nFor example, 13:00-2:00 or 1:00PM-2:00AM",
        "write_success": "Successfully saved!",
        "add_task": """To add task, please, enter task name or full info about task in the following format:\n\t
        ```[task_name]-[duration (in minutes)]-[importance]-[complexity]-[start_time]-[date]```\n
        start_time and date are optional""",
        "get_duration_task": """Cool, now enter duration of task, please""",
        "get_complexity_task": "Please, enter complexity of task",
        "get_importance_task": "Please, enter importance of task",
        "get_start_time_task": """Now, write time is the following format:\n\t
        13:00 or 1:00PM\n
        Or enter 'no' if no specific start time""",
        "get_date_task": """Please, enter date in the following format:\n\t
        dd/mm/yyyy\n
        For example, 1/1/1970\n
        Or enter 'no' if no specific date""",
        "add_event": """To add event, please, enter event name""",
        "event_start_time": "Now, please, enter start time of event",
        "event_duration": f"Please, enter duration of the event up to {24 * 60}",
        "event_date": "Please, enter date of event. If no specific date, enter 'no'",
        "event_repeat_each_number": "Please, enter each number",
        "event_repeat_each_argument": "Please, enter each argument",
        "event_repeat_number_of_repetitions": "Please, enter number of repetitions",
        "mark_history": "Choose active task. If no task, make task using '/add_task'",
        "ask_history": """Please, enter history in the following format:\n\t
        [start_time]-[end_time]-[is_done (true or false)]""",
        # retries
        "retry_int": "Please, enter integer",
        "retry_optional_time": "Please, enter time in the specific following format:\n\t13:00 or 1:00PM\nOr enter 'no' if no specific start time",
        "retry_optional_date": """Please, enter date in the specific following format:\n\t
        dd/mm/yyyy\n
        For example, 1/1/1970\n
        Or enter 'no' if no specific date""",
        "retry_event": """Please, enter event in the following format:\n\t
        [event_name]-[start_time]-[duration (in minutes)]-[Number] [day | {day of week (e.g. Sunday)} | month] [Number of events]""",
        "retry_history": """Please, enter history in the following format:\n\t
        [start_time]-[end_time]-[is_done (true or false)]""",
        "retry_time": """Please, enter time in the following format:\n\t
        '11:00' or '1:00AM'""",
        "retry_trouble": "Sorry, unexpected error. Please, try again",
        "error": "Got unexpected error: \n\t{}",
    }
}


def get_lexicon_with_argument(message_args: str, *args) -> Optional[str]:
    if not isinstance(message_args, str):
        logging.error("Got unexpected type in lexicon")
        return ""

    if message_args not in lexicon["en"].keys():
        logging.error("Got unexpected argument in lexicon: %s", message_args)
        return ""

    try:
        return lexicon["en"][message_args].format(*args)
    except IndexError:
        return ""
