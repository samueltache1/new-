"""Output formatting helpers for the CLI."""
import sys


def _bold(text: str) -> str:
    """Return bold text if output is a terminal."""
    if sys.stdout.isatty():
        return f"\033[1m{text}\033[0m"
    return text


def format_report(report: dict) -> str:
    """Return a human-readable multi-line string for a report dict."""
    lines = []
    for key, value in report.items():
        lines.append(f"{_bold(key.capitalize())}: {value}")
    return "\n".join(lines)
