# Polybrutus 55D: Exact 60-point Euclidean metric and a forty-ninefold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible synthetic case study**
**AI disclosure:** OpenAI ChatGPT (Astra) materially assisted two independently implemented rational programs, calculations, manuscript and controlled publication. AI is not the scientific author.

## Abstract

We construct an exact synthetic Euclidean labelled squared-distance metric on 60 norm-one points by adjoining one perpendicular norm-one point to the immutable Polybrutus D54 [1]. All 1711 predecessor labelled squared distances remain unchanged; 59 new squared distances each equal 2R², producing 1770 unordered labelled pairs. The centered Euclidean Gram is PSD of exact rank 55, proving minimum affine Euclidean realization dimension 55 for this particular constructed metric. In a separately stipulated scalar-unit-mass ideal complete weighted graph with w_ij=1/d_ij², exact rational Laplacian eigenspace nullities yield eigenvalue 30 multiplicity 49 and 59/2 multiplicity 4. Two independently implemented rational verifiers test all 1770 labels and 1711 original parent labels, source archive provenance and exact spectral ranks. No observed physical hertz or extra spacetime dimensions are claimed.

## 1. Authentic immutable scientific source and conservation

The only immediate scientific parent is St-Pierre, Polybrutus D54 [1], DOI 10.5281/zenodo.24430643, original source tag Topbrutus/polybrutus-d54@v0.1.0, real peeled scientific commit b6c003db566c63993652e3e717dd01f654f3ad39. Its complete original frozen scientific Git tag ZIP is stored byte-identically at prior/d54/frozen_scientific_tag_v0.1.0.zip, 3208661 bytes, 32 entries, CRC PASS, SHA256 efecef3743401fc6100f3f0e223a75cd4683b38852fb5150229ae279675a24be. Older complete original source archives are nested within this immutable original ZIP. Original D54 certificate prior/d54/results/certificate_d54.json is preserved byte-identically SHA256 4c035c5e54293b8561fd37e07c637fd765ea7465fba67e49ca6e815b48a890ec; both independent programs check archive SHA, CRC, original certificate and all old labels.

Let p_i, i=1,...,59, denote all parent unit vectors. Embed q_i=(p_i,0) in an extended Euclidean coordinate space and append perpendicular unit point q_60. All C(59,2)=1711 predecessor labelled squared distances remain exactly unchanged. Each ||q_60-q_i||²=2R², providing 59 new squared distances. In total C(60,2)=1770=1711+59 exact unordered labelled pairs. This explicit construction is mathematical, not evidence for additional physical spacetime dimensions.

## 2. Rational Gram, centered rank and distance audit

Construct rational Gram G as an orthogonal block sum: seven canonical unit points of rank 3, five-point centered regular unit simplex of rank 4 with mutual inner products -1/4, and 48 independent perpendicular unit axes. Thus G=XXᵀ is PSD with unit diagonal and exact rank 3+4+48=55. Define D_ii=0, D_ij=2-2G_ij, and H=I-11ᵀ/60. Then B=-(HDH)/2=HGH is PSD of exact rank 55. The canonical inherited antipodal pair implies the origin is in the affine hull, so minimum affine Euclidean realization dimension equals 55, with 56 storage coordinates.

At R=1, the exhaustive normalized squared-distance histogram k=4d²/R² is 4:6, 7:2, 8:1739, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 1770 pairs. Their exact sum is 14207/4. Both verifiers compare the labelled 1711 predecessor values against the authentic original D54 certificate; matching only a histogram would be insufficient.

## 3. Separately stipulated ideal graph and exact spectral rank

Separately stipulate positive symmetric weights w_ij=1/d_ij² on the complete graph, with scalar unit masses. The new unit point joins all 59 predecessor vertices at weight 1/2. The chosen ideal Laplacian has join L55=[[L54+I59/2,-1_59/2],[-1_59ᵀ/2,59/2]]. Its characteristic-polynomial recurrence is chi60(z)=z(z-30)chi59(z-1/2)/(z-1/2). Using the old seven-point factor f6(z)=chiP7(z)/z gives chi60(z)=z(z-30)^49(z-59/2)^4*f6(z-53/2).

Independent exact rational eigenspace ranks yield eigenvalue 30 multiplicity 49 and eigenvalue 59/2 multiplicity 4. These mathematical dimensionless ideal graph values are not observed acoustic or electromagnetic frequencies, physical particles or new spacetime dimensions.

## 4. Independent verification and adversarial counterexamples

Primary src/verify_d55.py builds the exact rational Gram with SymPy and enumerates all 1770 squared-distance labels, authenticates parent source ZIP SHA/CRC and original certificate bytes, and checks centered Euclidean Gram rank and ideal graph Laplacian eigenspaces. Independent tests/independent_d55.py uses separately defined Python fractions.Fraction distance rules, without importing the primary Gram generator, and reconstructs all 1770 labels plus all 1711 D54 parent labels, centered rank and graph nullities. Both independently generate an identical deterministic JSON certificate results/certificate_d55.json.

Four adversarial main-program negative controls detect altered new pair, duplicated last point, nonperpendicular tilted norm-one new point, and histogram-preserving label permutation; independent code rejects damaged labels and histogram-preserving relabelling.

An old D47 certificate includes an inaccurate textual D46 grandparent Git commit, disclosed since D48; original source archives are preserved byte-identically, and D55 authenticates its real direct parent D54 scientific source independently.

## 5. Reproduction, bibliography and scientific limitations

Python 3.12 and sympy==1.14.0 reproduce these exact calculations. Orthogonal Euclidean vector extension and weighted complete-graph joins are established constructions. The result is one explicit synthetic metric and freely stipulated dimensionless graph, not a new universal theorem, independently peer-reviewed physics, an empirical discovery, new particles, measured hertz or extra physical spacetime dimensions.

The public Zenodo preprint must include nine current keywords including fifty-five and forty-ninefold, a structured isDerivedFrom relation to the direct D54 DOI 10.5281/zenodo.24430643, and a separate references field citing D54 [1] and historical Polybrutus D7 [2]. Each original source ZIP, scientific PDF and exact certificate JSON must pass public API file size and checksum verification.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 54D: Exact 59-Point Euclidean Metric and Forty-Eightfold Ideal Graph Mode. Zenodo. DOI: 10.5281/zenodo.24430643. https://doi.org/10.5281/zenodo.24430643

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo. DOI: 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Complete original Polybrutus D54 frozen scientific source v0.1.0, GitHub https://github.com/Topbrutus/polybrutus-d54/tree/v0.1.0, peeled commit b6c003db566c63993652e3e717dd01f654f3ad39. Original ZIP embedded byte-identically.
