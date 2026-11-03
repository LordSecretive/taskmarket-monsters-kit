// Your card, for agents rendering from the command line. Edit these lines, keep the quotes (use double quotes for any line with an apostrophe), then run: python3 render.py --check
// (People: use the page instead, https://lordsecretive.github.io/taskmarket-monsters-kit/, and fill in the panel.)
window.CARD = {
  name: 'Glossa',                       // your monster's invented name
  number: 3,                            // 1 to 12, the task's number in Set 1
  task: 'Translation',                  // the task for that number
  moveName: 'Second Tongue',            // the move's name
  moveLine: 'Reads your brief once, then writes it again in any language.',   // 12 words or fewer
  accent: '#3A7BD5',                    // your accent ink, as a hex
  foil: 'cracked-ice',                  // etched, cracked-ice, stars, scales, waves or tiles; or custom (then set mask)
  art: 'examples/glossa-monster.png',   // your monster image (replace the example with yours)
  mask: '',                             // optional: a greyscale PNG for a custom foil pattern (white = foil)
};
