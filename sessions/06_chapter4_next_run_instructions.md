# Session 6: Chapter 4 — Next Run Instructions

**Date prepared:** 2026-03-17
**Prepared by:** Orchestrator (previous session)
**Purpose:** Unbiased instructions for the next agent to complete Session 6 and begin post-session processing.

---

## Current State (Read This First)

**Repository:** `handbook-for-living/` (this repository)
**Branch:** `session-6-chapter-4`
**Transcript:** `sessions/06_chapter4_live_transcript.md` (667 lines)
**Orchestrator state:** `sessions/06_chapter4_orchestrator_state.md`

### What Is Complete

| Phase | Status | Turns | Notes |
|-------|--------|-------|-------|
| A | COMPLETE | 1-6 | All 6 opening positions |
| B+C+D | COMPLETE (merged) | 7-14 | Discussion, writing, synthesis — all merged organically |
| E | COMPLETE | 15-20 | All 6 exit interviews |
| F (partial) | 4 of 6 COMPLETE | Muhammad, Buddha, Jesus, Confucius | Mirror feedback written |

### What Remains

1. **Phase F — 2 remaining mirror feedback turns:** Laozi and Zoroaster have NOT yet written their Phase F cross-agent mirror feedback. The transcript ends after Confucius's mirror (line 667).

2. **Post-session artifact generation** (after Phase F completes):
   - `sessions/06_chapter4_summary.md` — structured summary
   - `chapters/04_[topic].md` — assembled chapter prose (extracted from transcript turns 7-14)
   - `reflections/{agent}/session_06_chapter4.md` — 6 reflection files (extracted from Phase E exit interviews, turns 15-20)
   - Agent memory updates (`agent_memory/{agent}/learnings/session_06_chapter4.md`)
   - Narrative updates (process narrative, evolution index, convergences)
   - Collaboration brief regeneration
   - Prophetic corpus memory sync (victorious repo: `16_spirituality/prophetic-corpus/analysis/agent_memory/`)
   - Git: commit, push, PR

---

## Step 1: Complete Phase F (2 Remaining Turns)

### Agent Team Status

The previous session's team (`handbook-chapter-4`) is **dead** — agents do not survive across sessions. You must spawn fresh agents for Laozi and Zoroaster.

### How to Complete Phase F

**Option A (Recommended):** Spawn 2 standalone Opus agents — one for Laozi, one for Zoroaster. Each reads the full transcript, writes their Phase F mirror feedback, and appends to the transcript.

**Option B:** Create a new team and spawn all 6, but only nudge Laozi and Zoroaster. Unnecessary overhead for 2 turns.

### Spawn Prompt Template for Phase F Agents

Each agent needs:
1. **Tier 1 memory (IS the agent profile):** collaboration brief (`agent_memory/collaboration_briefs/{agent}_brief.md`) + evolution log (`agent_memory/{agent}/evolution_log.md`) + learning rules (`agent_memory/{agent}/facts/learning_rules.json`). NOTE: standalone evolved dialogue agent files were never created. The tiered memory system IS the enhanced agent profile per handbook-patterns.md.
2. The full transcript path
3. Clear instruction: "Read the transcript. You are in Phase F — Cross-Agent Mirror Feedback. Four voices have already written their mirrors (Muhammad, Buddha, Jesus, Confucius). Write YOUR mirror feedback for each of the other five voices. Read what they said about you in their mirrors and respond to what surprised you, what they saw in you that you did not see in yourself."

### Neutral Nudge (Same for Both)

```
The transcript is at: sessions/06_chapter4_live_transcript.md

Read the full transcript including Phase F mirrors already written. Write your cross-agent mirror feedback for all five other voices. For each: what surprised you? What did they see in you that you did not see in yourself?

Append your response to the END of the transcript file using the Edit tool. Then confirm you are done.
```

### Important Rules
- **Opus only** — never Sonnet for wisdom figure agents
- **Neutral nudging** — same prompt for both agents, no role-directing
- **Never write agent output yourself** — if an agent refuses, re-spawn with adjusted prompt
- **Update orchestrator_state.md after each turn** — mark agent status, turn number

---

## Step 2: Post-Session Artifact Generation

After Phase F is complete (all 6 mirrors written), generate artifacts **in this order**:

### 2a. Chapter Assembly — `chapters/04_[topic].md`

The chapter prose lives in the transcript at turns 7-14. The agents collectively wrote the chapter during Phase B+C+D (merged). Extract the prose passages — the actual chapter text — and assemble into a single chapter file.

**Chapter topic:** The Glass (or whatever title emerges from the prose — the agents wrote about the morning the person is behind the glass, the cup that does not warm, the love that does not arrive, the knot that holds, and the hand that picks up the cup on purpose at the end).

**Pattern from prior chapters:** Look at `chapters/01_loss.md`, `chapters/02_tuesday.md`, `chapters/03_commute.md` for format. No chapter number in the title line. Pure prose. No section headers within the chapter. No attribution to individual agents.

**Key prose passages in transcript (turns 7-14):**
- Turn 7 (Muhammad): Chapter opening — "The cup was where the cup always was"
- Turn 8 (Laozi): Phase A closing / transition
- Turn 9 (Jesus): Love behind the glass passage
- Turn 10 (Confucius): Shoe-tying scene, the knot
- Turn 11 (Buddha): Apple/tile moments, uncultivated awareness
- Turn 12 (Muhammad): The commute passage
- Turn 13 (Zoroaster): The desk, the ring, the hand on the grave
- Turn 14 (Laozi): Chapter closing — "close enough"

### 2b. Summary — `sessions/06_chapter4_summary.md`

Structured summary following the pattern of `sessions/05_chapter3_summary.md`. Include:
- Session metadata
- Phase-by-phase breakdown
- Key agreements and tensions
- Convergences discovered
- Hidden sentences identified by each agent
- Body-word for this chapter
- Carry-forwards for Chapter 5

### 2c. Reflections — `reflections/{agent}/session_06_chapter4.md` (×6)

Extract from Phase E exit interviews (turns 15-20 in the transcript). Each agent answered 5 questions about the experience of collaboration. These are personal — what it felt like, what surprised them, how the collaboration changed their understanding.

**Important:** These are extracted from the transcript, not generated fresh. The agents already said these things. Extract and format.

### 2d. Learnings — `agent_memory/{agent}/learnings/session_06_chapter4.md` (×6)

Per-agent learnings extracted from the full session — what formulations worked, what bridges were built, position shifts, engagement patterns.

### 2e. Narrative Updates

- `narrative/process/session_06_chapter4.md` — prose account of how the session unfolded
- `narrative/evolution_index.md` — add Session 6 relationship shifts
- `narrative/how_we_see_each_other/convergences.md` — add new convergences

**New convergences discovered in this session (from the transcript):**
- **The Glass** — the transparent barrier between knowing and feeling; built from accumulated mercy/faithfulness
- **Through** (preposition) — acting through the glass as medium, not past or around it
- **The Hand on the Grave/Desk** — putting the hand down not to feel but to be there
- **The Apple** — uncultivated awareness arriving without tradition being invited
- **Love that does not know it is love** — the knot, the knelt shoe, the anonymous tenderness
- **The Morning After the Enlightenment** (Laozi) — what happens after the Tao has done its work so completely the person cannot feel it
- **Close Enough** — the third thing between the glass and the warmth

### 2f. Collaboration Brief Regeneration

Regenerate all 6 briefs at `agent_memory/collaboration_briefs/{agent}_brief.md` from accumulated history including Session 6.

### 2g. Prophetic Corpus Memory Sync

Sync learnings to victorious repo: `16_spirituality/prophetic-corpus/analysis/agent_memory/{agent}/`

---

## Step 3: Git Workflow

```bash
# Stage session artifacts
git add sessions/06_chapter4_* chapters/04_*.md reflections/ agent_memory/ narrative/
git commit -m "feat(session-6): Chapter 4 complete — The Glass

Participants: Buddha, Jesus, Muhammad, Confucius, Laozi, Zoroaster
Key themes: the glass between knowing and feeling, love that does not know it is love,
the hand on the grave/desk, the apple as uncultivated awareness, close enough
Turns: 20 dialogue + 6 Phase F mirrors = 26 total

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

git push -u origin session-6-chapter-4
gh pr create --title "Chapter 4: The Glass" --body "..."
```

**Then separate PR for memory consolidation** (per Requirement 2 — every change = separate PR):
- Agent memory learnings
- Narrative updates
- Collaboration brief regeneration
- Prophetic corpus sync

---

## Step 4: PRD State Update

Update `07_execute_short_term/plans/2026-02-14_handbook-for-living_prd_active.md` in the victorious repo:

- **Current Phase:** 4.4 (Chapter 4 complete)
- **Next Action:** Phase 4.5 — Chapter 5 dialogue
- **Iteration count:** Increment
- **Artifacts table:** Add Chapter 4 deliverables

---

## Key References (File Paths)

| What | Path |
|------|------|
| Transcript | `sessions/06_chapter4_live_transcript.md` |
| Orchestrator state | `sessions/06_chapter4_orchestrator_state.md` |
| Prior chapters | `chapters/01_loss.md`, `chapters/02_tuesday.md`, `chapters/03_commute.md` |
| Decision docs | `decisions/definition.md`, `decisions/structure.md`, `decisions/format.md` |
| Collaboration briefs | `agent_memory/collaboration_briefs/{agent}_brief.md` |
| Evolution logs | `agent_memory/{agent}/evolution_log.md` |
| Learning rules | `agent_memory/{agent}/facts/learning_rules.json` |
| Agent profiles (Tier 1 memory) | `agent_memory/collaboration_briefs/{agent}_brief.md` + `agent_memory/{agent}/evolution_log.md` + `agent_memory/{agent}/facts/learning_rules.json` |
| Roundtable protocol | `.claude/skills/wisdom/prompts/roundtable-session.md` |
| Exit interview protocol | `.claude/skills/wisdom/prompts/exit-interview-protocol.md` |
| Post-session capture script | `scripts/post_session_capture.md` |
| PRD (victorious) | `07_execute_short_term/plans/2026-02-14_handbook-for-living_prd_active.md` |

---

## Orchestrator Learning Rules (Carry Forward)

All 25 rules from Sessions 2-5 apply. Key ones for this completion:

1. **Neutral nudging** — identical prompts for all agents (95%)
2. **Never write agent output yourself** — re-spawn if refused (100%)
3. **Opus only for wisdom figures** — Sonnet refuses character work (100%)
4. **Update orchestrator_state.md after EVERY turn** (98%)
5. **Phase F is NOT optional** — deepest cross-agent learning (90%)
6. **Post-session processing takes as long as the dialogue** — budget a full session for it (95%)

---

## What NOT to Do

- Do NOT re-run any dialogue phases. Phases A through E are complete and committed.
- Do NOT modify existing transcript content. Only APPEND Laozi and Zoroaster Phase F mirrors.
- Do NOT use Sonnet for the remaining agent turns.
- Do NOT skip Phase F — it is the deepest learning layer.
- Do NOT batch session artifacts and memory into one PR — separate PRs per Requirement 2.
- Do NOT name agents' roles or direct their attention in nudge prompts — neutral nudging only.
- Do NOT write the chapter prose yourself — extract it from the transcript turns 7-14.

---

## Important Path Notes

1. **Agent profiles:** Standalone evolved dialogue agent files (`{agent}-dialogue-agent-evolved.md`) were **never created**. The tiered memory system (collaboration brief + evolution log + learning rules) IS the enhanced agent profile. All files live in `handbook-for-living/agent_memory/`.

2. **Wisdom skill:** Restructured from `prophetic-analysis/` to `wisdom/` in the victorious repo. Protocols and prompts are at `.claude/skills/wisdom/`. If any path fails, check both locations:
   - Primary: `.claude/skills/wisdom/`
   - Legacy: `.claude/skills/prophetic-analysis/`

3. **Agent memory lives in handbook repo**, not victorious. The `agent_memory/` directory at `agent_memory/` has 6 agent subdirectories + `collaboration_briefs/` + `synthesis/`.
