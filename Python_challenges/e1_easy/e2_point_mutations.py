'''Point Mutations
Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid, in particular DNA. Because nucleic acids are vital to cellular functions, mutations tend to cause a ripple effect throughout the cell. Although mutations are technically mistakes, a very rare mutation may equip the cell with a beneficial attribute. In fact, the macro effects of evolution are attributable to the accumulated result of beneficial microscopic mutations over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken from different genomes with a common ancestor, we get a measure of the minimum number of point mutations that could have occurred on the evolutionary path between the two strands.

This is called the Hamming distance.'''

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^

'''The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length. If you have two sequences of unequal length, you should compute the Hamming distance over the shorter length.'''

'''
P
-compare 2 sequences of equal length to determine how many mutations (different items)
E
from test cases -> class DNA
                -> method hamming_distance -> compares 2 strings -> returns number of different characters
                -> if strings are diff length (ignore additional char from longer string)
                -> assume strings are always uppercase strings
D
strings -> we can iterate and compare strings by char
A
create class `DNA` with string parameter strand
    create method `hamming_distance` with parameter `distance`
        -> compare both strings char by char -> add 1 to var count if chars are diff
        -> stop when of of strings has no chars left
C
'''

class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, distance):
        count = 0
        shortest_strand = min(len(self.strand), len(distance))

        for idx in range(shortest_strand):
            if self.strand[idx] != distance[idx]:
                count += 1

        return count

##LSbot suggestion, try using zip, iterates through 2 strings and stops when the shortest runs out of characters. Make it more condense with a generator

    def hamming_distance(self, other_strand):
        return sum(
            1
            for c1, c2 in zip(self.strand, other_strand)
            if c1!=c2
        )
