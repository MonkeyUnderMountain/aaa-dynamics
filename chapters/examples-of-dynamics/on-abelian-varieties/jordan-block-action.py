import numpy as np
import matplotlib.pyplot as plt


M = np.array([[4,0,0],
              [1,4,-4],
              [-2,0,4]])

# # compute and print (M-4)^2
# M1 = M - 4*np.eye(3)
# M2 = M1 @ M1
# print("M2 = (M-4)^2 =")
# print(M2)

# define a function dy on R^2 induced by M
def dy(v):
    v3d = np.array([v[0]+1, 1-v[0], v[1]])
    w3d = M @ v3d
    normizedw3d = 2 * w3d / (w3d[0] + w3d[1]) 
    w = np.array([(normizedw3d[0]-normizedw3d[1])/2, normizedw3d[2]])
    return w

def inverse_dy(v):
    v3d = np.array([v[0]+1, 1-v[0], v[1]])
    w3d = np.linalg.inv(M) @ v3d
    normizedw3d = 2 * w3d / (w3d[0] + w3d[1]) 
    w = np.array([(normizedw3d[0]-normizedw3d[1])/2, normizedw3d[2]])
    return w

def iterate_dy(v, n):
    if n < 0:
        n = -n
        dy_func = inverse_dy
    else:
        dy_func = dy
    for _ in range(n):
        v = dy_func(v)
    return v  # <-- Add this line

# Draw a unit circle on the plane
theta = np.linspace(0, 2 * np.pi, 200)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(circle_x, circle_y, label='Unit Circle')
plt.axis('equal')

# Plot the iterates f^n(v) for v = (x, 0), x in [0.4, 0.7, 1, 1.3, 1.6], n = -3,...,3
xs = [0.3, 0.6, 1, 1.5, 2.5]
n_range = range(-10, 11)
colors = ['r', 'g', 'b', 'm', 'c']

for idx, x in enumerate(xs):
    v = np.array([x, 0])
    points = []
    for n in n_range:
        vn = iterate_dy(v, n)
        points.append(vn)
    points = np.array(points)
    plt.plot(points[:,0], points[:,1], 'o', color=colors[idx], label=f'x={x}')
    for i in range(len(points)-1):
        plt.arrow(points[i,0], points[i,1],
                  points[i+1,0]-points[i,0], points[i+1,1]-points[i,1],
                  shape='full', lw=0.5, length_includes_head=True, head_width=0.05, color=colors[idx])

plt.plot(-1, 0, 'o', color='black', label='(-1, 0)')
plt.axis('off')
plt.savefig("jordan-block-action-plot-product-of-elliptic-curve.png", format="png", dpi=300, bbox_inches='tight', pad_inches=0)
