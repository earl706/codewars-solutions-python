"""
4 KYU

Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|
has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|  
|d e f|  
|g h i|  
the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|  
Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

LINK:https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

"""

def determinant(matrix):
    if len(matrix) > 2:
        if len(matrix[0]) - 1 != 2:
            majors = matrix[0]
            multiplicands = []
            x = 0
            for iteration in range(len(majors)):
                for row in matrix[1:]:
                    y = 0
                    temp_array = []
                    for number in row:
                        if x != y:
                            temp_array.append(number)
                        y += 1
                    multiplicands.append(temp_array)
                x += 1
            final_multiplicands = []
            for iteration in range(len(multiplicands[0]) + 1):
                temp_array = []
                if iteration < len(multiplicands[0]):
                    for array in range((iteration % len(multiplicands[0])) * len(multiplicands[0]), (iteration % len(multiplicands[0])) * len(multiplicands[0]) + len(multiplicands[0])):
                        temp_array.append(multiplicands[array])
                else:
                    for array in range(iteration * iteration, (iteration * iteration) + iteration):
                        temp_array.append(multiplicands[array])
                final_multiplicands.append(temp_array)
            summation = 0
            x = 0
            for number in majors:
                if x % 2 == 0:
                    summation += number * determinant(final_multiplicands[x])
                else:
                    summation -= number * determinant(final_multiplicands[x])
                x += 1
            return summation
        else:
            majors = matrix[0]
            multiplicands = [[], [], []]
            for row in matrix[1:]:
                y = 0
                for number in row:
                    for iteration in range(len(majors)):
                        if y != iteration:
                            multiplicands[iteration].append(number)
                    y += 1
            x = 0
            for numbers in multiplicands:
                majors[x] *= (numbers[0]*numbers[-1]) - (numbers[1]*numbers[2])
                x += 1
            return majors[0] - majors[1] + majors[2]
    else:
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            return 0
          
  #BETTER SOLUTION
  def determinant(m):
    a = 0
    if len(m) == 1:
        a = m[0][0]
    else:
        for n in xrange(len(m)):
            if (n + 1) % 2 == 0:
                a -= m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
            else:
                a += m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
                
    return a
