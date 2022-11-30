# Testing

## Test IDE

 - [x] import standard library packages
 - [x] run basic analysis
 - [ ] create visualisations using seaborn, bokeh, matplotlib, folium
 - [ ] create script and link to console
 - [ ] link multiple scripts to one console
 - [x] git integration
 - [ ] debugger
 - [ ] customise JLab
 
## Test BQ interation
 - [ ] read in data from BQ
 - [ ] write data into WIP bucket
 - [ ] regression on Big Data using BQ ML
 
## Test Artifactory
 - [ ] set up pip and conda to install from Artifactory
 - [ ] install a package using pip and conda
 - [ ] use curl command to upload artifact
 
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
- Cloudflare is sometimes lagy (I think). Things that make it worse:
    - after leaving it for a bit them come back
    - going between tabs within JLab (maybe)
    - using the terminal in JLab (very lagy)
I sometimes think I've made a mistake and have to wait for the keyboard to catch up, 
- Need to PAT for GitHub, this is created in BI so can't save it anywhere for future use (maybe a good thing?). The fine-grained PAT didn't seem to work, I used my existing PAT, which I had to copy and paste outside Cloudflare's reach
- Logging into everything takes some time with 2FA for IDS and GitHub
- The JupyterLab git integration is great. No need to reuse PAT after first time.

