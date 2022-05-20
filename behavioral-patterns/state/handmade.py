from enum import Enum, auto


class State(Enum):
    """States for a phone call."""

    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(Enum):
    """Its elements call the transition between states."""

    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


if __name__ == "__main__":
    TRIGGER_INDEX = 0
    STATE_INDEX = 1
    # Rules to orquestate the state, what happens when
    # we transition to a particual state.
    # Example. When you are in State.OFF_HOOK,
    # if you Trigger.CALL_DIALED, you pass to
    # State.CONNECTING.
    # If you are State.CONNECED, you have three
    # options to change the state.
    rules = {
        State.OFF_HOOK: [(Trigger.CALL_DIALED, State.CONNECTING)],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED),
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
    }

    # Whe need to know the initial state of the state machine.
    state = State.OFF_HOOK
    # We need the final state of the state machine (some
    # state machines have not a final state, for example
    # a program that learns about the financial market).
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state}")

        # Offer all possible triggers to the user.
        for i in range(len(rules[state])):
            t = rules[state][i][TRIGGER_INDEX]
            print(f"{i}: {t}")

        idx = int(input("Select a trigger:"))
        s = rules[state][idx][STATE_INDEX]
        state = s

    print("We are done using the phone.")
