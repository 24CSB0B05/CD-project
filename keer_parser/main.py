import json

from lexer import tokenize
from parser import detect_vulnerability
from semantic import semantic_analysis
from ir import build_ir
from utils import load_cves


def process_cve(cve_text):

    tokens = tokenize(cve_text)

    vuln_type = detect_vulnerability(cve_text)

    semantics = semantic_analysis(cve_text)

    ir = build_ir(cve_text, vuln_type, semantics)

    return ir


def generate_statistics(results):

    stats = {}

    for r in results:

        vuln = r["vulnerability_type"]

        stats[vuln] = stats.get(vuln, 0) + 1

    return stats


def main():

    cves = load_cves("data/cves.txt")

    results = []

    for cve in cves:

        parsed = process_cve(cve)

        results.append(parsed)

    with open("output.json", "w") as f:

        json.dump(results, f, indent=4)

    print("\n===== CVE Vulnerability Mapping Output =====\n")

    print(json.dumps(results, indent=4))

    stats = generate_statistics(results)

    print("\n===== Vulnerability Statistics =====\n")

    for k,v in stats.items():

        print(k, ":", v)


if __name__ == "__main__":

    main()


