a, b, c, d = var('a b c d')

M = matrix([[a^2, c^2, -2*a*c],
            [b^2, d^2, -2*b*d],
            [-a*b, -c*d, a*d+b*c]])

I = identity_matrix(3)
M1 = M - (a*d-b*c)*I
M2 = M^2 - (a^2+d^2+2*b*c)*M + (a*d-b*c)^2*I

v1 = vector([2*c, -2*b, a-d])
v2 = vector([0, a-d, c])
v3 = vector([d-a, 0, b])

print("M1 * v1 =")
print((M1 * v1).simplify_full())
print()
print("M2 * v2 =")
print((M2 * v2).simplify_full())
print()
print("M2 * v3 =")
print((M2 * v3).simplify_full())
print()