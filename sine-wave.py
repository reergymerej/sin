#!/usr/bin/env python3
import math

class Wave:
    def __init__(self, freq, amp, sample_rate):
        # freq - cycles per second
        self.freq = freq
        # amp - height of peaks
        self.amp = amp
        # sample_rate = steps per second
        self.sample_rate = sample_rate
        # phase - radians of cycle
        self.phase = 0
        # what a loser
        self.value = 0
        self.current_step = 0
        self.time = 0
        print(self.describe())

    def describe(self):
        f = self.freq
        a = self.amp
        r = self.sample_rate
        p = f"{round(self.phase, 3)} ({round(self.phase / 2 * math.pi * 10)}%)"
        v = round(self.value * a, 3)

        left = math.ceil((self.value * self.amp) + self.amp)
        right = int(self.amp * 2 - left)
        return f"|{' ' * int(left)}*{' ' * right}|\t{self.time}s"

    def step(self):
        steps_per_cycle = self.sample_rate / self.freq
        degress_per_step = 360 / steps_per_cycle
        radians_per_step = math.radians(degress_per_step)
        self.phase += radians_per_step
        self.current_step += 1
        time_per_step = self.freq / steps_per_cycle
        self.time = round(self.current_step * time_per_step, 2)
        self.phase = self.phase % (2 * math.pi)
        self.value = math.sin(self.phase)
        print(self.describe())

freq = 1
amp = 42
sample_rate = 60
w = Wave(freq, amp, sample_rate)

for i in range(max(sample_rate * 2, 1000)):
    w.step()
