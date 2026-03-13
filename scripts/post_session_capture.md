# Post-Session Consolidation Protocol

**Purpose:** Repeatable 5-phase protocol for capturing all agent memory artifacts after a handbook dialogue session. Evolved from the original 3-phase protocol to include orchestrator learning rules and session comparison notes.

**Prerequisite:** Session has produced: transcript (Phases A-F), summary, structured JSON, decision doc, 6 exit interview reflections (Phase E), and 6 mirror feedback responses (Phase F). These primary artifacts are committed in the dialogue session PR.

---

## Phase 1: Extract (Per-Agent, ~15 min per agent)

**Process ONE agent at a time.** Fixed inputs → fixed outputs. No judgment calls about what to update — everything gets touched, every time.

### Inputs (read for each agent)

| Source | Location | Purpose |
|--------|----------|---------|
| Agent's reflection | `reflections/{agent}/session_NN_topic.md` | Primary — Phase E personal transformation + Phase F mirror feedback |
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
- **Mirror Feedback (TWO sources):**
  1. **Phase F responses (PRIMARY):** Extract this agent's own Phase F mirror feedback — what they saw in others' reflections. This is live, in-session observation.
  2. **Cross-read (SECONDARY):** Read ALL 5 other agents' reflections (Phase E + Phase F). Search for mentions of this agent by name. Extract the observation into "What Others Have Shown Me" section.
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

## Phase 1.5: Orchestrator Learning Rules (~10 min)

**NEW — process-level learnings about how the dialogue was facilitated.**

After all 6 agents are processed in Phase 1, extract 3-5 learning rules about the PROCESS (not the content).

### Output
- **Location:** `scripts/orchestrator_learnings/session_NN_topic.md`

### What to extract

| Category | Questions to Answer |
|----------|-------------------|
| **Nudging sequences** | Which speaker orders produced the most productive exchanges? Did starting with a particular agent set a better tone? |
| **Dyad heat map** | Which pairs produced the most heat (productive tension)? Which pairs were underutilized? |
| **Moderator interventions** | Where did the moderator intervene effectively? Where should the moderator have intervened but didn't? Where did the moderator over-intervene? |
| **Phase transitions** | Were phase boundaries well-timed? Did any phase run too long or end too early? |
| **Turn length discipline** | Did agents stay within word limits? Which agents needed more or less space? |

### Format
```markdown
# Orchestrator Learning Rules — Session NN: Topic

**Session:** NN — Topic
**Date:** YYYY-MM-DD
**Total turns:** N
**Context compactions:** N

## Process Learning Rules

### Rule 1: [title]
**Evidence:** [what happened in the session that demonstrates this rule]
**Applies to:** [future sessions — when to apply this rule]
**Confidence:** [0-100]

### Rule 2: [title]
...

## Dyad Heat Map

| Pair | Turns Together | Tension Level | Notes |
|------|---------------|---------------|-------|
| Buddha ↔ Muhammad | N | high/medium/low | ... |
...

## Moderator Effectiveness

### Effective Interventions
- [what worked and why]

### Missed Opportunities
- [where intervention would have helped]

## Recommendations for Next Session
- [3-5 specific recommendations]
```

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

## Phase 2.5: Session Comparison (Re-Runs Only, ~10 min)

**Only for re-run sessions.** Compare the original session's decisions with the re-run's decisions and document what changed and why.

### Output
- **Location:** `sessions/NN_topic_rerun_comparison.md`

### Inputs
- Original session summary: `sessions/NN_topic_summary.md` (the pre-replacement version — read from git history if already replaced)
- Original decision doc: `decisions/topic.md` (pre-replacement)
- Re-run session summary (current)
- Re-run decision doc (current)
- Foundation differences (what changed in the sessions that preceded this one)

### Format
```markdown
# Session NN: Topic — Re-Run Comparison

**Original Session:** YYYY-MM-DD
**Re-Run Session:** YYYY-MM-DD
**Foundation Change:** [what changed in the preceding sessions that required this re-run]

## What Changed

### Decisions That Survived
[items that remained the same — and why they were robust enough to survive a new foundation]

### Decisions That Changed
[items that changed — with specific descriptions of old vs. new]

### New Decisions
[items that emerged in the re-run that didn't exist in the original]

### Decisions That Were Dropped
[items from the original that didn't survive — and why]

## Why It Changed

### Foundation Effects
[how the changed foundation (e.g., mandala vs. linear) specifically caused different format conclusions]

### Agent Growth Effects
[how agents' accumulated memory and learning produced different positions than they held originally]

### Emergent Effects
[things that changed for reasons neither the foundation nor the agents' growth fully explains — genuine emergence]

## Implications for Next Session
[how these changes affect what comes next]
```

---

## Phase 3: Commit (~5 min)

1. **Stage** all Phase 1 + Phase 1.5 + Phase 2 + Phase 2.5 changes in handbook repo
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
| Orchestrator learning rules | 1 | handbook |
| Narrative evolution index | 1 | handbook |
| How we see each other | 4-8 | handbook |
| Session comparison (re-runs only) | 0-1 | handbook |
| **Total** | **~55-60** | **1 PR** |

---

## Key Design Principles

1. **Deterministic:** Every file gets touched every time. No judgment calls about whether something is "important enough" to update.
2. **Parallelizable:** Phase 1 processes 6 agents independently. Use parallel agents.
3. **Regenerated, not accumulated:** Collaboration briefs are REPLACED, not appended. They are always a current-state snapshot.
4. **Mirror feedback has two sources:** Phase F (live, in-session) is PRIMARY. Post-hoc cross-read (Phase 1 extraction) is SECONDARY. Both feed into "What Others Have Shown Me."
5. **Quality gate:** Learnings files must reference session-specific concepts. Generic summaries indicate stale/wrong source material.
6. **Process learning is separate from content learning:** Phase 1 captures what the agents learned. Phase 1.5 captures what the orchestrator learned about facilitating.
7. **Comparison is re-run specific:** Phase 2.5 only applies to re-run sessions. It documents what changed and why — this is the institutional memory for the re-run decision.
