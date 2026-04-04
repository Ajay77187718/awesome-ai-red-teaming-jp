"""Tests for the MCP server."""

from server import (
    _get_sections,
    _get_tools_data,
    _split_sections,
    get_regulations,
    get_section,
    get_tools,
    search,
)


# ---------------------------------------------------------------------------
# Parser tests
# ---------------------------------------------------------------------------


def test_split_sections_basic():
    text = "# Title\n\nintro\n\n## A\n\ncontent a\n\n## B\n\ncontent b\n"
    sections = _split_sections(text)
    assert "A" in sections
    assert "B" in sections
    assert "content a" in sections["A"]
    assert "content b" in sections["B"]


def test_get_sections_ja():
    sections = _get_sections("ja")
    assert len(sections) > 0
    # Section names include emojis, use partial match
    section_names = " ".join(sections.keys())
    assert "ツール" in section_names
    assert "攻撃手法" in section_names


def test_get_sections_en():
    sections = _get_sections("en")
    assert len(sections) > 0
    section_names = " ".join(sections.keys())
    assert "Tools" in section_names
    assert "Attack Techniques" in section_names


def test_get_tools_data_ja():
    tools = _get_tools_data("ja")
    assert len(tools) >= 4
    names = [t["name"] for t in tools]
    assert "Promptfoo" in names
    assert "Garak" in names
    assert "PyRIT" in names


def test_get_tools_data_fields():
    tools = _get_tools_data("ja")
    for tool in tools:
        assert "name" in tool
        assert "url" in tool
        assert "stars" in tool
        assert "language" in tool
        assert "license" in tool


# ---------------------------------------------------------------------------
# Tool tests
# ---------------------------------------------------------------------------


def test_search_finds_results():
    result = search("Promptfoo", "ja")
    assert "Promptfoo" in result
    assert "No results" not in result


def test_search_no_results():
    result = search("xyznonexistent12345", "ja")
    assert "No results" in result


def test_search_case_insensitive():
    result = search("promptfoo", "ja")
    assert "Promptfoo" in result


def test_search_invalid_lang():
    result = search("test", "fr")
    assert "Error" in result


def test_get_tools_all():
    result = get_tools(lang="ja")
    assert "Promptfoo" in result
    assert "Garak" in result


def test_get_tools_filter_language():
    result = get_tools(language="Python", lang="ja")
    assert "Garak" in result
    assert "PyRIT" in result
    assert "Promptfoo" not in result


def test_get_tools_filter_license():
    result = get_tools(license="MIT", lang="ja")
    assert "Promptfoo" in result
    assert "Garak" not in result


def test_get_tools_no_match():
    result = get_tools(license="GPL", lang="ja")
    assert "No tools match" in result


def test_get_regulations_all():
    result = get_regulations(lang="ja")
    assert "規制" in result


def test_get_regulations_japan():
    result = get_regulations("japan", "ja")
    assert "AISI" in result or "日本" in result


def test_get_regulations_international():
    result = get_regulations("international", "ja")
    assert "EU AI Act" in result or "NIST" in result


def test_get_regulations_invalid_region():
    result = get_regulations("mars", "ja")
    assert "Error" in result


def test_get_section_exact():
    result = get_section("攻撃手法", "ja")
    assert "プロンプトインジェクション" in result


def test_get_section_partial():
    result = get_section("MCP", "ja")
    assert "エージェント" in result or "MCP" in result


def test_get_section_english():
    result = get_section("Attack Techniques", "en")
    assert "Prompt Injection" in result


def test_get_section_not_found():
    result = get_section("存在しないセクション", "ja")
    assert "not found" in result
    assert "Available sections" in result
