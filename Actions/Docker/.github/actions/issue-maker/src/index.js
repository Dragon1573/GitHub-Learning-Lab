const core = require("@actions/core");
const github = require("@actions/github");

async function run() {
  const issueTitle = core.getInput("issueTitle");
  console.info(`Inputs (issueTitle): ${issueTitle}`);
  const catFact = core.getInput("catFact");
  console.info(`Inputs (catFact): ${catFact}`);

  const token = core.getInput("repoToken");
  try {
    const octokit = new github.GitHub(token);

    const newIssue = await octokit.issues.create({
      repo: github.context.repo.repo,
      owner: github.context.repo.owner,
      title: issueTitle,
      body: catFact
    });
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
