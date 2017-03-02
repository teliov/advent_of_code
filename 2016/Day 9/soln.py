import re

def decompress_sequence(sequence):
    pattern = '\((\d+)x(\d+)\)'
    decompressed = ''
    initial_sequence = sequence
    while len(initial_sequence) > 0:
        match = re.search(pattern, initial_sequence)
        if not match:
            decompressed += initial_sequence
            initial_sequence = ''
        else:
            compressed_length = int(match.group(1))
            decompress_factor = int(match.group(2))
            uncompressed_seq = initial_sequence[:match.start()]
            decompressed += uncompressed_seq
            compressed_seq = initial_sequence[match.end():]
            will_uncompress = compressed_seq[:compressed_length]
            initial_sequence = compressed_seq[compressed_length:]
            decompressed += will_uncompress*decompress_factor

    return decompressed

def get_file_decompressed_length(sequences):
    length = 0
    for sequence in sequences:
        sequence = sequence.strip()
        decompressed = decompress_sequence(sequence)
        length += len(decompressed)

    return length

def get_file_decompressed_length_pt2(sequences):
    length = 0
    for sequence in sequences:
        sequence = sequence.strip()
        length += decompress_sequence_pt2(sequence)

    return length

def decompress_sequence_pt2(sequence):
    pattern = '\((\d+)x(\d+)\)'
    length = 0
    initial_sequence = sequence
    while len(initial_sequence) >0:
        match = re.search(pattern, initial_sequence)
        if not match:
            length += len(initial_sequence)
            initial_sequence = ''
        else:
            compressed_length = int(match.group(1))
            decompress_factor = int(match.group(2))
            length += len(initial_sequence[:match.start()])
            compressed_seq = initial_sequence[match.end():]
            will_uncompress = compressed_seq[:compressed_length]
            initial_sequence = compressed_seq[compressed_length:]
            length += decompress_factor * decompress_sequence_pt2(will_uncompress)

    return length


if __name__ == "__main__":
    input_file = open("input.txt", 'r')
    sequences = input_file.readlines()
    # sequences = [
    #   'A(1x5)BC',
    #   '(3x3)XYZ',
    #   'A(2x2)BCD(2x2)EFG',
    #   '(6x1)(1x3)A',
    #   'X(8x2)(3x3)ABCY',
    #   '(27x12)(20x12)(13x14)(7x10)(1x12)A',
    #   '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    # ]
    decompressed_length = get_file_decompressed_length(sequences)
    print "decompressed file length is %d" % decompressed_length
    
    decompressed_length_pt2= get_file_decompressed_length_pt2(sequences)
    print "decompressed file length for pt2 is %d" % decompressed_length_pt2
