seq = str(input()).upper()


class RNA:
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)

    def gc(self):
        self.gc_count = 0
        for i in range(self.length):
            if (self.seq[i] == 'G') or (self.seq[i] == 'C'):
                self.gc_count += 1
        self.gc_content = str(int((self.gc_count / self.length) * 100)) + str('%')
        return (self.gc_content)

    def reverse_complement(self):
        self.complementation = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        self.complement_seq = str()
        for i in self.seq:
            self.complement_seq += self.complementation[i]
        return (self.complement_seq)


class DNA:
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)

    def gc(self):
        self.gc_count = 0
        for i in range(self.length):
            if (self.seq[i] == 'G') or (self.seq[i] == 'C'):
                self.gc_count += 1
        self.gc_content = str(int((self.gc_count / self.length) * 100)) + str('%')
        return (self.gc_content)

    def reverse_complement(self):
        self.complementation = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        self.complement_seq = str()
        for i in self.seq:
            self.complement_seq += self.complementation[i]
        return (self.complement_seq)

    def transcribe(self):
        self.matrix = self.seq.replace('T', 'U')
        self.transcript_complement = RNA(self.matrix)
        self.transcript = self.transcript_complement.reverse_complement()
        return (self.transcript)









