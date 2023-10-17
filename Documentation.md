# About the github action, We will explain what it is, its part and some results which is required by the HW.
# Overview
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.
GitHub Actions gives developers the ability to automate their workflows across issues, pull requests, and more—plus native CI/CD functionality. Here’s everything you need to know about Actions including its benefits, how it works, popular use cases, and more.

# The components of GitHub Actions
# Workflows
To automate development workflows with GitHub Actions, users create definitions using a workflow file, or YAML file, and store these files in the GitHub repository under the .github/workflows directory. A workflow run is triggered three ways: via an external event, a scheduled event, or a GitHub repository event (such as push or pull requests to a GitHub repo or issue creation). 
# Events
An event is a specific activity in a repository that triggers a workflow run. For example, activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow to run on a schedule, by posting to a REST API, or manually.
# Jobs
A job is a set of steps in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other. When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run. For example, you may have multiple build jobs for different architectures that have no dependencies, and a packaging job that is dependent on those jobs. The build jobs will run in parallel, and when they have all completed successfully, the packaging job will run.
# Actions
An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files. An action can pull your git repository from GitHub, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider.

You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.
# Runners
A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger configurations
# Create an example workflow
GitHub Actions uses YAML syntax to define the workflow. Each workflow is stored as a separate YAML file in your code repository, in a directory named .github/workflows.
You can create an example workflow in your repository that automatically triggers a series of commands whenever code is pushed. In this workflow, GitHub Actions checks out the pushed code, installs the bats testing framework, and runs a basic command to output the bats version: bats -v.
---->In your repository, create the .github/workflows/ directory to store your workflow files.
----> In the .github/workflows/ directory, create a new file called learn-github-actions.yml and add the following code.
```
{name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v}
```
Your new GitHub Actions workflow file is now installed in your repository and will run automatically each time someone pushes a change to the repository.


----> Commit these changes and push them to your GitHub repository.



# Understanding the workflow file
```name: learn-github-actions```

Optional - The name of the workflow as it will appear in the "Actions" tab of the GitHub repository. If this field is omitted, the name of the workflow file will be used instead.

```run-name: ${{ github.actor }} is learning GitHub Actions```

Optional - The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab. This example uses an expression with the github context to display the username of the actor that triggered the workflow run
```on: [push]```
Specifies the trigger for this workflow. This example uses the push event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request. This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags
```jobs:```
Groups together all the jobs that run in the learn-github-actions workflow.
```check-bats-version:```
Defines a job named check-bats-version. The child keys will define properties of the job.
```runs-on: ubuntu-latest```
Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub
```steps:```
Groups together all the steps that run in the check-bats-version job. Each item nested under this section is a separate action or shell script.
```- uses: actions/checkout@v4```
The uses keyword specifies that this step will run v4 of the actions/checkout action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will use the repository's code.
```- uses: actions/setup-node@v3```
        ```with:```
         ``` node-version: '14'```
This step uses the actions/setup-node@v3 action to install the specified version of the Node.js. (This example uses version 14.) This puts both the node and npm commands in your PATH.
```- run: npm install -g bats```
The run keyword tells the job to execute a command on the runner. In this case, you are using npm to install the bats software testing package.
```- run: bats -v```
Finally, you'll run the bats command with a parameter that outputs the software version.
# References.
[1]
[2]
[3]
[4]
[5]
[6]
[7]
[8]
[9]
[10]

