# Git & GitHub

## Creating a Repository from a Template

GitHub allows you to create new repositories from templates, which can include pre-configured files, workflows, and settings. This is useful for starting projects with best practices already in place.

### Using the Secure Repository Template

The course repository includes a template URL for creating repositories with security best practices. Here's how to use it:

**Step 1: Get the template URL**

The template URL is located in `github-new-repo-from-template.txt` in this directory (`practice/03-git/`). The URL format is:

```
https://github.com/new?owner=YOUR_USERNAME&template_name=secure-repository-supply-chain&template_owner=skills&name=YOUR_REPO_NAME&visibility=public
```

**Step 2: Customize the URL**

Replace the placeholders:
- `YOUR_USERNAME` - Your GitHub username or organization name
- `YOUR_REPO_NAME` - The name you want for your new repository
- `visibility=public` - Change to `visibility=private` if you want a private repository

**Step 3: Create the repository**

1. Copy the complete URL with your customizations
2. Paste it into your browser's address bar
3. Press Enter
4. GitHub will open the repository creation page with the template pre-selected
5. Review the settings and click "Create repository"

**Example:**

If your username is `johndoe` and you want to create a repo called `my-secure-project`:

```
https://github.com/new?owner=johndoe&template_name=secure-repository-supply-chain&template_owner=skills&name=my-secure-project&visibility=public
```

**What you get:**

The "secure-repository-supply-chain" template from GitHub Skills includes:
- Security best practices configuration
- Supply chain security settings
- Dependabot setup for dependency updates
- Security policies
- Code scanning workflows
- GitHub Actions for security checks

**Alternative: Using GitHub's Web Interface**

You can also create a repository from a template using GitHub's web interface:

1. Go to the template repository: https://github.com/skills/secure-repository-supply-chain
2. Click the green **"Use this template"** button
3. Select **"Create a new repository"**
4. Choose your owner, repository name, and visibility
5. Click **"Create repository"**

## GitHub Codespaces

### Useful commands

### List your active codespaces
```
gh codespace list
```