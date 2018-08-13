#!/usr/bin/env python

class MathModel:
    def __init__(self):
        self.t = 0.0

    def init(self):
        """Init internal data structures."""
        return

    def advance(self):
        """Advance the solution one time step."""
        return

    def get_previous_state(self):
        """Return state at the previous time level."""
        return

    def get_current_state(self):
        """Return state at the current time level."""
        return

    def time(self):
        """Return current time in the math. model."""
        return self.t
