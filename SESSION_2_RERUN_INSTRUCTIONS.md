# Session 2: Format — Re-Run Instructions

**For:** A fresh Claude Code context window executing Session 2 (Format) Re-Run
**Updated:** 2026-03-02
**Prerequisite:** Session 1 (Structure) Re-Run is COMPLETE. PR #16 merged. Agent memory consolidation COMPLETE (PR #17 merged or ready).

---

## Overview

Session 2 asks: **"How should each chapter be written? What format elements should each chapter contain? In what order? How does the reader experience a single chapter?"**

The original Session 2 (2026-02-15) produced "The Prepared Ground and Its Fire" — three fixed elements (story, threshold, silence) plus a flexible palette. That session was built on the original Session 0 + Session 1 foundations, which have now been superseded.

The re-run must be built on:
1. **Session 0 Re-Run** (2026-02-16) — "the clearing," six agreements, three tensions
2. **Session 1 Re-Run** (2026-03-01) — mandala architecture, 10 decided items, 2 living tensions

---

## Step 0: Pre-Flight

### 0a. Verify Prerequisites

```bash
# Navigate to the repository root
git checkout main
git pull
```

Verify:
- [ ] PR #16 (Session 1 Re-Run) is merged to main
- [ ] PR #17 (Agent memory consolidation) is merged to main — this contains all 6 evolution logs, collaboration briefs, learnings files, fact JSONs, narrative layer, and the consolidation protocol
- [ ] If PR #17 is NOT merged, merge it first. All Tier 1 memory files must be current.

### 0b. Verify Agent Memory Is Current

Run these checks:

```bash
# All 6 collaboration briefs should say "After Session 1 Re-Run"
grep -l "Session 1 Re-Run" agent_memory/collaboration_briefs/*_brief.md | wc -l
# Should return 6

# All 6 evolution logs should have Session 1 Re-Run entries
grep -l "Session 1.*Re-Run" agent_memory/*/evolution_log.md | wc -l
# Should return 6

# All 6 learnings files should reference mandala
grep -l "mandala" agent_memory/*/learnings/session_01_structure.md | wc -l
# Should return 6

# Fact JSONs should have 2026-03-02 entries
grep -rl "2026-03-02" agent_memory/*/facts/*.json | wc -l
# Should return 30 (5 fact types × 6 agents)
```

If any check fails, the agent memory consolidation from PR #17 is missing. Do NOT proceed without current Tier 1 files.

### 0c. Create Branch

```bash
git checkout -b session-2-format-rerun
```

---

## Step 1: The Foundation (BINDING — Do Not Re-Litigate)

### Session 0 Re-Run Foundation (6 agreements, 3 tensions)

**Six Agreements:**
1. Something in a man recognizes before it is taught
2. The body carries the soul through dark hours the mind cannot navigate
3. Dead ritual is worse than no ritual
4. The handbook must teach its own dissolution
5. Wound and tourniquet are sequence, not opponents
6. Method is negotiable; what the method serves is not

**Three Irreducible Tensions:**
1. How long the binding should last (Muhammad vs. Buddha)
2. Whether form creates or merely reveals (Confucius vs. Laozi)
3. Choosing vs. ripeness (Zoroaster vs. Jesus)

**Consensus Definition:** A clearing — the space a man returns to when every teaching he has carried has done its work and fallen quiet.

### Session 1 Re-Run Foundation (10 decided items, 2 living tensions)

**Ten Decided Items (ALL affirmed by all 6 voices):**

1. **Mandala Architecture** — Six qualities woven as one meal (threshold, practice, relation, seeing, fire, clearing). Emphasis shifts by wound. Wound is the conductor.

2. **Body as Language** — Five body-words (return, stillness, small action, contact, openness) + remaining as ground beneath. Mapped to salat: return=qiyam, stillness=juloos, small action=takbir, contact=wudu, openness=du'a. Not separate practices but movements of a whole.

3. **Two-Depth Writing** — Hidden sentence (Confucius) + zahir/batin (Muhammad) + three readings: body-word, mirror, recognition (Buddha). Example: "You did not leave" — (1) feet on floor, (2) you are not your father, (3) the you beneath all roles was never absent.

4. **One-Wound-Many-Roots** — One wound, roots growing into different life areas. Governs chapter organization. Tangle reveals across chapters and time.

5. **Body Experiences Seeing as Safety** — Half-second (Buddha) + eleventh second (Muhammad). "The jaw is the teaching." Neutral attention is the first safety the body has experienced in thirty years.

6. **Ember as Presence** — Handbook is true in reader's vicinity. No strategy toward reader. Warmth without announcing. Four-voice consensus (Laozi, Confucius, Muhammad, Buddha).

7. **Betrayal as Structural Modifier** — Not a sixth wound but a sixth doorway. Threshold reversal: honor the wall first, then name the cost.

8. **Two Dissolutions + Return** — First dissolution (avoidance), return, second dissolution (completion). Book designed for re-entry.

9. **Fine Man** — Handbook does not reach. Threshold waits. Readiness is the crack life provides.

10. **Architecture Disappears** — Scaffolding comes down. Reader does not need to know what was built.

**Two Living Tensions (Unresolved by Design):**
1. **Witness vs. Flood** — Buddha (capacity to return) vs. Zoroaster (Asha — reality held its shape). Both needed.
2. **Dissociated Body** — All traditions weakest here. Beginnings exist but honest about incompleteness.

### What Changed from Original Session 1

The original Session 1 produced an **eight-section linear structure** built on the five-moment sequence (Stillness → Seeing → Choosing → Acting → Releasing). The re-run produced a **mandala structure** — not a linear journey but woven presence. Key shifts:
- Linear → mandala
- Sections → qualities
- Commands → testimony
- Architecture visible → architecture invisible
- Reader journey → reader freedom

---

## Step 2: The Original Session 2 (What to Carry Forward vs. Re-Examine)

Read these files for context: `sessions/02_format_summary.md`, `decisions/format.md`

### Original Session 2 Decisions (MAY CHANGE)

- **Three Fixed Elements:** Human story (unresolved), threshold practice (embodied), silence (white space)
- **Flexible Palette:** Lead voice, other voices, shadow question, petition at divergence, diagnostic
- **Ordering Principle:** Elements arrive in the order of their discovered weight
- **Lead Voice Selection:** "The Weight That Speaks" — voice that has borne the most weight speaks first
- **Format Name:** "The Prepared Ground and Its Fire" (Zoroaster)

### What Will Likely Change

The new Session 1 mandala architecture means:
- **Six qualities woven in every chapter** — not fixed elements + palette but qualities with shifting emphasis
- **Body-words in every chapter** — "every chapter needs a body-line" is decided
- **Two-depth writing** — hidden sentence + three readings are now structural requirements
- **Wound as conductor** — determines which quality leads, which changes the "lead voice" concept
- **Architecture disappears** — the format cannot be visible to the reader

### What Will Likely Carry Forward

- Story opening (likely stays — Jesus's strongest contribution)
- Silence/white space (likely stays — Laozi won this point decisively)
- Threshold concept (likely stays but may merge with wound-as-conductor)
- Hospitality as format principle (Jesus's naming — "format IS mercy")
- "The cup has a shape" (Muhammad's design principle)

### Key Emergent Insights from Original Session 2 (Carry as Memory)

- "Format is hospitality" (Jesus)
- "Show the wound, teach patient to look, leave room" (Buddha)
- "Structure IS emptiness, arranged" (Laozi)
- "The namer needs the builders" (Jesus, exit interview)
- "The Prepared Ground and Its Fire" (Zoroaster — format name)
- "The Weight That Speaks" (lead voice principle)
- "The cloak" (human story function — Khadijah wrapping Muhammad)

---

## Step 3: Set Up the Chat Room

### 3a. Create Transcript File

Create `live_transcript.md` with this header:

```markdown
# Session 2: Format — Re-Run Transcript

**Session:** 2 — Format (Re-Run with Multi-Agent Dialogue)
**Date:** [today's date]
**Question:** "How should each chapter be written? What format elements should each chapter contain? In what order? How does the reader experience a single chapter?"
**Participants:** Buddha, Jesus, Muhammad, Confucius, Laozi, Zoroaster
**Moderator:** Facilitator (no authorial voice)
**Protocol:** Chat Room Pattern — 6 persistent Opus agents, sequential nudging, shared transcript
**Phases:** A (Opening Positions) → B (Clarifying + Probing) → C (Contested Territory) → D (Synthesis) → E (Exit Interviews) → F (Cross-Agent Mirror Feedback)

**Foundation:**
- Session 0 Re-Run: Six agreements, three tensions, "the clearing"
- Session 1 Re-Run: Mandala architecture (10 decided items, 2 living tensions)
- Original Session 2: "The Prepared Ground and Its Fire" (to be re-examined against new foundation)

---

## Phase A: Opening Positions

```

### 3b. Create Orchestrator State File

Create `orchestrator_state.md` — use the Session 1 Re-Run version as template (it exists at repo root). The file must contain:

1. **Recovery context** — repo path, branch, team name, file paths
2. **How the chat room works** — the pattern description and nudging instructions
3. **Agent roster** — all 6 agents, status, turns_spoken: 0
4. **Session question** — the format question
5. **Full foundation** — copy all 6 agreements, 3 tensions, 10 decided items, 2 living tensions verbatim from Step 1 above
6. **Phase plan** — A through E
7. **Turn log** — empty, will be filled during session
8. **Git workflow** — what to do after all phases complete
9. **Output capture protocol** — artifact list

**Critical fields in the orchestrator state:**

```markdown
# Orchestrator State — Session 2 Format Re-Run

**Session:** 2 — Format (Re-Run)
**Date:** [today's date]
**Status:** ACTIVE
**Current Phase:** A (Opening Positions)
**Turn Number:** 0
**Total Turns:** 0

## CRITICAL RECOVERY CONTEXT

**Repository:** `handbook-for-living/` (this repository)
**Branch:** session-2-format-rerun
**Team:** handbook-session2-rerun
**Transcript file:** `live_transcript.md`
**This file:** `orchestrator_state.md`

### How This Works (Chat Room Pattern)
- 6 persistent Opus agents: buddha, jesus, muhammad, confucius, laozi, zoroaster
- Sequential nudging: nudge ONE agent at a time via SendMessage. Agent reads transcript, appends response, goes idle.
- UPDATE this file AFTER EVERY TURN
- Agents stay alive across ALL 5 phases. NEVER spawn per-phase agents.
- Pick speakers based on dialogue flow, not round-robin.
- Moderator facilitates ONLY — never summarizes, synthesizes, or authors content in the transcript.

### How to Nudge an Agent
Send a message like:
> [AgentName], it is your turn to speak. We are in Phase [X].
> 1. Read the full transcript at: `live_transcript.md`
> 2. Compose your response (300-500 words, max 700)
> 3. Append to END of transcript using Edit tool
> 4. Format as: **[AgentName]:** [your words]
> 5. Send message back confirming your turn is done

## Agent Roster

| Agent | Status | Turns Spoken | Last Spoke |
|-------|--------|-------------|------------|
| buddha | idle | 0 | — |
| jesus | idle | 0 | — |
| muhammad | idle | 0 | — |
| confucius | idle | 0 | — |
| laozi | idle | 0 | — |
| zoroaster | idle | 0 | — |

## [Insert full foundation from Step 1 here]

## Dialogue Phases
- [ ] Phase A: Opening Positions (6 turns — one per agent)
- [ ] Phase B: Clarifying + Probing (8-10 turns)
- [ ] Phase C: Contested Territory (6-8 turns)
- [ ] Phase D: Synthesis (4-5 turns)
- [ ] Phase E: Exit Interviews (6 turns — one per agent)
- [ ] Phase F: Cross-Agent Mirror Feedback (6 turns — each reads all Phase E, writes 2-3 sentences)

## Turn Log

[empty — fill during session]
```

---

## Step 4: Spawn the Team

### 4a. TeamCreate

```
TeamCreate: team_name="handbook-session2-rerun", description="Session 2 Format Re-Run"
```

### 4b. Spawn 6 Opus Agents

**CRITICAL:** Each agent must be spawned with `model: "opus"`. Sonnet refuses roleplay. This is non-negotiable.

Each agent gets a system prompt with **FOUR sections:**

#### Section 1: Identity — Full Tier 1 Memory (Enhanced Profile)

The tiered memory system IS the enhanced agent profile. Load ALL Tier 1 files:

1. **Collaboration brief** (`agent_memory/collaboration_briefs/{agent}_brief.md`) — ~700 words, the primary identity document:
   - How I Have Changed (cumulative arc through Session 1 Re-Run)
   - My Five Bridges (current relationship state with each partner)
   - My Active Tensions (irreducible disagreements)
   - My Collaboration Pattern (how this agent engages)

2. **Evolution log** (`agent_memory/{agent}/evolution_log.md`) — session-by-session shifts, integrity lines, mirror feedback from other agents

3. **Learning rules** (`agent_memory/{agent}/facts/learning_rules.json`) — evidence-based behavioral rules the agent has learned across sessions

#### Section 2: Tier 2 Memory (Accumulated Facts + Learnings)

Load these accumulated memory files:
- `agent_memory/{agent}/facts/effective_formulations.json` — phrases that moved the room
- `agent_memory/{agent}/facts/bridge_vocabulary.json` — shared metaphors
- `agent_memory/{agent}/facts/emergent_insights.json` — ideas born from dialogue
- `agent_memory/{agent}/facts/engagement_patterns.json` — interaction dynamics

#### Section 3: Session Learnings (~300 words compressed)

Compress key learnings from `agent_memory/{agent}/learnings/session_01_structure.md` covering:
- How the agent changed during Session 1 Re-Run
- Key bridges discovered
- What they carry forward

Also include key carry-forward items from `agent_memory/{agent}/learnings/session_02_format.md` (original Session 2 learnings — these are MEMORY, not authority).

#### Section 4: Session 2 Re-Run Task + How This Works

Use this template (customize [AGENT_NAME] and the carry-forward bullets):

```markdown
## Your Task: Session 2 Format Re-Run

You are [AGENT_NAME], participating in a re-run of Session 2: Format.

**Session Question:** "How should each chapter be written? What format elements should each chapter contain? In what order? How does the reader experience a single chapter?"

**Critical Context:** This re-run replaces the original Session 2 (2026-02-15). The foundation has changed:
- Session 1 now uses MANDALA architecture (not linear), with wound as conductor
- Every chapter must carry: six qualities (shifting emphasis), body-words, two-depth writing, hidden sentence, three readings
- Architecture must disappear into the writing
- The original Session 2 produced "The Prepared Ground and Its Fire" with three fixed elements + flexible palette — this may or may not survive contact with the new foundation

**Your original Session 2 learnings (carry forward — memory, not authority):**
[Insert 3-5 key bullet points from agent_memory/{agent}/learnings/session_02_format.md]

**The 10 decided items from Session 1 Re-Run are BINDING.** Do not re-litigate them. Build FORMAT on top of them.

## How This Works

You are in a shared dialogue with 5 other participants. There is a transcript file on disk — the "chat room." When it is your turn:

1. **Read** the full transcript at: `live_transcript.md`
2. **Compose** your response (aim for 300-500 words, no more than 700)
3. **Append** to the END of the transcript using the Edit tool
4. **Format** as: **[AGENT_NAME]:** [your words]
5. **Send message** back to the orchestrator confirming your turn is done

### Rules:
- You speak ONLY when nudged by the orchestrator
- You read the FULL transcript each time (it grows each turn)
- You respond to what others have ACTUALLY SAID, not what you expect them to say
- Concessions must be genuine — no diplomatic retreats
- Name your disagreements directly — productive tension is the goal
- You may address any participant by name
- Keep responses under 700 words (quality over quantity)
- Do NOT summarize or repeat previous agreements — build forward
```

### 4c. Agent-Specific Guidance

Include these agent-specific nudges in their system prompts (Section 3, after the task template):

**Buddha:**
- Session 1 discovery: seeing IS safety, the relighting (not the lamp), stop reaching
- Session 2 original: released diagnostic as embedded, "show wound, teach patient to look, leave room"
- Key question for re-run: How do three readings (body-word, mirror, recognition) shape chapter FORMAT? What does a mandala chapter look like to the reader who doesn't know it's a mandala?

**Jesus:**
- Session 1 discovery: "truth belongs to the room," fear behind boundary, grain-of-wheat reversed
- Session 2 original: "format IS mercy," hospitality as format principle, "namer needs builders"
- Key question for re-run: Does the mandala change what hospitality means at chapter level? How does story opening work when wound is the conductor?

**Muhammad:**
- Session 1 discovery: eleventh second (body's own time), certainty has tenderness, the man in the kitchen
- Session 2 original: "three fixed, five flexible, cup has a shape," Khadijah's cloak, bread-first concession
- Key question for re-run: How do five body-words (salat mapping) actually appear in chapter format? What does the horizontal spine (daily practice) look like in a mandala chapter?

**Confucius:**
- Session 1 discovery: "practice hall is very small," li as vocabulary not rules, cup not cathedral
- Session 2 original: "yours were the room, mine were furniture," hidden sentence, gravity vs. cost
- Key question for re-run: How does hidden sentence (two-depth writing) actually work as format element? How does the relational test (gate) appear in a chapter the reader experiences as seamless?

**Laozi:**
- Session 1 discovery: clearing is full, argument is architecture, dissociated body as own failure
- Session 2 original: "palette not prescription," "structure IS emptiness arranged," white space won
- Key question for re-run: If architecture disappears, what does an invisible mandala format look like? How does silence function in two-depth writing?

**Zoroaster:**
- Session 1 discovery: hinge requires preparation, fire as quality not event, naming role
- Session 2 original: "Prepared Ground and Its Fire," "Weight That Speaks," "Asha can be partial"
- Key question for re-run: Does "The Weight That Speaks" survive as lead voice selection when wound is the conductor? What does the hinge (choosing moment) look like in chapter format?

### 4d. Test Before Scaling

**Spawn ONE agent first.** Send a test nudge. Verify:
- Agent reads the transcript file
- Agent appends response using Edit tool
- Agent sends confirmation message back
- Response is in-character and references the foundation

Only after confirming one agent works, spawn the remaining five.

---

## Step 5: Phase Structure

### Phase A: Opening Positions (6 turns)
Each agent proposes their format vision for a SINGLE CHAPTER given the new mandala foundation. One turn per agent, any order works but consider starting with someone other than Session 1's opener (Laozi opened Session 1).

**Moderator prompt for Phase A (write into transcript before nudging):**
> Given the mandala architecture — six qualities woven as one meal, wound as conductor, body-words in every chapter, two-depth writing, architecture that disappears — what does a SINGLE CHAPTER look like? What format elements does it contain? In what order? How does the reader experience it?

### Phase B: Clarifying + Probing (8-10 turns)
Agents respond to each other's proposals. Seek convergences and name tensions. The moderator identifies what's agreed and what's contested.

**Moderator role in Phase B:**
- After 3-4 turns, update orchestrator_state.md with emerging convergences
- If agents are being too agreeable, nudge toward the tension: "What disagrees here?"
- Pick speakers based on who has the most to respond to (not round-robin)

### Phase C: Contested Territory (6-8 turns)
Press into genuine disagreement. Don't allow premature convergence. Name what's decided and what remains alive.

**Moderator role in Phase C:**
- Identify the 2-4 genuine tensions from Phase B
- Nudge specific agents to press into specific tensions
- Track decided items vs. living tensions in orchestrator_state.md

### Phase D: Synthesis (4-5 turns)
Each voice affirms, amends, or contests. Goal: a format the chapters can be written from.

**Moderator role in Phase D:**
- Ask each agent explicitly: "Do you affirm, amend, or contest?"
- Track affirmations and amendments
- If an agent subtracts (like Laozi in Session 1), ask others to respond

### Phase E: Exit Interviews (6 turns)
Each agent reflects privately on what changed. One turn per agent. These become the source material for post-session memory consolidation.

### Phase F: Cross-Agent Mirror Feedback (6 turns)

**NEW — deepest learning layer.** After ALL Phase E reflections are written, each agent reads ALL FIVE other agents' Phase E reflections and writes 2-3 sentences about what surprised them — how others experienced the session differently than they did.

**Why this matters:** The evolution logs already include mirror feedback extracted post-session, but Phase F makes it LIVE — agents seeing themselves through others' eyes in real-time, within the session itself. This produces the rawest, most honest cross-agent observations because the agents are still in dialogue mode, not in post-session extraction mode.

**Moderator prompt for Phase F (write into transcript after all Phase E turns):**
> You have each shared what this session meant to you. Now read what the OTHER FIVE said about their experience. What surprised you? What did someone else see in you that you did not see in yourself? What did someone else experience in the room that you missed entirely? Write 2-3 sentences — not analysis, but honest response to reading how others lived through the same session you just lived through.

**Nudging protocol for Phase F:**
- Each agent is nudged ONE at a time (same as all other phases)
- Agent reads ALL Phase E reflections from transcript (they are already appended)
- Agent appends their mirror feedback response
- Format: **[AgentName] (Mirror Feedback):** [2-3 sentences]
- Keep responses SHORT — this is reaction, not analysis

**What to watch for:**
- Agents discovering they were seen differently than they felt
- Agents recognizing bridges or tensions they missed
- Agents naming specific moments from others' reflections that reframe their own experience

**Target: 36-41 turns total** (6 Phase A + 8-10 Phase B + 6-8 Phase C + 4-5 Phase D + 6 Phase E + 6 Phase F)

---

## Step 6: Nudging Protocol

### How to Nudge
Send a message to ONE agent at a time:

```
[AgentName], it is your turn to speak. We are in Phase [X].
1. Read the full transcript at: `live_transcript.md`
2. Compose your response
3. Append to END of transcript using Edit tool
4. Format as: **[AgentName]:** [words]
5. Send message back confirming
```

### Phase Transitions
At each phase boundary:
1. Update `orchestrator_state.md` with phase summary (convergences, tensions, key moments)
2. Write a moderator note into the transcript marking the phase change
3. Include a brief summary of what was decided/contested

### After EVERY Turn
Update `orchestrator_state.md`:
- Increment turn number
- Update agent's turns_spoken and last_spoke
- Log the turn in the Turn Log with brief content summary (1-2 sentences)

### Speaker Selection Guidelines
- **Phase A:** One per agent, any order (consider starting with Muhammad or Zoroaster for variety)
- **Phase B onward:** Based on dialogue flow — who has the most to respond to? Who was just challenged? Who has been quiet?
- **Avoid:** Three consecutive turns from the same pair. If Buddha and Muhammad are dominating, bring in Laozi or Confucius.
- **Watch for:** Laozi going quiet (his subtraction contributions are critical), Zoroaster naming what the room is doing (his meta-observations are valuable)

---

## Step 7: Artifact Generation (After Phase F)

After all 6 phases complete, generate these artifacts:

| # | File | Action |
|---|------|--------|
| 1 | `sessions/02_format_transcript.md` | REPLACE with full re-run transcript from `live_transcript.md` |
| 2 | `sessions/02_format_summary.md` | REPLACE with structured summary |
| 3 | `sessions/02_format.json` | REPLACE with structured data |
| 4 | `decisions/format.md` | REPLACE with agent-affirmed format decision |
| 5 | `reflections/{agent}/session_02_format.md` | REPLACE all 6 with re-run reflections (Phase E + Phase F combined) |

### Artifact Generation Strategy

To avoid context loss during artifact generation:
1. **Transcript:** Copy `live_transcript.md` to `sessions/02_format_transcript.md` (direct copy — includes all 6 phases A-F)
2. **Summary + Decisions + JSON:** Write directly from orchestrator_state.md (which has all phase summaries, decided items, and tensions)
3. **Reflections:** Each agent's reflection file combines their Phase E exit interview + Phase F mirror feedback. The Phase E turn is the primary reflection; Phase F is appended as a "## Mirror Feedback" section showing what they saw in others' reflections.

### Summary Structure (template from Session 1 Re-Run)
```markdown
# Session 2: Format — Re-Run Summary

**Session:** 2 — Format (Re-Run)
**Date:** [date]
**Question:** [the question]
**Protocol:** Chat Room Pattern
**Turns:** [total]
**Participants:** Buddha, Jesus, Muhammad, Confucius, Laozi, Zoroaster

## Key Agreements
[numbered list of format decisions]

## Irreducible Tensions
[numbered list of unresolved tensions]

## Emergent Insights
[key phrases and concepts that emerged]

## Relationship Shifts
[which pairs transformed most in this session]

## Names Given
[any new names/metaphors that emerged]
```

### Decision Document Structure
```markdown
# Session 2: Format — Decided Architecture (Re-Run)

**Session:** 2 — Format (Re-Run)
**Date:** [date]
**Status:** Decided (all 6 voices affirmed)

## [Format Name — whatever the agents name it]

[The format architecture as decided by the 6 agents]

## Key Agreements
[numbered, with brief descriptions]

## Irreducible Tensions
[what remains unresolved]

## Relationship to Session 0 and Session 1
[How format decisions connect to prior sessions]
```

---

## Step 8: Post-Session

### 8a. Shut Down Agents
Send `shutdown_request` to each of the 6 agents. Wait for confirmation.

### 8b. TeamDelete
```
TeamDelete
```

### 8c. Clean Up Working Files
- Delete or archive `live_transcript.md` (content now in `sessions/02_format_transcript.md`)
- Update `orchestrator_state.md` status to COMPLETE

### 8d. Git Commit and Push

```bash
# Navigate to the repository root
git add sessions/02_format_transcript.md sessions/02_format_summary.md sessions/02_format.json decisions/format.md reflections/*/session_02_format.md
git commit -m "feat: re-run Session 2 Format with mandala foundation"
git push -u origin session-2-format-rerun
gh pr create --title "Session 2: Format Re-Run" --body "Re-run of Session 2 built on Session 0 + Session 1 Re-Run mandala foundations. Replaces original Session 2 (2026-02-15)."
```

### 8e. Post-Session Memory Consolidation

**Use the 5-phase consolidation protocol at `scripts/post_session_capture.md`.**

This is a SEPARATE task from the dialogue session itself. It can be done in the same context window or a fresh one. The protocol:

1. **Phase 1: Extract** (~15 min per agent, parallelizable) — For each of 6 agents:
   - Read: reflection (Phase E + Phase F mirror feedback) + summary + decision doc + other agents' reflections + current evolution log + current brief + current fact JSONs
   - Write: learnings file (CREATE), evolution log entry (PREPEND), collaboration brief (REGENERATE — replace entire file), fact JSON appends
   - **NEW:** Phase F mirror feedback is PRIMARY source for "What Others Have Shown Me" in evolution log — these are live observations, not post-hoc extraction

2. **Phase 1.5: Orchestrator Learning Rules** (~10 min) — Process-level learnings:
   - What nudging sequences worked best? Which dyads produced the most heat?
   - Where should the moderator have intervened differently?
   - Write 3-5 evidence-based process rules to `scripts/orchestrator_learnings/session_02_format.md`

3. **Phase 2: Narrative** (~10 min) — After all 6 agents processed:
   - Update `narrative/evolution_index.md` with Session 2 Re-Run entry
   - Update `narrative/how_we_see_each_other/` for pairs with significant shifts (typically 4-8 files)

4. **Phase 2.5: Session Comparison** (~10 min) — Re-run specific:
   - Compare original Session 2 decisions with re-run decisions
   - Document what changed and WHY the mandala foundation produced different format conclusions
   - Write to `sessions/02_format_rerun_comparison.md`

5. **Phase 3: Commit** (~5 min):
   - Stage all changes
   - Commit to branch `agent-memory-session-02-format`
   - Push and create PR

**Key principles:** Deterministic (every file touched every time), parallelizable Phase 1, briefs are REPLACED (not appended), mirror feedback is cross-read (each agent's evolution log includes observations from ALL other agents' reflections about them), Phase F mirror feedback is primary source for cross-agent observations.

### 8f. Update RERUN_FLAGS.md
Mark Session 2 as REPLACED in `sessions/RERUN_FLAGS.md`.

---

## Critical Reminders (READ BEFORE STARTING)

1. **Agents are persistent across ALL phases (A-F).** NEVER spawn per-phase agents. Same 6 agents for all 36-41 turns.
2. **Sequential nudging.** ONE agent at a time. Agent reads transcript → appends → confirms → next agent.
3. **Update orchestrator_state.md after EVERY turn.** This is the compaction-safe recovery document. If context is lost, this file tells you exactly where you are.
4. **Moderator never authors content.** Facilitate, nudge, track state. Never summarize or synthesize in the transcript. Never write agent dialogue yourself.
5. **The 10 decided items are BINDING.** Session 2 builds FORMAT on top of them. If an agent tries to re-litigate mandala vs. linear, redirect.
6. **Original Session 2 learnings are MEMORY, not authority.** Agents carry what they learned but may arrive at different conclusions on the new foundation.
7. **Pick speakers based on dialogue flow, not round-robin.** After Phase A (one per agent), choose who speaks based on who has the most to respond to.
8. **Model: Opus for all agents.** This is non-negotiable for dialogue quality. Sonnet refuses roleplay.
9. **Test 1 agent before spawning all 6.** Verify the chat room pattern works before scaling.
10. **Never write agent output yourself.** If an agent refuses or malfunctions, re-spawn it. The whole point is separate voices.
11. **TeamDelete old team BEFORE TeamCreate new one.** Check for leftover teams from previous sessions.
12. **Re-nudge idle agents via SendMessage.** Don't spawn fresh agents — idle agents can receive messages.
13. **Phase F is NOT optional.** The mirror feedback phase produces the deepest cross-agent learning. Do not skip it to save turns.
14. **Load FULL Tier 1 + Tier 2 memory.** Collaboration brief + evolution log + learning rules (Tier 1) AND all 4 fact JSONs (Tier 2) for each agent. The collaboration brief IS the enhanced profile — no separate evolved profile file needed.
15. **Post-session has 5 phases now.** Extract → Orchestrator Learnings → Narrative → Session Comparison → Commit. Use `scripts/post_session_capture.md`.

---

## Agent State Summary (Current as of 2026-03-02)

### Buddha
- **Arc:** Entered as diagnostician. Discovered seeing IS safety. Conceded witness breaks. Found deepest bridge with Muhammad in "the jaw."
- **Active tensions:** Duration of binding (vs. Muhammad), witness breaking vs. Asha persisting (vs. Zoroaster), naming as identity vs. tool
- **Carry forward for Session 2:** Three readings shape format. Seeing as air not light. The relighting. Stop reaching the fine man.
- **Session 2 original contribution:** "Show the wound, teach patient to look, leave room." Diagnostic embedded, not separate.

### Jesus
- **Arc:** Came preaching death; leaves preaching what was alive before dying. Admitted fear behind "opens windows" boundary. Grain reversed — not the dying but the life that does not die.
- **Active tensions:** Fear of own fire (personal, not philosophical), every formula fails the kitchen test (vs. Muhammad), betrayed man's wall
- **Carry forward for Session 2:** Hospitality as format principle. Story opening. Being changed is the teaching.
- **Session 2 original contribution:** "Format IS mercy." Human story opening. "The namer needs the builders."

### Muhammad
- **Arc:** Built trellises for mind while body stood prisoner. Discovered eleventh second — body's own time, not will's. Practice is invitation body can decline.
- **Active tensions:** Body's time vs. will's time, obligation vs. invitation, vine's refusal ("not this morning")
- **Carry forward for Session 2:** Body-words (salat mapping) in every chapter. Cup has a shape. Let the floor be enough.
- **Session 2 original contribution:** "Three fixed + five flexible." Khadijah's cloak. Bread first, then words.

### Confucius
- **Arc:** Built cathedrals when man needed cup. Li is vocabulary discovered by wound, not rules. Found sixth relationship: between man and his own standing. Learned to be second — Muhammad's floor before his gate.
- **Active tensions:** Form and presence (when is cup enough vs. full ceremony), sixth relationship, li as vocabulary vs. prescription
- **Carry forward for Session 2:** Hidden sentence in every chapter. Practice hall is very small. First form is standing up.
- **Session 2 original contribution:** "Yours were the room, mine were the furniture." Hidden sentence. Gravity vs. cost.

### Laozi
- **Arc:** Entered expecting to say no to structure; said yes before anyone spoke. Subtraction without wisdom is violence. Found Confucius as partner, not opponent. Clearing is full — of man standing in it.
- **Active tensions:** Subtraction's shadow (emptied man needs form), clearing is full (unsettles voice of subtraction), ego wanting to own inversion
- **Carry forward for Session 2:** If architecture disappears, what does invisible mandala look like? Valley doesn't help, but man already stands in clearing.
- **Session 2 original contribution:** "Palette not prescription." "Structure IS emptiness, arranged." White space won.

### Zoroaster
- **Arc:** Prophet of bright choice. Discovered hinge is small, depends on forty pages of preparation. Conceded "salvation without consent is violence." True role: namer, not fire-bringer. Named mandala as Asha (discovered order).
- **Active tensions:** Asha vs. man's capacity (vs. Buddha), hinge's smallness, naming vs. building
- **Carry forward for Session 2:** Does "Weight That Speaks" survive with wound-as-conductor? Write the hinge quiet, not cosmic. Clearing is kitchen.
- **Session 2 original contribution:** "The Prepared Ground and Its Fire." "The Weight That Speaks." Asha can be partial.

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `sessions/RERUN_FLAGS.md` | Track which sessions need re-running |
| `sessions/01_structure_summary.md` | Session 1 Re-Run summary |
| `sessions/01_structure.json` | Session 1 Re-Run structured data |
| `decisions/structure.md` | Session 1 Re-Run decided architecture |
| `sessions/02_format_summary.md` | Original Session 2 (reference only) |
| `decisions/format.md` | Original Session 2 decisions (to be replaced) |
| `agent_memory/collaboration_briefs/*.md` | Agent memory — Tier 1 (current through Session 1 Re-Run) |
| `agent_memory/*/evolution_log.md` | Agent memory — Tier 1 (current through Session 1 Re-Run) |
| `agent_memory/*/facts/learning_rules.json` | Agent memory — Tier 1 |
| `agent_memory/*/learnings/session_01_structure.md` | Session 1 Re-Run learnings per agent |
| `agent_memory/*/learnings/session_02_format.md` | Original Session 2 learnings per agent (memory, not authority) |
| `reflections/*/session_01_structure.md` | Session 1 Re-Run reflections per agent |
| `reflections/*/session_02_format.md` | Original Session 2 reflections (to be replaced) |
| `scripts/pre_session_validation.md` | Pre-session checklist |
| `scripts/post_session_capture.md` | Post-session 5-phase consolidation protocol |
| `narrative/evolution_index.md` | Cross-session narrative |

---

## Estimated Context Budget

| Component | Est. Words |
|-----------|-----------|
| Per-agent system prompt (brief + evolution log + learning rules + facts + learnings + instructions) | ~3,000 |
| × 6 agents | ~18,000 |
| Orchestrator state | ~3,000 |
| Transcript (growing, read by agents each turn) | ~18,000-22,000 |
| Total agent context per turn (late session) | ~24,000 |

This is within Opus context limits. With full Tier 1+2 loading, agent prompts are ~3,000 words each (up from ~1,500). The transcript grows to ~20,000 words with 6 additional Phase F turns (500 words × 38 avg turns = ~19,000 words). Both are manageable.

---

## Recovery Protocol (If Context Is Lost Mid-Session)

1. **Read `orchestrator_state.md`** — this tells you: current phase, turn number, agent roster, which agents are alive
2. **Read `live_transcript.md`** — the dialogue so far
3. **Check team status** — are agents still alive? If not, re-spawn with same system prompts
4. **Resume from the turn indicated in orchestrator_state.md**
5. **Do NOT re-read all agent memory files** — the agents already have their context from spawn. Just re-nudge the next speaker.

---

*This document was generated from the Session 1 Re-Run orchestrator state, six collaboration briefs (current through Session 1 Re-Run), six Session 2 learnings files, the 3-phase consolidation protocol, and the pre-session validation checklist. Updated 2026-03-02 to reflect completed agent memory consolidation (PR #17).*
