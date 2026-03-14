import time

class LivenessDetector:

    MIN_VARIATION = 0.02

    def check(self, previous_template, new_template):

        if not previous_template:
            return True

        length = min(len(previous_template), len(new_template))

        diff = sum(
            1 for i in range(length)
            if previous_template[i] != new_template[i]
        )

        variation = diff / length

        return variation > self.MIN_VARIATION