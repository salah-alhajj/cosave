# ✨🚀 cosave:  Command-Line Nirvana Achieved! 🧘‍♀️  (Seriously!) 

[![PyPI version](https://badge.fury.io/py/cosave.svg)](https://badge.fury.io/py/cosave) [![Python Versions](https://img.shields.io/pypi/pyversions/cosave.svg)](https://pypi.org/project/cosave/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub stars](https://img.shields.io/github/stars/salah-alhajj/cosave?style=social)](https://github.com/salah-alhajj/cosave) [![GitHub forks](https://img.shields.io/github/forks/salah-alhajj/cosave?style=social)](https://github.com/salah-alhajj/cosave) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Awesome README](https://awesome.re/badge.svg)](https://awesome.re)  

**Stop. 👏  Wasting. 👏 Time. 👏  Typing. 👏  The. 👏  Same. 👏  Commands!**

`cosave` is not just *another* CLI tool – it's your personal command-line assistant, your terminal sidekick, your productivity pal! 🌟  It's designed to banish command repetition to the history books and inject pure, unadulterated efficiency into your daily workflow.  Imagine: **saving complex commands, using variables like a wizard, and executing them with a single, elegant command.**  Sounds like magic? ✨  It's `cosave`!

---

##  😩  Command-Line Struggles?  We Feel You.  (And We Fixed It!) 💪

Let's be honest, the command line can be a *beautiful* place, but also a source of…frustration.  Do any of these sound familiar?

*   🤯  **Command Amnesia:**  That *perfect* command you crafted last week? Gone. Vanished. Poof.
*   😫  **Repetitive Strain Injury (RSI) from Typing:**  Your fingers are screaming from typing the same verbose commands *again* and *again*.
*   🤬  **Configuration Chaos:**  Need to run the same command in slightly different environments?  Copy-pasting and editing is a recipe for disaster.
*   🙈  **Long, Unreadable Commands:**  Commands that stretch across your screen and look like alien hieroglyphics.

**`cosave` is the antidote to command-line chaos!**  It empowers you to:

*   **💖  Cherish Your Commands:**  Save those command gems and give them names you'll actually remember.
*   **✨  Variable Virtuosity:**  Become a variable master! Use placeholders for dynamic values – no more hardcoding!
*   **⚡️  Instant Execution:**  Run saved commands with the speed of thought. Just invoke the name and provide your variables.
*   **🗂️  Command Organization Bliss:**  Manage your command library like a pro – list, update, delete, backup, restore – you're in control!

---

## 🔥  Core Features That Will Make You Say "Whoa!" 🤩

*   **🚀  Super-Fast Command Saving:**  `cosave --add deploy-prod "deploy.sh --env production --version [version]"` - Saved! Deployed! Done! (Okay, maybe not *that* fast, but you get the idea!)
*   **🧙‍♂️  Dynamic Variables - Unleash the Power:**  Imagine variables for project names, API keys, server IPs, anything! `cosave` makes it effortless.
*   **🗂️  Your Personal Command Codex:**  `cosave --list` - Boom! Your entire command collection, beautifully organized and ready for action.
*   **🧹  Keep it Clean - Command Updates & Deletions Made Easy:**  Refine your commands, remove the outdated ones – maintain command-line zen.
*   **🛡️  Backup & Restore - Command Security Fortress:**  Protect your precious command knowledge with simple backup and restore operations.  Because losing your commands is like losing your keys!
*   **🤫  🤫  🤫  Silent Mode - For When You Need to Be Stealthy:**  Suppress command output for clean scripts or when you just want things done quietly.

---

##  ⬇️  Installation -  Join the Command Revolution in Seconds! ⏱️

Getting `cosave` on your system is easier than making toast! (And way more productive!)

```bash
pip install cosave
```

Yep, that's it!  Make sure you've got Python 3.7+ installed (because, you know, modern Python is awesome 😎).

---

##  ⚡️  Quick Start -  Your First Steps to Command-Line Enlightenment! ✨

Let's say you're a DevOps engineer and you frequently need to deploy services to Kubernetes.  Get ready for `cosave` to blow your mind! 🤯

1.  **Save your Kubernetes deployment command (prepare for a *long* one!):**

    ```bash
    cosave --add kube-deploy "kubectl apply -f <(cat <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: [deployment_name]
      labels:
        app: [app_name]
    spec:
      replicas: [replicas]
      selector:
        matchLabels:
          app: [app_name]
      template:
        metadata:
          labels:
            app: [app_name]
        spec:
          containers:
          - name: [container_name]
            image: [image_registry]/[image_name]:[image_tag]
            ports:
            - containerPort: [container_port]
            env:
            - name: API_KEY
              value: "[api_key]"
    EOF
    )"
    ```

    🤯  **WHOA!** That's a *long* command!  Imagine typing that out every time!  `cosave` to the rescue!

2.  **List your saved commands (admire your efficiency already!):**

    ```bash
    cosave --list
    ```

    You'll see `kube-deploy` listed with a bunch of variables: `(Variables: deployment_name, app_name, replicas, container_name, image_registry, image_name, image_tag, container_port, api_key)`.  Yes, `cosave` handles even *complex* commands like this!

3.  **Execute the Kubernetes deployment with ease!** Let's deploy a service called `my-awesome-app`:

    ```bash
    cosave kube-deploy \
    --deployment_name my-awesome-app-deploy \
    --app_name awesome-app \
    --replicas 3 \
    --container_name awesome-app-container \
    --image_registry docker.my-repo.com \
    --image_name awesome-app-image \
    --image_tag v1.2.3 \
    --container_port 8080 \
    --api_key super-secret-api-key
    ```

    ✨  **BOOM!**  Just *one* `cosave` command, and that monstrous Kubernetes deployment command is executed perfectly, with all your variables filled in!  You just saved yourself minutes of tedious typing and potential errors.  🎉  **THAT'S the power of `cosave`!**

---

##  📖  Dive Deeper -  Become a Cosave Master! 🎓

###  🧩  Cosave's Inner Magic - Modules Revealed!

`cosave` is built with a super-clean, modular design:

*   **`cosave.py` (The Captain's Chair 💺):**  The main command center!  Handles all the command-line parsing, argument handling, and directs the flow.
*   **`/cosave/commands/` (Command Central Command 🏢):**  The heart of command management:
    *   `add.py`:  Recruiting new commands to your cause.
    *   `delete.py`:  Retiring commands that have served their purpose.
    *   `list.py`:  Presenting your command arsenal in all its glory.
    *   `update.py`:  Refining, tweaking, and perfecting your commands.
    *   `backup.py`:  Securing your command knowledge for future generations.
    *   `restore.py`:  Bringing back commands from the brink (or from your backup file!).
*   **`/cosave/utils/` (Utility Belt of Wonders 🛠️):**  Essential tools that make `cosave` tick:
    *   `loader.py`:  Reading commands from the YAML command vault (like Indiana Jones, but for YAML).
    *   `saver.py`:  Writing commands to the YAML vault (atomically – data integrity is key!).
    *   `executor.py`:  The command execution powerhouse – variable replacement ninja and output wrangler.
    *   `variables.py`:  Parsing and managing those dynamic variable arguments like a boss.

###  🕹️  Usage Examples -  Unlock Cosave's Full Potential! 🔓

*   **Adding a Command (Level 1 - Beginner):**

    ```bash
    cosave --add <command_name> "<your_command_string_with_[variables]>"
    ```

    *Example:* `cosave --add create-file 'touch [filename].txt'`

*   **Updating a Command (Level 2 - Apprentice):**

    ```bash
    cosave --update <command_name> "<your_even_better_command_string>"
    ```

    *Example:* `cosave --update create-file 'touch [filepath]/[filename].txt'` (Now with filepath!)

*   **Listing Commands (Level 1 - Beginner):**

    ```bash
    cosave --list
    ```

*   **Deleting a Command (Level 2 - Apprentice):**

    ```bash
    cosave --delete <command_name>
    ```

    *Example:* `cosave --delete create-file`

*   **Executing a Command with Variables (Level 3 - Master!):**

    ```bash
    cosave <command_name> [--variable1 value1] [--variable2 value2] [--output <y/n>]
    ```

    *Example:* `cosave create-file --filename my-document`
    *Example (Silent Mode - Ninja Level!):* `cosave create-file --filename secret-file --output n` (No output, just pure file creation magic!)

*   **Backing Up Your Command Wisdom (Level 2 - Apprentice):**

    ```bash
    cosave --backup-path my_commands_backup.yaml
    ```

*   **Restoring Commands (Override - Level 3 - Use with Power & Responsibility!):**

    ```bash
    cosave --restore-path my_commands_backup.yaml --override
    ```

*   **Restoring Commands (Merge - Level 2 - Safe & Sound):**

    ```bash
    cosave --restore-path my_commands_backup.yaml
    ```

---

##  🧑‍🤝‍🧑 Contributing -  Become a Cosave Co-Creator! 🎨

Got a spark of genius?  Found a bug hiding in the code?  Want to add a feature that will make `cosave` even *more* amazing?  **We welcome contributions with open arms!** 🤗  Fork the repo, unleash your coding skills, and send us those pull requests!  Let's build the ultimate command-line companion, together! 🤝

**Bonus Points for Visual Demos!**  Want to *really* make a contribution that shines?  Create a short GIF or video demonstrating `cosave` in action!  Visuals speak volumes and help others see the magic of `cosave` instantly. ✨

---

##  📜 License -  Free for the World, Thanks to MIT! 🌍

`cosave` is proudly released under the [MIT License](https://opensource.org/licenses/MIT).  Go forth, command boldly, and build amazing things! 🚀

---

Made with ❤️ by Salah AlHajj and the incredible open-source community.  If `cosave` has brought joy and efficiency to your terminal life, **give us a shiny star on [GitHub](https://github.com/salah-alhajj/cosave)!** ⭐  Happy commanding, and may your terminal sessions be ever productive! ✨  🙏
