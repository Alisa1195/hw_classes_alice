seq = str(input()).upper()


class RNA:
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)
        self.complementation = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

    def gc(self):
        gc_count = 0
        for i in range(self.length):
            if (self.seq[i] == 'G') or (self.seq[i] == 'C'):
                gc_count += 1
        gc_content = str(round(((gc_count / self.length) * 100), 1)) + str('%')
        return (gc_content)

    def reverse_complement(self):
        complement_seq = str()
        for i in self.seq:
            complement_seq += self.complementation[i]
        return (complement_seq[::-1])


class DNA(RNA):
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)
        self.complementation = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    def transcribe(self):
        matrix = self.seq.replace('T', 'U')
        transcript_complement = RNA(matrix)
        transcript = transcript_complement.reverse_complement()
        return (transcript[::-1])









