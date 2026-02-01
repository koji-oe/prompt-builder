from enum import IntEnum


class PromptPriority(IntEnum):
    SYSTEM = 100
    INSTRUCTION = 200
    CONTEXT = 300
    CODE_CONTEXT = 400
    CONSTRAINT = 500
    PROHIBITED = 600
    OUTPUT_FORMAT = 700
