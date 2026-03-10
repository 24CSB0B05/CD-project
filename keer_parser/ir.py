def build_ir(description, vuln_type, semantics):

    ir = {
        "description": description.strip(),
        "vulnerability_type": vuln_type,
        "root_cause": semantics["root_cause"],
        "impact": semantics["impact"],
        "affected_component": semantics["affected_component"],
        "severity": semantics["severity"]
    }

    return ir