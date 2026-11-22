#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d55.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==55
assert c['vertices']==m['norm_one_vertices']==60 and c['pairs']==m['exact_labelled_squared_pairs']==1770
assert c['affine_rank']==c['centered_gram_rank']==55
assert c['eigenvalue_30_multiplicity']==m['model_eigenvalue_30_multiplicity']==49
assert c['eigenvalue_59_over_2_multiplicity']==m['model_eigenvalue_59_over_2_multiplicity']==4
assert c['parent_tag_commit']=='b6c003db566c63993652e3e717dd01f654f3ad39'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24430643'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24430643','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension fifty-five' in m['keywords']
assert 'forty-ninefold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24430643' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('fifty-four','forty-eightfold','fifty-six','fiftyfold'))
note=(R/'publication/POLYBRUTUS_55D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24430643','10.5281/zenodo.24407952'))
print('D55_CURRENT_9_KEYWORDS_STRUCTURED_PARENT_AND_SEPARATE_D54_D7_REFERENCES_PASS')
