# Test your business idea before you spend a dollar

Your IDEA starter setup: the best order to run the Founder skills, your first test prompts, and a small skill that runs it all for you.

**Founder is not mine.** It's a free pack of 11 Claude skills by Jake Schincariol: [github.com/Jakeschincariol/founder-skill](https://github.com/Jakeschincariol/founder-skill) (MIT licence). All credit for it goes to him. This starter is separate, and he isn't involved.

## What you need

- **Claude Code.** It comes with paid Claude plans. Founder's 100-buyer panel and profit tools need it, and they don't run in the normal Claude chat. New to it? [Install guide](https://code.claude.com/docs/en/overview).
- **Python 3.8 or newer.** It's free, and there's nothing else to install. If you don't have it, Claude will tell you.
- A new empty folder for each idea. Everything gets saved there, in a folder called `founder`.

## Set it up (5 minutes)

**1. Open Claude Code in a new empty folder.**

**2. Install Founder.** Paste this and send it:

```text
https://github.com/Jakeschincariol/founder-skill

install skill
```

Claude will read the page and copy the skills. It will ask your permission to save files: say yes. If that doesn't work, use these two commands instead. Then the skills are named like `/founder-skill:founder-board`:

```text
/plugin marketplace add Jakeschincariol/founder-skill
/plugin install founder-skill@founder-skill
```

**3. Install the starter.** Paste this and send it, then say yes when Claude asks to save files:

```text
https://github.com/puneet766/ai-senseii-skills/tree/main/IDEA/idea-test

install this skill in my personal skills folder
```

Or copy the `idea-test` folder into your skills folder by hand:

- Mac: `~/.claude/skills/`
- Windows: `C:\Users\<your name>\.claude\skills\`

**4. Start it.** Type `/idea-test`. It asks about your idea, then does the rest.

## The best order

Founder's own list runs all 11 skills in a row. For a first test, don't. Spend the least to find out if the idea deserves more.

**First, is this idea worth it?**

| Step | Skill | What it tells you |
|---|---|---|
| 1 | `founder-board` | Three judges score the idea, using lessons from published books |
| 2 | `founder-competitors` | Who else sells this, and what their customers hate |
| 3 | `founder-consumer` | How test buyers react, with 20 buyers rather than 100 |
| 4 | `founder-cfo` | Your real profit on each sale, and how many you need to sell |
| 5 | `founder-plan` | The verdict: Profitable, Not yet or Incomplete |

**Only if it passes:** `founder-pricing`, `founder-offer`, `founder-marketing`, `founder-brand`, `founder-ops`, `founder-launch`, then `founder-plan` again.

**Why I moved the CFO up.** The price and offer skills read a numbers file that only the CFO writes. In the original order they run before it exists.

## Your first test prompts

Don't want the skill? Use these one at a time, in the same folder. Replace the matcha example with your own idea. These are the first ones to try:

```text
/founder-board A matcha cafe in Toronto called Moss. Iced matcha lattes, $6.50 a cup, for office workers aged 24 to 38.
```

```text
/founder-competitors Toronto, King Street West
```

```text
/founder-consumer Run the panel with 20 buyers. Make sure the tool really uses 20.
```

```text
/founder-cfo Here are my costs. Mark every guess as a guess.
```

```text
Before you run the plan, open founder/numbers.json and tell me if any costs are missing. Then run /founder-plan.
```

Press **Shift+Tab** before the buyer panel to accept file edits. If you don't, Claude asks for your OK on every buyer's file.

## Seven traps

1. **A "Profitable" verdict can be false.** Missing costs count as zero, and with no buyer panel the verdict ignores demand. "Profitable" means the numbers you entered add up. It never means people will buy. `/idea-test` checks this for you.
2. **`--quick` may not work.** The docs say it runs 20 buyers, but the panel tool doesn't have that option. Say "20 buyers" in words.
3. **The offer re-test can repeat the old result.** The panel keeps old answers. Before the re-test, move the old `panel` folder aside. `/idea-test` does this for you.
4. **The margin can be a dream.** The matcha example shows 38% at 383 cups a day, but its own year one only reaches 292 cups, where the margin is about 27%. Always compare your plan with what you really reach.
5. **`python3` may fail on Windows.** Tell Claude to use `python` or `py -3` instead.
6. **Not in dollars?** The tools print `$` for everything. In our test, a salary in rupees showed up as dollars, so the buyers looked rich. `/idea-test` fixes this before the buyers run. If you go by hand, ask Claude to check the buyer briefs for your currency.
7. **Don't let your pitch invent things.** Check it says only what's true. Buyers react to every word, and in our test Claude added payment terms nobody gave.

## The one rule

AI buyers lean polite. Treat every yes as the most you'd get. Use the panel to find doubts, never as a forecast, and never use its words as customer reviews.

Then test on real people. Put up a page with the real price and a sign-up or pre-order button. Decide your pass line before you look, for example 20 sign-ups from 500 visitors in 7 days. If real people fall short of the panel, trust the real people.

## What it costs

Founder is free. It runs on your own Claude plan, and each test buyer is one helper, so 100 buyers uses a lot more of your limit than 20. That's why we start with 20.

## What a real run looks like

We tested this setup on a made-up lunch subscription. It said **Not yet**: 0 of 20 test buyers bought, and year one made a loss. It also named the main doubt (trust, not price) and a smaller cost to fix first. That's the point: a clear no for free is the best result you can get before you spend.

This is research, not financial, legal or tax advice. The board uses published frameworks: it isn't those authors, and they aren't involved.
