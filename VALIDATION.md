# Polybrutus D55 exact-source validation and publication protocol

1. Read and authenticate frozen scientific D54 source Git tag \`v0.1.0\` peeled commit \`b6c003db566c63993652e3e717dd01f654f3ad39\`, Zenodo DOI 10.5281/zenodo.24430643, original full source ZIP SHA256 efecef3743401fc6100f3f0e223a75cd4683b38852fb5150229ae279675a24be, original D54 certificate SHA256 4c035c5e54293b8561fd37e07c637fd765ea7465fba67e49ca6e815b48a890ec. Two verifiers check ZIP CRC, embedded original certificate byte identity and all parent labels.
2. Recompute 60 unit points, all 1770 exact labelled squared-distance pairs, all 1711 old D54 labels, 59 new squared distances each 2R², Gram PSD and affine rank 55.
3. Verify separately selected ideal scalar-unit-mass weighted complete graph eigenspaces: eigenvalue 30 multiplicity 49 and 59/2 multiplicity 4. No inference of physical hertz.
4. Independently reconstruct all labels with fractions.Fraction without importing SymPy Gram constructor. Require same deterministic JSON certificate and 4/4 adversarial primary negative controls.
5. GitHub Actions must pass on main and frozen scientific tag before Zenodo release, then third postpublication main CI success.
6. Zenodo original frozen scientific ZIP, PDF preprint and deterministic certificate JSON need public MD5, sizes and names equal local SHA256 originals, nine fifty-five/forty-ninefold keywords, structured isDerivedFrom DOI D54 and separate references D54/D7.
7. Verify public DOI, file checksums and relationships, write documentary \`main\` commit only, save checkpoint and central Memoria register.

    python -m pip install sympy==1.14.0
    python src/verify_d55.py
    python tests/independent_d55.py
    python src/check_zenodo_metadata.py
