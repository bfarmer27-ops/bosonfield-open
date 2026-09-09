# Open AI-video stack and product plan — 2026-09-09

Research check: **2026-09-09T16:49:52Z**.

## Product choice

BosonField should not promise Higgsfield parity. The first product is an independent, local-first Open Creator Lab: turn a beginner's brief into a repeatable shot plan, run legally tracked local models, preserve the random seed and source record, and export an editable package with video, captions, workflow, prompt, model version, and license list. It will win on teaching, clear hardware checks, plain repair steps, and community-tested workflows—not by copying Higgsfield branding, screen design, code, prompts, or private service behavior.

The first real-machine backend is **Wan2.1 T2V-1.3B at 480p**. The official project states Apache-2.0 terms and 8.19 GB VRAM. The live BosonField machine has an NVIDIA TITAN X with 12,288 MiB VRAM. Wan2.2 TI2V-5B remains the later 24 GB quality tier. HunyuanVideo-1.5, CogVideoX, LTX-2.5, H3, and ComfyUI stay behind exact license checks.

## Model and tool screen

### Wan2.1 T2V-1.3B

- Use: First backend to test on the live 12 GB BosonField machine; 480p text-to-video starter path.
- License: Apache-2.0 for the official Wan2.1 model release and repository.
- Business limit: Keep the Apache notice, audit every bundled add-on and input asset, and apply the official use limits. The license does not grant rights to a creator's third-party source media.
- Hardware: The official project states 8.19 GB VRAM and recommends 480p for the 1.3B model. The stated fit is not proof of a working Pascal-GPU render; the pinned install and real output must be tested.
- Official source: https://github.com/Wan-Video/Wan2.1 ; https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B

### Wan2.2 (TI2V-5B; also A14B T2V/I2V)

- Use: Later 24 GB quality tier for text-to-video and image-to-video, plus a heavier multi-GPU option.
- License: Apache-2.0 for the Wan2.2 code and the Wan-AI/Wan2.2-TI2V-5B model card.
- Business limit: Permissive Apache terms still require notices and preservation of license text. Audit every bundled dependency, text encoder/VAE, LoRA, and community workflow separately; do not treat a model card license as a blanket license for third-party assets or training-data rights.
- Hardware: Official model card says TI2V-5B supports 720p/24fps and can run on a single RTX 4090; its example says at least 24GB VRAM with CPU/model offload, while 80GB can disable those options. A14B is a materially heavier multi-GPU path.
- Official source: https://github.com/Wan-Video/Wan2.2 ; https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt ; https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B ; https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md

### HunyuanVideo-1.5

- Use: Strong optional quality/speed backend and a useful benchmark target for 480p/720p T2V/I2V; not the legal default for a globally distributed product.
- License: Custom Tencent Hunyuan Community License Agreement; not an OSI-approved permissive license.
- Business limit: License excludes the European Union, United Kingdom, and South Korea; it imposes territory, use-policy, downstream-notice, attribution/disclosure, and model-improvement restrictions. A service over 100 million monthly active users at release needs a separate Tencent license. Keep territory gating and legal review explicit.
- Hardware: Official README states NVIDIA CUDA, Linux, and 14GB minimum GPU memory with model offloading; the 480p step-distilled I2V path reports a single RTX 4090 generating in about 75 seconds. These are model/version/configuration-specific measurements.
- Official source: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 ; https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE ; https://huggingface.co/tencent/HunyuanVideo-1.5 ; https://huggingface.co/tencent/HunyuanVideo-1.5/blob/main/README.md

### LTX-2.5

- Use: Advanced synchronized audio-video option and future adapter target, especially for talking/music/video-with-audio workflows; defer from the legal-critical MVP path.
- License: LTX-2.x Community License Agreement dated 2026-08-11, a custom source-available license rather than Apache/MIT.
- Business limit: Entities with annual revenue of at least $10,000,000 need a paid Commercial Use Agreement for commercial use of LTX-2.x and derivatives. The license also defines broad model derivatives and has additional restrictions; verify the exact checkpoint license before shipping. Do not call it unrestricted open source.
- Hardware: Current repository publishes a 22B BF16 transformer plus a Gemma 4 12B text encoder, with FP8 casting and CPU/disk offload flags, but does not state one fixed minimum VRAM. Expect high-VRAM or offloaded/multi-GPU operation and benchmark the exact pipeline.
- Official source: https://github.com/Lightricks/LTX-2 ; https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x ; https://huggingface.co/Lightricks/LTX-2.5 ; https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/installation.md

### CogVideoX1.5 / CogVideoX

- Use: Low-VRAM fallback and educational backend; useful for a compatibility test and beginner hardware tier, but not the default commercial backend without registration.
- License: Custom CogVideoX model license; repository code includes Apache-2.0 material, but the model weights are governed by the CogVideoX license.
- Business limit: Academic use is allowed; commercial users must register for a basic commercial license. That license is free but capped at 1 million service visits per month; higher traffic needs additional licensing. Include the required copyright/license statement and prohibited-use terms.
- Hardware: Official table reports CogVideoX1.5-5B diffusers inference from 10GB BF16 or 7GB INT8, and CogVideoX-2B from 5GB BF16 or 4.4GB INT8, subject to resolution, frames, and settings. README also documents older-GPU use cases.
- Official source: https://github.com/THUDM/CogVideo ; https://huggingface.co/THUDM/CogVideoX-5b/blob/main/LICENSE ; https://huggingface.co/THUDM/CogVideoX-2b/blob/main/LICENSE ; https://open.bigmodel.cn/mla/form

### Mochi 1

- Use: Permissive research/creator backend and ComfyUI-compatible alternative; good for experimentation but older and heavier than the MVP default.
- License: Apache-2.0 for the Genmo repository/model release.
- Business limit: Apache obligations apply to the released work, but dependencies, fine-tunes, input footage, and downstream assets can carry their own terms. Apache does not grant rights to copyrighted training/input material or guarantee output ownership in every jurisdiction.
- Hardware: Official README describes a 10B model with CPU offload and a 480x848 example; it says LoRA fine-tuning needs one A100/H100 80GB, but does not publish a single minimum inference VRAM number. Treat consumer-GPU claims as configuration-dependent.
- Official source: https://github.com/genmoai/mochi ; https://github.com/genmoai/mochi/blob/main/LICENSE ; https://huggingface.co/genmo/mochi-1-preview

### MiniMax H3

- Use: Important current ecosystem reference for native audio-video generation, but a poor BosonField MVP dependency because of territory, commercial, and architecture constraints.
- License: MiniMax H3 Community License Agreement dated 2026-08-02; custom and not OSI-approved.
- Business limit: The license excludes the EU, UK, Republic of Korea, and United States; products above US$20M yearly revenue need prior written authorization; commercial UI must prominently display MiniMax H3; outputs cannot be used to improve another AI model; hosted products need safeguards and enforceable downstream restrictions. The context-IR and 2K regeneration modules are not open-sourced.
- Hardware: Official card specifies BF16 checkpoints with a 33B dense Omni-Transformer and Qwen3-VL-32B encoder, but gives no fixed minimum VRAM. This implies a high-memory/multi-GPU deployment in practice; measure before considering it for users.
- Official source: https://github.com/MiniMax-AI/MiniMax-H3 ; https://huggingface.co/MiniMaxAI/MiniMax-H3 ; https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE ; https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/README.md

### ComfyUI

- Use: Leading node-graph UI/workflow runtime; use as an optional local integration and workflow interchange layer, not as copied product UX.
- License: GPL-3.0 for ComfyUI core; custom nodes have independent licenses.
- Business limit: If BosonField distributes or modifies ComfyUI core, comply with GPL source/notice obligations and review how custom nodes are bundled. Do not assume every workflow, node, checkpoint, or embedded asset is commercially redistributable. A process-boundary integration reduces coupling but is not a substitute for counsel.
- Hardware: Core supports NVIDIA, AMD, Intel, Apple Silicon, Ascend, and CPU paths, but actual video VRAM is determined by the selected model; it documents offloading, quantization, queueing, and local API features.
- Official source: https://github.com/comfyanonymous/ComfyUI ; https://github.com/comfyanonymous/ComfyUI/blob/master/LICENSE ; https://comfy.org/workflows/tag/video-generation/

### Hugging Face Diffusers

- Use: Apache-licensed Python orchestration/library layer for direct model adapters, reproducible pipelines, and a cleaner first-party API than embedding a full node editor.
- License: Apache-2.0 for the Diffusers library.
- Business limit: Diffusers licensing does not relicense downloaded checkpoints, encoders, VAEs, LoRAs, or custom code. Enforce per-artifact license metadata and pin revisions; a pipeline library alone does not make a model commercial-use safe.
- Hardware: No library-wide minimum; memory, precision, offload, and speed are model- and pipeline-specific. Use Diffusers first for a Wan2.1 T2V-1.3B adapter on the live 12 GB test machine, then add a measured Wan2.2 24 GB preset.
- Official source: https://github.com/huggingface/diffusers ; https://github.com/huggingface/diffusers/blob/main/LICENSE ; https://huggingface.co/docs/diffusers/main/en/api/pipelines/overview

### OpenAI Whisper

- Use: Optional local speech-to-text/subtitle layer for H3 ambiguity, captions, searchable transcripts, and edit markers.
- License: MIT for the released code and model package.
- Business limit: MIT permits commercial use with notice, but does not clear rights in uploaded speech, speaker consent, source recordings, or downstream transcript use. Add local-only defaults, deletion controls, and user responsibility for consent/privacy.
- Hardware: Official README reports approximately 1GB VRAM for tiny/base, 2GB small, 5GB medium, 10GB large, and 6GB turbo; CPU use is possible but slower. Keep tiny/base/turbo presets for beginner machines.
- Official source: https://github.com/openai/whisper ; https://github.com/openai/whisper/blob/main/LICENSE ; https://github.com/openai/whisper/blob/main/model-card.md

### Open-Sora 2.0

- Use: Research/training reference and future contributor path, not a 90-day creator MVP backend.
- License: Apache-2.0 for the Open-Sora repository; audit each released checkpoint and external component separately.
- Business limit: Large open training repositories still require checkpoint, dataset, dependency, and generated-asset provenance review. Do not imply that a fully open code repository clears all training-data or output rights.
- Hardware: Official benchmarks use H100/H800; README shows roughly 52.5GB peak on one GPU for a 256px configuration and eight GPUs for 768px examples. This is research-scale compared with the 12 GB Wan2.1 starter path and the 24 GB Wan2.2 quality tier.
- Official source: https://github.com/hpcaitech/Open-Sora ; https://github.com/hpcaitech/Open-Sora/blob/main/LICENSE ; https://github.com/hpcaitech/Open-Sora#computational-efficiency

## Version 0.1 parts

1. Own-brand local web/desktop shell (React or Svelte frontend, FastAPI backend) with Projects, Shots, References, Prompt, Seed, Aspect Ratio, Duration, Model, and Export views; no Higgsfield assets, copy, CSS, names, or reverse-engineered endpoints.
2. ModelAdapter interface with a first-party Wan2.1 T2V-1.3B adapter and a later Wan2.2 TI2V-5B adapter; each adapter declares model revision, checkpoint URLs, license, territory constraints, VRAM presets, and supported tasks.
3. Local job runner using SQLite plus a filesystem/object directory, resumable jobs, progress, cancellation, CPU offload, OOM-friendly presets, and deterministic seeds; no paid service required.
4. Creator workflow: brief -> shot cards -> text/image-to-video generation -> review -> regenerate selected shot -> concatenate/export. Store prompt, negative prompt if applicable, seed, dimensions, fps, frame count, software versions, and hashes in a manifest.
5. Optional local Whisper adapter for transcript, SRT/VTT captions, searchable markers, and rough cut notes; keep speech files local by default and make deletion explicit.
6. FFmpeg-based media packaging with explicit codec/license documentation, thumbnail/contact-sheet generation, and export of MP4 plus editable project JSON and provenance/license manifest.
7. Beginner guardrails: hardware check, model-download size estimate, one-click known-good presets, explainable OOM/dependency errors, prompt templates for camera/action/timing, and a continuity checklist for character/reference drift.
8. Optional ComfyUI bridge only after core flow works: call a separately installed local ComfyUI API or import/export workflow JSON; do not ship an unreviewed custom-node bundle in v0.1.
9. Legal/ops layer: SPDX-like inventory for code and model artifacts, pinned revisions and checksums, model-license acceptance screen, territory block for restricted models, abuse/reporting path, and clear 'outputs require user rights/consent' terms.

## 90-day build

### Days 0-14 — scope, legal inventory, and reproducible skeleton

- Write a one-page product boundary: local-first shot planning and generation, not a Higgsfield clone or parity claim.
- Create the adapter and source-record schemas; pin Wan2.1 T2V-1.3B, Diffusers, PyTorch/CUDA, Whisper, and FFmpeg revisions. Record Wan2.2 as the next 24 GB tier.
- Build a CLI that records prompt, seed, dimensions, model revision, hashes, and output path, even before the web UI.
- Create a machine-readable model/asset license registry with Apache/MIT/custom-license categories and a human review checklist.
- Proof gate: A clean-machine smoke test produces one tiny deterministic artifact and a manifest; a reviewer can trace every shipped code/model artifact to an official URL and license file.

### Days 15-30 — first useful generation path

- Implement the Wan2.1 T2V-1.3B text-to-video adapter first, with a 480p preset, seed control, memory logging, and resumable jobs. Run the real 12 GB machine test before promising support.
- Add a minimal local FastAPI job API and SQLite queue with status/progress/error records.
- Add a small own-brand shot-card UI and reference-image upload with local filesystem storage.
- Proof gate: On the live 12 GB NVIDIA machine, the documented command either completes one 480p Wan2.1 T2V render or records the exact blocked instruction and memory error. The UI reruns the same seed and writes a matching settings manifest. Record actual run time, peak VRAM, and failure modes.

### Days 31-45 — creator workflow and beginner ergonomics

- Add brief-to-shot-card form, prompt templates for subject/action/camera/lighting/timing, aspect-ratio presets, contact sheets, and regenerate-selected-shot.
- Add hardware detector and model-download estimator with explicit 'estimated, verify on your machine' language.
- Add actionable OOM, CUDA, missing-model, and codec troubleshooting; ship a reproducible Windows/Linux setup guide.
- Proof gate: Five first-time testers can go from install to a two-shot export using only the free tutorial; collect time-to-first-success, error logs, and the top three confusing screens.

### Days 46-60 — edit, speech, and packaging

- Integrate local Whisper tiny/base/turbo presets for SRT/VTT captions and transcript markers.
- Implement FFmpeg concat, trim, audio mux, thumbnail/contact-sheet, and MP4 plus editable project JSON export.
- Add per-shot provenance and license manifest export, including input-file hashes and user acknowledgement of rights/consent.
- Proof gate: An end-to-end project imports two generated shots and an audio file, exports a playable MP4 and SRT, and reproduces the project from JSON on a second machine.

### Days 61-75 — benchmark and model-choice evidence

- Run a fixed 20-30 prompt suite covering motion, camera movement, subject consistency, text in scene, portrait/landscape, and I2V adherence.
- Measure Wan2.1 on the live 12 GB machine and other available 8/12 GB systems. Measure Wan2.2 only on supported 24 GB or larger systems. Record real memory errors and run time; do not extend README claims to untested hardware.
- Prototype read-only adapters for HunyuanVideo-1.5 and CogVideoX behind license/territory gates; compare only on the same prompts and settings.
- Decide whether ComfyUI import/export is worth v0.2 based on user demand and GPL/custom-node review, not on feature checklist pressure.
- Proof gate: Publish a versioned benchmark report with prompts, seeds, hardware, model revisions, render times, VRAM, failures, and human-rating rubric; label all unknowns and avoid 'best/SOTA/parity' language.

### Days 76-90 — release hardening and community loop

- Ship v0.1 source, installer/container recipes, example project, tutorials, troubleshooting, SECURITY.md, NOTICE/SBOM, and model-license registry.
- Sandbox optional third-party runners/custom nodes, validate uploaded media paths, cap resource use, and add cancel/delete controls.
- Add workflow import/export versioning and a community recipe format that includes model/license provenance and expected VRAM.
- Open a small beta with explicit supported hardware and restricted-model exclusions; triage feedback into a v0.2 backlog.
- Proof gate: A fresh install passes automated unit/integration tests, license/provenance checks, media export tests, and a documented two-machine reproduction; public docs list every known limitation and no unbenchmarked parity claim.

## Main risks

- Model code, weights, VAE, text encoder, LoRA, custom node, and dataset licenses often differ; maintain an artifact-level manifest and legal review, not a single project-level label.
- HunyuanVideo-1.5, MiniMax H3, CogVideoX, and LTX-2.5 use custom licenses with territory, revenue, attribution, or use restrictions; a globally reachable hosted service can violate them even when local files run.
- ComfyUI GPL-3.0 and third-party node licensing create redistribution and supply-chain obligations; treat downloaded custom nodes as untrusted code and avoid bundling them in v0.1.
- Generated output ownership and commercial clearance depend on local law, input rights, consent, music/voice rights, and model terms; never promise unrestricted output ownership.
- Consumer GPU reality is the main beginner failure point: model downloads, CUDA/PyTorch mismatch, VRAM spikes, offload latency, and long render times need tested presets, not optimistic minimums.
- Temporal consistency, character identity, camera control, and prompt adherence vary sharply by model and seed; a shot-planning/provenance wedge is more defensible than promising a one-click film generator.
- H3 is not a drop-in open speech-to-text component: its context-IR and 2K modules are hosted/not open in the official release, and its 33B-plus-Qwen3-VL stack is not an MVP hardware target.
- Avoid trademark/trade-dress confusion: use original BosonField naming, UI, documentation, and workflow language; mention other products only nominatively for comparison, and do not copy code, assets, prompts, or endpoints.
- Open-source model releases change quickly; pin revisions, archive license snapshots, and rerun a compatibility/license audit before every release.

## H3 answer

The current official MiniMax-AI/MiniMax-H3 repository and Hugging Face model card define H3 as a 33B multi-input model that accepts text, image, video, and audio and generates synchronized video plus stereo audio. It is not a speech-to-text model. Its current license excludes both the EU and the US, so BosonField does not run it from Spain or the Dallas machine. The initial stack is Wan2.1 T2V-1.3B for the live 12 GB machine test, OpenAI Whisper for local speech-to-text and captions, FFmpeg for media, and direct Diffusers or official Wan adapters.
