# Carta - Frontend take-home interview assignment

## GitHub User Viewer

You are creating a client-side application that consumes the GitHub API and
show the most popular repos of a specific user.

API: [https://developer.github.com/v3/](https://developer.github.com/v3/)

#### Tasks:
The tasks are divided into specific Levels that should be completed separetely.
It's more important to have a complete and tested Level than multiple incomplete ones.
Do as many as you can.

##### Level 1
- The user should be able to search for a GitHub User;
- The user should be able to see the searched GitHub User info - avatar, followers, following, e-mail and bio;
- The user should be able to see the GitHub User repos. Listed in order by number of stars;
##### Level 2
- The user should be able to change the ordering of the listed repos - order by name/date/etc;

##### Level 3
- Once a specific repo is clicked, the route changes, showing a page for the specific repo, with
it's details - repo name, description, number of stars, language and a link to the GitHub repo page;

#### Evaluation Criteria
- Project Organization - does it have an organized structure, documentation and version control;
- Good Practices - does it follow good practices, including security and optimization;
- Quality Control - does it have it's quality assured with unit tests;

#### Considerations
The endpoints that will be used are:
- User details: [https://api.github.com/users/{username}](https://developer.github.com/v3/users/)
- Repos of a specific user: [https://api.github.com/users/{username}/repos](https://developer.github.com/v3/repos/#list-user-repositories)
- Repo details: [https://api.github.com/repos/{full_name}](https://developer.github.com/v3/repos/#get)
### Project instructions
- Fork this repository on your machine
- make your changes in the `./react_project` directory
- We provide you with a basic start script and CSS files in this repo.
To see your changes, just run `yarn start`

Once finished, open up a PR with your code.

If you decide to create a private repository, be prepared to add 
your interviewer as a contributor.