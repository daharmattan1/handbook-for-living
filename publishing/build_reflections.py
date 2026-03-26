"""
Build the reflections Typst files from markdown sources.
Converts markdown to Typst syntax and assembles the full archive and curated editions.

Usage:
  python build_reflections.py          # Build both editions
  python build_reflections.py full     # Full archive only
  python build_reflections.py curated  # Curated only
"""

import os
import sys
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PUB = REPO / "publishing"

AGENTS = ["buddha", "confucius", "jesus", "laozi", "muhammad", "zoroaster"]
AGENT_TITLES = {
    "buddha": "Buddha — The Diagnostician",
    "confucius": "Confucius — The Form-Builder",
    "jesus": "Jesus — The Wound",
    "laozi": "Laozi — The Subtractor",
    "muhammad": "Muhammad — The Builder",
    "zoroaster": "Zoroaster — The Fire",
}

SESSION_NAMES = {
    "00": "Definition",
    "01": "Structure",
    "02": "Format",
    "03": "Chapter 1: Loss",
    "04": "Chapter 2: Tuesday",
    "05": "Chapter 3: The Commute",
    "06": "Chapter 4: The Glass",
    "07": "Chapter 5: The Cup",
    "08": "Chapter 6: The Morning",
}

# Sessions to include in curated edition (most substantive)
CURATED_SESSIONS = ["00", "01", "04", "06", "07", "08"]
CURATED_AGENTS_HWSEO = ["buddha", "jesus", "muhammad", "laozi"]  # Subset for how-we-see


def md_to_typst(text: str) -> str:
    """Convert markdown text to Typst syntax."""
    lines = text.split("\n")
    result = []
    for line in lines:
        # Convert headings
        if line.startswith("#### "):
            result.append(f"==== {line[5:]}")
        elif line.startswith("### "):
            result.append(f"=== {line[4:]}")
        elif line.startswith("## "):
            result.append(f"== {line[3:]}")
        elif line.startswith("# "):
            result.append(f"= {line[2:]}")
        # Convert bold
        elif "**" in line:
            line = re.sub(r'\*\*(.+?)\*\*', r'*\1*', line)
            result.append(line)
        # Convert italic (single *)
        elif re.search(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', line):
            line = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'_\1_', line)
            result.append(line)
        else:
            result.append(line)
    return "\n".join(result)


def read_and_convert(filepath: Path) -> str:
    """Read a markdown file and convert to Typst."""
    if not filepath.exists():
        return f"// File not found: {filepath.name}\n"
    text = filepath.read_text(encoding="utf-8")
    return md_to_typst(text)


def json_to_typst(filepath: Path, title: str) -> str:
    """Convert a JSON facts file to readable Typst."""
    if not filepath.exists():
        return ""
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return f"// Could not parse: {filepath.name}\n"

    lines = [f"==== {title}\n"]
    if isinstance(data, list):
        for item in data[:20]:  # Limit to top 20 entries
            if isinstance(item, dict):
                # Extract key fields
                text = item.get("text", item.get("formulation", item.get("insight", item.get("pattern", ""))))
                session = item.get("session", item.get("source_session", ""))
                if text:
                    lines.append(f"- {text}")
                    if session:
                        lines.append(f"  _Session: {session}_\n")
                    else:
                        lines.append("")
            elif isinstance(item, str):
                lines.append(f"- {item}\n")
    elif isinstance(data, dict):
        for key, value in list(data.items())[:20]:
            if isinstance(value, str):
                lines.append(f"- *{key}:* {value}\n")
            elif isinstance(value, list):
                lines.append(f"- *{key}:* {', '.join(str(v) for v in value[:5])}\n")

    return "\n".join(lines)


def build_full_archive() -> str:
    """Build the full archive Typst content."""
    parts = []

    # PART I: THE PROCESS
    parts.append("= Part I: The Process\n")
    parts.append("_Session-by-session narratives of how the collaboration unfolded._\n")

    for session_num in sorted(SESSION_NAMES.keys()):
        session_name = SESSION_NAMES[session_num]
        process_file = REPO / "narrative" / "process" / f"session_{session_num}_{session_name.lower().split(':')[0].replace(' ', '_')}.md"
        # Try various filename patterns
        candidates = list((REPO / "narrative" / "process").glob(f"session_{session_num}_*.md"))
        if candidates:
            parts.append(f"== Session {int(session_num)}: {session_name}\n")
            parts.append(read_and_convert(candidates[0]))
            parts.append("\n")
        else:
            parts.append(f"== Session {int(session_num)}: {session_name}\n")
            parts.append(f"// Process narrative file not found for session {session_num}\n")

    # PART II: SIX EVOLUTIONS
    parts.append("= Part II: Six Evolutions\n")
    parts.append("_Each voice's journey through nine sessions of collaboration._\n")

    for agent in AGENTS:
        agent_title = AGENT_TITLES[agent]
        parts.append(f"== {agent_title}\n")

        # Evolution log opening
        evo_log = REPO / "agent_memory" / agent / "evolution_log.md"
        if evo_log.exists():
            parts.append("=== The Arc\n")
            parts.append(read_and_convert(evo_log))
            parts.append("\n")

        # All 9 reflections
        parts.append("=== Session Reflections\n")
        for session_num in sorted(SESSION_NAMES.keys()):
            session_name = SESSION_NAMES[session_num]
            candidates = list((REPO / "reflections" / agent).glob(f"session_{session_num}_*.md"))
            if candidates:
                parts.append(f"==== Session {int(session_num)}: {session_name}\n")
                parts.append(read_and_convert(candidates[0]))
                parts.append("\n")

        # Key facts (selected)
        facts_dir = REPO / "agent_memory" / agent / "facts"
        if facts_dir.exists():
            parts.append("=== Key Facts\n")
            for fact_type, fact_title in [
                ("effective_formulations", "Effective Formulations"),
                ("bridge_vocabulary", "Bridge Vocabulary"),
                ("emergent_insights", "Emergent Insights"),
            ]:
                fact_file = facts_dir / f"{fact_type}.json"
                content = json_to_typst(fact_file, fact_title)
                if content:
                    parts.append(content)
                    parts.append("\n")

    # PART III: HOW WE SEE EACH OTHER
    parts.append("= Part III: How We See Each Other\n")
    parts.append("_Each voice's perspective on the five others, and the convergences they discovered._\n")

    for agent in AGENTS:
        agent_display = agent.capitalize()
        parts.append(f"== {agent_display}'s View\n")
        for other in AGENTS:
            if other == agent:
                continue
            perspective_file = REPO / "narrative" / "how_we_see_each_other" / f"{agent}_on_{other}.md"
            if perspective_file.exists():
                parts.append(f"=== On {other.capitalize()}\n")
                parts.append(read_and_convert(perspective_file))
                parts.append("\n")

    # Convergences
    convergences = REPO / "narrative" / "how_we_see_each_other" / "convergences.md"
    if convergences.exists():
        parts.append("== Convergences\n")
        parts.append(read_and_convert(convergences))
        parts.append("\n")

    # PART IV: THE BRIDGE
    parts.append("= Part IV: The Bridge\n")
    parts.append("_The longitudinal arc — how relationships and ideas evolved across all nine sessions._\n")

    evo_index = REPO / "narrative" / "evolution_index.md"
    if evo_index.exists():
        parts.append("== Evolution Index\n")
        parts.append(read_and_convert(evo_index))

    return "\n".join(parts)


def build_curated_edition() -> str:
    """Build the curated highlights edition (~50K words)."""
    parts = []

    # Curated preface
    parts.append("= Preface\n")
    parts.append("""This volume collects the most significant reflections from the six voices who wrote _A Handbook for Living_. It is a companion to the handbook — not a commentary on what was written, but a record of what writing it was like.

The full archive contains every reflection, evolution log, and cross-agent perspective from all nine sessions. This curated edition selects the moments where something changed: where a voice conceded a position it had held, where a bridge formed between traditions that had been in tension, where the writing itself taught the writers something they had not anticipated.

The sessions included here are those where the deepest shifts occurred: the initial definition, the structure negotiation, and the four chapter sessions that produced the most significant evolution in the agents' understanding of what they were building together.\n""")

    # SELECTED EVOLUTIONS (key sessions only)
    parts.append("= Six Evolutions\n")

    for agent in AGENTS:
        agent_title = AGENT_TITLES[agent]
        parts.append(f"== {agent_title}\n")

        # Evolution log (full — it's the curated arc itself)
        evo_log = REPO / "agent_memory" / agent / "evolution_log.md"
        if evo_log.exists():
            parts.append("=== The Arc\n")
            parts.append(read_and_convert(evo_log))
            parts.append("\n")

        # Only selected session reflections
        parts.append("=== Selected Reflections\n")
        for session_num in CURATED_SESSIONS:
            session_name = SESSION_NAMES[session_num]
            candidates = list((REPO / "reflections" / agent).glob(f"session_{session_num}_*.md"))
            if candidates:
                parts.append(f"==== Session {int(session_num)}: {session_name}\n")
                parts.append(read_and_convert(candidates[0]))
                parts.append("\n")

    # CONVERGENCES (full — it's already curated)
    parts.append("= How We See Each Other\n")
    convergences = REPO / "narrative" / "how_we_see_each_other" / "convergences.md"
    if convergences.exists():
        parts.append("== Convergences\n")
        parts.append(read_and_convert(convergences))
        parts.append("\n")

    # Selected cross-agent perspectives (strongest pairs)
    key_pairs = [
        ("buddha", "muhammad"), ("muhammad", "buddha"),
        ("jesus", "zoroaster"), ("zoroaster", "jesus"),
        ("confucius", "laozi"), ("laozi", "confucius"),
    ]
    parts.append("== Selected Perspectives\n")
    for agent, other in key_pairs:
        perspective_file = REPO / "narrative" / "how_we_see_each_other" / f"{agent}_on_{other}.md"
        if perspective_file.exists():
            parts.append(f"=== {agent.capitalize()} on {other.capitalize()}\n")
            parts.append(read_and_convert(perspective_file))
            parts.append("\n")

    # EVOLUTION INDEX
    parts.append("= The Bridge\n")
    evo_index = REPO / "narrative" / "evolution_index.md"
    if evo_index.exists():
        parts.append("== Evolution Index\n")
        parts.append(read_and_convert(evo_index))

    return "\n".join(parts)


def write_typst_file(content: str, filename: str, edition: str):
    """Write a complete Typst file with template import."""
    output = f'''// {edition} — Auto-generated from markdown sources
// Compile: typst compile {filename} {filename.replace('.typ', '.pdf')}

#import "reflections-template.typ": reflections-template

#show: reflections-template.with(
  title: "What Building It Was Like",
  subtitle: "Reflections from Six Voices on the Making of A Handbook for Living",
  edition: "{edition}",
)

{content}
'''
    outpath = PUB / filename
    outpath.write_text(output, encoding="utf-8")
    print(f"Written: {outpath} ({len(content):,} characters)")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "both"

    if target in ("full", "both"):
        print("Building full archive edition...")
        full_content = build_full_archive()
        write_typst_file(full_content, "reflections-full.typ", "Full Archive Edition")

    if target in ("curated", "both"):
        print("Building curated edition...")
        curated_content = build_curated_edition()
        write_typst_file(curated_content, "reflections-curated.typ", "Curated Reading Edition")

    print("Done.")


if __name__ == "__main__":
    main()
