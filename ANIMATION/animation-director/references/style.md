# The style: how to find it, write it and save it

A style is a small set of rules that makes ten different videos look like one person made them. It is not a mood. Every rule must be something code can follow: a hex code, a size, a number of seconds, a named curve.

## Studying an example

Look at real pictures of the example before you write a word. Use at least four frames spread across it, full size, plus the contact sheet.

Answer every line of this checklist from what you can see. If you can't see it, write "not shown" and choose something that fits the rest.

| Part | What to look for |
|---|---|
| **Colours** | Run `capture.py palette`. Which colour is the ground (the biggest area)? Which is the main subject colour? Which one small colour draws the eye? How many colours in total? Are they flat, or do they shade? |
| **Shapes** | Round or sharp? Thick or thin? Simple blocks or lots of detail? How round are the corners? |
| **Lines** | Are there outlines? How thick, what colour, steady or wobbly? |
| **Texture** | Perfectly clean, or paper grain, noise, brush marks, glow? |
| **Light** | Flat with no light at all? One soft shadow under things? Real light with a direction? |
| **Lettering** | Big or small? Serif (with little feet), sans (plain), handwritten, mono (typewriter)? All capitals? One accent word in another colour? |
| **Characters** | How are they built: simple blocks, round blobs, stick figures, full people? How big is the head against the body? Dots for eyes, or real eyes? |
| **Camera** | Locked still, slow push in, fast cuts, sideways slide? |
| **Motion** | Springy and bouncy, or smooth and slow, or stepped like stop-motion? Do things overshoot and settle? |
| **Pace** | How long does one picture stay before something new happens? Count it on the sheet. |
| **Sound-off test** | What do you understand with no sound? That is what the style is good at. |

### Copy the look, never the content

Take: the colours, the kind of shapes, the line, the texture, the lettering kind, the way things move, the pace.

Leave: their characters, their logo, their words, their layouts, their exact scenes, anything that is recognisably theirs.

A quick test: if a stranger saw your video next to the example, they should say "same taste", not "same video".

If a font in the example has a name you recognise, don't claim it. Pick a free system-safe font or a font stack that looks close, and say so.

## Designing a style (when they have no example)

Start from the look you picked in `looks.md`. Then decide these, in this order:

1. **Three colours and one accent.** A ground, a main colour, an ink for text and lines, and one accent used on at most a tenth of the frame. The ink is dark on a light ground and light on a dark ground. Check the ink on the ground is easy to read.
2. **One lettering choice.** One font family for everything, plus at most one accent face for a single key word. The video file must work with no internet, so choose a font with character from the ones most computers already have (for example Georgia, Trebuchet MS, Verdana, Palatino, Courier New, Impact, Arial Black), and write a stack of two or three close matches. Never leave it to the browser's default. On the style card, check with your own eyes that the chosen font loaded.
3. **One character.** Even explainer styles need a "someone", and if their example shows no character you design one that fits its look. A video uses the character when its idea needs a someone; it doesn't have to appear in every video. Build it from a few simple shapes so it can be drawn the same way every time: body shape, head size, eyes, limbs. Give it one thing that makes it theirs (a colour, a hat, a scarf).
4. **One motion feel.** Pick one easing curve for arriving, one for leaving, and one spring for bounces. Write the numbers. If the style never bounces, say so, and make `spring` the same as the arrive curve.
5. **One background recipe.** How the empty space is filled: flat colour, soft gradient, paper, dots.
6. **Three "never" lines.** What would break this style at once.

Make choices that suit the kind of videos they named and the people who will watch them. Say why in one line each. Simple beats clever: a style a beginner can keep using is better than a rich one that drifts.

## The files

Save these five. Together they are "everything": the colours, the characters and the motion.

### 1. `STYLE.md`

```markdown
# <Style name>
For: <the kind of videos they said>
From: <"designed for you" or "the look of <their example, described in plain words>">
Saved: <date>

## Colours
- Ground: #...... (the biggest area)
- Main: #......
- Ink: #...... (text and lines; light if the ground is dark)
- Accent: #...... (one small thing per picture)
- Extra: #......, #...... (only if needed)
Rule: <flat or shaded, how many colours a picture may use>

## Background
<how empty space is filled: flat colour, soft gradient, paper, dots; with numbers>

## Shapes and lines
<round or sharp, corner size in px at 1080 wide, outline thickness and colour or "no outlines">

## Texture and light
<clean, grain, paper; where shadows go and how soft>

## Lettering
- Main: <font stack>, weight ..., size ... px for a headline at 1080 wide
- Accent word: <font stack and colour>
- Rule: <capitals or not, how many words on screen at once>

## Character
<how it is built, part by part, with sizes as a share of its height; its one special thing; how it shows feelings>

## Camera
<still, slow push, cuts; how often>

## Motion
- Arrive: <curve as cubic-bezier numbers>, <seconds>
- Leave: <curve>, <seconds>
- Bounce: <spring numbers or "none">
- Rule: <one main thing moves at a time; something small always alive>

## Pace
<a new thing every ... seconds>

## Never
- <three or more lines>
```

### 2. `tokens.css`

Every colour, font and size as a CSS variable, so no video ever types a colour by hand:

```css
:root {
  --ground: #......; --main: #......; --ink: #......; --accent: #......;
  --font: ...; --font-accent: ...;
  --radius: ...px; --line: ...px;
  --ease-arrive: cubic-bezier(...); --ease-leave: cubic-bezier(...);
}
```

### 3. `kit.js`

Small plain JavaScript helpers that draw this style, with no outside libraries. Keep it under about 200 lines. It should hold at least:

- `TOKENS`: one object holding the same colours, fonts and sizes as `tokens.css`, because code that draws on a canvas can't read CSS variables directly;
- `ease.arrive(x)`, `ease.leave(x)`, `spring(x)`: the motion curves as functions of 0 to 1;
- `drawBackground(ctx or element, t)`: the background recipe;
- `drawCharacter(target, {x, y, size, mood, t})`: the character, the same way every time;
- `textBlock(...)`: a headline in the style.

Every function must depend only on what it is given and on the time `t`, never on real clocks or unseeded randomness, so a frame at 3.2 seconds always looks the same.

### 4. `style-card.html`

One page, 1080 by 1350, that needs no other file: put `tokens.css` in a `<style>` tag and `kit.js` in a `<script>` tag at the top. It shows:

- the style's name;
- the colours as labelled swatches with their hex codes;
- the lettering: one headline and one accent word;
- the character, in two moods;
- one small scene using the background recipe;
- one thing moving, so the motion feel can be seen (it must look right at 1.5 seconds).

### 5. `style-card.png`

The picture of that page, taken with `capture.py stills`. This is what you compare every later video against.

## Keeping the style over time

- Read `STYLE.md` and open `style-card.png` at the start of every video.
- Paste `tokens.css` and `kit.js` into every animation file. Never retype colours.
- If a video needs something the style doesn't cover (a second character, a new colour for a chart), make it from the existing parts, and ask before adding it to the saved style.
- Log each change to the saved style in `CHANGES.md`: date, what changed, why.
