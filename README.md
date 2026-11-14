# Sudoku Solving Assistant (PWA, English version)

This is the English version of the Japanese app 数独回答支援アプリ ([takusaka-arch/sudoku](https://github.com/takusaka-arch/sudoku)). It runs as a separate app at https://takusaka-arch.github.io/num-place/, alongside the Japanese version at https://takusaka-arch.github.io/sudoku/.

Put the contents of this folder on any https server, such as GitHub Pages, and it works as an app.

- Windows (Chrome / Edge): open the page and press the “Install” button in the address bar
- iPhone (Safari): Share button → “Add to Home Screen”
- Android (Chrome): menu → “Install app” or “Add to Home screen”

Once opened, it works without an internet connection (including reading puzzles from photos).

Reading photos uses Tesseract.js (Apache License 2.0), and detecting the board’s outer frame uses OpenCV.js (@techstark/opencv-js, Apache License 2.0).

## Living next to the Japanese version

Both apps are served from the same origin (`takusaka-arch.github.io`), so the English version keeps its data separate:

- localStorage keys start with `numplace-en-` (the Japanese version uses `sudoku-`)
- the service worker cache is named `num-place-v…` and only deletes its own caches

Puzzle and progress files (`.json`) use the same format in both versions, so a file saved in one can be opened in the other.

## Updating from the Japanese version

`tools/build_en.py` rebuilds `index.html` from the Japanese `index.html` using the string tables in `tools/strings/`:

```sh
python3 tools/build_en.py ../sudoku/index.html index.html
```

If the Japanese text changed, the script lists the strings it couldn’t find so you can update the tables.
