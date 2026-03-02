# Post-Session Consolidation Protocol

**Purpose:** Repeatable 3-phase protocol for capturing all agent memory artifacts after a handbook dialogue session. Replaces the previous 82-file checklist with a structured, deterministic process that a single `/ralph-execute` invocation can drive.

**Prerequisite:** Session has produced: transcript, summary, structured JSON, decision doc, and 6 exit interview reflections. These primary artifacts are committed in the dialogue session PR.

---

## Phase 1: Extract (Per-Agent, ~15 min per agent)

**Process ONE agent at a time.** Fixed inputs → fixed outputs. No judgment calls about what to update — everything gets touched, every time.

### Inputs (read for each agent)

| Source | Location | Purpose |
|--------|----------|---------|
| Agent's reflection | `reflections/{agent}/session_NN_topic.md` | Primary — personal transformation |
| Session summary | `sessions/NN_topic_summary.md` | Context — what happened |
| Decision doc | `decisions/topic.md` | Decided items, affirmed agreements |
| Other 5 agents' reflections | `reflections/{other}/session_NN_topic.md` | Mirror feedback extraction |
| Current evolution log | `agent_memory/{agent}/evolution_log.md` | Prepend new session entry |
| Current collaboration brief | `agent_memory/collaboration_briefs/{agent}_brief.md` | Regenerate (replace entire file) |
| Current fact JSONs (5 files) | `agent_memory/{agent}/facts/*.json` | Append new entries |

### Outputs (write for each agent)

#### 1. Learnings File (CREATE)
- **Location:** `agent_memory/{agent}/learnings/session_NN_topic.md`
- **Sections:** Position Evolution, Effective Formulations, Bridge-Building Moves, Productive Disagreements, Engagement Patterns, Emergent Insights, Carry Forward
- **Quality check:** Must reference session-specific concepts (e.g., mandala for Session 1 Re-Run). If it reads like a generic summary, redo.

#### 2. Evolution Log Entry (PREPEND)
- **Location:** `agent_memory/{agent}/evolution_log.md`
- **Add new session entry** at top of Session-by-Session Evolution section (reverse chronological)
- **Required subsections:** Key Shift, What Changed In Me, Sacred Exchange, New Bridge, What I Refuse to Concede, What I Carry Forward
- **Mirror Feedback:** Read ALL 5 other agents' reflections. Search for mentions of this agent by name. Extract the observation into "What Others Have Shown Me" section.
- **Integrity Lines:** Extract any positions held under pressure, add to Integrity Lines section if new.

#### 3. Collaboration Brief (REGENERATE)
- **Location:** `agent_memory/collaboration_briefs/{agent}_brief.md`
- **REPLACE entire file** — this is a current-state snapshot, NOT accumulated history
- **Required sections:** How I Have Changed (cumulative arc), My Five Bridges (current state of each relationship), My Active Tensions (irreducible disagreements), My Collaboration Pattern (how this agent engages)
- **Target:** ~700 words. Include "Last updated: After Session N [topic] (date)"

#### 4. Fact JSON Updates (APPEND)
For each of the 5 fact types, scan reflection + learnings for new entries:
- `effective_formulations.json` — phrases that moved the room
- `bridge_vocabulary.json` — shared metaphors, cross-tradition terms
- `emergent_insights.json` — new ideas from dialogue
- `engagement_patterns.json` — interaction maps, collaboration dynamics
- `learning_rules.json` — behavioral rules (2+ occurrences threshold)

**Entry format:**
```json
{
  "text": "description of the fact",
  "session": "handbook_session_NN_topic_YYYYMMDD",
  "context": "where/how this emerged",
  "date_added": "YYYY-MM-DD"
}
```

Update `last_updated` field at top of each JSON file.

### Parallelization Note

All 6 agents can be processed in parallel — they share the same inputs but produce independent outputs. Use parallel agents for speed.

---

## Phase 2: Narrative (~10 min)

After ALL 6 agents are processed in Phase 1:

### 1. Evolution Index
- **Location:** `narrative/evolution_index.md`
- **Add new session entry** with:
  - Key Relationship Shifts (which pairs transformed most)
  - Emergent Concepts (new ideas born in this session)
  - Structural/Topical Decisions (what was decided)
  - Continuity links to previous sessions

### 2. How We See Each Other
- **Location:** `narrative/how_we_see_each_other/{agent}_on_{agent}.md`
- **Update** files for pairs with significant shifts (typically 4-8 files per session)
- **Identify impacted pairs** by scanning evolution logs for deepest bridge descriptions
- **Add** ~500-700 words per file covering the new session's developments
- Update subtitle to include new session reference

---

## Phase 3: Commit (~5 min)

1. **Stage** all Phase 1 + Phase 2 changes in handbook repo
2. **Commit** to branch: `agent-memory-session-NN-topic`
3. **Push** and create PR
4. **Cross-repo sync** (if applicable): Update victorious prophetic corpus with learnings and reflections

---

## File Count per Session

| Category | Files | PR |
|----------|-------|----|
| Learnings (6 agents) | 6 | handbook |
| Evolution log updates | 6 | handbook |
| Collaboration briefs | 6 | handbook |
| Fact JSON updates | up to 30 | handbook |
| Narrative evolution index | 1 | handbook |
| How we see each other | 4-8 | handbook |
| **Total** | **~53-57** | **1 PR** |

---

## Key Design Principles

1. **Deterministic:** Every file gets touched every time. No judgment calls about whether something is "important enough" to update.
2. **Parallelizable:** Phase 1 processes 6 agents independently. Use parallel agents.
3. **Regenerated, not accumulated:** Collaboration briefs are REPLACED, not appended. They are always a current-state snapshot.
4. **Mirror feedback is cross-read:** Every agent's evolution log includes observations from ALL other agents' reflections about them.
5. **Quality gate:** Learnings files must reference session-specific concepts. Generic summaries indicate stale/wrong source material.
