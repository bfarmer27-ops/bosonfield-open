# BosonField Roadmap

Target: **v0.1 — First Open Creator Lab**, due **8 December 2026**.

This roadmap is a public work order. Dates can move when real tests find a hardware, license, or safety block. A task is complete only when its proof is public.

## Weeks 1–2: prove the starter path

- Pin the exact Wan2.1 T2V-1.3B model revision and software versions.
- Run one 480p text-to-video test on the 12 GB NVIDIA TITAN X.
- Record the command, seed, size, frame count, run time, peak video memory, output file, and any error.
- Publish the first hardware report, whether the run works or fails.
- Add a license card that separates BosonField code terms from model and asset terms.

## Weeks 3–4: ship the first beginner pack

- Build a local hardware checker that gives one of three results: fits, may fit with memory-saving settings, or does not fit.
- Publish the first versioned workflow pack.
- Publish the first lesson: **Your First Open AI Video with Wan2.1 (No Paid API)**.
- Add a repair guide for download, install, video-memory, and missing-file errors.
- Let a new user follow the lesson without private help. Record every step that stops them.

## Weeks 5–8: make community work repeatable

- Turn common questions into short fixes and new lessons.
- Accept hardware reports through the public issue form.
- Add tested results to one public table. Do not copy numbers from model cards into the measured-results table.
- Run one live build or question session each week.
- Give public credit to each useful test, fix, translation, or guide.

## Weeks 9–13: test the wider stack

- Compare the Wan2.1 starter tier with Wan2.2 on a community machine that meets the 24 GB requirement.
- Add image-to-video only after a tested text-to-video path is stable.
- Review one more model only after its exact license, location limits, and hardware needs are recorded.
- Publish a v0.1 release with a fixed setup, example output, known limits, and rollback steps.

## Release gates

v0.1 does not ship until all of these are true:

1. One clean install is repeated from the written guide.
2. One real 480p run is measured on the named hardware, or the exact block is published.
3. Every file and model revision has a source and license note.
4. The workflow can resume after an interrupted download or render.
5. No account key, password, cookie, private input, or private output is in Git.
6. A beginner can report a failure with the provided issue form.

## Growth and support

- Use YouTube for full lessons and Shorts for one clear result or fix.
- Use GitHub Discussions for questions and member results.
- Add donations only after a real donation account exists and the public funding file is checked.
- Treat ad and view income as later outcomes. Do not plan spending around money that has not been earned.

The detailed posting, community, and income plan is in [GROWTH_AND_REVENUE_PLAN.md](GROWTH_AND_REVENUE_PLAN.md).
