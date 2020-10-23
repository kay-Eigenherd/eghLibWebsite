# General information
This repo is for testing purposes! The package in here has been created for testing purposes.  

It should be noted, that the user, which authenticates will also be "responsible" for all actions of the CI and will also receive email notifications on installation of the package. This is because the Auth URL is linked to the account, which has been authenticated through the web sign-in. 

### ToDo  
- [ ] Also a quick note, that the version does not get updated in the sfdx-project.json. I am working to create a better overview.  
- [X] Repo-variable for an installation key. This way it is safer.

# Setup
## Setting the CI up
I have created a Trailhead Playground for testing with CI.  
Login link: https://playful-moose-suoor6-dev-ed.my.salesforce.com/  
Username: kay.jenss@playful-moose-suoor6.com  
Pw: Hallo2020!  
  
1. Authenticate uthe Org you are planning to use as a DevHub on your local device through Salesforce CLI and the web based authorization

2. Use `sfdx force:org:display --targetusername <username> --verbose` command to retrieve the URL for authentification.

3. Add the retrieved Link to the variables under **Settings > CI/CD > Variables** right now the variable for the Org is named $PLAYGROUND_AUTH_URL

## Creating a package
The CI can currently only create new package versions and promote them(job needs to be started manually).  
It can, however **not create a package** itself. So it requires, that the initial package creation command is performed manually on a local machine.
  
# Considerations
It should be noted, that Playgrounds only allow for the creation of 10 ScratsOrgs per day. The limit for the **EghProd is at 80/day**  
When using two Scratch Orgs(testing, package installation testing) per pipeline this is not much.
This could be reduced by running the tests straight within the specified Org, but again this code could lead to problems down the road.


