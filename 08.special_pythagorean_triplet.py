'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc'''


def pyth_triplets(n):
    for c in xrange(5, n+1):  # minimum value of c is 5 so starting from that
        c2 = c*c              # time saver to have a square of c already
        a = a2 = 1            # starting from a = 1 and
        b = c - 1             # b = whatever the value of c, towards a
        b2 = b*b
        while a < b:
            a2_b2 = a2 + b2     # get the addition of squared values of a and b in a variable
            if a2_b2 == c2:     # if a2 + b2 = c2 Then It's a pythagorean triplet
                yield a, b, c   # Store the value as generator and
                a += 1          # go for next triplet checking
                a2 = a*a        # preparing values for next triplet checking
                b -= 1
                b2 = b*b
            elif a2_b2 < c2:    # If that was not a triplet but a and b square addition is less than c square then
                a += 1          # increment the a values and
                a2 = a*a        # have square of a with me
            else:
                b -= 1          # if a and b square addition greater than c sqaure then decrement the b value
                b2 = b*b        # have square of b with me


triplet_list = list(pyth_triplets(425))
for ele in triplet_list:
    if (ele[0]+ele[1]+ele[2]) == 1000:
        print 'Product of abc =', ele[0]*ele[1]*ele[2]

# Answer = 31875000
