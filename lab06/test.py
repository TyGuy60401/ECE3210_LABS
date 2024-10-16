import matplotlib.pyplot as plt

# Create a figure
# fig = plt.figure(figsize=(6, 4))
fig = plt.figure()

# Top left subplot (at position (0, 0), size 1x1)
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax1.set_title('Top Left')

# Top right subplot (at position (0, 1), size 1x1)
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2.set_title('Top Right')

# Bottom subplot (at position (1, 0), spanning both columns, size 1x2)
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
ax3.set_title('Bottom')

# Adjust layout for clarity
plt.tight_layout()
plt.show()
