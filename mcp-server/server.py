"""MCP server for awesome-ai-red-teaming-jp.

Provides search and retrieval tools for AI Red Teaming / AI Safety resources.
Runs as a local stdio server — no cloud infrastructure required.
"""

from __future__ import annotations

import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("awesome-ai-red-teaming-jp")

# ---------------------------------------------------------------------------
# README parser
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_readme(lang: str = "ja") -> str:
    path = REPO_ROOT / ("README.md" if lang == "ja" else "README.en.md")
    return path.read_text(encoding="utf-8")


def _split_sections(text: str) -> dict[str, str]:
    """Split markdown by ## headings into {section_name: content}."""
    sections: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []

    for line in text.splitlines(keepends=True):
        m = re.match(r"^## (.+)", line)
        if m:
            if current is not None:
                sections[current] = "".join(lines).strip()
            current = m.group(1).strip()
            lines = []
        else:
            lines.append(line)

    if current is not None:
        sections[current] = "".join(lines).strip()

    return sections


def _parse_tool_table(section_text: str) -> list[dict[str, str]]:
    """Parse markdown table rows into list of dicts.

    Expects: | Name | Stars | Language | License | Description |
    """
    tools: list[dict[str, str]] = []
    for line in section_text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|-") or line.startswith("| -"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 5:
            continue
        # Skip header row
        link_match = re.match(r"\[(.+?)]\((.+?)\)", cells[0])
        if not link_match:
            continue
        tools.append(
            {
                "name": link_match.group(1),
                "url": link_match.group(2),
                "stars": cells[1],
                "language": cells[2],
                "license": cells[3],
                "description": cells[4],
            }
        )
    return tools


# Cache parsed data
_cache: dict[str, dict[str, str]] = {}
_tools_cache: dict[str, list[dict[str, str]]] = {}


def _get_sections(lang: str = "ja") -> dict[str, str]:
    if lang not in _cache:
        _cache[lang] = _split_sections(_load_readme(lang))
    return _cache[lang]


def _get_tools_data(lang: str = "ja") -> list[dict[str, str]]:
    if lang not in _tools_cache:
        sections = _get_sections(lang)
        for name, content in sections.items():
            if "ツール" in name or "Tools" in name:
                parsed = _parse_tool_table(content)
                if parsed:
                    _tools_cache[lang] = parsed
                    break
        if lang not in _tools_cache:
            _tools_cache[lang] = []
    return _tools_cache[lang]


# Map for regulation subsections
_REGULATION_MAP_JA = {
    "international": "国際規制・ガイドライン",
    "japan": "日本の規制・ガイドライン",
    "industry": "業界標準",
}

_REGULATION_MAP_EN = {
    "international": "International Regulations",
    "japan": "Japan-Specific Regulations",
    "industry": "Industry Standards",
}


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def search(query: str, lang: str = "ja") -> str:
    """Search all resources by keyword. Returns matching sections and lines.

    Args:
        query: Search keyword (case-insensitive)
        lang: Language - "ja" for Japanese, "en" for English
    """
    if lang not in ("ja", "en"):
        return "Error: lang must be 'ja' or 'en'"

    sections = _get_sections(lang)
    query_lower = query.lower()
    results: list[str] = []

    for name, content in sections.items():
        matching_lines = [
            line
            for line in content.splitlines()
            if query_lower in line.lower()
        ]
        if matching_lines:
            results.append(f"## {name}\n" + "\n".join(matching_lines))

    if not results:
        return f"No results found for '{query}'"
    return "\n\n".join(results)


@mcp.tool()
def get_tools(license: str | None = None, language: str | None = None, lang: str = "ja") -> str:
    """Get the list of open source AI Red Teaming tools with optional filtering.

    Args:
        license: Filter by license (e.g. "MIT", "Apache 2.0")
        language: Filter by programming language (e.g. "Python", "TypeScript")
        lang: README language - "ja" for Japanese, "en" for English
    """
    if lang not in ("ja", "en"):
        return "Error: lang must be 'ja' or 'en'"

    tools = _get_tools_data(lang)
    if not tools:
        return "No tool data found"

    filtered = tools
    if license:
        license_lower = license.lower()
        filtered = [t for t in filtered if license_lower in t["license"].lower()]
    if language:
        language_lower = language.lower()
        filtered = [t for t in filtered if language_lower in t["language"].lower()]

    if not filtered:
        return "No tools match the given filters"

    lines: list[str] = []
    for t in filtered:
        lines.append(
            f"- [{t['name']}]({t['url']}) | {t['stars']} stars | "
            f"{t['language']} | {t['license']} | {t['description']}"
        )
    return "\n".join(lines)


@mcp.tool()
def get_regulations(region: str | None = None, lang: str = "ja") -> str:
    """Get regulations and frameworks for AI Red Teaming.

    Args:
        region: Filter by region - "international", "japan", or "industry". Returns all if omitted.
        lang: README language - "ja" for Japanese, "en" for English
    """
    if lang not in ("ja", "en"):
        return "Error: lang must be 'ja' or 'en'"

    sections = _get_sections(lang)
    reg_map = _REGULATION_MAP_JA if lang == "ja" else _REGULATION_MAP_EN

    if region:
        if region not in reg_map:
            return f"Error: region must be one of: {', '.join(reg_map.keys())}"
        subsection_name = reg_map[region]
        # Find the subsection within the regulations section
        for name, content in sections.items():
            if subsection_name in content:
                # Extract the subsection
                lines = content.splitlines()
                capturing = False
                result_lines: list[str] = []
                for line in lines:
                    if f"### {subsection_name}" in line:
                        capturing = True
                        result_lines.append(line)
                    elif capturing and line.startswith("### "):
                        break
                    elif capturing:
                        result_lines.append(line)
                if result_lines:
                    return "\n".join(result_lines).strip()
        return f"Section '{region}' not found"

    # Return all regulation sections
    parent_key_ja = "規制・フレームワーク"
    parent_key_en = "Regulations & Frameworks"
    parent_key = parent_key_ja if lang == "ja" else parent_key_en

    for name, content in sections.items():
        if parent_key in name:
            return f"## {name}\n\n{content}"

    return "Regulations section not found"


@mcp.tool()
def get_section(name: str, lang: str = "ja") -> str:
    """Get the full content of a section by name.

    Args:
        name: Section name or keyword to match (e.g. "攻撃手法", "Attack Techniques", "MCP", "論文")
        lang: README language - "ja" for Japanese, "en" for English
    """
    if lang not in ("ja", "en"):
        return "Error: lang must be 'ja' or 'en'"

    sections = _get_sections(lang)
    name_lower = name.lower()

    # Exact match first
    for section_name, content in sections.items():
        if section_name.lower() == name_lower:
            return f"## {section_name}\n\n{content}"

    # Partial match
    for section_name, content in sections.items():
        if name_lower in section_name.lower():
            return f"## {section_name}\n\n{content}"

    available = ", ".join(sections.keys())
    return f"Section '{name}' not found. Available sections: {available}"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
