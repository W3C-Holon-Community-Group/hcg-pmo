# Access and admins: the backstop page

For admins who don't normally operate the tooling. This is everything you need in an emergency.

## Who to call

| Order | Person | GitHub access | Call them for |
|---|---|---|---|
| 1 | Christine Connors | Admin | Anything: PMO lead, owns automations |
| 2 | Kurt Cagle | Admin | Anything, if Christine is unavailable; org secrets |
| 3 | Patrick Audley | Maintainer | Broken workflows, PR reviews |
| — | Heather Ray | Admin (backstop) | Emergency access only |

Contact details are in the HCG contact list, not in this public repo.

## Grant access

1. Go to the org's **People** page: `https://github.com/orgs/W3C-Holon-Community-Group/people`.
2. Choose **Invite member**, enter their GitHub username, and choose the role **Member**.
3. To give access to one repo only, open that repo's **Settings → Collaborators and teams** and add them with **Write** (contributors) or **Maintain** (team leads).
4. Post a line on the PMO board so the change is on the record.

## Revoke access

1. Org **People** page → find the person → **⋯ → Remove from organization**, or lower their role.
2. If they owned an automation, check [`../REGISTRY.md`](../REGISTRY.md) and make the backup owner the owner.
3. If they could see org secrets, ask Kurt or Christine to rotate those secrets.

## If an automation is misbehaving

Open the repo's **Actions** tab, choose the workflow, then **⋯ → Disable workflow**. That stops it safely. Then tell Christine or Kurt.

## Never

- Never share a personal access token, or put one in a secret.
- Never remove the last other admin. There must always be at least two.
