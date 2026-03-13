# Chapter Launch Instructions — Neutral Protocol

**For:** Any fresh Claude Code context window launching a chapter dialogue session.
**Created:** 2026-03-12
**Source:** Proven launch protocol from Chapter 1 execution.

---

## The Question

### For First Chapter:

> You have defined what this handbook is, how it is organized, and how each chapter should be written. Now: write the first chapter. Which wound do you begin with? And then — write it.

### For Subsequent Chapters:

> The first chapter is written. Which wound comes next? And then — write it.

**Critical: Do NOT suggest wounds, topics, or directions. The agents decide.**

---

## Pre-Flight

1. Ensure on correct branch (or create session branch)
2. Create two compaction-safe files:
   - `sessions/0X_[session_name]_live_transcript.md` — shared transcript with context header + dialogue section
   - `sessions/0X_[session_name]_orchestrator_state.md` — phase, turn count, agent roster, speaker queue, phase flow

The shared context header in the transcript must include:
- All decision documents (definition, structure, format)
- Convergences + evolution index
- **For Chapter 2+:** Prior chapter(s) prose and any decisions made during them

---

## Agent Spawning Protocol

- **All Opus — no Sonnet/Haiku**
- **Test 1 before 6** — spawn one agent, verify it writes to transcript, then spawn remaining 5
- Each agent gets: collaboration brief, learning rules, Tier 2 facts (effective_formulations, engagement_patterns, bridge_vocabulary, emergent_insights), evolution log, most recent session reflection
- **Agents are persistent (standing)** — same 6 agents across all phases A-F

---

## Nudging Protocol

- Same prompt for all agents (neutral): **"The question is on the table. Read the transcript. What do you need to say?"**
- Pick speakers based on dialogue flow, not round-robin
- **Neutral nudges only — do NOT suggest wounds, topics, or directions**
- Update orchestrator state after EVERY turn

---

## Phase Flow

| Phase | What | Target Turns |
|-------|------|-------------|
| A | Opening — which wound, first approaches | ~6 |
| B | Clarifying — probing, hooks | ~12-18 |
| C | Contested — real disagreements | ~6-12 |
| D | Synthesis — convergence, chapter draft emerges | ~6 |
| E | Exit interviews — 5 questions per agent | ~30 |
| F | Mirror feedback — each reads 5 others' reflections, 2-3 sentences | 6 |

---

## Exit Interview Questions (Phase E)

1. What did you come into this session believing that you no longer believe?
2. Which moment in the dialogue changed you most, and why?
3. What is the one thing you contributed that you are most proud of — and the one thing you contributed that you would take back?
4. What do you now understand about one of the other five voices that you did not understand before this session?
5. If the person in the kitchen could hear one sentence from you — not from the chapter, from you — what would you say to them?

---

## Post-Session Artifacts

- Transcript + summary + JSON + chapter content
- Reflections per agent
- Narrative updates (evolution index, convergences)
- Collaboration brief regeneration
- Git commit/push/PR

---

## Critical Rules

| Rule | Why |
|------|-----|
| Neutral nudging only | Agents decide everything |
| Update state after every turn | Compaction safety |
| All Opus | Quality of voice |
| Test 1 before 6 | Catch failures early |
| Agents are standing | Memory across phases |
| No authorial voice | Facilitator only |

---

*Proven in Chapter 1 execution. Use this as the core launch protocol for all chapter sessions.*
