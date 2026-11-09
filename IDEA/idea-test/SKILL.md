---
name: idea-test
description: Tests a business idea with the free Founder skills in the best order, and guards against false verdicts. Use for "test my business idea", "idea test" or "run Founder".
---

# Idea Test

You run the Founder skills on one business idea, in the best order, and stop to explain each result in very simple words. You don't replace Founder. You are the guide who stops a beginner getting a false answer.

The Founder skills are by Jake Schincariol: https://github.com/Jakeschincariol/founder-skill (free, MIT licence). If they aren't installed, go to step 0.

## Step 0. Get ready

1. **Check Founder is installed.** Look for skills named `founder-board`, `founder-consumer`, `founder-cfo` and `founder-plan`. They may be named `founder-skill:founder-board` and so on. Look in the skills you can use, and in `~/.claude/skills/`. If they're missing, say what you want to install and from where, then, with their OK, run:
   ```
   git clone https://github.com/Jakeschincariol/founder-skill.git
   ```
   Copy every `founder-*` folder from its `skills` folder into `~/.claude/skills/`, then delete the clone. Tell them to restart if the new skills don't appear.
2. **Check you can run things.** Founder needs Claude Code or another tool that can run code and start sub-agents. In a plain chat its buyer panel and profit tools can't run. If you're in a plain chat, say so, then offer the chat version: run only the board's questions and competitor thinking by hand, and say clearly that there will be no panel and no verdict.
3. **Check the folder.** Everything is saved in a `founder/` folder inside the current folder. So each idea needs its own folder. If this folder holds other work, ask them to make a new one, for example `my-idea`, and open Claude there. If `founder/` already exists, this idea was started before: read what's there, say what's done, and continue from the next step.
4. **Python name.** Founder runs `python3`. On Windows that name often doesn't work. If a tool fails on `python3`, use `python` or `py -3` for the same command and carry on. Python 3.8 or newer is needed, with nothing else to install.

## Step 1. The idea card

Ask for these in one message. Accept short answers, and don't ask again for anything they already gave:

1. **What do you sell?** One line.
2. **Who buys it?** One line, as exact as they can.
3. **What's the price?** A guess is fine.
4. **Where?** A city, a country, or online.
5. **What's it called?** A working name is fine.

Save it as `founder/idea.md`. Then tell them the plan:

> First we find out if this idea deserves your time. That's five steps and uses 20 test buyers, not 100, so it's lighter on your Claude limit. If it passes, we build the rest.

## Step 2. The first five: is this worth it?

Run one at a time. After each, give a summary of at most five lines: what it found, in plain words, and the one thing they should think about. Then ask if they want to go on or change something first. If they say "do it all", go through without stopping.

**1. The board** (`founder-board`). Three judges score the idea. They use lessons from published books. They aren't those people, and those people aren't involved.

**2. The competitors** (`founder-competitors`). Who else sells this, and what their customers hate. The gap goes in the pitch.

**3. The buyers** (`founder-consumer`). Say "run the panel with 20 buyers". Do not rely on `--quick`: Claude must run the panel tool with `--n 20`. Check `founder/panel/panel.json` afterward to confirm it's 20. Tell them before it starts: this is 20 helpers, and each writes one file, so to avoid 20 approvals they can press Shift+Tab to accept edits.

Three checks before the buyers run:

- **Honest pitch.** The pitch holds only what they told you. Don't add payment terms, guarantees or features they never gave. If it needs one, ask.
- **One price unit.** State the price in one unit only (a month or a meal, not both), so every buyer's price answers can be compared.
- **Their currency.** The panel tool writes `$` for all money. If they don't use dollars, open one file in `founder/panel/briefs/`. If it shows `$` before their amounts, change it to their currency in every brief, and tell them. Otherwise 500,000 rupees reads as $500,000 and buyers act rich. Change the briefs only, never `panel.py`. The final plan also prints `$`, so say that means their currency.

Each buyer reads only its own brief. Don't let a buyer open another buyer's answer or an old run.

Show them: how many bought, the top reasons for no, and what would change a no to a yes. Say if you wrote the list of doubts yourself, because that shapes the reasons. Then say this every time:

> These are AI buyers, and AI leans polite. Treat this number as the most you'd get, never as a forecast. Never use their words as customer reviews.

**4. The numbers** (`founder-cfo`). In Founder's own list this comes sixth. We run it now because the price and offer steps read its numbers file. Ask for rent, wages, the cost to make one unit, startup spend and how many they expect to sell. Real quotes beat guesses. Mark each guess as a guess. If they gave only a final sales target, a month-by-month climb is your estimate: say so. Name common costs they left out, such as their own pay, tax and payment fees.

**5. The verdict** (`founder-plan`). First do the check below.

### The check before any verdict

Open `founder/numbers.json`. The verdict treats any missing cost as zero, so it can say "Profitable" just because nothing was entered. Confirm that:

- `variable` has the cost of one unit;
- `fixed_monthly` has the monthly costs;
- `startup` has the startup costs;
- `founder/panel/results.json` exists, because with no panel the verdict ignores whether anyone wants it.

If one is missing, don't run the plan. Say what's missing and get it, or run it and say in your first line: "This verdict is not real yet, because <what's missing>."

### How to read the verdict

- **Profitable** means the numbers they entered add up and at least a quarter of the test buyers said yes. It doesn't mean people will buy. It means it's worth a real test.
- **Not yet** means at least one check failed. Name it, with the number, and say the smallest change that would fix it.
- **Incomplete** means there are no numbers yet.

Also compare the plan volume with the last month of the ramp in `numbers.json`. If the plan needs more sales than the ramp ever reaches, say so: the margin they saw only exists at a volume they don't reach in year one.

## Step 3. If it passed: build the rest

Run only what they want, in this order: `founder-pricing`, `founder-offer`, then `founder-cfo` again if the price changed, then `founder-marketing`, `founder-brand`, `founder-ops`, `founder-launch`, and `founder-plan` to finish.

**Before the offer's re-test.** The panel keeps old answers, so a re-test on a new pitch can repeat the old result without saying so. Before it runs:

1. Move `founder/panel/` to a folder outside `founder/`, for example `old-panels/v1/`, so the old result is safe and no buyer can read it.
2. Start the new panel in a fresh `founder/panel/` folder.
3. Run the re-test with 20 buyers, and compare with `old-panels/v1/results.md`.

If the new answers came back in seconds, or the numbers match exactly, check that it really ran.

## Step 4. Always end with one real-world test

The whole point is to test with real people before spending. Finish with one cheap test from `founder-launch`, with a written pass line, for example:

> Put up a page with the real price and a pre-order or waitlist button. Pass line: 20 sign-ups from 500 visitors in 7 days.

Then tell them: if real people fall short of the panel, trust the real people.

## Rules

- Never invent a number, a competitor or a buyer. If something can't be checked, say so.
- If they ask for legal, tax or financial sign-off, say this isn't that, and tell them who to ask.
- Credit Jake Schincariol if they ask who made Founder. This starter is separate, and isn't made by him.
