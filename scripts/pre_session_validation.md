# Pre-Session Validation Checklist

**Purpose:** Verify all agent memory, profiles, and context are correctly loaded BEFORE starting any handbook dialogue session. Run through every numbered item. Do not skip any.

---

## 1. Evolved Agent Profiles Loaded (NOT Base Profiles)

- [ ] Verify loading `{agent}-dialogue-agent-evolved.md` (not `{agent}-dialogue-agent.md`) for all 6 agents
- [ ] Grep each spawn prompt for the word "evolved" — must be present
- [ ] Check version number in each evolved file: should match latest (currently v1.2)
- [ ] Files located at: `victorious/.claude/skills/prophetic-analysis/agents/dialogue/{agent}-dialogue-agent-evolved.md`

**Verification command:**
```bash
grep -l "version:" victorious/.claude/skills/prophetic-analysis/agents/dialogue/*-evolved.md
# Should return 6 files
```

## 2. Tier 1 Memory Loaded (ALWAYS — ~1,500 words per agent)

For each of the 6 agents, verify these 3 files are loaded:
- [ ] Collaboration brief: `agent_memory/collaboration_briefs/{agent}_brief.md`
- [ ] Evolution log: `agent_memory/{agent}/evolution_log.md`
- [ ] Learning rules: `agent_memory/{agent}/facts/learning_rules.json`

**Verification:** Count loaded files = 18 (3 per agent x 6 agents)

## 3. Tier 2 Memory Loaded (When Accumulated — ~3,000 words per agent)

For each of the 6 agents, verify these are loaded (if they exist):
- [ ] Effective formulations JSON
- [ ] Engagement patterns JSON
- [ ] Bridge vocabulary JSON
- [ ] Emergent insights JSON
- [ ] Most recent session learnings (e.g., `learnings/session_02_format.md`)
- [ ] Most recent reflection (e.g., `reflections/{agent}/session_02_format.md`)

**Verification:** Check that the most recent session number matches the last completed session

## 4. Decision Documents Loaded

- [ ] All prior decision documents from `decisions/` directory are loaded
- [ ] Count matches the number of completed sessions

**Verification:**
```bash
ls handbook-for-living/decisions/*.md | wc -l
```

## 5. Shared Context in Transcript Header (NOT Spawn Prompt)

- [ ] Shared context (convergences, process narrative) goes in the transcript file header
- [ ] Per-agent memory goes in spawn prompt
- [ ] Do NOT put all 6 agents' memory into a single shared context block

## 6. Team Infrastructure Ready

- [ ] Previous team deleted (if any) before creating new one
- [ ] Using TeamCreate + "Chat Room" pattern (shared transcript file + sequential nudging)
- [ ] `live_transcript.md` file created with session header
- [ ] `orchestrator_state.md` file created with agent roster, phase plan, speaker queue
- [ ] All agents spawned with Opus model
- [ ] Test 1 agent before spawning all 6

## 7. Branch Created

- [ ] On new branch: `session-N-topic`
- [ ] Not on `main`
- [ ] No uncommitted changes from prior work

---

**If ANY item fails: STOP. Fix before proceeding. Do not start the dialogue with incomplete context.**
