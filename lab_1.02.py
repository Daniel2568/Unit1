
'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2               9
b   2/3                     0.6666666666
c   2.0 * 1.5               3.0
d   (2 + 3) * 10            50
e   5.0 // 2                2.0
f   5.0 % 2                 1.0

Section 2
    Input                   Output                          Did it do something unexpected?
a   a
b   'a'

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'
b   'a' + 'b'

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'
b   'a' * 2

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      float                       1.0                                 1.0     
c   10/2                        integer                     5                                   2.0
d   10%2                        integer                     5                                   0
e   2 ** 3                      string                      "stynx error"                       8
f   (2+5)*3                     Integer                     25                                  25
g   2 + 5 * 3                   integer                     17                                  17
h   'ab' + '12' + '3'           string                      ?                                   ab123
i   x                           Integer                     x                                   'x' is not defined
j   "ab" + "cd"                 string                      ?                                   'abcd'
k   'abc' * 2                   string                      abcabc                              'abcabc'
l   '1'*2 + '2' * 3             string                      ?                                   '11222'
m   1 * 2 + '3' * 2             
n   'A' ** 2
o   'bc' % 2
p   'bc' / 2

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''