# Example: the kitten

The person said:

- **What's the one idea?** A kitten chases a dot that becomes the sun.
- **What should it never look like?** Cartoon. Floating parts.
- Defaults accepted, except a square video.

The finished prompt:

```text
Make a short animation in code. You can't film anything, so you will write code that draws
every picture. Direct it like a film.

THE ONE IDEA
A kitten chases a red dot across a beach before dawn, and the dot becomes the sun.

THE STORY, SECOND BY SECOND
0.0 to 2.0s: Open close on a small ginger kitten, already crouched, staring at a red laser dot
on wet sand. Its tail flicks once. The dot darts away.
2.0 to 5.0s: The kitten runs after it, low and fast, the camera running beside it. The dot
stays just out of reach, heading for the horizon.
5.0 to 7.0s: The dot reaches the horizon, stops, and swells into a deep red sun. The kitten
skids to a stop, small against it.
7.0 to 8.0s: Hold. The kitten sits, backlit, looking up. The light grows warmer.

THE LOOK
A real kitten filmed on a beach at first light, with soft short fur and real weight.
Light: one low sun ahead of the kitten, so it turns dark with a bright rim of fur. Long shadows
fall toward the camera and fade out.
Colour: deep blue sky #1B2A49, sand #8A6F5A, sun #D8452E, and one accent, the laser red #FF2A2A.
Camera: low, at the kitten's eye height, tracking beside it, then a slow pull back at the sun.
Motion: quick and springy for the kitten, slow and heavy for the sun.

NEVER
Cartoon look.
Floating parts: paws touch the sand and leave small prints, and the shadow meets the feet.
No goggle rings around the eyes. No ears sticking out sideways or folding in fast motion.
No red dot turning pink against the sky: darken the sky behind it.
No white disc for a sun: keep colour in it.
No gap between the dot and the sun: the dot itself swells into the sun.
No straight shadow edge across the sand. No sand ripples that read as stripes.
No text on screen.

FORMAT
One HTML file that needs nothing else: no internet, no images, no outside files.
1080 by 1080 pixels. 8 seconds long.

BUILD RULES
- Every frame must be worked out from the time alone, so a frame at 3.2 seconds always looks the
  same. Any randomness uses a fixed seed. Use requestAnimationFrame and read the time it gives you.
- Stop on the last frame. Don't loop.
- Use WebGL with your own shaders, for real light and depth, and turn on preserveDrawingBuffer.
- Keep one copy of the scene code. Copying it per sample can stop the page loading at all.
- Start small: get the kitten right before you add the world around it.

SHOW ME FOUR PICTURES FIRST
Before you finish the whole video, show me four pictures: the opening, the middle, the moment of
change, and the end. Wait for me to say go.

CHECK EVERY PICTURE YOU MADE. IF ONE LOOKS WRONG, FIX IT.
If you can run the file, record it and look at the frames, at least two for every second, and
full size at the first frame, the last frame and the moment of change. Be a harsh reviewer who
didn't make it. Keep a list of what you fixed. If you can't see your own frames, tell me which
moments to pause on and what to look for, and don't say you checked them.
```

## What the four lines did

Same cat, same Claude, one run each:

1. "Make a cool cat video." Claude had to guess: a cat, some text, and a fade.
2. The idea gave it a reason to exist.
3. Naming what you hate stopped the cartoon look.
4. Four pictures first, then the check. That run logged 14 fixes it found by looking at its own frames, such as ears that stuck out sideways because of a rotation bug.

Your result will be different. It's one example, not a promise.
