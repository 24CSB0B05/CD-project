def semantic_analysis(text):

    text = text.lower()

    result = {
        "root_cause": "Unknown",
        "impact": "Unknown",
        "affected_component": "Unknown",
        "severity": "Medium"
    }

    if "improper" in text or "unsanitized" in text:
        result["root_cause"] = "Improper input validation"

    if "overflow" in text:
        result["root_cause"] = "Boundary checking failure"

    if "memory" in text:
        result["root_cause"] = "Memory management issue"

    if "traversal" in text:
        result["root_cause"] = "Improper path validation"

    if "authentication" in text:
        result["root_cause"] = "Authentication validation flaw"

    if "malformed" in text:
        result["root_cause"] = "Improper input handling"

    if "execute" in text:
        result["impact"] = "Arbitrary code execution"
        result["severity"] = "High"

    if "access" in text:
        result["impact"] = "Unauthorized access"

    if "crash" in text:
        result["impact"] = "System crash"

    if "script" in text:
        result["impact"] = "Client-side script execution"

    if "denial of service" in text:
        result["impact"] = "Service disruption"

    if "database" in text:
        result["affected_component"] = "Database"

    if "function" in text:
        result["affected_component"] = "Application function"

    if "server" in text:
        result["affected_component"] = "Server"

    if "browser" in text:
        result["affected_component"] = "Web browser"

    if "memory" in text:
        result["affected_component"] = "Memory management"

    return result