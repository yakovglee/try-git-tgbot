import re


def parse_message(raw_message: str):
    regexp_result = re.search(r"(\d+)(?:\s*,\s*(\d+))?", raw_message)

    if regexp_result:
        pwr1 = int(regexp_result.group(1))

        pwr2_raw = regexp_result.group(2)
        pwr2 = int(pwr2_raw) if pwr2_raw is not None else 0
        return pwr1, pwr2

    return 0, 0
