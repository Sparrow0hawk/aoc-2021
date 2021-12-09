import sys
import importlib


def main(day: str):

    challenge_cls = getattr(importlib.import_module(day), "Challenge")

    challenge_inst = challenge_cls(day=day)

    challenge_inst.get_data()

    challenge_inst.get_result()

    challenge_inst.get_part2()

    return challenge_inst.return_result()


if __name__ == "__main__":

    day = sys.argv[1]

    print(main(day))
