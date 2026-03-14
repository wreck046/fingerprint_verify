class FingerprintMatcher:

    def similarity(self, t1, t2):

        length = min(len(t1), len(t2))

        match = 0

        for i in range(length):

            if t1[i] == t2[i]:
                match += 1

        return match / length


    def match(self, template, templates, threshold):

        best_score = 0

        for stored in templates:

            score = self.similarity(template, stored)

            if score > best_score:
                best_score = score

        return best_score >= threshold, best_score