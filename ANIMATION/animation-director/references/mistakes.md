# What goes wrong in code-drawn animation

Two uses. Before making: pick the ones that fit this subject and add them to the prompt's NEVER list. While checking: look for all of them, frame by frame.

Most of these came from real fixes on real test runs.

## Faces and creatures

- Eyes are bare balls stuck on the head. Seat them in the skull, with lids.
- Goggle rings or a raccoon mask around the eyes, from a shadow or eyeliner spreading too far. Keep it thin.
- The face looks angry when it should be curious. Lift the brow.
- Ears, nose or whiskers too big or too thick. Most small parts should be smaller than your first guess.
- Ears stick out sideways, or fold into stubs in fast motion. Check the rotation at speed, not only at rest.
- A dark crease where the head joins the neck. Blend the join.
- Legs look like grey pegs, or a thigh looks like a slab pasted on. Limbs should grow out of the body, in the same colour and texture.
- Fur or hair takes its colour from the wrong body part.
- Fur smears backward in fast moves. Use less drag.

## People and hands

- Wrong number of fingers. Hands that melt or bend the wrong way.
- Hands that hover near what they should touch. Contact must be real.
- Arms that stretch or change length during a move.
- A stiff upper body. People lean into every move.

## Standing on the world

- Floating parts: a subject that hovers above its shadow, or a shadow that doesn't touch its feet. Contact shadows must meet the feet. A running or jumping animal does leave the ground, so write "feet land on the ground", not "every foot touches in every frame".
- Feet that slide on the ground while walking.
- Anything that passes through something solid.
- A shadow on the wrong side of the light.
- A shadow map with a hard straight edge, showing as a line across the ground. Fade long shadows out.

## Light and colour

- Flat, even light on everything. Pick one main light, and let some parts fall into shadow.
- The ending washes out, or the sun is a plain white disc. Deepen the sky around it, and keep colour in the bright part.
- A colour that shifts because of what's behind it: red turning pink on a bright sky. Darken behind it.
- Backlit subjects still lit from the front. If the light is behind, the subject goes dark with a bright edge.
- Banding: visible stripes in smooth gradients. Add a tiny amount of fine grain.

## Framing

- The camera cuts off the subject's head.
- The most important thing leaves the frame, or passes behind something, at the key moment.
- The subject is too small to read on a phone, or a third of the frame sits empty the whole time. The main subject should be at least half the width.
- On a phone video, key things sit where the app's buttons cover them. Keep them away from the bottom fifth and the right edge.

## Timing

- Dead gaps: one thing ends before the next begins, so for half a second nothing happens.
- A change so fast nobody sees it. Give the change at least a full second.
- The last picture is cut short. Hold it for a second or more.
- Linear motion: everything moves at one speed, like a machine. Ease into and out of every move. Heavy things start slowly.
- Everything moves at once. Only one main thing at a time, with something small staying alive in the background.
- Jumps between two frames: a part pops to a new place for one frame.

## Text

- Letters cut off at the edge, or running out of a box.
- Text that appears for too short a time to read. Allow about 0.3 seconds a word.
- Spelling mistakes. Check every word, every time.
- A plain default font, or a chosen font that silently fell back to the default. Pick a font with character that most computers have, and check the lettering in the picture.

## Technical

- A blank or black frame, often at the very first picture.
- Patterns that read as scan lines, such as sand ripples drawn too evenly. Break them up.
- The page never finishes loading, because a heavy WebGL scene takes too long to compile. Keep one copy of the scene code.
- A different picture on each run, from unseeded randomness.
- Errors in the page's console, even when the video seems fine.
