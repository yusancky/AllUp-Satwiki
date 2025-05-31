# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.


def build_switch(data_map):
    result = "{{#switch:{{{" + data_map["switch_key"] + "|}}}"
    for data_key, data_value in data_map.items():
        if data_key == "switch_key":
            continue
        if isinstance(data_value, str):
            result += f"|{data_key}={data_value}"
        elif isinstance(data_value, dict):
            result += f"|{data_key}={build_switch(data_value)}"
        else:
            raise TypeError(
                f"A string or a dictionary is required, not '{type(data_value)}'."
            )
    result += "}}"
    return result
