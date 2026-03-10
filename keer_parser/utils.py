def load_cves(filepath):

    cves = []

    with open(filepath, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line:
                cves.append(line)

    return cves