VULNERABILITY_PATTERNS = {

    "Buffer Overflow": [
        "buffer overflow",
        "heap buffer overflow",
        "stack overflow",
        "out of bounds",
        "memory overflow"
    ],

    "SQL Injection": [
        "sql injection",
        "database query",
        "database",
        "unsanitized input",
        "database injection"
    ],

    "Cross Site Scripting": [
        "cross site scripting",
        "cross-site scripting",
        "xss",
        "script injection"
    ],

    "Use After Free": [
        "use after free",
        "use-after-free",
        "dangling pointer"
    ],

    "Directory Traversal": [
        "directory traversal",
        "path traversal",
        "../"
    ],

    "Authentication Bypass": [
        "authentication bypass",
        "unauthorized access",
        "bypass authentication",
        "credential validation failure"
    ],

    "Integer Overflow": [
        "integer overflow",
        "arithmetic overflow"
    ],

    "Denial Of Service": [
        "denial of service",
        "dos attack",
        "service disruption",
        "resource exhaustion"
    ],

    "Command Injection": [
        "command injection",
        "os command injection",
        "shell command execution"
    ],

    "Race Condition": [
        "race condition",
        "concurrent access issue"
    ],

    "Privilege Escalation": [
        "privilege escalation",
        "gain elevated privileges"
    ]
}