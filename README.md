# Testing

## Test IDE

 - [x] import standard library packages
 - [x] run basic analysis
 - [ ] create visualisations using:
     - [x] seaborn
     - [ ] bokeh 
     - [x] matplotlib
     - [ ] folium
 - [x] create script and link to console
 - [x] link multiple scripts to one console
 - [x] git integration
 - [ ] debugger
 - [ ] customise JLab
 
## Test BQ interation
 - [ ] read in data from BQ:
     - [x] open data
     - [ ] IDS data (use another project for this)
     - [x] using a Python file
     - [ ] using a JupyterNotebook
 - [ ] write data into WIP bucket
     - [ ] using a JupyterNotebooks
     - [ ] using a Python file
 - [ ] regression on Big Data using BQ ML
 
## Test Artifactory
 - [ ] set up pip and conda to install from Artifactory
 - [ ] install a package using pip and conda
 - [ ] use curl command to upload artifact (will obviously not work)
 
## Test GitHub
 - [x] create a repository in GitHub
 - [x] clone a repository in JLab
 - [ ] check privilages 
 - [ ] add/remove someone
 - [ ] create/delete repo
 - [ ] make a repo public/private

## Test Cloudflare
 - [x] copy and paste inside browser isolation (BI)
 - [x] copy outside paste inside BI
 - [x] copy inside paste outside BI
 - [x] copy paste outside BI (i.e. doesn't interfere with anything outside Cloudflare)
 
# Notes

*30/11/2022*

- Cloudflare is sometimes lagy (I think). Things that make it worse:
    - after leaving it for a bit them come back
    - going between tabs within JLab (maybe)
    - using the terminal in JLab (very lagy)
I sometimes think I've made a mistake and have to wait for the keyboard to catch up, 
- Need to PAT for GitHub, this is created in BI so can't save it anywhere for future use (maybe a good thing?). The fine-grained PAT didn't seem to work, I used my existing PAT, which I had to copy and paste outside Cloudflare's reach
- Logging into everything takes some time with 2FA for IDS and GitHub
- The JupyterLab git integration is great. No need to reuse PAT after first time.
- Can't view hidden files in JLab. I went into *settings > advanced settings editor > file browser* and switched on *show hidden files*, but they don't appear, and there isn't an extra option in the *view* menu.
- Can't import data from Seaborn, but can use functions from the package.

*01/11/2022*

- Can't seem to access UAT through Cloudflare, getting a *website blocked* error:

![website_blocked](images/website_blocked.png)

- GitHub website not rendering properly through Cloudflare:

![github_render_issue](images/github_render_issue.png)

- Can't delete a folder in JLab, I think it's because there's a hidden file in there and JLab won't let you delete folders with files in them.
- Option to view .gitignore under the *Git* menu doesn't work

*06/12/2022

- Struggling to log into UAT through Hub again. Also GitHub not rendering properly, when I navigate through the IDS org on there it sometimes gives me website blocked.
- Can't install packages from script because it's asking for credentials.
- Credentials don't seem to be stored when using pip for the second time. Also asked me if I wanted to store credentials but got an error when saying yes. Install worked thoughw