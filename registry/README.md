# Registry Notes

This directory contains metadata used when submitting the skill to external
skill registries such as aghub / skillhub.

## Files

- `skillhub-submission.json` - minimal searchable record for the skill

## Packaging rule

The installable package must be built from `skills/michael-polanyi/`, not from
the repository root.

The resulting zip must expose `SKILL.md` at the archive root, for example:

```text
michael-polanyi/
  SKILL.md
  examples.md
  polanyi-notes.md
  references/
  scripts/
```

## Build the package

```bash
python3 scripts/build_skill_package.py --clean
```

This is the default development build. It emits a version like
`0.5.3+<commit>` and leaves `package_url` / `update_url` empty so the metadata
can be filled after upload.

For a formal GitHub release asset, use:

```bash
python3 scripts/build_skill_package.py --clean --release
```

That mode uses the plain top `CHANGELOG.md` version, for example `0.5.3`, and
precomputes the expected GitHub release asset URLs under `releases/download/`.

This writes:

- `dist/michael-polanyi-<version>.zip`
- `dist/michael-polanyi-update.json`

It also refreshes `registry/skillhub-submission.json` with the current version,
zip filename, and SHA256.

## Before submission

Replace the placeholder local filenames in the generated metadata with the
actual remote URLs used by the target registry or download service.
