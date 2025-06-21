# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.


def build_switch(data_map: dict[str, object]) -> str:
    match data_map:
        case {"switch_key": str(switch_key), **rest}:
            parts = [f"{{{{#switch:{{{{{switch_key}|}}}}}"]
            for data_key, data_value in rest.items():
                match data_value:
                    case str(value):
                        parts.append(f"|{data_key}={value}")
                    case dict() as subdict:
                        parts.append(f"|{data_key}={build_switch(subdict)}")
                    case _:
                        raise TypeError(
                            f"Value for key '{data_key}' must be str or dict, not {type(data_value).__name__}."
                        )
            parts.append("}}")
            return "".join(parts)
        case _:
            raise ValueError("'switch_key' must be present and be a string.")
