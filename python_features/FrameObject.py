import sys
import dis
from pprint import pprint


def get_frame_n_instructions():
    local_var = "local_var"
    frame = sys._getframe()
    instruction = frame.f_lasti
    return frame, instruction


frame, instruction = get_frame_n_instructions()
print("\nПеременные фрейма")
pprint(frame.f_locals)
print(f"\nКоличество глобальных переменных: {len(frame.f_globals)}")

