# Vulnerability Description Parser

## About the Project

This project is a simple **Python3-based tool that analyzes vulnerability descriptions and extracts useful security information from them**. Many security databases (like CVE databases) describe vulnerabilities in plain English. Reading and analyzing them manually can take time.

The goal of this project is to take a vulnerability description as input and process it through multiple stages to identify the type of vulnerability and convert it into a structured format.

The design of this system is inspired by **compiler design concepts**, where text is processed step by step using techniques similar to lexical analysis, parsing, and semantic analysis.



## How the System Works

The program processes a vulnerability description through several stages:

1. **Tokenization (Lexer)**
   The text is broken down into smaller tokens such as words.

2. **Vulnerability Detection (Parser)**
   The system checks the tokens and identifies possible vulnerability types.

3. **Semantic Analysis**
   Important security information such as impact or attack type is analyzed.

4. **Intermediate Representation (IR)**
   The extracted information is converted into a structured format (dictionary/JSON style).

This step-by-step approach helps transform unstructured text into structured security information.



## Project Files

```
lexer.py        → Tokenizes the vulnerability description
parser.py       → Detects the vulnerability type
semantic.py     → Performs semantic analysis
ir.py           → Builds the structured representation
utils.py        → Helper functions
main.py         → Runs the complete pipeline
```



## Example

Example vulnerability description:

```
A buffer overflow vulnerability in the web server allows remote attackers to execute arbitrary code.
```

Output produced by the system may include:

* Tokens extracted from the description
* Detected vulnerability type
* Structured representation of the vulnerability

Example structured output:

```
{
  "vulnerability": "buffer overflow",
  "impact": "remote code execution"
}
```



## Running the Project (Mac – Python3)

This project was developed and tested using **Python3 on macOS**.

### Step 1: Clone the repository

```
git clone https://github.com/yourusername/repository-name.git
```

### Step 2: Go to the project folder

```
cd repository-name
```

### Step 3: Run the program

```
python3 main.py
```

Make sure Python3 is installed on your system.



## Why This Project

This project demonstrates how **concepts from compiler design can be applied to cybersecurity problems**. Instead of compiling programming languages, the system processes security descriptions and extracts meaningful information from them.

It also shows how simple text processing techniques can help in **automating vulnerability analysis**.



## Possible Improvements

Some ideas that could be added in the future:

* Support for a larger CVE dataset
* Better pattern detection for vulnerabilities
* More detailed semantic analysis
* Visualization of detected vulnerabilities




