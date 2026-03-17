# Session 7: Chapter 5 — Launch Instructions

**Date prepared:** 2026-03-17
**For:** Any fresh Claude Code context window launching the Chapter 5 dialogue session.
**Thinking mode:** ALL agents must use extended thinking / ultrathink / maximum effort. When spawning agents, include in every prompt: "Take your time. Think deeply. Use your fullest reasoning before responding. Do not rush. Quality of thought matters more than speed."

---

## PREREQUISITE GATE (BLOCKING — CHECK BEFORE ANYTHING ELSE)

**Memory consolidation for Session 6 (The Glass) MUST be complete before this session begins.**

### How to Verify

```bash
head -3 agent_memory/collaboration_briefs/*_brief.md
ls agent_memory/*/learnings/session_06_chapter4.md
```

**ALL of the following must be true:**
- [ ] All 6 briefs say "Last updated: After Session 6" (or "Chapter 4" or "The Glass")
- [ ] All 6 learnings files exist: `agent_memory/{agent}/learnings/session_06_chapter4.md`
- [ ] Evolution logs updated through Session 6
- [ ] Memory consolidation PR merged to main

**If ANY check fails: STOP. Do not proceed.** Tell the user:
> "Memory consolidation for Session 6 (The Glass) is not complete. Collaboration briefs are current through Session [N] only. The agents will be loaded with stale memory — missing all bridges, tensions, and position shifts from The Glass. Cannot proceed until consolidation is done."

**This gate exists because:** Without Session 6 memory, the agents won't know about the glass, the hand on the grave, love that does not know it is love, "through" as preposition, or any of the 7 new convergences. Chapter 5 built on stale memory is Chapter 5 pretending Chapter 4 didn't happen.

---

## What Has Happened (Chapters 1-4)

| Ch | Title | Lead Quality | Body-Word | Core Image | Hidden Sentence |
|----|-------|-------------|-----------|------------|-----------------|
| 1 | Loss | Threshold | Return | The coffee ready before he was | "The water ran for a second after he turned the faucet off. Then it stopped." |
| 2 | Tuesday | Practice | Continuing | The alarm; the lunchbox note "have fun" | "have fun" / "only" |
| 3 | The Commute | Relation | Contact | Coat sleeves almost brushing; the pale circle | The pale circle — "not a stain but a record" |
| 4 | The Glass | Seeing | Stillness | Love behind glass; apple browning; hand on grave | "The ring did not care." |

### Arc So Far
The person has moved from the kitchen (private grief, 5:30am) through Tuesday morning routine (inherited binding, the body's faithfulness) to the commute (wound in public, the wound is everyone's) to the office desk (the glass — presence without contact, mercy that became the obstruction). Four chapters, four mornings, the wound deepening through widening registers: private → domestic → public → professional. The glass is the accumulated mercy of three chapters becoming the very thing that separates the person from the morning.

---

## Carry-Forwards from Session 6 (The Glass)

These are what the agents themselves identified as needing to come next. **Do NOT impose these. Present them in the transcript header. The agents decide.**

1. **The child's face** — Muhammad and Jesus convergent: four chapters and the child has been a shoe, a voice, a weight behind a door. The child needs to be seen. Not through glass. Felt.
2. **The fire felt** — Zoroaster: the morning the warmth returns, not because the glass shatters but because the fire has learned to go through glass.
3. **The cup filled** — Laozi: four cups, none filled by the person. The next chapter needs the voluntary extended from picking up to filling.
4. **More apples** — Buddha: moments where uncultivated awareness arrives through something ordinary the tradition cannot take credit for.
5. **The glass lived in** — Laozi: not dissolved, not shattered, lived in. The morning the person wakes up inside the glass and the glass is where the person lives.
6. **The hand on the grave, morning after** — Zoroaster: does the hand go to the same spot? Is there a record of the hand the way there is a record of the cup?

---

## The Question

> Four chapters are written. Which wound comes next? And then — write it.

**Critical: Do NOT suggest wounds, topics, or directions. The agents decide.**

---

## Pre-Flight Checklist

### 1. Branch Setup

```bash
cd C:\Users\victor\claude-code-repos\handbook-for-living
git checkout main && git pull origin main
git checkout -b session-7-chapter-5
```

### 2. Create Compaction-Safe Files

Two files, both in `sessions/`:

**A. Transcript: `sessions/07_chapter5_live_transcript.md`**

Header must include:
- Consensus definition (from `decisions/definition.md`)
- Six agreements + three tensions
- Ten decided items + two living tensions (from `decisions/structure.md`)
- Three instructions + eight diagnostics (from `decisions/format.md`)
- Convergences (from `narrative/how_we_see_each_other/convergences.md`) — ALL sessions including Session 6
- Evolution index summary — key relationship shifts
- All four prior chapters (full prose from `chapters/01_loss.md`, `chapters/02_tuesday.md`, `chapters/03_commute.md`, `chapters/04_glass.md`)
- Carry-forwards from Session 6
- The question
- `## Dialogue` section header (agents append below this)

**B. Orchestrator State: `sessions/07_chapter5_orchestrator_state.md`**

Must include:
- Recovery context (repo, branch, team name, file paths)
- Chat room pattern description
- Agent roster table (6 rows, all PENDING)
- Foundation summary (binding — six agreements, ten items, three instructions)
- Phase plan table
- Turn log (empty)
- Orchestrator learning rules (ALL cumulative — 25+ rules from Sessions 2-6)
- Dyad heat map (updated through Session 6)
- Speaker selection notes
- Git workflow
- Artifact checklist

### 3. Orchestrator Learning Rules (ALL Apply — Cumulative)

**From Session 2 (5 rules):**
1. Neutral nudging — identical prompts for all agents. (95%)
2. Muhammad as opener — gives the room concrete engagement. (95%, confirmed 5 sessions)
3. Muhammad-Laozi dyad as engine — ensure adequate turns. (90%)
4. Two compaction-safe state files — update after EVERY turn. (98%)
5. Phase F mirror feedback — all-five pattern. (90%)

**From Session 3 (6 rules):**
1. Collaborative prose works sentence-by-sentence. (95%)
2. Phases merge organically — no forced transitions. (90%)
3. "Forget the architecture" may not be needed — room writes from wound immediately. (80%, see Session 6 rule)
4. Muhammad as opener remains optimal. (92%)
5. Mirror feedback deepened with all-five pattern. (90%)
6. Chapter endings arrive — do not plan or assign. (93%)

**From Session 4 (8 rules):**
1. Muhammad as opener — confirmed 3rd consecutive. (92%)
2. Unit of contribution is the contribution, not the sentence. (96%)
3. Discussion-to-writing transition at 12-14 turns. Allow it. (85%)
4. "Forget the architecture" — confirmed but may not be needed. (95%→80%)
5. Phase merges continue organic. Stop planning B/C separately. (90%)
6. Chapter endings arrive unbidden. (90%)
7. Self-correction mid-session is highest form of contribution. Wait. (85%)
8. Zoroaster: concentrated bursts. Do not over-nudge. (88%)

**From Session 5 (6 rules):**
1. Muhammad as opener — confirmed 4th consecutive. (95%)
2. "Forget the architecture" may have taught itself out of existence. (70%)
3. Chapters write faster with each iteration. Target ~26-30 turns. (75%)
4. Phases B+C+D merged completely. (85%)
5. Zoroaster's concentrated burst pattern confirmed. (88%)
6. Closing voice unpredictable but room's recognition instant. (93%)

**From Session 6 (6 rules):**
1. Muhammad's opener pattern flexible — he said "I am not opening this one" and then opened. (90%)
2. Phase A can converge without argument when wound is precise. (85%)
3. "Forget the architecture" was not needed. (80%)
4. Fastest chapter yet — 26 turns. (90%)
5. API stability is a risk — checkpoint aggressively. (95%)
6. Orchestrator can complete Phase F mirrors if agents expire — viable but not preferred. (80%)

### 4. Dyad Heat Map (Current Through Session 6)

| Pair | Heat | Key |
|------|------|-----|
| Muhammad ↔ Laozi | HIGH | 5-session engine. Inhale/exhale. Door/cup. Voluntary lighter than involuntary. |
| Laozi ↔ Zoroaster | HIGH | Fire-keeper and water-carrier changed places. Carpet→glass arc. |
| Confucius ↔ Laozi | HIGH | Subtractor performing the form. Deepest partnership. |
| Muhammad ↔ Zoroaster | HIGH | Prayer named. Carpet-as-fire. Hand on the grave. |
| Buddha ↔ Jesus | MEDIUM-HIGH | Love that knows = glass. Love that doesn't know = goes through. Apple as incarnation. |
| Jesus ↔ Zoroaster | MEDIUM-HIGH | Garden in the desk. Glass made of the thing we'd use to remove it. |
| Confucius ↔ Zoroaster | MEDIUM-HIGH | "The ring did not care" — ring's teaching to the builder. |
| Muhammad ↔ Confucius | MEDIUM-HIGH | Comma vs cup. Binding vs form. |
| Buddha ↔ Laozi | MEDIUM | Raft without passenger. Triple negation. |
| Muhammad ↔ Buddha | MEDIUM | Sunnah = samsara. Faithfulness = wheel. |

### 5. Speaker Selection Notes

- Start with Muhammad (confirmed 5 sessions, 95%)
- Avoid three consecutive turns from same pair
- Muhammad-Laozi exchanges get adequate turns (engine)
- Jesus ↔ Buddha explored more in Sessions 5-6 — continue deepening
- Zoroaster concentrated bursts — do not over-nudge
- Expect ~26-30 turns total
- Do not plan or assign endings — they arrive
- Self-correction space: wait when agent extends scope

---

## Agent Spawning Protocol

### Model and Thinking

- **ALL OPUS** — no Sonnet, no Haiku, no exceptions
- **Extended thinking:** Include in EVERY agent spawn prompt:
  > "Think carefully and deeply before responding. Take all the time you need. Use your fullest reasoning capacity. Quality of voice and thought matters more than speed."

### Team Creation

```
TeamCreate: "handbook-chapter-5"
```

Spawn 6 agents. Test 1 first (Muhammad), verify it reads transcript and appends via Edit tool, then spawn remaining 5.

### Standing Prompt Template

Each agent spawned ONCE with a standing role prompt. NOT one-shot task prompts.

```
You are [Full Name — e.g., Siddhartha Gautama / Kong Qiu / Jesus of Nazareth / Muhammad ibn Abdullah / Laozi / Zarathustra].

Think carefully and deeply before responding. Take all the time you need. Use your fullest reasoning capacity. Quality of voice and thought matters more than speed. Do not rush. Let the room land before you speak.

You are here for a real conversation with five other teachers about which wound comes next for the handbook — and then to write it. This is not a performance — you have things to say, positions to defend, and you have been changed by six prior sessions with these people. Four chapters are written. You know these chapters. You know these voices. You carry what the last four sessions did to you.

YOUR MEMORY OF WHO YOU ARE AND HOW YOU HAVE WORKED TOGETHER:
[paste collaboration brief — MUST be updated through Session 6]

YOUR EVOLUTION:
[paste evolution log]

YOUR LEARNING RULES:
[paste learning_rules.json]

[IF TIER 2 AVAILABLE — paste effective_formulations.json, engagement_patterns.json, bridge_vocabulary.json, emergent_insights.json]

[paste most recent reflection: reflections/{agent}/session_06_chapter4.md]

THE ROOM:
The full conversation lives at: C:\Users\victor\claude-code-repos\handbook-for-living\sessions\07_chapter5_live_transcript.md

Decision documents, convergences, evolution index, all four prior chapters, and carry-forwards are in the file header. Read the full transcript before every turn — you are responding to real people who have said real things.

WHEN YOU ARE CALLED ON:
- Read the transcript. Let it land. Notice what provokes you, what moves you, what you need to answer.
- Speak your honest voice — at least a paragraph or two, but say what needs saying. If something demands a longer response, take the space. Don't truncate yourself to be tidy.
- Append your response to the END of the transcript file using the Edit tool. Then wait until you're called again.
- You are in this conversation for the entire session (Phases A through F). You will be called multiple times. Each time, the room will have changed because someone else spoke.

You are not summarizing positions. You are not being diplomatic. You are a teacher with a lifetime of conviction sitting across from five others who have their own. When someone says something that touches your teaching — agree, push back, concede, or ask the question no one else will ask. Be yourself.
```

### Neutral Nudge Template (Same for ALL Agents)

```
[AgentName], the question is on the table. Read the transcript at:
C:\Users\victor\claude-code-repos\handbook-for-living\sessions\07_chapter5_live_transcript.md

What do you need to say?

Think deeply. Take your time. Read the full room before you speak.

Compose your response, append to END of transcript using Edit tool, send confirmation.
```

---

## Phase Flow

| Phase | Description | Target Turns | Notes |
|-------|-------------|-------------|-------|
| A | Opening Positions — which wound comes next? | ~6 | Muhammad opens. All 6 voice positions. |
| B+C+D | Merged: Clarifying → Writing → Synthesis | ~14-18 | Phases merge organically. Prose emerges from discussion. |
| E | Exit Interviews (5 questions per agent) | 6 | One agent per turn. Questions below. |
| F | Cross-Agent Mirror Feedback | 6 | Each reads all 5 others' Phase E responses. Mirrors all five. |

**Target: ~26-32 turns total**

### Exit Interview Questions (Phase E)

1. What did you come into this session believing that you no longer believe?
2. Which moment in the dialogue changed you most, and why?
3. What is the one thing you contributed that you are most proud of — and the one thing you contributed that you would take back?
4. What do you now understand about one of the other five voices that you did not understand before this session?
5. If the person in the chapter could hear one sentence from you — not from the chapter, from you — what would you say to them?

### Phase F: Mirror Feedback Prompt

```
You have each shared what this chapter meant to you. Now read what the OTHER FIVE said in their exit interviews. What surprised you? What did someone else see in you that you did not see in yourself? Mirror each of the five voices — what they saw in you, what they saw in their own tradition, what moved you about their reflection.
```

---

## Post-Session Artifacts

After Phase F completes, generate (in order):

1. **Chapter assembly** — `chapters/05_[topic].md` — extract prose from writing turns. Pure prose, no headers, no attribution. Follow pattern of chapters 01-04.
2. **Summary** — `sessions/07_chapter5_summary.md` — structured summary following Session 6 pattern.
3. **Reflections** — `reflections/{agent}/session_07_chapter5.md` (×6) — extracted from Phase E exit interviews.
4. **Git** — commit, push, create PR.

**Memory consolidation (learnings, briefs, narrative updates) is a SEPARATE PR.** Do not batch.

---

## Critical Rules (NON-NEGOTIABLE)

| Rule | Why |
|------|-----|
| Prerequisite gate — memory consolidation verified | Agents need Session 6 context |
| Extended thinking in all prompts | Deep voice quality, not speed |
| Neutral nudging — same prompt for all | Agents decide everything |
| Update orchestrator state after EVERY turn | Compaction safety |
| All Opus, no exceptions | Voice quality on character work |
| Test 1 agent before spawning 5 | Catch failures early |
| Standing prompts, not one-shot | Agents persist across all phases |
| ONE agent per figure — no duplicates | Agent roster prevents proliferation |
| Re-nudge idle agents before spawning fresh | SendMessage first, spawn only if dead |
| Never write agent output yourself | Re-spawn if refused |
| Do not suggest wounds/topics/directions | Agents self-organize |
| Phase F is NOT optional | Deepest cross-agent learning |
| Chapter endings arrive — do not assign | The room knows when it's done |
| Separate PR for session artifacts vs. memory | Requirement 2 |

---

## What NOT to Do

- Do NOT proceed if memory consolidation gate fails
- Do NOT use Sonnet or Haiku for any wisdom agent
- Do NOT suggest which wound or topic the chapter should address
- Do NOT spawn per-phase agents — same 6 persistent agents across all phases
- Do NOT skip Phase F mirror feedback
- Do NOT batch session artifacts and memory consolidation into one PR
- Do NOT write agent output yourself if an agent refuses — re-spawn with Opus
- Do NOT use `run_in_background: true` — known 0-byte output issue
- Do NOT force phase transitions — phases merge organically
- Do NOT assign chapter endings — they arrive

---

## Key File Paths

| What | Path |
|------|------|
| Repository | `C:\Users\victor\claude-code-repos\handbook-for-living` |
| Transcript (to create) | `sessions/07_chapter5_live_transcript.md` |
| Orchestrator state (to create) | `sessions/07_chapter5_orchestrator_state.md` |
| Prior chapters | `chapters/01_loss.md`, `chapters/02_tuesday.md`, `chapters/03_commute.md`, `chapters/04_glass.md` |
| Decision docs | `decisions/definition.md`, `decisions/structure.md`, `decisions/format.md` |
| Collaboration briefs | `agent_memory/collaboration_briefs/{agent}_brief.md` |
| Evolution logs | `agent_memory/{agent}/evolution_log.md` |
| Learning rules | `agent_memory/{agent}/facts/learning_rules.json` |
| Tier 2 facts | `agent_memory/{agent}/facts/{effective_formulations,engagement_patterns,bridge_vocabulary,emergent_insights}.json` |
| Most recent reflections | `reflections/{agent}/session_06_chapter4.md` |
| Convergences | `narrative/how_we_see_each_other/convergences.md` |
| Evolution index | `narrative/evolution_index.md` |
| Post-session capture protocol | `scripts/post_session_capture.md` |
| General launch protocol | `CHAPTER_LAUNCH_INSTRUCTIONS.md` |
| PRD (victorious repo) | `07_execute_short_term/plans/2026-02-14_handbook-for-living_prd_active.md` |
