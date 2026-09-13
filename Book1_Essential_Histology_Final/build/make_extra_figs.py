#!/usr/bin/env python3
"""Generate additional teaching figures: GI four-layer plan (Ch12) and cerebellar cortex (Ch7)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

NAVY='#1F3A5F'; BLUE='#2C6FAD'; RED='#B03A3A'; GREEN='#2E7D5B'; ORANGE='#C6862B'; PURPLE='#6B4C9A'; GREY='#5A6472'

# ---------- Figure: GI four-layer plan ----------
fig, ax = plt.subplots(figsize=(10, 6.4), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 64); ax.axis('off')
ax.text(50, 61, 'The Four-Layer Plan of the Digestive Tract', ha='center', fontsize=13.5, fontweight='bold', color=NAVY)
ax.text(50, 58, 'Every region is described by how it deviates from this template', ha='center', fontsize=7.8, style='italic', color='#53606E')

layers = [
    (44.0, 9.0, '#FDF1F1', RED,    'MUCOSA',            'epithelium · lamina propria · muscularis mucosae'),
    (34.0, 8.0, '#FAF3E2', ORANGE, 'SUBMUCOSA',         'dense irregular CT · vessels · submucosal (Meissner) plexus'),
    (22.5, 9.5, '#E9F0F8', BLUE,   'MUSCULARIS EXTERNA','inner circular + outer longitudinal · myenteric (Auerbach) plexus between'),
    (14.5, 6.0, '#E8F1EC', GREEN,  'SEROSA / ADVENTITIA','serosa if intraperitoneal · adventitia if fixed'),
]
for y, h, fc, ec, name, sub in layers:
    ax.add_patch(FancyBboxPatch((14, y), 72, h, boxstyle="round,pad=0.25,rounding_size=0.6",
                                linewidth=1.7, edgecolor=ec, facecolor=fc))
    ax.text(17, y + h*0.63, name, fontsize=9, fontweight='bold', color=ec, va='center')
    ax.text(17, y + h*0.26, sub, fontsize=6.9, color='#3A4654', va='center')

ax.text(50, 54.6, '▲  LUMEN', ha='center', fontsize=8.5, fontweight='bold', color=GREY)
ax.annotate('', xy=(10.5, 14.5), xytext=(10.5, 53.0),
            arrowprops=dict(arrowstyle='<|-', color=GREY, linewidth=1.4))
ax.text(8.6, 33.7, 'read from the lumen outward', rotation=90, ha='center', va='center',
        fontsize=7.2, color=GREY)

ax.text(88.5, 48.5, 'Glands in submucosa\nONLY here:', fontsize=7.0, color=ORANGE, fontweight='bold', va='center')
ax.text(88.5, 44.4, 'oesophagus\nduodenum (Brunner)', fontsize=6.8, color='#3A4654', va='center')
ax.text(88.5, 27.0, 'Myenteric = motility\nSubmucosal = secretion', fontsize=6.8, color=BLUE, va='center')

ax.plot([6, 94], [10.6, 10.6], color='#B9C2CC', linewidth=0.9)
ax.text(50, 7.8, 'Position predicts function: each plexus governs the layer it lies beside.', ha='center', fontsize=7.6, color='#3A4654')
ax.text(50, 4.6, 'Hirschsprung disease = absent ganglion cells in BOTH plexuses → tonically contracted, narrow distal segment',
        ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
plt.tight_layout(); fig.savefig('assets/images/gi_layers.png', dpi=200, bbox_inches='tight', facecolor='white')
print('wrote assets/images/gi_layers.png')

# ---------- Figure: cerebellar cortex ----------
fig, ax = plt.subplots(figsize=(10, 6.0), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
ax.text(50, 57, 'Cerebellar Cortex — Three Layers, One Unmistakable Row', ha='center', fontsize=13.2, fontweight='bold', color=NAVY)

ax.add_patch(Rectangle((12, 36), 76, 15, facecolor='#F4F7FB', edgecolor=BLUE, linewidth=1.5))
ax.text(14.5, 49.0, 'MOLECULAR LAYER', fontsize=8.6, fontweight='bold', color=BLUE)
ax.text(14.5, 46.4, 'pale · few cells · dendrites + parallel fibres', fontsize=6.9, color='#3A4654')

ax.add_patch(Rectangle((12, 29.5), 76, 6.5, facecolor='#FDF1F1', edgecolor=RED, linewidth=1.8))
ax.text(14.5, 33.9, 'PURKINJE CELL LAYER', fontsize=8.6, fontweight='bold', color=RED)
ax.text(14.5, 31.3, 'a SINGLE row of giant flask-shaped neurons', fontsize=6.4, color='#3A4654')

ax.add_patch(Rectangle((12, 14), 76, 15.5, facecolor='#EDEAF4', edgecolor=PURPLE, linewidth=1.5))
ax.text(14.5, 27.0, 'GRANULAR LAYER', fontsize=8.6, fontweight='bold', color=PURPLE)
ax.text(14.5, 24.4, 'densely packed small neurons — the most crowded nuclei in the body', fontsize=6.9, color='#3A4654')

import numpy as np
rng = np.random.default_rng(7)
for _ in range(430):
    ax.add_patch(Circle((rng.uniform(13, 87), rng.uniform(15, 23.3)), 0.36,
                        facecolor=PURPLE, edgecolor='none', alpha=0.62))
for x in (40, 54, 68, 82):
    ax.add_patch(Circle((x, 32.7), 1.75, facecolor='#F2C9C9', edgecolor=RED, linewidth=1.5))
    for dx, dy in ((-1.5, 3.2), (0, 3.6), (1.5, 3.2)):
        ax.add_patch(FancyArrowPatch((x, 34.4), (x+dx*2.0, 34.4+dy*2.3),
                                     arrowstyle='-', linewidth=1.0, color=RED, alpha=0.75))
    ax.add_patch(FancyArrowPatch((x, 30.9), (x, 26.5), arrowstyle='-|>', mutation_scale=9,
                                 linewidth=1.2, color=RED))

ax.text(91.5, 43.0, 'dendritic tree\nbranches in\nONE plane', fontsize=6.6, color=RED, va='center')
ax.text(91.5, 25.5, 'axon = the sole\noutput, and it is\nINHIBITORY (GABA)', fontsize=6.6, color=RED, va='center')
ax.plot([6, 94], [11.2, 11.2], color='#B9C2CC', linewidth=0.9)
ax.text(50, 8.4, 'DECISIVE FEATURE: one row of giant cells between a pale outer and a dark inner layer.', ha='center', fontsize=7.8, fontweight='bold', color=NAVY)
ax.text(50, 5.4, 'Nothing else in the body looks like this. The whole cortex computes onto one inhibitory output cell.', ha='center', fontsize=7.3, color='#3A4654')
plt.tight_layout(); fig.savefig('assets/images/cerebellum.png', dpi=200, bbox_inches='tight', facecolor='white')
print('wrote assets/images/cerebellum.png')
