#!/usr/bin/env python3


import logging
import gzip


def collect_kmer_coverage_stats(input_file):
    """Combine the kmer coverage stats for all samples.

    :param input_file: Text TSV file (Sample\tContig\tSum\tMean\tMedian\tHitrate\tVariance)
    :returns all_coverage: Dictionary of counts for each contig (dict[contigID]["sum"/"mean"/"median"])
    """
    allCoverage = {}
    with gzip.open(input_file, "rt") as infh:
        infh.readline()
        for line in infh:
            l = line.strip().split()
            try:
                assert (type(allCoverage[l[1]]) is dict)
            except (AssertionError, KeyError):
                allCoverage[l[1]] = {"sum": 0, "mean": 0, "median": 0}
            allCoverage[l[1]]["sum"] += float(l[2])
            allCoverage[l[1]]["mean"] += float(l[3])
            allCoverage[l[1]]["median"] += float(l[4])
    return allCoverage


def print_kmer_coverage(allCoverage, output_file):
    """Print the combined kmer coverage statistics from collect_kmer_coverage_stats().

    :param output_file: Gzipped Text TSV filepath for writing
    :param allCoverage: Dictionary of counts for each contig (dict[contigID]["sum"/"mean"/"median"])
    :returns: None
    """
    with gzip.open(output_file, "wt", compresslevel=1) as file:
        lines_per_batch = 1000
        batch = ["Contig\tSum\tMean\tMedian"]
        for contig in sorted(allCoverage.keys()):
            batch.append("\t".join([
                contig,
                "{:.{}g}".format(allCoverage[contig]["sum"], 4),
                "{:.{}g}".format(allCoverage[contig]["mean"], 4),
                "{:.{}g}".format(allCoverage[contig]["median"], 4)
            ]))
            if len(batch) >= lines_per_batch:
                file.write('\n'.join(batch) + '\n')
                batch = []
        if batch:
            file.write('\n'.join(batch) + '\n')


def main(input_file, output_file, log_file):
    logging.basicConfig(filename=log_file, filemode="w", level=logging.DEBUG)
    logging.debug("Collecting combined coverage stats")
    allCoverage = collect_combined_coverage_stats(input_file)
    logging.debug("Printing all sample coverage")
    print_sample_coverage(allCoverage, output_file)


if __name__ == "__main__":
    main(snakemake.input[0], snakemake.output.all_cov, snakemake.log[0])
