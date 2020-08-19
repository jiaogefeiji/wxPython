import matplotlib.pyplot as plt

fig, (ax2) = plt.subplots(1)

ax2.set_xscale("log")
ax2.set_yscale("log")

#ax2.xlabel('Pr/nC18')
#ax2.ylabel('Pr/nC17')
ax2.set_adjustable("datalim")
ax2.plot([1, 3, 10], [1, 9, 100], "o-")
ax2.set_xlim(1e-1, 1e2)
ax2.set_ylim(1e-1, 1e2)
ax2.set_aspect(1)
ax2.grid()
ax2.set_title("Pr/nC18")

plt.show()