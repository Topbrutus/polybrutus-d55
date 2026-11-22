# Polybrutus D55 - 60-point exact labelled Euclidean metric

**Only scientific predecessor:** Topbrutus/polybrutus-d54@v0.1.0, peeled commit b6c003db566c63993652e3e717dd01f654f3ad39, Zenodo DOI 10.5281/zenodo.24430643, original complete frozen ZIP SHA-256 efecef3743401fc6100f3f0e223a75cd4683b38852fb5150229ae279675a24be and exact original certificate SHA-256 4c035c5e54293b8561fd37e07c637fd765ea7465fba67e49ca6e815b48a890ec.

## Exact conservative Euclidean extension

Embed all 59 predecessor unit vectors p_i by q_i=(p_i,0), and adjoin one perpendicular norm-one vector q_60. The old C(59,2)=1711 labelled squared distances remain unchanged. For each of the 59 new pairs, d²=2R². Total C(60,2)=1770 unordered labelled squared distances.

Construct explicit rational Gram G as direct orthogonal sum of seven canonical unit points (rank 3), a centered regular five-point unit simplex with cross-dot -1/4 (rank 4), and 48 mutually independent perpendicular norm-one axes (rank 48). Hence G=XXᵀ is positive semidefinite, diagonal one, exact rank **3+4+48=55**.

Define D_ii=0 and D_ij=2-2G_ij. The centering H=I-11ᵀ/60 yields B=-(HDH)/2=HGH, PSD exact rank 55. An inherited antipodal canonical pair ensures the origin belongs to the affine hull, proving the metric's minimum affine Euclidean realization dimension is **55** (56-coordinate storage).

Exhaustive normalized squared-distance histogram at R=1: \`k=4d²/R²\` 4:6, 7:2, 8:1739, 9:3, 10:10, 12:6, 13:2, 16:2, total 1770 unordered pairs. Exact sum at R=1: **14207/4**.

## Separately stipulated ideal weighted complete graph

For scalar unit masses and positive symmetric weights w_ij=1/d_ij², each of the 59 new edges has weight 1/2. The Laplacian join has block form L55=[[L54+I59/2,-1_59/2],[-1_59ᵀ/2,59/2]].

Characteristic recurrence: chi60(z)=z(z-30)chi59(z-1/2)/(z-1/2).
With the original seven-point factor f6(z)=chiP7(z)/z, the selected-model closed form is:
chi60(z)=z(z-30)^49(z-59/2)^4*f6(z-53/2).

Exact rank-nullity of the rational Laplacian yields eigenvalue **30** of multiplicity **49** and **59/2** of multiplicity **4**. These are dimensionless model modes, not observed frequencies.

**Bibliography:** direct D54 DOI 10.5281/zenodo.24430643, historical D7 DOI 10.5281/zenodo.24407952.
