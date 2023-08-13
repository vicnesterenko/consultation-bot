from .parse_json import parse
import os


def vaginal(choose_sex_type, choose_lub):
    msg_id = "vaginal.1"
    path = os.path.join(os.getcwd(), "bot/type_sex/data_vaginal.json")

    DEFAULT_ACTIONS = {
        "default-1": (choose_sex_type, choose_lub),
        "default-2": (vaginal, *(choose_sex_type, choose_lub)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)
