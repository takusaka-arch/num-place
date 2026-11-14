# Layout tweaks needed because the English text is longer than the Japanese
P = [
# App name has 24 letters instead of 9: smaller font so it fits on phones, faster typing
('.splash-title { position: relative; margin: 0; will-change: transform; min-height: 1.4em; font-size: clamp(1.45rem, 6.4vw, 2rem);', '.splash-title { position: relative; margin: 0; will-change: transform; min-height: 1.4em; font-size: clamp(1.1rem, 5vw, 2rem);'),
('animation: splash-ch 0.7s cubic-bezier(.22, .61, .36, 1) calc(0.7s + var(--i) * 0.24s) both; }', 'animation: splash-ch 0.7s cubic-bezier(.22, .61, .36, 1) calc(0.7s + var(--i) * 0.1s) both; }'),
('title.style.transition = `transform ${last ? "0.5s cubic-bezier(.22, .61, .36, 1)" : "0.24s linear"}`;', 'title.style.transition = `transform ${last ? "0.5s cubic-bezier(.22, .61, .36, 1)" : "0.1s linear"}`;'),
# spaces inside inline-block letters would collapse to nothing
('ch.textContent = c;', 'ch.textContent = c === " " ? "\\u00a0" : c;'),
# The English app name is much longer: let it wrap onto two lines on phones instead of overflowing
('.head h1 { display: flex; align-items: baseline; flex-wrap: nowrap; white-space: nowrap; column-gap: 6px; min-width: 0; font-size: min(1.35rem, 5vw); }', '.head h1 { display: flex; align-items: baseline; flex-wrap: nowrap; white-space: nowrap; column-gap: 6px; min-width: 0; font-size: min(1.35rem, 5vw); }\n@media (max-width: 760px) { .head h1 { white-space: normal; line-height: 1.15; } }'),
]
