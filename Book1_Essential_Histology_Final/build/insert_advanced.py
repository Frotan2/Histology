#!/usr/bin/env python3
"""Insert 'Advanced Concepts' section before 'Transition' in chapters that need depth."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / 'chapters'

# Per-chapter advanced content keyed on chapter number
ADVANCED = {
    '03': {
        'title': 'Advanced Concepts',
        'body': '''### Recognition Micro-Features

At higher magnification and EM, additional nuclear features become diagnostic:

- **Heterochromatin pattern** — *facultative heterochromatin* (X chromosome inactivation = Barr body, attached to nuclear envelope); *constitutive heterochromatin* (centromeres, telomeres). Barr body count = number of X chromosomes − 1; useful in sex-chromosome aneuploidies (Turner 0, Klinefelter 1).
- **Nuclear bodies** — *Cajal bodies* (coiled bodies, snRNP assembly, coilin scaffold); *PML bodies* (PML protein scaffold, role in DNA damage response); *nuclear speckles* (splicing factor storage).
- **Nuclear lamina** — lamin A/C meshwork underlying the inner nuclear membrane; mutations in *LMNA* cause progeria (Hutchinson-Gilford) and laminopathies (Emery-Dreifuss muscular dystrophy, dilated cardiomyopathy).
- **Nuclear pores** — ~100 nm, eight-fold symmetric; basket structure on nuclear side; FG-repeats in nucleoporins mediate selective transport of molecules >40 kDa (Ran-GTP gradient drives directionality).

### Cell Cycle Regulatory Detail

The cell cycle is governed by cyclin-dependent kinases (CDKs) whose activity oscillates with cyclin levels:

- **G1/S transition** — cyclin D/CDK4-6 phosphorylates Rb → releases E2F → transcription of S-phase genes; cyclin E/CDK2 drives S-phase entry. *Restriction point* = commitment to S-phase.
- **S-phase** — cyclin A/CDK2 drives DNA replication.
- **G2/M transition** — cyclin B/CDK1 (MPF) drives mitotic entry; CDK1 activation = the commitment to mitosis.
- **Mitotic exit** — APC/C (anaphase-promoting complex) degrades cyclin B and securin → sister chromatid separation and mitotic exit.

Checkpoints monitor fidelity: G1 checkpoint (DNA damage → p53 → p21 → CDK2 inhibition → G1 arrest), intra-S checkpoint, G2/M checkpoint (DNA damage → ATR → Chk1 → CDK1 inhibition), spindle assembly checkpoint (kinetochore-microtubule attachment → separase activation).

p53 (the "guardian of the genome") is the most commonly mutated gene in human cancer (~50% of all cancers); p53 loss removes the G1 DNA-damage checkpoint, allowing cells with damaged DNA to proliferate. Li-Fraumeni syndrome (germline p53 mutation) predisposes to multiple cancers.

### Apoptosis vs Necrosis vs Autophagy

| Feature | Apoptosis | Necrosis | Autophagy |
|---|---|---|---|
| Trigger | Programmed, physiological/pathological | Pathological, acute injury | Stress, starvation |
| Cell size | Shrinks | Swells | Variable |
| Nucleus | Pyknosis, karyorrhexis | Karyolysis | Intact |
| Membrane | Blebs, apoptotic bodies | Rupture | Intact |
| Inflammatory | No | Yes | No |
| Mechanism | Caspase cascade | ATP failure → membrane rupture | Lysosomal degradation |
| Marker | Annexin V+, TUNEL+ | HMGB1 release | LC3-II, p62 |

Apoptosis pathways:
- **Intrinsic (mitochondrial)** — stress (DNA damage, growth factor withdrawal) → Bax/Bak → cytochrome c release → apoptosome (Apaf-1 + caspase-9) → caspase-3/-7 activation.
- **Extrinsic (death receptor)** — FasL/FasR, TRAIL/TRAIL-R, TNF/TNFR1 → FADD → caspase-8 → caspase-3/-7.
- **Common pathway** — caspase-3/-7 execute: DNA fragmentation (CAD), cytoskeletal breakdown, blebbing, phagocytic uptake.

Necrosis is uncontrolled cell death from membrane rupture (inflammation, ATP depletion, complement). Coagulative necrosis (preserved architecture, e.g., MI), liquefactive necrosis (CNS, abscess), caseous necrosis (TB), fat necrosis (pancreatitis, breast trauma), gangrenous necrosis (limb ischaemia ± infection).

Autophagy ("self-eating") wraps organelles in autophagosomes that fuse with lysosomes; degrades long-lived proteins and damaged organelles; protective during nutrient stress; implicated in neurodegeneration, cancer, infection.'''
    },
    '04': {
        'title': 'Advanced Concepts',
        'body': '''### Recognition Micro-Features

At higher magnification, the type of epithelium is diagnostic:

- **Basement membrane thickness** — ~50 nm in routine H&E, but thicker in PAS stain; *thickening of BM* is a feature of diabetes (capillary BM), bullous pemphigoid (subepidermal split above thickened BM), and membranous glomerulonephritis (subepithelial immune deposits).
- **Goblet cells** — distended apical cytoplasm with clear/pale mucin (mucinogen), basal compressed nucleus. Number increases from duodenum to colon (most numerous in colon). *Goblet cell metaplasia* in respiratory epithelium → chronic bronchitis, smoker's airway; *goblet cells in Barrett's esophagus* define intestinal metaplasia.
- **Brush border vs striated border** — intestinal microvilli form the brush border (well-defined, ~1–2 µm thick, eosinophilic, contains brush-border enzymes); kidney proximal tubule has a similar but taller striated border.
- **Cilia** — apical eosinophilic fringe in ciliated epithelium; *9+2 axoneme*, basal bodies; in the respiratory tract, ciliary dyskinesia (primary ciliary dyskinesia, Kartagener syndrome) → immotile cilia → recurrent sinopulmonary infections, situs inversus.
- **Stratified squamous keratinised** vs **non-keratinised** — *keratinised* has anucleate surface layer (skin, keratinised portion of anal canal above pectinate line); *non-keratinised* retains nuclei in surface layer (esophagus, vagina, oral cavity).

### Epithelial Renewal

Epithelia are among the most rapidly renewing tissues in the body:

- **Intestinal epithelium** — 3–5 days from crypt stem cell to villus tip shedding.
- **Skin epidermis** — 4–6 weeks from basal layer to stratum corneum desquamation.
- **Respiratory epithelium** — turnover ~1 month.
- **Liver hepatocytes** — long-lived but can regenerate: 70% hepatectomy → full mass restoration in ~2 weeks via hepatocyte proliferation.

Stem cells reside in specific niches:
- **Intestinal crypts** — Lgr5+ stem cells at the crypt base; Paneth cells provide Wnt, EGF, Notch signals.
- **Epidermal basal layer** — interfollicular stem cells; hair follicle bulge stem cells (K15+) contribute to wound re-epithelialisation.
- **Corneal limbus** — limbal stem cells; deficiency → corneal neovascularisation and opacification.

### Common Misconceptions Extended

- *All epithelia are avascular.* Stratified squamous of the cornea is avascular; most epithelia rest on a vascularised basement membrane.
- *Transitional epithelium is "transitional" because it changes shape.* It is transitional because it was thought to be intermediate between stratified squamous and stratified columnar; it is specialised urothelium, not a "transition" between other types.
- *Pseudostratified means multiple layers.* A single layer with nuclei at different heights (every cell touches the basement membrane).
- *Microvilli = cilia.* Microvilli = membrane protrusions (actin core); cilia = membrane-bound organelles (microtubule core). Different ultrastructure, different motility, different functions.
- *Squamous cells are only on surfaces.* Mesothelium is also simple squamous (peritoneum, pleura, pericardium); mesothelial cells are squamous but have microvilli on their free surface (unique).'''
    },
    '05': {
        'title': 'Advanced Concepts',
        'body': '''### Collagen Synthesis Pathway Detail

Collagen synthesis is a multistep process that explains collagen diseases:

1. **Pre-procollagen synthesis** (RER) — signal peptide directs nascent polypeptide into ER; pro-α chains assemble into triple helix (procollagen) with N- and C-terminal propeptides.
2. **Hydroxylation** (RER, requires vitamin C) — proline and lysine residues hydroxylated by prolyl/lysyl hydroxylases; *vitamin C deficiency → hydroxyproline deficiency → triple helix unstable → scurvy* (bleeding gums, poor wound healing, perifollicular haemorrhages).
3. **Glycosylation** (RER, Golgi) — hydroxylysine residues glycosylated.
4. **Triple helix formation** (Golgi) — procollagen triple helix with retained propeptides.
5. **Exocytosis** — procollagen secreted.
6. **Cleavage of propeptides** (extracellular) — procollagen peptidases cleave N- and C-terminal propeptides → insoluble tropocollagen.
7. **Cross-linking** (extracellular, lysyl oxidase, requires Cu²⁺) — lysine and hydroxylysine residues oxidatively deaminated → allysine → cross-links with adjacent tropocollagen molecules → collagen fibril.
   - *Menkes disease* (Cu²⁺ transport defect) → defective cross-linking → kinky hair, brittle bones.
   - *Ehlers-Danlos* (various, e.g., lysyl hydroxylase deficiency in type VI) → defective cross-linking → hyperextensible skin, hypermobile joints.
8. **Fibril assembly** (extracellular) — staggered tropocollagen molecules → 67 nm D-banding periodicity.

### Elastic Fibre Detail

Elastic fibres are composed of an elastin core surrounded by a fibrillin-1 microfibril sheath. The tropoelastin molecules are cross-linked by lysyl oxidase (same enzyme as collagen). The cross-links are *desmosine* and *isodesmosine* — unique to elastin.

- *Marfan syndrome* — FBN1 (fibrillin-1) mutation; fibrillin-1 microfibrils defective → *aortic dissection, ectopia lentis, skeletal overgrowth*. Fibrillin-1 also sequesters TGF-β; defective fibrillin → excess TGF-β signalling → additional pathology.
- *Williams syndrome* — elastin gene deletion (7q11.23); supravalvular aortic stenosis, "elfin" facies, hypercalcaemia, friendly personality.
- *Cutis laxa* — elastin gene mutation or acquired (post-inflammatory); loose, redundant skin.

### Ground Substance Detail Extended

GAG turnover is mediated by specific enzymes:
- *Hyaluronidase* degrades hyaluronic acid (target of bacterial hyaluronidase, which spreads infection through CT).
- *Sulfatases* degrade sulfated GAGs; *mucopolysaccharidoses* (Hurler, Hunter, Morquio) are deficiencies in specific lysosomal sulfatases or hydrolases → GAG accumulation → coarse facies, hepatosplenomegaly, skeletal dysplasia, intellectual disability.

Decorin, biglycan, lumican, and fibromodulin are small leucine-rich proteoglycans that bind TGF-β and regulate collagen fibril assembly. Decorin deficiency → irregular collagen fibrils and skin fragility.

Fibronectin has two forms: *plasma fibronectin* (circulating, in fibrin clots, supports wound healing) and *cellular fibronectin* (insoluble, in ECM). Fibronectin binds integrins (RGD sequence), collagen, fibrin, and heparan sulfate; it is essential for cell migration in embryogenesis and wound healing.'''
    },
    '06': {
        'title': 'Advanced Concepts',
        'body': '''### Adipose as an Endocrine Organ Extended

White adipose is one of the largest endocrine organs in the body. Principal adipokines:

- **Leptin** (16 kDa) — produced in proportion to fat mass; signals satiety via hypothalamic LepRb receptor → POMC/AgRP regulation → appetite suppression and increased energy expenditure.
- **Adiponectin** (30 kDa) — paradoxically produced more by lean than obese adipose; insulin-sensitising (AMPK activation in muscle and liver); anti-atherogenic; low levels in metabolic syndrome.
- **Resistin** — links adipose to insulin resistance (resistin name reflects this); more clearly demonstrated in rodents than humans.
- **Inflammatory cytokines** — TNF-α, IL-6, MCP-1 (CCL2); recruit macrophages; contribute to chronic low-grade inflammation in obesity.

Adipose macrophages (ATM) form crown-like structures around dead adipocytes in obese adipose. In lean adipose, ATMs are M2-polarised (anti-inflammatory, wound healing). In obese adipose, ATMs become M1-polarised (pro-inflammatory) and drive chronic inflammation, contributing to insulin resistance.

Adipose tissue dysfunction is a central feature of metabolic syndrome: hypertrophic obesity, hypoxia, macrophage infiltration, ER stress, and altered adipokine secretion all converge on insulin resistance. Bariatric surgery reverses much of this dysfunction, often before significant weight loss (via altered gut hormones GLP-1, PYY).

### Thermogenesis Detail

Brown adipose tissue is metabolically active, sympathetic-innervated, and UCP1-dependent. Cold exposure activates the sympathetic nervous system → NE release on brown adipocytes → β3-adrenergic receptor → cAMP → PKA → lipolysis and UCP1 activation → mitochondrial proton leak → heat. Newborns have substantial BAT (interscapular, perirenal) for non-shivering thermogenesis because they cannot shiver. Adult humans retain BAT deposits (supraclavicular, neck, mediastinal) detectable by PET-CT.

Beige adipocytes arise within white fat depots upon chronic cold or β-adrenergic stimulation. They express UCP1 and have a thermogenic capacity intermediate between white and brown adipocytes. Recruitment of beige fat is being investigated as an obesity/metabolic disease therapy.

### Adipocyte Plasticity and Pathology

Adipocytes are highly plastic:
- **Hypertrophy** — increase in cell size; associated with metabolic disease.
- **Hyperplasia** — increase in cell number; healthier; recruits new adipocytes from progenitors.
- **Dedifferentiation** — under extreme conditions, mature adipocytes can lose their lipid and become fibroblast-like.

Major pathological correlates:
- **Obesity** — BMI ≥ 30; visceral adipose accumulation → metabolic syndrome, type 2 diabetes, NAFLD, atherosclerosis.
- **Lipodystrophy** — selective loss of adipose; may be genetic (e.g., *LMNA* mutations in familial partial lipodystrophy) or acquired (HIV antiretroviral therapy).
- **Lipoma** — most common benign soft-tissue tumour; mature adipocytes.
- **Liposarcoma** — most common soft-tissue sarcoma in adults; lipoblasts with atypia and mitoses; well-differentiated, myxoid/round cell, pleomorphic subtypes.
- **Hibernoma** — rare benign tumour of brown adipose.'''
    },
    '07': {
        'title': 'Advanced Concepts',
        'body': '''### Synapse Detail

Synapses are specialised junctions where one neuron communicates with another (or with an effector). Two major classes:

- **Electrical synapses** — gap junctions allow direct ionic current flow; fast, bidirectional; found in cardiac muscle, smooth muscle, some CNS neurons (esp. inhibitory interneurons in retina, thalamic reticular nucleus, hippocampal interneurons).
- **Chemical synapses** — neurotransmitter in presynaptic vesicles released into synaptic cleft; bind postsynaptic receptors; slower but plastic.

Chemical synapse structure: presynaptic terminal (active zones, mitochondria, synaptic vesicles), synaptic cleft (~20–30 nm, with adhesion molecules like neurexin/neuroligin), postsynaptic density (receptors, scaffolding proteins). Synaptic vesicles cluster at active zones (docked) and are primed for release. Ca²⁺ entry through voltage-gated Ca²⁺ channels triggers SNARE-mediated vesicle fusion (synaptobrevin/VAMP, syntaxin, SNAP-25). Botulinum toxin cleaves SNARE proteins → flaccid paralysis.

Neurotransmitter types:
- **Amino acids** — glutamate (principal excitatory), GABA (principal inhibitory), glycine (inhibitory, spinal cord).
- **Monoamines** — dopamine, norepinephrine, epinephrine, serotonin, histamine.
- **Acetylcholine** — neuromuscular junction, autonomic preganglionic, parasympathetic postganglionic.
- **Neuropeptides** — substance P, enkephalins, endorphins, neuropeptide Y, somatostatin; stored in dense-core vesicles, slower action.

Postsynaptic potentials:
- **EPSP** (excitatory postsynaptic potential) — depolarisation, opens Na⁺ channels.
- **IPSP** (inhibitory postsynaptic potential) — hyperpolarisation, opens Cl⁻ or K⁺ channels.

### Myelination and Saltatory Conduction

Myelin is a multilamellar lipid-rich sheath (mostly lipid, some protein) wrapped around axons by oligodendrocytes (CNS) or Schwann cells (PNS). It increases conduction velocity by:
- Reducing membrane capacitance (less charge stored across the bilayer).
- Increasing membrane resistance (less current leak).

Conduction is *saltatory*: action potentials "jump" between nodes of Ranvier (gaps in myelin where Na⁺ channels are concentrated). Saltatory conduction is much faster than continuous conduction (up to ~120 m/s in large myelinated axons vs ~1 m/s in small unmyelinated).

Demyelinating disease:
- **Multiple sclerosis** — autoimmune destruction of CNS myelin (oligodendrocytes); periventricular plaques on MRI; symptoms depend on plaque location (optic neuritis, hemiparesis, ataxia).
- **Guillain-Barré syndrome** — autoimmune PNS demyelination (Schwann cells); ascending paralysis.
- **Charcot-Marie-Tooth** — hereditary demyelinating neuropathy (PMP22, MPZ mutations); foot drop, stork-leg deformity.

### Neuronal Cell Biology

Neurons are post-mitotic; they cannot divide. They have high metabolic demands (high O₂ consumption, glucose uptake, mitochondrial density). The neuronal cytoskeleton is specialised:
- **Neurofilaments** — intermediate filaments; accumulate in ageing neurons (neurofibrillary tangles in Alzheimer disease).
- **Microtubules** — track for fast axonal transport (kinesin anterograde, dynein retrograde).
- **Actin** — dendritic spines, growth cones.

Axonal transport:
- **Anterograde** (cell body → terminal) — kinesin; fast transport of vesicles, slow transport of cytoskeletal proteins.
- **Retrograde** (terminal → cell body) — dynein; carries trophic signals (NGF), viruses (rabies, HSV), toxins (tetanus).

Neuronal injury: chromatolysis (cell body swells, Nissl substance disperses, nucleus moves peripherally) after axonal injury reflects the metabolic shift to regeneration. Central neurons rarely regenerate (no Schwann cell tube, glial scar, myelin inhibitors); peripheral neurons regenerate along the Schwann cell tube (~1 mm/day).'''
    },
    '08': {
        'title': 'Advanced Concepts',
        'body': '''### Endothelial Heterogeneity and Specialised Circulations

Endothelium is highly heterogeneous, specialised to local function:
- **Brain (continuous with tight junctions)** — BBB; pericytes, astrocyte foot processes; prevents most molecules >400 Da from crossing.
- **Endocrine glands (fenestrated)** — rapid hormone exchange; pituitary, adrenal, thyroid.
- **Liver (sinusoidal, discontinuous)** — large fenestrations, no diaphragm; allows bidirectional exchange of macromolecules.
- **Kidney glomerulus (fenestrated, no diaphragm)** — combined with podocyte slit diaphragm and GBM to form a triple filter.
- **Spleen (sinusoidal, open circulation)** — RBCs squeeze through; macrophages in sinuses phagocytose aged RBCs.
- **Lung (continuous)** — extremely thin for gas exchange; pneumocyte on air side.

Lymphatics:
- **Initial lymphatics** — blind-ended capillaries with overlapping endothelial cells (function as primary valves), no BM, no pericytes; entry of interstitial fluid driven by tissue pressure.
- **Collecting lymphatics** — have smooth muscle and valves; lymphangions contract to propel lymph.
- **Lymph nodes** — along the lymphatic pathway; filter lymph (see Chapter 11).

### Vascular Pathology Correlates

- **Atherosclerosis** — intimal lipid accumulation + inflammation; plaques form in high-pressure, turbulent-flow regions (branch points); risk factors: hypertension, hyperlipidaemia, smoking, diabetes.
- **Aneurysm** — focal dilation of artery (>50% of normal); risk of rupture; abdominal aortic aneurysm is most common.
- **Vasculitis** — inflammatory destruction of vessel wall; examples: giant cell arteritis (temporal artery, elderly, headache, jaw claudication), Takayasu arteritis (aorta, young women), Kawasaki disease (coronary arteries, children), polyarteritis nodosa (medium arteries, ANCA-negative).
- **Capillary leak** — endothelial barrier breakdown → tissue oedema; seen in sepsis, burns, anaphylaxis.
- **Diabetic microangiopathy** — capillary BM thickening; retinopathy, nephropathy, neuropathy.

### Cardiac Muscle vs Smooth Muscle vs Skeletal Muscle (recognition primer)

Although muscle tissue is out of core scope, the heart and vessels contain contractile cells worth contrasting:

| Feature | Skeletal | Cardiac | Smooth |
|---|---|---|---|
| Striations | Yes | Yes | No |
| Nuclei | Multinucleate (peripheral) | 1–2 central | 1 central |
| Intercalated discs | No | Yes | No |
| Cell shape | Long cylinder | Branched cylinder | Spindle/fusiform |
| Ca²⁺ source | SR only | SR + extracellular | Extracellular + SR |
| Gap junctions | No | Yes (intercalated disc) | Yes (single-unit) |
| Control | Voluntary | Involuntary | Involuntary |
| Regeneration | Limited (satellite cells) | Minimal | Good |

Smooth muscle in the tunica media of arteries is the principal effector of vascular tone (α1-adrenergic → contraction; β2-adrenergic → relaxation).'''
    },
    '09': {
        'title': 'Advanced Concepts',
        'body': '''### Neutrophil Detail

Neutrophils are the principal cells of acute inflammation. Key features:
- **Half-life** — 6–8 hours in blood; 1–4 days in tissue.
- **Granules**:
  - *Primary (azurophilic)* — myeloperoxidase (MPO), defensins, lysozyme, elastase, cathepsin G. MPO converts H₂O₂ + Cl⁻ → HOCl (bleach); deficiency → chronic granulomatous disease–like (actually MPO deficiency is milder).
  - *Secondary (specific)* — collagenase, lysozyme, lactoferrin, NADPH oxidase components.
  - *Tertiary (gelatinase)* — gelatinase, lysozyme.
- **Receptors** — FcγRIII (CD16), complement receptors (CR1, CR3), L-selectin, β2 integrins (LFA-1, Mac-1), TLRs, chemokine receptors.
- **Function** — phagocytosis, degranulation, NETosis (neutrophil extracellular traps = DNA + histones + granule proteins that trap bacteria).

Recruitment cascade:
1. **Rolling** — selectins (E-selectin on endothelium, P-selectin, L-selectin on leukocytes) bind sialyl-Lewis X.
2. **Activation** — chemokines (IL-8, CXCL8) activate integrins.
3. **Firm adhesion** — β2 integrins bind ICAM-1.
4. **Transmigration** — diapedesis between endothelial cells (paracellular) or through them (transcellular).
5. **Chemotaxis** — toward chemoattractants (C5a, LTB4, IL-8, bacterial peptides).

Neutrophilia (infection, inflammation, leukaemia); neutropenia (chemotherapy, viral infection, autoimmune); left shift (band neutrophils in circulation, immature).

### Eosinophil Detail

Eosinophils mediate parasitic infections and allergy. Granules contain:
- *Major basic protein* (MBP) — toxic to parasites.
- *Eosinophil cationic protein* (ECP) — RNase activity.
- *Eosinophil peroxidase* — less potent than MPO.
- *Eosinophil-derived neurotoxin* (EDN) — RNase activity.

Eosinophil surface receptors: CCR3 (eotaxin receptor), FcεRI (IgE), CR1. Eosinophilia in allergy, parasitic infection, hypereosinophilic syndrome, certain leukaemias (chronic eosinophilic leukaemia). Curschmann spirals (extruded mucus casts) and Charcot-Leyden crystals (galectin-10, from eosinophil breakdown) are seen in sputum of asthmatics.

### Lymphocyte Subsets (extended)

- **T cells** — mature in thymus. Subtypes:
  - *CD4+ T helper (Th)* — recognise MHC II; subtypes Th1 (IFN-γ, cell-mediated immunity), Th2 (IL-4, IL-5, IL-13, humoral/allergy), Th17 (IL-17, neutrophil recruitment), Tfh (B cell help in germinal centres), Treg (IL-10, TGF-β, immune tolerance).
  - *CD8+ T cytotoxic (Tc)* — recognise MHC I; kill via perforin/granzyme and FasL.
- **B cells** — mature in bone marrow; produce immunoglobulins; present antigen to CD4+ T cells; form germinal centres after activation.
- **NK cells** — innate lymphoid cells; kill via perforin/granzyme and ADCC; recognise missing-self (MHC I downregulation).
- **NKT cells** — express both T-cell receptor and NK markers; recognise CD1d-presented glycolipids.

Recirculation: naive T cells enter lymph nodes via HEVs; activated T cells up-regulate tissue-homing receptors (CLA for skin, α4β7 integrin + CCR9 for gut).'''
    },
    '10': {
        'title': 'Advanced Concepts',
        'body': '''### Stem Cell Niche Detail

Haematopoietic stem cells (HSCs) reside in a specific niche that regulates self-renewal and differentiation:

- **Endosteal niche** — near the endosteum; quiescent HSCs; osteoblasts produce CXCL12 (SDF-1) and SCF; HSCs adhere via CXCR4.
- **Vascular niche** — near sinusoidal endothelium; activated HSCs; CXCL12 also expressed by sinusoidal endothelial cells; mobilisation (G-CSF, chemotherapy) drives HSC egress into circulation.

HSC mobilisation: G-CSF → neutrophil activation → proteolytic cleavage of CXCL12 and VCAM-1 → HSC detachment → mobilisation into circulation. Mobilised HSCs can be harvested by leukapheresis for transplantation.

HSC homing to bone marrow after transplant: HSC CXCR4 binds CXCL12 → integrin activation → firm adhesion → transendothelial migration → niche.

### Erythropoiesis Detail

Erythropoiesis proceeds through morphologically recognisable stages:

1. **Proerythroblast** — large, basophilic, euchromatic nucleus; first committed erythroid progenitor.
2. **Basophilic erythroblast** — smaller, deeply basophilic; high RER for globin synthesis.
3. **Polychromatophilic erythroblast** — intermediate staining (basophilic + eosinophilic); haemoglobin synthesis begins.
4. **Orthochromatophilic erythroblast** — small, pyknotic nucleus; cytoplasm strongly eosinophilic (haemoglobin dominant).
5. **Reticulocyte** — nucleus extruded; residual RNA and organelles; released into blood; matures to erythrocyte in 1–2 days. Supravital staining (new methylene blue) reveals residual RNA as reticular network → reticulocyte count.

Erythropoietin (EPO) acts on CFU-E and proerythroblast; iron is essential (Fe²⁺ incorporated into protoporphyrin IX by ferrochelatase); vitamin B₁₂ and folate are essential for DNA synthesis (deficiency → megaloblastic anaemia with nuclear-cytoplasmic asynchrony).

Reticulocyte count is the most useful index of effective erythropoiesis: increased in haemolysis or post-iron/B₁₂ replacement; decreased in aplastic anaemia, renal failure (EPO deficiency), marrow infiltration.

### Granulopoiesis Detail

Granulopoiesis proceeds through myeloblast → promyelocyte → myelocyte → metamyelocyte → band → segmented (mature neutrophil).

- **Myeloblast** — large, euchromatic nucleus with prominent nucleoli; no granules; first recognisable granulocyte precursor.
- **Promyelocyte** — azurophilic (primary) granules appear (peroxidase, defensins).
- **Myelocyte** — specific (secondary) granules appear; last mitotic stage.
- **Metamyelocyte** — kidney-shaped nucleus; non-mitotic; nuclear indentation.
- **Band** — horseshoe-shaped nucleus; non-mitotic; immature circulating neutrophil.
- **Segmented** — multi-lobed nucleus (3–5 lobes); mature.

Specific granules determine cell identity (neutrophil, eosinophil, basophil). Granule content is packaged during the myelocyte stage; mutations affecting granule formation cause specific granule deficiency.

G-CSF shortens the transit time of the granulocytic series and shifts the marginating pool to the circulating pool; used clinically to accelerate neutrophil recovery after chemotherapy.

### Megakaryopoiesis and Platelet Production

Megakaryocytes are giant polyploid cells (up to 64N) that produce platelets by cytoplasmic fragmentation:

1. **Megakaryoblast** — committed progenitor.
2. **Promegakaryocyte** — endomitosis (DNA replication without cell division → polyploidy).
3. **Megakaryocyte** — large polylobulated nucleus; abundant cytoplasm with platelet-specific granules; *demarcation membrane system* (invaginations of plasma membrane that partition the cytoplasm into future platelets).
4. **Proplatelets** — cytoplasmic extensions that protrude through sinusoidal endothelium into the blood; platelets shear off from the proplatelet tips.

Platelets are anucleate cell fragments ~2–3 µm with α-granules (PDGF, TGF-β, vWF, fibrinogen, PF4) and δ-granules (dense bodies: ADP, ATP, serotonin, Ca²⁺).'''
    },
    '11': {
        'title': 'Advanced Concepts',
        'body': '''### Lymphocyte Trafficking

Lymphocytes continuously recirculate between blood, lymphoid tissue, and lymph — a process essential for immune surveillance. Trafficking is governed by addressins (homing receptors) on endothelium and selectins/integrins on lymphocytes:

- **Naive T cells** enter lymph nodes via HEVs using L-selectin (CD62L) → PNAd (peripheral node addressin) binding + CCR7 → CCL19/21 chemokine signalling.
- **Activated T cells** in tissues up-regulate tissue-specific homing receptors:
  - *Skin-homing* — CLA (cutaneous lymphocyte antigen) binds E-selectin on dermal endothelium.
  - *Gut-homing* — α4β7 integrin binds MAdCAM-1 on gut endothelium; CCR9 binds CCL25.
  - *Lung-homing* — CCR4 binds CCL17.
- **Memory T cells** — central memory (CCR7+, in lymph nodes) vs effector memory (CCR7−, in tissues).

This compartmentalisation explains the regional specialisation of mucosal immunity (MALT: GALT in gut, BALT in bronchus, NALT in nasopharynx).

### Antigen Presentation and MHC

- **MHC class I** — on all nucleated cells; presents endogenous peptides (8–10 aa) to CD8+ T cells; recognised after viral infection, tumour, intracellular pathogen. β2-microglobulin is the invariant light chain.
- **MHC class II** — on professional APCs (dendritic cells, macrophages, B cells); presents exogenous peptides (~15 aa) to CD4+ T cells.

Antigen processing:
- **Endogenous (cytosolic)** — proteasome cleaves proteins → TAP transporter to ER → MHC I binding → cell surface.
- **Exogenous** — endocytosis → lysosomal degradation → MHC II loaded in MIIC compartment → cell surface.

Dendritic cells (DCs) are the principal initiators of adaptive immune responses:
- **Conventional DC (cDC)** — antigen capture and presentation; migrate to lymph nodes after antigen uptake.
- **Plasmacytoid DC (pDC)** — produce massive type I IFN in viral infection.
- **Follicular DC (FDC)** — not from HSC; trap antigen-antibody complexes in B-cell follicles.
- **Langerhans cell** — epidermal dendritic cell; Birbeck granules (tennis racket-shaped, langerin/CD207+).

### Hypersensitivity and Autoimmunity

Four classic hypersensitivity mechanisms:
- **Type I** (IgE-mediated, immediate) — allergens → IgE on mast cells → crosslinking → degranulation → histamine, leukotrienes; examples: allergic rhinitis, asthma, anaphylaxis, urticaria.
- **Type II** (antibody-mediated cytotoxic) — IgG/IgM against cell-surface antigens → complement-mediated lysis or ADCC; examples: autoimmune haemolytic anaemia, Goodpasture syndrome, myasthenia gravis, Graves disease (stimulating), transfusion reactions, Rh disease.
- **Type III** (immune complex) — antigen-antibody complexes deposit in tissues → complement activation → neutrophil recruitment → tissue damage; examples: serum sickness, post-streptococcal glomerulonephritis, SLE, Arthus reaction.
- **Type IV** (delayed-type, T-cell mediated) — CD4+ Th1 + macrophages + CD8+ Tc; 48–72 hours; examples: contact dermatitis (poison ivy), tuberculin (PPD) test, granulomatous inflammation (TB, sarcoid), transplant rejection, type 1 diabetes.

Autoimmunity arises from a combination of genetic susceptibility (HLA alleles, e.g., HLA-DR4 in RA, HLA-B27 in ankylosing spondylitis) and environmental triggers (infection, smoking, drugs). Central tolerance (negative selection in thymus) and peripheral tolerance (Treg, anergy, deletion) normally prevent autoreactive lymphocytes from causing disease; their failure → autoimmunity.'''
    },
    '12': {
        'title': 'Advanced Concepts',
        'body': '''### Gastric Acid Secretion Mechanism

The parietal cell is the most sophisticated acid-secreting cell in the body. Resting parietal cells have *tubulovesicles* containing H⁺/K⁺-ATPase in the cytoplasm. On stimulation:

1. **Histamine** (from ECL cells) → H2 receptor → Gs → cAMP → PKA.
2. **Gastrin** (from G cells) → CCK-B receptor → Gq → PLC → IP3/Ca²⁺.
3. **ACh** (from vagus) → M3 receptor → Gq → PLC → IP3/Ca²⁺.

All three converge on PKA/Ca²⁺ → tubulovesicles fuse with apical membrane → H⁺/K⁺-ATPase inserted → acid secretion.

Acid generation:
- CO₂ + H₂O → H₂CO₃ (carbonic anhydrase) → H⁺ + HCO₃⁻.
- H⁺ pumped into lumen by H⁺/K⁺-ATPase (proton pump; target of PPIs).
- Cl⁻ follows via ClC-2 channel.
- HCO₃⁻ exchanged for Cl⁻ across basolateral membrane (anion exchanger AE2).

Parietal cells also secrete **intrinsic factor** (essential for B₁₂ absorption in the terminal ileum); *autoimmune gastritis* → anti-parietal cell + anti-intrinsic factor antibodies → pernicious anaemia (B₁₂ deficiency).

PPI pharmacokinetics: PPIs are prodrugs activated by acid; they irreversibly inhibit H⁺/K⁺-ATPase (covalent cysteine modification), so acid secretion resumes only after new pump synthesis (~24 hours). Best taken 30–60 min before meals when parietal cells are most active.

### Pancreatic Exocrine Activation Cascade

Pancreatic enzymes are secreted as inactive zymogens to prevent autodigestion. Activation is a controlled cascade in the duodenum:

1. **Trypsinogen** → **trypsin** by *enterokinase* (enteropeptidase) on the duodenal brush border. Trypsin is the master activator.
2. Trypsin activates:
   - Chymotrypsinogen → chymotrypsin.
   - Proelastase → elastase.
   - Procarboxypeptidase → carboxypeptidase.
3. Trypsin also activates *phospholipase A2* and *procolipase* (essential for lipid digestion).

Failure of activation: *trypsinogen gene mutations* (cationic trypsinogen PRSS1) → premature intra-pancreatic activation → hereditary pancreatitis.

*Premature activation within the pancreas* (trypsin autodigestion) → acute pancreatitis; common causes: gallstones (ampullary obstruction), alcohol, hypertriglyceridaemia, hypercalcaemia, drugs, ERCP, trauma. Trypsin also activates complement and kinins → systemic inflammation, ARDS, DIC.

### Intestinal Absorption Mechanisms

- **Glucose/galactose** — SGLT1 (Na⁺-coupled cotransporter, apical); GLUT2 (basolateral).
- **Fructose** — GLUT5 (apical facilitated diffusion); GLUT2 (basolateral).
- **Amino acids** — various apical transporters (B⁰, X⁻AG, b⁰,+); Na⁺-coupled.
- **Di- and tripeptides** — PepT1 (H⁺-coupled); broken down to amino acids in cytosol.
- **Long-chain fatty acids and monoglycerides** — diffuse across apical membrane; re-esterified to TG in ER; packaged with apolipoproteins (ApoB-48, ApoA-IV) into chylomicrons; secreted by exocytosis into lacteals (lymphatics); reach blood via thoracic duct.
- **Short-chain fatty acids** — absorbed directly into portal blood.
- **Iron** — DMT1 (apical, Fe²⁺ uptake); ferroportin (basolateral export); hephaestin (oxidises Fe²⁺ → Fe³⁺ for binding to transferrin).
- **Vitamin B₁₂** — intrinsic factor-B₁₂ complex absorbed in terminal ileum via cubilin receptor.
- **Calcium** — transcellular (duodenum, vitamin D-dependent); paracellular (jejunum, ileum, concentration-dependent).

### GI Hormones

- **Gastrin** (G cells, antrum) — stimulates acid secretion; growth of gastric mucosa.
- **CCK** (I cells, duodenum, jejunum) — stimulates pancreatic enzyme secretion, gallbladder contraction, relaxes sphincter of Oddi; satiety signal.
- **Secretin** (S cells, duodenum) — stimulates pancreatic bicarbonate secretion.
- **GIP** (K cells, duodenum, jejunum) — *glucose-dependent insulinotropic peptide*; insulin release in response to oral glucose (incretin effect).
- **GLP-1** (L cells, ileum, colon) — incretin; insulin release, glucagon suppression, satiety, gastric emptying delay. GLP-1 agonists (exenatide, liraglutide, semaglutide) used in type 2 diabetes and obesity.
- **Somatostatin** (D cells) — inhibits gastrin, CCK, secretin, gastric acid, pancreatic secretion.
- **Motilin** (M cells, duodenum) — stimulates gastric motility; target of erythromycin (motilin agonist).'''
    },
    '13': {
        'title': 'Advanced Concepts',
        'body': '''### Bile Acid Metabolism

Bile acids are synthesised from cholesterol in hepatocytes (~500 mg/day). Two pathways:
- *Classical* (neutral) — cholesterol 7α-hydroxylase (CYP7A1) is rate-limiting; produces cholic acid (CA) and chenodeoxycholic acid (CDCA).
- *Alternative* (acidic) — sterol 27-hydroxylase (CYP27A1); produces CDCA.

Primary bile acids (CA, CDCA) are conjugated with glycine or taurine (increased solubility, decreased passive reabsorption), secreted into bile via BSEP (bile salt export pump), stored in gallbladder, released into duodenum after a meal. In the ileum, bacteria deconjugate and 7α-dehydroxylate primary bile acids → secondary bile acids (deoxycholic acid, lithocholic acid). ~95% of bile acids are reabsorbed in the ileum (enterohepatic circulation) and returned to the liver via portal blood; only ~5% lost in faeces (compensated by new synthesis).

Bile acid functions:
- *Micelle formation* — emulsify dietary lipids and fat-soluble vitamins; critical for lipid absorption.
- *Bile flow* — choleretic; primary driving force for bile secretion.
- *Signalling* — bind FXR (farnesoid X receptor) and TGR5; regulate glucose, lipid, and energy homeostasis. FXR agonists (obeticholic acid) used in primary biliary cholangitis and NASH.

Gallstones: most are cholesterol stones (supersaturation of bile with cholesterol, nucleation, growth); risk factors are "5 F's" (Female, Fat, Forty, Fertile, Fair). Pigment stones (bilirubin): chronic haemolysis, cirrhosis.

### Pancreatic Islet Cell Organisation

Islet cell distribution is non-random:
- **Mouse/rat** — β cells central, α cells peripheral (mantle).
- **Human** — β cells ~55–70%, α cells ~20–35%, δ cells ~5–10%, scattered throughout islet; α cells more peripheral than in rodents; PP cells peripheral.

Vascular supply is rich and fenestrated; islets receive ~10× the blood flow of surrounding exocrine tissue. Insulin (β) and glucagon (α) flow into the portal vein → liver (first-pass effect; insulin acts directly on hepatocytes).

β-cell stimulus-secretion coupling: glucose → GLUT2 → glycolysis → ATP/ADP ratio rises → ATP-sensitive K⁺ channel closes → depolarisation → voltage-gated Ca²⁺ channel opens → Ca²⁺ entry → insulin granule exocytosis. Sulfonylureas close the K⁺ channel directly → insulin release (independent of glucose); risk of hypoglycaemia.

### Liver Regeneration Detail

Liver regeneration after partial hepatectomy is the classical model of regenerative biology:
- 70% hepatectomy in rat → full mass restoration in ~2 weeks.
- Hepatocytes are the principal proliferating cell; oval cells (Hepatic stem cells) participate in severe injury when hepatocyte proliferation is blocked.
- Regeneration is driven by cytokines (TNF, IL-6) and growth factors (HGF, EGF, TGF-α); inhibited by TGF-β once appropriate size is reached.
- Architecture is preserved — original lobular pattern restored.

Liver disease severity:
- **Steatosis** — fat accumulation; reversible.
- **Steatohepatitis** (NASH/ASH) — fat + inflammation + ballooning degeneration; reversible if cause removed.
- **Fibrosis** — collagen deposition (Ito cell activation); potentially reversible if cause removed (new antifibrotic therapies).
- **Cirrhosis** — nodules + fibrous bands; irreversible; portal hypertension, synthetic failure, risk of HCC.

### Liver Sinusoidal Cell Functions

- **Hepatocytes** — most functions.
- **Sinusoidal endothelial cells** — fenestrated (~100 nm pores), no diaphragm; large surface area for plasma exchange; clear macromolecules (hyaluronic acid) from blood; express L-SIGN and SR-B1 (hepatitis B entry).
- **Kupffer cells** — resident macrophages; phagocytose aged RBCs, bacteria from portal blood (first-pass defence against gut-derived pathogens), tumour cells, debris; produce cytokines (TNF, IL-6).
- **Hepatic stellate (Ito) cells** — store vitamin A in lipid droplets (largest reservoir of vitamin A in body); quiescent in normal liver; activated in chronic injury to myofibroblast-like cells producing type I and III collagen → fibrosis.
- **Pit cells** — liver-specific NK cells; tumour surveillance.

### Liver Pathology Recognition

| Pattern | Likely Cause |
|---|---|
| Centrilobular necrosis | Acetaminophen, ischaemia, CCl₄ |
| Midzonal necrosis | Yellow phosphorus |
| Periportal necrosis | Hepatitis B, autoimmune hepatitis |
| Microvesicular steatosis | Reye syndrome, valproate, acute fatty liver of pregnancy |
| Macrovesicular steatosis | NAFLD, alcohol, obesity |
| Canalicular cholestasis | Drugs, sepsis |
| Ductular cholestasis | Primary biliary cholangitis, primary sclerosing cholangitis |
| Mallory-Denk bodies | Alcohol, NASH |
| Ground-glass hepatocytes | Chronic hepatitis B (HBsAg accumulation), drug-induced SER proliferation |'''
    },
    '14': {
        'title': 'Advanced Concepts',
        'body': '''### Mucociliary Escalator Detail

The mucociliary escalator is the principal defence of the conducting zone. Components:
- **Mucus layer** — two sublayers: a low-viscosity periciliary layer (~7 µm, surrounds cilia) and a high-viscosity gel layer (~5–10 µm, on top). Mucus traps inhaled particles (dust, bacteria, allergens).
- **Cilia** — ~200 per cell, ~5–7 µm long, ~0.3 µm diameter; beat at ~10–20 Hz with metachronal rhythm (recovery stroke in the periciliary layer, effective stroke in the gel layer). Velocity of mucus transport: ~5 mm/min in small airways, up to ~20 mm/min in trachea.

Ciliary structure:
- 9+2 axoneme — 9 outer doublet microtubules + 2 central singlets.
- Dynein arms (inner and outer) on outer doublets — motor proteins that generate sliding force.
- Nexin links connect adjacent doublets; radial spokes to central pair; basal body anchors cilium to cell.

Ciliary dysfunction:
- *Primary ciliary dyskinesia (Kartagener syndrome)* — dynein arm defects → immotile cilia → recurrent sinopulmonary infections, bronchiectasis, infertility (sperm flagella), situs inversus (~50%).
- *Smoking* — paralyses cilia; metaplasia (squamous instead of pseudostratified columnar); goblet cell hyperplasia → chronic bronchitis.
- *CF* — dehydrated mucus → impaired ciliary transport → chronic infection.

### Pulmonary Vascular Bed

The lung has a dual blood supply:
- **Pulmonary circulation** — low-pressure (~25/8 mmHg), high-flow, thin-walled; carries deoxygenated blood from RV for gas exchange; arteries accompany bronchi.
- **Bronchial circulation** — high-pressure (systemic pressure), low-flow; supplies the conducting airways down to respiratory bronchioles; bronchial veins drain systemic venous blood.

Pulmonary capillaries form a dense sheet in the alveolar septum; each capillary is shared between adjacent alveoli. The capillary endothelium is continuous and extremely thin (~0.2 µm), apposed to the type I pneumocyte across a fused BM (air-blood barrier).

Pulmonary vascular responses:
- **Hypoxic pulmonary vasoconstriction** — unique to the lung (systemic vessels dilate in hypoxia); diverts blood from poorly ventilated regions to better-ventilated regions; mediated by smooth muscle Ca²⁺ entry. Failure → V/Q mismatch.
- **V/Q ratio** — normal = 0.8 (4 L/min ventilation / 5 L/min perfusion); apex has high V/Q (~3.3) → wasted ventilation; base has low V/Q (~0.6) → physiological shunt.

### Lung Pathophysiology Correlates

| Disease | Pathology | Functional Consequence |
|---|---|---|
| Asthma | Bronchiolar smooth muscle hypertrophy, mucus plugging, eosinophilic inflammation, subepithelial fibrosis | Reversible airflow obstruction (FEV₁/FVC ↓) |
| COPD | Centriacinar emphysema (smoking), panacinar (α₁-antitrypsin), chronic bronchitis (Reid index ↑) | Irreversible airflow obstruction, air trapping |
| Pulmonary fibrosis | Interstitial fibrosis, fibroblast foci, honeycombing | Restrictive pattern, ↓ DLCO |
| Pulmonary embolism | Thrombus in pulmonary artery, often from DVT | V/Q mismatch, RV strain |
| ARDS | Diffuse alveolar damage, hyaline membranes | Severe hypoxaemia, bilateral infiltrates |
| Bronchogenic carcinoma | Most common cancer worldwide; smoking; adenocarcinoma most common type, then squamous, then small-cell | Mass effect, paraneoplastic syndromes |
| Tuberculosis | Caseating granulomas with Langhans giant cells, AFB stain | Cavitary disease, miliary spread, meningitis |'''
    },
    '15': {
        'title': 'Advanced Concepts',
        'body': '''### Melanocyte Biology Extended

Melanocytes are dendritic, neural-crest-derived cells that reside in the stratum basale (~1 melanocyte per 5 basal keratinocytes) and transfer melanosomes to surrounding keratinocytes via their dendritic processes.

Melanin synthesis (melanogenesis):
1. Tyrosine → DOPA → dopaquinone (tyrosinase; rate-limiting; Cu²⁺ cofactor).
2. Dopaquinone → DOPA-chrome → DHICA → eumelanin (brown/black) or dopaquinone + cysteine → pheomelanin (red/yellow).
3. Melanin polymerises on a tyrosinase scaffold within melanosomes (lysosome-related organelles).
4. Mature melanosomes are transported along melanocyte dendrites to tips, then transferred to keratinocytes (cytocrine secretion).
5. Within keratinocytes, melanosomes form a *supranuclear cap* that absorbs UV before it can damage nuclear DNA.

Pigmentation variation:
- *Dark skin* — large, numerous, non-degraded melanosomes in keratinocytes.
- *Light skin* — smaller, fewer melanosomes, more rapid degradation in keratinocytes.
- *Red hair* — predominance of pheomelanin (high cysteine); pheomelanin is photoprotective but also generates ROS upon UV exposure.
- *Albinism* — tyrosinase mutations (oculocutaneous albinism type 1) → no melanin → severe sunburn risk, nystagmus, photophobia.
- *Vitiligo* — autoimmune destruction of melanocytes; well-demarcated depigmented patches.
- *Freckles (ephelides)* — increased melanin production without increase in melanocyte number; UV-induced.
- *Lentigo* — increased melanocytes along the basal layer; benign; solar lentigo = age spot.
- *Melasma* — hyperpigmentation on face; pregnancy, OCPs, sun exposure.

Melanoma staging (Breslow depth, Clark level, ulceration, mitotic rate) is the principal prognostic indicator. ABCDE rule for clinical suspicion: Asymmetry, Border irregularity, Colour variation, Diameter >6 mm, Evolution.

### Hair Growth Cycle Extended

Hair cycles through anagen (growth, 2–7 years), catagen (regression, 2–3 weeks), telogen (rest, 3 months), then back to anagen. At any time, ~85% of scalp hairs are in anagen, ~1–2% in catagen, ~10–15% in telogen.

- *Alopecia areata* — autoimmune destruction of anagen hair follicles; exclamation-point hairs; T-cell mediated.
- *Androgenetic alopecia* — dihydrotestosterone (DHT, from testosterone via 5α-reductase) miniaturises follicles in genetically susceptible individuals; vertex and frontal scalp in men (Hamilton-Norwood pattern); diffuse thinning in women (Ludwig pattern).
- *Telogen effluvium* — premature shift of anagen follicles to telogen after stress (illness, childbirth, surgery); diffuse shedding ~3 months later.

### Sweat Gland Detail

Eccrine sweat glands:
- Simple coiled tubular; ~3–4 million in the body; highest density on palms, soles, forehead.
- Secretory coil (cuboidal/columnar, clear cells + dark cells); reabsorptive duct (two layers of cuboidal cells, no myoepithelium) — primary sweat is isotonic; duct reabsorbs Na⁺ (via ENaC) and Cl⁻ (CFTR); final sweat is hypotonic. In CF, CFTR defective → impaired Cl⁻ reabsorption → salty sweat (basis of the pilocarpine iontophoresis sweat test).
- Stimulated by sympathetic cholinergic fibers (unusual: sympathetic innervation but ACh neurotransmitter); thermoregulation.

Apocrine sweat glands:
- Larger; coiled tubular; secrete by decapitation (apical cytoplasm pinched off).
- Viscous, protein-rich, odourless secretion; bacterial metabolism in the axilla produces characteristic body odour.
- Stimulated by sympathetic adrenergic fibers; become active at puberty (androgen-dependent).

### Wound Healing Detail

Wound healing proceeds in three overlapping phases:

1. **Inflammatory phase** (0–3 days) — haemostasis (platelet plug, fibrin clot); neutrophils (24–48 h); macrophages (day 2–3) phagocytose debris and release cytokines (TGF-β, PDGF, FGF, VEGF).
2. **Proliferative phase** (3 days to 3 weeks) — fibroblasts migrate into wound along fibrin scaffold (fibronectin-mediated); proliferate; produce type III collagen (granulation tissue). Myofibroblasts (TGF-β-driven) contract the wound. Angiogenesis (VEGF-driven) restores blood supply. Re-epithelialisation from wound edges.
3. **Remodelling phase** (3 weeks to 1–2 years) — type III collagen replaced by type I; wound contracts; tensile strength increases to ~80% of unwounded tissue. Matrix metalloproteinases (MMPs) remodel; TIMPs regulate MMPs.

Primary vs secondary intention:
- *Primary* — wound edges approximated (sutured); minimal granulation tissue; minimal scarring.
- *Secondary* — wound left open; abundant granulation tissue; more scarring.

Keloid: scar extends beyond original wound boundaries; exuberant collagen synthesis; more common in dark-skinned individuals; high recurrence after excision. Hypertrophic scar: raised but within wound boundaries.'''
    },
    '16': {
        'title': 'Advanced Concepts',
        'body': '''### Steroid Hormone Synthesis

Steroid hormones are synthesised from cholesterol through a series of cytochrome P450 enzymes and hydroxysteroid dehydrogenases. The pathway:

- **Adrenal cortex zones**:
  - *Glomerulosa* — aldosterone synthase (CYP11B2) at end of pathway → aldosterone (mineralocorticoid).
  - *Fasciculata* — 17α-hydroxylase (CYP17) converts pregnenolone to 17α-hydroxypregnenolone → cortisol; no aldosterone synthase → no aldosterone.
  - *Reticularis* — CYP17 activity + 17,20-lyase activity → DHEA → androstenedione.

- *21-hydroxylase (CYP21)* — required for cortisol and aldosterone synthesis; *most common cause of congenital adrenal hyperplasia (CAH)* (95%); 21-hydroxylase deficiency → impaired cortisol/aldosterone synthesis → shunting into androgen pathway → virilisation of female fetuses (ambiguous genitalia at birth), salt wasting (hypotension, hyperkalaemia) in ~75%.

- *11β-hydroxylase (CYP11B1)* — converts 11-deoxycortisol to cortisol; deficiency → CAH with hypertension (excess 11-deoxycorticosterone has mineralocorticoid activity).

- *17α-hydroxylase (CYP17)* — converts pregnenolone/progesterone to 17α-hydroxy forms; deficiency → CAH with hypertension (excess mineralocorticoids), sexual infantilism (no sex steroids).

Steroid hormones bind intracellular receptors → heat-shock protein dissociation → receptor-ligand complex translocates to nucleus → binds hormone-response elements → modulates gene transcription (slow onset, hours to days).

### Thyroid Hormone Action

T3 binds nuclear thyroid hormone receptors (TRα, TRβ) → recruit co-activators or co-repressors → regulate gene transcription. Effects of thyroid hormone:
- *Basal metabolic rate* — ↑ Na⁺/K⁺-ATPase, mitochondrial biogenesis, O₂ consumption, heat production.
- *Cardiovascular* — ↑ β1-adrenergic receptors → ↑ heart rate, contractility.
- *CNS* — development (myelination, synaptogenesis); deficiency in childhood → cretinism (intellectual disability, short stature, deafness).
- *Growth* — synergises with GH.
- *Bone* — ↑ bone turnover (osteoclast and osteoblast activity).

Hyperthyroidism: weight loss despite appetite, heat intolerance, tachycardia, tremor, anxiety, exophthalmos (Graves-specific), pretibial myxoedema.
Hypothyroidism: weight gain, cold intolerance, bradycardia, fatigue, dry skin, myxoedema, depression. Hashimoto thyroiditis (most common cause in iodine-sufficient regions); iodine deficiency (most common cause worldwide).

### Calcium Homeostasis

PTH (chief cells, parathyroid) — raises blood Ca²⁺:
- *Bone* — stimulates osteoblasts to express RANKL → activates osteoclast precursors → bone resorption (Ca²⁺ + phosphate release).
- *Kidney* — increases distal tubule Ca²⁺ reabsorption; decreases proximal tubule phosphate reabsorption (phosphaturia); stimulates 1α-hydroxylase → 1,25-(OH)₂-vitamin D (calcitriol).
- *Intestine* (indirect) — via calcitriol → increases Ca²⁺ and phosphate absorption.

Calcitonin (C cells, thyroid) — lowers blood Ca²⁺ (minor role in adults):
- Inhibits osteoclast activity; promotes renal Ca²⁺ excretion.

Vitamin D — increases blood Ca²⁺ (and phosphate):
- Skin: 7-dehydrocholesterol → cholecalciferol (vitamin D₃) by UV.
- Liver: cholecalciferol → 25-hydroxyvitamin D (calcidiol) by 25-hydroxylase.
- Kidney: 25-OH-D → 1,25-(OH)₂-vitamin D (calcitriol) by 1α-hydroxylase (stimulated by PTH, inhibited by FGF23 and high phosphate).
- Calcitriol binds VDR → ↑ intestinal Ca²⁺ absorption; ↑ bone mineralisation; feedback inhibition of PTH.

FGF23 (osteocytes) — lowers blood phosphate:
- Inhibits 1α-hydroxylase, stimulates 24-hydroxylase → ↓ calcitriol → ↓ phosphate absorption.
- Causes phosphaturia.

Clinical correlations:
- *Primary hyperparathyroidism* (parathyroid adenoma) → hypercalcaemia (stones, bones, abdominal groans, psychiatric overtones); PTH elevated, phosphate low.
- *Hypoparathyroidism* (post-thyroidectomy, DiGeorge) → hypocalcaemia (tetany, Chvostek and Trousseau signs, prolonged QT); PTH low.
- *Vitamin D deficiency* → rickets (children), osteomalacia (adults); hypocalcaemia, secondary hyperparathyroidism.
- *Paget disease of bone* (out of core scope but illustrative) — disordered bone remodelling with abnormal osteoclasts (paramyxovirus-like inclusions suspected); mosaic pattern of lamellar bone.'''
    },
}

# Insert the Advanced Concepts section before "## Transition" in each chapter
import re
for chap_num, content in ADVANCED.items():
    chapters = sorted(CHAPTERS.glob(f'Chapter{chap_num}_*.md'))
    if not chapters:
        print(f'No chapter for {chap_num}')
        continue
    chap = chapters[0]
    txt = chap.read_text()
    if '## Advanced Concepts' in txt:
        print(f'Skipping {chap.name} (already has Advanced Concepts)')
        continue
    # Find "## Transition" line
    m = re.search(r'^## Transition', txt, re.M)
    if not m:
        print(f'No Transition in {chap.name}')
        continue
    insertion = f"\n## {content['title']}\n\n{content['body']}\n"
    new_txt = txt[:m.start()] + insertion + '\n' + txt[m.start():]
    chap.write_text(new_txt)
    print(f'Updated {chap.name} ({len(content["body"])} chars added)')
