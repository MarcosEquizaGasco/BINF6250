from project01 import parse_line, read_file
import pytest

# PARSE_LINE(): test case for line with rare disease (expected behavior)
def test_rare_disease():
    disease = parse_line('AF_EXAC=0.00007;CLNDN=Immunodeficiency_38_with_basal_ganglia_calcification')
    assert disease == ['Immunodeficiency_38_with_basal_ganglia_calcification']

# PARSE_LINE(): test case for line with no rare variant (no AF_EXAC)
def test_no_rare_disease():
    no_disease = parse_line('CLNDN=Immunodeficiency_38_with_basal_ganglia_calcification')
    assert no_disease == []

# PARSE_LINE(): test case for line with multiple diseases (separated by |)
def test_multiple_diseases():
    diseases = parse_line('AF_EXAC=0.000007;CLNDN=disease1|disease2')
    assert diseases == ['disease1', 'disease2']

# PARSE_LINE(): test case for line with "not_specified"
def test_not_specified():
    not_specified = parse_line('AF_EXAC=0.00007;CLNDN=not_specified')
    assert not_specified == []

# PARSE_LINE(): test case for line with "not_provided"
def test_not_provided():
    not_provided = parse_line('AF_EXAC=0.00007;CLNDN=not_provided')
    assert not_provided == []

# READ_FILE(): test case for expected behavior
def test_rare_disease_dict(tmp_path):
    content = '1	1014255	571208	G	A	.	.	AF_ESP=0.00008;AF_EXAC=0.00003;ALLELEID=556509;CLNDISDB=MedGen:C4015293,OMIM:616126,Orphanet:ORPHA319563;CLNDN=Immunodeficiency_38_with_basal_ganglia_calcification;CLNHGVS=NC_000001.11:g.1014255G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=ISG15:9636;MC=SO:0001583|missense_variant;ORIGIN=1'
    p = tmp_path / 'test'
    p.mkdir()
    file = p / 'normal.vcf'
    file.write_text(content, encoding='utf-8')
    assert read_file(file) == {'Immunodeficiency_38_with_basal_ganglia_calcification': 1}

# READ_FILE(): test case for file with only # lines
def test_no_data_dict(tmp_path):
    content = '##INFO=<ID=AF_ESP,Number=1,Type=Float,Description="allele frequencies from GO-ESP">'
    p = tmp_path / 'test'
    p.mkdir()
    file = p / 'no_data.vcf'
    file.write_text(content, encoding='utf-8')
    assert read_file(file) == {}

# READ_FILE(): test case for file with no rare diseases (no AF_EXAC lines)
def test_no_disease_dict(tmp_path):
    content = '1	1014012	661610	C	T	.	.	ALLELEID=626468;CLNDISDB=MedGen:C4015293,OMIM:616126,Orphanet:ORPHA319563;CLNDN=Immunodeficiency_38_with_basal_ganglia_calcification;CLNHGVS=NC_000001.11:g.1014012C>T;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=ISG15:9636;MC=SO:0001583|missense_variant;ORIGIN=1'
    p = tmp_path / 'test'
    p.mkdir()
    file = p / 'no_disease.vcf'
    file.write_text(content, encoding='utf-8')
    assert read_file(file) == {}

# READ_FILE(): test case for file with no rare diseases (AF_EXAC too high)
def test_no_rare_disease_dict(tmp_path):
    content = '1	1014012	661610	C	T	.	.	AF_EXAC=0.5;ALLELEID=626468;CLNDISDB=MedGen:C4015293,OMIM:616126,Orphanet:ORPHA319563;CLNDN=Immunodeficiency_38_with_basal_ganglia_calcification;CLNHGVS=NC_000001.11:g.1014012C>T;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=ISG15:9636;MC=SO:0001583|missense_variant;ORIGIN=1'
    p = tmp_path / 'test'
    p.mkdir()
    file = p / 'no_rare_disease.vcf'
    file.write_text(content, encoding='utf-8')
    assert read_file(file) == {}