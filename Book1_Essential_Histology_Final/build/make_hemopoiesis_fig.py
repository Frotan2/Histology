#!/usr/bin/env python3
"""Generate the Hemopoiesis lineage diagram (Chapter 10)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6.2), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 62); ax.axis('off')

NAVY='#1F3A5F'; BLUE='#2C6FAD'; RED='#B03A3A'; GREEN='#2E7D5B'; ORANGE='#C6862B'; PURPLE='#6B4C9A'; GREY='#5A6472'

def box(x, y, w, h, label, sub, ec, fc):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.35,rounding_size=0.8",
                                linewidth=1.6, edgecolor=ec, facecolor=fc))
    ax.text(x+w/2, y+h*0.62, label, ha='center', va='center', fontsize=8.6, fontweight='bold', color='#12202F')
    if sub:
        ax.text(x+w/2, y+h*0.24, sub, ha='center', va='center', fontsize=6.9, color='#3A4654')

def arrow(x1, y1, x2, y2, color=GREY):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=11,
                                 linewidth=1.3, color=color, shrinkA=1, shrinkB=1))

ax.text(50, 59.2, 'Hemopoiesis: the Stem-Cell Hierarchy', ha='center', fontsize=13.5,
        fontweight='bold', color=NAVY)
ax.text(50, 56.2, 'Self-renewal is lost at commitment; morphological recognition begins at the blast stage',
        ha='center', fontsize=7.8, style='italic', color='#53606E')

box(38, 47.5, 24, 6.4, 'Hemopoietic stem cell (HSC)', 'CD34+ · self-renewing · multipotent', NAVY, '#E8EEF6')
box(38, 39.5, 24, 5.4, 'Multipotent progenitor (MPP)', 'self-renewal lost', GREY, '#EEF1F4')
arrow(50, 47.5, 50, 44.9)

box(13, 30.5, 26, 5.6, 'Common myeloid progenitor', 'CMP', BLUE, '#E4EFF8')
box(61, 30.5, 26, 5.6, 'Common lymphoid progenitor', 'CLP', PURPLE, '#EFE9F6')
arrow(45, 39.5, 30, 36.1, BLUE); arrow(55, 39.5, 70, 36.1, PURPLE)

box(2, 20.5, 20, 5.4, 'MEP', 'megakaryocyte–erythroid', RED, '#F8E9E9')
box(24, 20.5, 20, 5.4, 'GMP', 'granulocyte–monocyte', ORANGE, '#FAF1DF')
arrow(20, 30.5, 13, 25.9, RED); arrow(30, 30.5, 34, 25.9, ORANGE)

box(57, 20.5, 15, 5.4, 'B / NK', 'marrow', PURPLE, '#EFE9F6')
box(75, 20.5, 15, 5.4, 'T cell', 'thymus', GREEN, '#E4F1EB')
arrow(70, 30.5, 64, 25.9, PURPLE); arrow(78, 30.5, 82, 25.9, GREEN)

box(1, 10.5, 10.5, 5.2, 'RBC', 'EPO', RED, '#F8E9E9')
box(13, 10.5, 11.5, 5.2, 'Platelets', 'TPO', RED, '#F8E9E9')
box(26, 10.5, 15, 5.2, 'Granulocytes', 'G-CSF', ORANGE, '#FAF1DF')
box(43, 10.5, 12, 5.2, 'Monocyte', 'GM-CSF', ORANGE, '#FAF1DF')
arrow(8, 20.5, 6, 15.7, RED); arrow(16, 20.5, 19, 15.7, RED)
arrow(31, 20.5, 33, 15.7, ORANGE); arrow(39, 20.5, 48, 15.7, ORANGE)
arrow(63, 20.5, 62, 15.7, PURPLE); arrow(82, 20.5, 81, 15.7, GREEN)
box(57, 10.5, 11, 5.2, 'B cell', 'plasma cell', PURPLE, '#EFE9F6')
box(75, 10.5, 13, 5.2, 'T subsets', 'CD4 / CD8', GREEN, '#E4F1EB')

ax.plot([1, 99], [7.6, 7.6], color='#B9C2CC', linewidth=0.9)
ax.text(50, 5.4, 'Maturation rule: cell shrinks · chromatin condenses · nucleoli disappear · cytoplasm takes the colour of its product',
        ha='center', fontsize=7.4, color='#3A4654')
ax.text(50, 2.6, 'Last dividing stage — erythroid: polychromatophilic erythroblast   |   granulocytic: myelocyte',
        ha='center', fontsize=7.4, fontweight='bold', color=NAVY)

plt.tight_layout()
fig.savefig('assets/images/hemopoiesis.png', dpi=200, bbox_inches='tight', facecolor='white')
print('wrote assets/images/hemopoiesis.png')
