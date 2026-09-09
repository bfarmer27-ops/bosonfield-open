# Security policy

## Report privately

Do not open a public issue for:

- exposed passwords, tokens, cookies, or private links;
- code that can run commands without clear user approval;
- a path that uploads local media without clear notice;
- unsafe file extraction or path handling;
- a way to reach a local service from another machine without authentication;
- personal data exposed in logs, examples, or benchmark files.

Until a private reporting inbox is live, do not send exploit details or secrets. Open a public issue titled `Private security contact needed` with no exploit details. A maintainer will publish a safe private route before asking for the report.

## Scope

Only BosonField Open code is in scope. Model behavior, third-party tools, hosting services, and social platforms must be reported to their owners.

## Release rule

A security fix must reproduce the bug, repair the same path, pass the existing checks, and verify the full user task that exposed it.
