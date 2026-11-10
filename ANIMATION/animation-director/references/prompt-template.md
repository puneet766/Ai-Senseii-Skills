# The whole prompt

Fill in every part. Keep the headings. The finished prompt must work on its own: someone could paste it into a new chat with no skill installed and get the same job done. Write short, concrete lines a stranger could picture. Replace every `<...>`.

```text
Make a short animation in code. You can't film anything, so you will write code that draws
every picture. Direct it like a film.

THE ONE IDEA
<one sentence with a change in it>

THE STORY, SECOND BY SECOND
0.0 to <x>s: <what we see. The very first frame is already interesting and already moving.>
<x> to <y>s: <what happens>
<y> to <z>s: <the change, the moment this animation exists for>
<z> to end: <how it lands. Hold the last picture for at least one second.>

THE STYLE (saved: do not change it)
<the style's name, and its rules copied from the saved STYLE.md: colours with hex codes, shapes and lines,
texture and light, lettering, character, motion curves, pace>
Use the saved tokens.css and kit.js, pasted into the file. Do not invent new colours, lettering or
character shapes. (If this prompt is used somewhere the saved files are not available, build the
same things from the rules above.)

THE LOOK OF THIS VIDEO
<what this one video adds inside that style, for example "a night version: the ground colour darkened">
Light: <where the light comes from, its colour, and what it does to shadows>
Colour: <2 or 3 main colours, as hex codes, and one accent>
Camera: <what the saved style says. If it allows a move: one slow move, for example "slow push in">
Motion: <the feel, for example "heavy and slow", or "quick and springy">

WORDS ON SCREEN
<every word that appears, spelled exactly, with the second it appears, or "none". The opening words are
already there on the very first frame.>

NEVER
<each "never" line from the saved STYLE.md>
<each thing they said they hate, in their words>
<each extra mistake picked for this subject>
No cartoon clip-art look unless asked for. No floating parts: whatever stands, stands on something
and has a shadow that touches it. No text on screen unless written in this prompt.

FRAMING
The main subject is at least half the width of the picture. No third of the frame stays empty for
the whole video. On a phone video, keep key things out of the bottom fifth and off the right edge.

FORMAT
One HTML file that needs nothing else: no internet, no images, no outside files.
<width> by <height> pixels. <seconds> seconds long.

BUILD RULES
- Every frame must be worked out from the time alone, so a frame at 3.2 seconds always looks the
  same. Any randomness uses a fixed seed. Use requestAnimationFrame and read the time it gives you.
- Stop on the last frame. Don't loop unless this prompt asks for a loop.
- Use canvas, SVG or CSS for flat looks, and WebGL with your own shaders for anything with real
  light or depth. If you use WebGL, turn on preserveDrawingBuffer.
- For WebGL, keep one copy of the scene code. Copying it per sample can stop the page loading at all.
- Start small: get the main subject right before you add the world around it.

SHOW ME FOUR PICTURES FIRST
Before you finish the whole video, show me four pictures: the opening, the middle, the moment of
change, and the end. Wait for me to say go.

CHECK EVERY PICTURE YOU MADE. IF ONE LOOKS WRONG, FIX IT.
If you can run the file, record it and look at the frames, at least two for every second, and
full size at the first frame, the last frame and the moment of change. Be a harsh reviewer who
didn't make it. Keep a list of what you fixed. If you can't see your own frames, tell me which
moments to pause on and what to look for, and don't say you checked them.
```

## How to fill it in well

- **The story:** three or four beats. A beat is one thing the viewer notices. If two things happen at once, make them two beats.
- **First frame:** on a phone people decide in under a second. Open on the subject, already moving, never on a fade from black.
- **The change:** give it the most time and the best light. Everything before it is setup.
- **Camera:** one move per shot. Slow. Most amateur work has too many moves.
- **The style:** copy it from the saved `STYLE.md`, don't rewrite it from memory. The prompt must still work on its own, so the rules go in as text.
- **Colours:** give hex codes. "Warm" means nothing to code. `#E8A04C` does.
- **Numbers:** add a size or speed wherever you can. "The kitten takes up a third of the frame" beats "big kitten".
- **Length:** 8 seconds is about four beats. A longer video needs more beats, not slower ones.
