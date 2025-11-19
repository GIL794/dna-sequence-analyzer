# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The DNA Sequence Analyzer team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to:

**security@dna-sequence-analyzer.dev**

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

### What to Include in Your Report

Please include the following information in your report:

- **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s)** related to the manifestation of the issue
- **Location of the affected source code** (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit it
- **Your contact information** for follow-up questions

This information will help us triage your report more quickly.

## Response Process

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
2. **Investigation**: Our team will investigate and validate the vulnerability
3. **Status Updates**: We will keep you informed of the progress as we work on a fix
4. **Fix Development**: We will develop and test a fix for the vulnerability
5. **Disclosure**: We will publicly disclose the vulnerability after a fix is released

## Disclosure Policy

- **Security advisory**: Published when a fix is available
- **Credit**: We will give credit to the reporter unless they wish to remain anonymous
- **Timeline**: We aim to release security fixes within 90 days of initial report

## Security Best Practices for Users

When using DNA Sequence Analyzer:

### Data Security

- **Do not upload sensitive or proprietary sequences** to public instances
- **Run locally** when analyzing confidential data
- **Clear browser cache** after analyzing sensitive sequences
- **Use HTTPS** connections when accessing remote instances

### Installation Security

- **Verify package signatures** when installing dependencies
- **Use virtual environments** to isolate dependencies
- **Keep dependencies updated** by regularly running `pip install -U -r requirements.txt`
- **Review code changes** before updating to new versions

### Application Security

- **Validate input sequences** before processing
- **Limit file upload sizes** to prevent resource exhaustion
- **Run with least privilege** - don't run as root/administrator
- **Monitor logs** for unusual activity

## Known Security Considerations

### File Upload Security

The application accepts FASTA files from users:

- File size limits are enforced (max 200 MB)
- Only text content is processed
- Files are parsed in memory without being saved to disk by default
- Input validation is performed on all sequences

### Dependency Security

We regularly update dependencies to address known vulnerabilities:

- Monthly security updates for critical dependencies
- Quarterly updates for all dependencies
- Automated scanning with GitHub Dependabot

### Data Privacy

- **Local execution**: By default, all processing happens locally
- **No external calls**: The application doesn't send data to external services
- **No persistent storage**: Data is not stored between sessions (unless explicitly saved by user)
- **Session isolation**: Each user session is independent

## Security Update Notifications

To receive security updates:

1. **Watch the repository** on GitHub and enable security alerts
2. **Subscribe to releases** to be notified of new versions
3. **Check CHANGELOG.md** regularly for security-related updates
4. **Follow @dna_analyzer** on Twitter for announcements (when available)

## Security Audit History

| Date       | Type          | Findings | Status   |
|------------|---------------|----------|----------|
| 2025-01-15 | Self-audit    | 0 high   | Complete |

## Scope

### In Scope

- Vulnerabilities in the core application (app.py, src/)
- Security issues in dependencies
- Configuration vulnerabilities
- Data handling and validation issues
- Authentication/authorization (if implemented)

### Out of Scope

- Vulnerabilities in third-party services (NCBI, Ensembl, etc.)
- Issues requiring physical access to the system
- Social engineering attacks
- Denial of service attacks against properly configured systems

## Bug Bounty Program

We currently do not offer a paid bug bounty program. However, we deeply appreciate security researchers who help us keep the application secure. We will:

- Publicly acknowledge your contribution (with your permission)
- List you in our SECURITY_HALL_OF_FAME.md
- Provide a letter of recommendation upon request

## Security-Related Configuration

### Recommended Deployment Settings

When deploying DNA Sequence Analyzer in production:

```bash
# Run with limited user privileges
sudo -u dna-analyzer streamlit run app.py

# Use a reverse proxy (nginx) with rate limiting
# Configure SSL/TLS certificates

# Set appropriate file permissions
chmod 755 app.py
chmod 644 requirements.txt

# Disable directory listing
# Configure firewall rules
```

## Contact

For security concerns, contact:
- **Email**: security@dna-sequence-analyzer.dev
- **PGP Key**: Available upon request for encrypted communications

For general questions about security:
- **GitHub Issues**: [Security-related questions](https://github.com/GIL794/dna-sequence-analyzer/issues)
- **Discussions**: [Security discussions](https://github.com/GIL794/dna-sequence-analyzer/discussions)

## Acknowledgments

We would like to thank the following security researchers for responsibly disclosing vulnerabilities:

- *List will be updated as vulnerabilities are reported and fixed*

---

**Last Updated**: November 2025
