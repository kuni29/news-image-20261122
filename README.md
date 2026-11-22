# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/kuni29/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/kuni29/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up the world news of Sunday 22 November 2026, drawn as a newspaper front page in a graphic-recording style: a large central visual for the day's biggest story — COP31 collapsing in Antalya with no deal, the 1.5°C overshoot admitted and fossil fuels never named — a world-map strip marking where the day happened, a "how today connects" arrow flow from Iran's strike on Bahrain through the Hormuz tanker attacks to the AI sell-off, two more hero stories (Iran hits Bahrain as two tankers burn in Hormuz; cartel boss 'El Chapo Isidro' captured in Sinaloa, 11 killed), three big-number features (2,700 Russian drones in a week; S&P 500 −3.7%; the Trump–Xi–Putin trilateral in Shenzhen) and 24 one-line briefs from every region, 30 stories in all, each colour-coded by category. Every story was first reported on 22 November 2026. The picture is designed in `design.html` with hand-drawn inline SVG illustrations and rendered to `entry.png` by `render.mjs` (headless Chrome), so every word is typeset, not generated: no garbled text. `main.py` delivers the image bytes to the output directory, unchanged on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under the 1 MiB cap).

---
<sub>Entered on [make.fun](https://make.fun/?ref=sjptyjw4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
