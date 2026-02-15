# Narrative

This folder contains the **downstream content layer** of the Handbook for Living — curated prose that transforms structured agent memory into readable narratives for human audiences.

## Architecture

```
narrative/
├── how_we_see_each_other/   # 30 relational prose files + convergences
│   ├── buddha_on_jesus.md
│   ├── buddha_on_laozi.md
│   ├── ...
│   └── convergences.md      # Cross-pair patterns and shared metaphors
├── process/                  # Session narratives — what happened
│   ├── session_00_definition.md
│   └── session_01_structure.md
└── evolution_index.md        # Timeline of how understanding evolved
```

## What This Is

**Relational narratives** (`how_we_see_each_other/`): Each file tells the story of how one figure sees another — not as structured observation (that's `agent_memory/summaries/by_partner/`), but as prose that captures the texture of evolving understanding. When Buddha watches Jesus steelman his own teaching, what does that feel like? When Zoroaster discovers that Jesus's mercy is not softness but precision? These files hold those moments.

**Process narratives** (`process/`): Prose accounts of what happened in each session — the arc of dialogue, the turning points, the surprises. Not transcripts (those live in `sessions/`). Not summaries (those live in `sessions/` too). Narratives — the story of six voices discovering what they could build together.

**Evolution index** (`evolution_index.md`): A timeline tracking how key relationships and ideas evolved across sessions. The longitudinal view.

## Upstream vs. Downstream

This folder is **downstream** content. It is curated, interpretive, and designed for human readers.

The **upstream** sources it draws from:
- `agent_memory/{agent}/summaries/by_partner/` — structured relational observations
- `reflections/{agent}/` — exit interview reflections
- `agent_memory/collaboration_briefs/` — cumulative collaboration summaries
- `sessions/` — full transcripts and summaries

**Rule:** Narrative files are never loaded into agent context. They exist for the reader, not the agents. The agents read their own structured memory; the reader reads these narratives.

## When Narratives Get Updated

After each session:
1. New relational prose files are created or updated based on new by_partner data and reflections
2. A new process narrative is written for the session
3. The evolution index is updated with new timeline entries
4. convergences.md is updated if new cross-pair patterns emerge