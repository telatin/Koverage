![](koverage.png)


[![](https://img.shields.io/static/v1?label=CLI&message=Snaketool&color=blueviolet)](https://github.com/beardymcjohnface/Snaketool)
[![](https://img.shields.io/static/v1?label=Licence&message=MIT&color=black)](https://opensource.org/license/mit/)
![](https://img.shields.io/static/v1?label=Install%20with&message=PIP&color=success)
[![](https://github.com/beardymcjohnface/Koverage/actions/workflows/py-app.yaml/badge.svg)](https://github.com/beardymcjohnface/Koverage/actions/workflows/py-app.yaml/)

---

Quickly get coverage statistics given reads and an assembly.

# Motivation

While there are tools that will calculate read-coverage statistics, they do not scale particularly well for large 
datasets, large sample numbers, or large reference FASTAs.
Koverage is designed to place minimal burden on I/O and RAM to allow for maximum scalability.

# Install

Koverage is still in development and is not yet packaged on Bioconda or PyPI.
Setup.py may be missing some packages but just install them with pip.

```shell
git clone https://github.com/beardymcjohnface/Koverage.git
cd Koverage
pip install -e .
```

# Usage

Get coverage statistics from mapped reads (default method).

```shell
koverage run --reads readDir --ref assembly.fasta
```

Get coverage statistics using kmers (scales much better for very large reference FASTAs).

```shell
koverage run --reads readDir --ref assembly.fasta kmer
```

Any unrecognised commands are passed onto Snakemake.
Run Koverage on a HPC using a Snakemake profile.

```shell
koverage run --reads readDir --ref assembly.fasta --profile mySlurmProfile
```

# Test

You can test the methods like so.

```shell
# test default method
koverage test

# test all methods
koverage test map kmer bench
```

# Outputs

## Mapping-based

Default output files using fast estimations for contig coverage and variance.

<details>
    <summary><b>sample_coverage.tsv</b></summary>
Per sample and per contig counts.

Column | description
--- | ---
Sample | Sample name derived from read file name
Contig | Contig ID from assembly FASTA
Count | Raw mapped read count
RPM | Reads per million
RPKM | Reads per kilobase million
RPK | Reads per kilobase
TPM | Transcripts per million
Hitrate | _Estimated_ fraction of contig with depth > 0
Variance | _Estimated_ read depth variance

</details>

<br>

<details>
    <summary><b>all_coverage.tsv</b></summary>
Per contig counts (all samples).

Column | description
--- | ---
Contig | Contig ID from assembly FASTA
Count | Raw mapped read count
RPM | Reads per million
RPKM | Reads per kilobase million
RPK | Reads per kilobase
TPM | Transcripts per million

</details>

_(more outputs to come, watch this space)_
    
## Kmer-based

Outputs for kmer-based coverage metrics.
Kmer outputs are gzipped as it is anticipated that this method will be used with very large reference FASTA files.

<details>
    <summary><b>sample_kmer_coverage.NNmer.tsv.gz</b></summary>
Per sample and contig kmer coverage.

Column | description
--- | ---
Sample | Sample name derived from read file name
Contig | Contig ID from assembly FASTA
Sum | Sum of sampled kmer depths
Mean | Mean sampled kmer depth
Median | Median sampled kmer depth
Hitrate | Fraction of kmers with depth > 0
Variance | Variance of lowest 95 % of sampled kmer depths

</details>

<br>

<details>
    <summary><b>all_kmer_coverage.NNmer.tsv.gz</b></summary>
Contig kmer coverage (all samples).

Column | description
--- | ---
Contig | Contig ID from assembly FASTA
Sum | Sum of sampled kmer depths
Mean | Mean sampled kmer depth
Median | Median sampled kmer depth

</details>

_(more outputs to come, watch this space)_    
