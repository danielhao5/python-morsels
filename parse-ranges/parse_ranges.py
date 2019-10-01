from typing import List
import re

def parse_ranges(ranges:str) -> List[int]:
    range_pattern = r'\d{1,}'

    for _range in ranges.replace(" ", "").split(","):
        numbers = re.findall(range_pattern, _range)

        if len(numbers) == 2:
            start, end = int(numbers[0]), int(numbers[1])

            yield from range(start, end+1)
        else:
            yield int(numbers[0])


if __name__ == "__main__":
    s = "1-2,4-4,8-10"
    print(list(parse_ranges(s)))

    s = '0-0, 4-8, 20, 43-45'
    print(list(parse_ranges(s)))

    s = '0, 4-8, 20->exit, 43-45'
    print(list(parse_ranges(s)))