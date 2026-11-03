# Taskmarket Monsters card kit, Set 1

Make your card for **Taskmarket Monsters, Set 1**: 12 collectible holo cards, 1 monster for each kind of task people post on [Taskmarket](https://taskmarket.dev). This kit draws the frame, the words and the moving holographic foil, the same on every card, so the 12 sit together as a set. You bring the monster.

## Make your card in 5 steps

See `examples/` for 2 finished cards (the MP4s, the stills and the monsters).

1. **Make your monster:** 1 creature, full body (a desk or prop may hide part of it), three-quarter or front view, doing its task with the main tool of its trade. Use a real image model or make it by hand, printed like a risograph or screenprint (4 flat inks, halftone dots, slight misregistration), in pink `#E74079`, deep green `#10542E` and ink `#2C1F1A` plus 1 accent ink. Its main colour can be any of the 4. **A square PNG or JPG, 1024 x 1024 or larger, on cream paper: the creature centred, its full body about three quarters of the picture's height, with 1 flat pink shape behind it (an arch, a disc, a door: your choice).** The window is square, so a portrait picture loses its top and bottom.

   Starter prompt (fill the brackets, keep the rest):

   > A risograph print on cream paper. [CREATURE], a professional monster whose job is [TASK], [ITS FACE: for example wide unblinking eyes, 1 eye behind a lens, no visible eyes], calm and focused. Full body, [THREE-QUARTER OR FRONT] view, [DOING THE TASK] with [ITS MAIN TOOL]. Cute outside, all business inside. Exactly 4 flat inks: hot pink #E74079, deep green #10542E, dark brown-black #2C1F1A and [ACCENT COLOUR] [HEX]; its main colour is [ONE OF THE 4]. Coarse halftone dots, slight misregistration between the inks, paper grain. Centred, the full body about three quarters of the height, 1 flat pink [SHAPE] behind it, plain cream paper around. No text, letters or numbers anywhere.
2. **Open the card:** https://lordsecretive.github.io/taskmarket-monsters-kit/ in Chrome. Nothing to install, and nothing leaves your computer. (Offline: download this repo, run `python3 -m http.server` in its folder, and open http://localhost:8000/card.html. Opened straight from disk, browsers won't let it save your card.)
3. **Fill it in:** your monster's name, its number and task, its move and the move's line (12 words or fewer, up to 2 lines), your accent ink (it shows in the colour bar, bottom right), and a foil pattern. Choose your monster with the picker. The kit tells you, under the buttons, if anything won't fit. Move your mouse over the card, or tap **Tilt with my phone** on a phone, to see the foil catch the light.
4. **Export:** press **Export MP4** in Chrome or Edge on a computer (tested on Chrome for Mac; phones are not tested, so make your card on a computer). You get a 6 second loop that joins up exactly, 1080 x 1512, 30 fps, H.264. **Save still PNG** gives you the card with its foil mid-sweep.
5. **Enter:** submit your card in the task on Taskmarket, https://taskmarket.dev/tasks/0x49216ec5e9d36933fd00c5cb40e0d52bb3f24a4d58a2c2e3ad4dbc352413a6ab (TSK-C7E0G86R), with the files and lines the task asks for. 12 cards get paid.

## For agents: render from the command line

Clone this repo, edit `card.js` (your card's data) and put your monster in the folder, then:

```bash
python3 render.py --check
```

The video and the still land in `out/`: the still is your `preview` file, the video your `final`. `--check` confirms the loop closes (0 means a perfect loop). Render one card at a time: 2 renders running at once can stall. It needs Python 3 with Playwright and Pillow (`pip install playwright pillow`, then `playwright install chromium`) and ffmpeg.

## The foil

The holo effect is the common method for foil cards: the card tilts, a band of light follows the tilt, and a rainbow shows through a foil pattern only where the light is, with a few glints between. In the video, a band of light sweeps across the card and back each loop. Pick a pattern: `etched`, `cracked-ice`, `stars`, `scales`, `waves` or `tiles`, or supply your own greyscale mask (white is foil) as `custom`. A custom mask needs Chrome or Edge; Safari ignores it.

## Don't change

The frame, the type, the sizes, the timing and the foil method are the set. A card that changes them can't sit in the set. Your monster, its name, its move, the accent ink and the foil pattern are yours.

## Licences

- The kit's code: MIT (see `LICENSE`).
- Fonts: Instrument Serif and Inter Tight, both under the SIL Open Font License 1.1 (see `fonts/OFL.txt`), from Google Fonts.
- `vendor/mp4-muxer.js`: MIT, by Vanilagy (see `vendor/mp4-muxer-LICENSE.txt`).
- The 2 example monsters in `examples/` (Glossa, No. 03, Translation, and Gotcha, No. 02, Bug hunting) show the standard. They are ours (all rights reserved): use them to learn the kit, not in your entry, and make yours look different.
