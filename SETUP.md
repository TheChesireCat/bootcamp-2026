# Pre-session setup: do this BEFORE the bootcamp

Two 5-minute tasks so we don't lose session time to logins.

---

## 1. Request Explorer access
Fill out the RC access form (ServiceNow, log in with your NU account):

- Choose **"I do not have access… requesting a new account."**
- University Sponsor: **Daria Alekseeva**
- Sponsor Storage Space: **`/projects/netsi`**
- Accept the agreement ▸ Submit.

Form + docs links are in `references/Bootcamp Fall 2026 Agenda.docx.pdf`.
Docs: <https://rc-docs.northeastern.edu>

---

## 2. Set up SSH so `ssh explorer` just works

The **login host** is `login.explorer.northeastern.edu`. Your username is your NU
username (usually `lastname.f`).

### a) Create an SSH key (if you don't have one)
```bash
ssh-keygen -t rsa        # press Enter through every prompt, no passphrase
```

### b) Add a host alias: edit `~/.ssh/config` and add:
```
Host explorer
    HostName login.explorer.northeastern.edu
    User YOUR_USERNAME          # e.g. ramakrishnan.ank
    IdentityFile ~/.ssh/id_rsa
```

### c) Enable passwordless login (required for OOD / GUI apps)
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub YOUR_USERNAME@login.explorer.northeastern.edu
# enter your NU password once when prompted
```

### d) Test it
```bash
ssh explorer            # should log you straight in, no password
```

> On Windows, use MobaXterm or Windows OpenSSH; the `~/.ssh/config` block is the same.
> rc-docs has per-OS guides: <https://rc-docs.northeastern.edu/en/latest/connectingtocluster/>

---

## 3. VS Code (recommended editor)
1. Install VS Code: <https://code.visualstudio.com>
2. Install the **Remote - SSH** extension (Microsoft).
3. `Cmd/Ctrl+Shift+P` ▸ **Remote-SSH: Connect to Host** ▸ pick **`explorer`**.
   (It appears automatically because of your `~/.ssh/config` alias.)

---

## 4. Claude (for the afternoon Agentic session)
1. Go to <https://claude.northeastern.edu> ▸ **First time? Start here** ▸ accept guidelines.
2. Log in with **SSO** (NU email + credentials).
3. We'll use **Claude Code** (terminal) and **Claude Desktop**.

---

### Quick self-check
- [ ] `ssh explorer` logs me in without a password
- [ ] VS Code connects to host `explorer`
- [ ] I can open <https://ood.explorer.northeastern.edu>
- [ ] I can log into <https://claude.northeastern.edu>
