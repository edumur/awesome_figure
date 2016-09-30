import matplotlib as mpl

# Get this from LaTeX using \the\textwidth
fig_width_pt = 345.
 # Convert pt to inch
pt2inch = 1.0/72.27
# Aesthetic ratio (you could change this)
golden_mean = (np.sqrt(5.0)-1.0)/2.0
# Width in inches
fig_width = fig_width_pt*pt2inch*scale
# Height in inches
fig_height = fig_width*golden_mean
# Final fig size
fig_size = (fig_width, fig_height)

pgf_with_latex = {
    "texsystem"          : "pdflatex",
    "text.usetex"        : True,
    'text.latex.unicode' : True,
    "axes.labelsize"     : 10,
    "text.fontsize"      : 10,
    "legend.fontsize"    : 10,
    "xtick.labelsize"    : 10,
    "ytick.labelsize"    : 10,
    "figure.figsize"     : fig_size,
    "text.latex.preamble": [
        r"\usepackage[utf8x]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[bitstream-charter]{mathdesign}",
        r"\usepackage{siunitx}",
    ]
}

mpl.rcParams.update(pgf_with_latex)
