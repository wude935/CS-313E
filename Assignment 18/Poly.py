#  File: Poly.py

#  Description: This program adds and multiplies polynomials

#  Student Name: Derek Wu

#  Student UT EID:

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/22/19

class Link (object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'


class LinkedList (object):
    def __init__(self):
        self.first = None
        self.length = 0

    # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        current = self.first
        previous = self.first
        new_link = Link(coeff, exp)
        self.length += 1
        # creates new a polynomial
        if current == None:
            # print('exp created!')
            self.first = new_link
            return

        else:
            # if the new_link.exp is larger than current exp add new_link exp to the front
            if new_link.exp > current.exp:
                # print('inserted begininng')
                new_link.next = self.first
                self.first = new_link
            else:
                # traversals through linked list until new_link's exponent is larger than current's exponent
                while new_link.exp < current.exp and current.next != None:
                    previous = current
                    current = current.next
                # if insertion occurs at the end of the linked list, then change current.next to new_link
                if current.next == None:
                    # print('inserted end')
                    current.next = new_link
                # else insert the link before current link
                else:
                    # print('inserted before')
                    previous.next = new_link
                    new_link.next = current

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        p_current = p.first
        # makes output a deep copy of self
        output = LinkedList()
        self_current = self.first
        for i in range(self.length):
            output.insert_in_order(self_current.coeff, self_current.exp)
            self_current = self_current.next

        for i in range(p.length):
            output_current = output.first
            for k in range(output.length):
                # if the polynomials have the same exponents add them together
                if p_current.exp == output_current.exp:
                    output_current.coeff = output_current.coeff + p_current.coeff
                    break
                # if you reach the end of p, insert the exponent order in the original polynomial
                elif output_current.next == None:
                    output.insert_in_order(p_current.coeff, p_current.exp)
                output_current = output_current.next

            p_current = p_current.next

        return output

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        p_current = p.first
        output = LinkedList()
        # makes output a deep copy of self
        copy = LinkedList()
        self_current = self.first
        for i in range(self.length):
            copy.insert_in_order(self_current.coeff, self_current.exp)
            self_current = self_current.next

        for i in range(copy.length):
            copy_current = copy.first
            temp =  LinkedList()
            # distrbute p_current to all exponents in polynomial copy
            for k in range(copy.length):
                new_coeff = p_current.coeff * copy_current.coeff
                new_exp = p_current.exp +  copy_current.exp 
                temp.insert_in_order(new_coeff, new_exp)
                copy_current = copy_current.next
            # copys output if it is empty
            if output.length == 0:
                temp_current = temp.first
                for i in range(temp.length):
                    output.insert_in_order(temp_current.coeff, temp_current.exp)
                    temp_current = temp_current.next
            # otherwise adds output
            else:
                output = output.add(temp)
            p_current = p_current.next
        return output
            

    # create a string representation of the polynomial
    def __str__(self):
        current = self.first
        string = ''

        for i in range(self.length):
            string += str(current) + ' + '
            current = current.next
        string = string.rstrip(' + ')
        return string


def main():
        # open file poly.txt for reading
    inf = open("poly.txt", "r")

    # create polynomial p
    p = LinkedList()

    line = int(inf.readline().rstrip("\n"))

    for i in range(line):
        next_line = inf.readline().rstrip('\n').split()
        coeff = int(next_line[0])
        exp = int(next_line[1])
        p.insert_in_order(coeff, exp)

    # create polynomial q
    inf.readline()

    q = LinkedList()

    line = int(inf.readline().rstrip("\n"))

    for i in range(line):
        next_line = inf.readline().rstrip('\n').split()
        coeff = int(next_line[0])
        exp = int(next_line[1])
        q.insert_in_order(coeff, exp)

    # get sum of p and q and print sum
    print('Sum:', q.add(p))
    print()

    # get product of p and q and print product
    print("Product:", q.mult(p))


if __name__ == "__main__":
    main()
