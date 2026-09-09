# BosonField Open

**Open-source AI video, made usable.**

BosonField Open will turn free and openly licensed AI-video tools into beginner lessons, tested workflows, and community-built software. The goal is not to copy Higgsfield. The goal is to build an independent, inspectable path that creators can run, learn from, and improve.

## What ships first

1. **License map** — exact model terms, region limits, and commercial-use notes.
2. **Hardware checker** — a local tool that tells a creator what will run on their computer.
3. **Tested workflow packs** — versioned ComfyUI workflows with sample inputs and measured run settings.
4. **Beginner lessons** — one result per lesson, exact files, exact settings, and a repair path for common errors.
5. **Public benchmark table** — time, memory use, output size, and quality notes on real hardware.

## Important H3 finding

MiniMax H3 is not the launch model for this project. The official MiniMax H3 Community License dated 2 August 2026 excludes the European Union, United Kingdom, Republic of Korea, and United States from its licensed territory. Ryan is in Spain and the build computer is in the United States, so BosonField will not download, run, or redistribute H3 unless MiniMax publishes terms that cover both places.

Official source: <https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE>

BosonField can still publish a plain-language news lesson explaining that limit and can teach lawful alternatives whose official terms permit the intended use.

## First engine decision

Start the real-machine test with **Wan2.1 T2V-1.3B at 480p**. Its official project states Apache-2.0 terms and 8.19 GB of video memory, called VRAM. The BosonField test machine has an NVIDIA TITAN X with 12,288 MiB of VRAM, so this is the first engine whose stated memory fits the machine. A real render must still prove that this GPU, its driver, the exact Python packages, and the pinned model revision work together.

Add **Wan2.2 TI2V-5B** later as the 24 GB quality tier. Its official instructions say at least 24 GB of VRAM with memory offloading, which moves parts of the model out of GPU memory. Keep every other engine behind a license and location check.

Official Wan2.1 source: <https://github.com/Wan-Video/Wan2.1>

## Project rules

- Our code is Apache-2.0 licensed.
- Every model keeps its own license. We never call a model “open source” without checking its exact license.
- Every tutorial shows the exact software version, input files, hardware, run time, memory use, and output.
- No copied Higgsfield code, text, art, workflows, or brand style.
- No hidden affiliate link. Paid links are labeled.
- No training data or upload is collected without a clear opt-in.
- Synthetic media is labeled when a platform requires it or when a reasonable viewer could mistake it for a real event.

## Working public name

- Display name: **BosonField Open**
- Main handle target: **@bosonfieldopen**
- Short bio: **Open-source AI video. Free beginner guides. Tested workflows. Build with us.**

The added word “Open” is deliberate. A separate public GitHub project named `stale2000/bosonfield`, a live `bosonfield.vercel.app` site, Instagram `@bosonfield`, and X `@Bosonfield` already existed when checked on 9 September 2026. BosonField Open is an independent project and is not affiliated with those accounts, MiniMax, or Higgsfield.

## Live project

- Website: <https://bfarmer27-ops.github.io/bosonfield-open/>
- Code and public work: <https://github.com/bfarmer27-ops/bosonfield-open>
- Beginner questions and member results: <https://github.com/bfarmer27-ops/bosonfield-open/discussions>
- 90-day work list: <https://github.com/bfarmer27-ops/bosonfield-open/milestone/1>

## Plans and evidence

- [90-day roadmap](ROADMAP.md)
- [Growth and revenue plan](GROWTH_AND_REVENUE_PLAN.md)
- [First 30 videos](CONTENT_PLAN.md)
- [Social profile copy](SOCIAL_PROFILE_COPY.md)
- [Current monetization rules](research/MONETIZATION_EVIDENCE.md)
- [Open AI-video stack and 90-day build](research/OPEN_VIDEO_STACK.md)
- [Name and conflict check](research/NAME_CHECK.md)

## Local start

Open `index.html` directly in a browser. No build step and no tracking script are required.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). Use the issue forms for a tutorial request, hardware result, or broken workflow. Use GitHub Discussions for public help and finished results.

## License

BosonField Open code and original documentation in this repository are licensed under Apache License 2.0. Model weights, third-party workflows, names, and media keep their own terms.
