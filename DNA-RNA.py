class RNA:
    def __init__(self, seq):
        self.seq = seq.upper()
        self.length = len(seq)
        self.complementation = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        supported_signs = "AUGC"
        for i in self.seq:
            if i not in supported_signs:
                raise Exception('This sequence is not supported. Make sure it is RNA sequence')


    def gc(self):
        gc_count = 0
        for i in range(self.length):
            if (self.seq[i] == 'G') or (self.seq[i] == 'C'):
                gc_count += 1
        gc_content = str(round(((gc_count / self.length) * 100), 1)) + str('%')
        return gc_content

    def reverse_complement(self):
        complement_seq = str()
        for i in self.seq:
            complement_seq += self.complementation[i]
        return complement_seq[::-1]


class DNA(RNA):
    def __init__(self, seq):
        self.seq = seq.upper()
        self.length = len(seq)
        self.complementation = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        self.complementation_rna = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        supported_signs = "ATGC"
        for i in self.seq:
            if i not in supported_signs:
                raise Exception('This sequence is not supported. Make sure it is DNA sequence')

    def transcribe(self):
        matrix = self.seq.replace('T', 'U')
        transcript_complement = str()
        for i in matrix:
            transcript_complement += self.complementation_rna[i]
        transcript = RNA(transcript_complement)
        return transcript  # function returns a link to RNA object, wich can be assigned to a variable to use methods
