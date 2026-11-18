1. In the Databricks workspace sidebar, open **Workspace** and choose **Create → Git folder** (some workspaces label this **Repos** or **Add Git folder**).
2. Paste the HTTPS URL of your GitHub repository, for example `https://github.com/your-name/your-repo.git`.
3. Select the branch, then create/clone the Git folder. Databricks pulls the repository files into your workspace.

## 3. Run the script

1. Open `databricks_first_run.py` inside the Git folder.
2. Attach/select available compute (for a first test, the workspace's allowed serverless compute is fine).
3. Click **Run all**. If your workspace presents a Python file as a job instead of an interactive editor, create a **Job**, add a **Python script** task, and select this file from the Git folder.
4. You should see “Hello from Databricks!”, a three-row table, and `Number of people: 3` in the output.

## 4. Push a change back to GitHub

Edit the script in the Git folder, then use the Git panel to review the diff, enter a commit message, commit, and push. If GitHub rejects the push, check that your GitHub credential has write access to that repository and that your organization has approved the credential if it requires SSO.

The Git folder is a working copy. Pull brings remote changes into Databricks; commit and push send your Databricks changes back to GitHub.1. In the Databricks workspace sidebar, open **Workspace** and choose **Create → Git folder** (some workspaces label this **Repos** or **Add Git folder**).
2. Paste the HTTPS URL of your GitHub repository, for example `https://github.com/your-name/your-repo.git`.
3. Select the branch, then create/clone the Git folder. Databricks pulls the repository files into your workspace.

## 3. Run the script

1. Open `databricks_first_run.py` inside the Git folder.
2. Attach/select available compute (for a first test, the workspace's allowed serverless compute is fine).
3. Click **Run all**. If your workspace presents a Python file as a job instead of an interactive editor, create a **Job**, add a **Python script** task, and select this file from the Git folder.
4. You should see “Hello from Databricks!”, a three-row table, and `Number of people: 3` in the output.

## 4. Push a change back to GitHub

Edit the script in the Git folder, then use the Git panel to review the diff, enter a commit message, commit, and push. If GitHub rejects the push, check that your GitHub credential has write access to that repository and that your organization has approved the credential if it requires SSO.

The Git folder is a working copy. Pull brings remote changes into Databricks; commit and push send your Databricks changes back to GitHub.
