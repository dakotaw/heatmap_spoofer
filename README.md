# heatmap-spoofer

A little throwaway script for arbitrarily pushing code to Github to keep your heatmap active because casual observers care wayyyy too much about your heatmap. 

Probably better off as a gist but whatever yolo

## Quick Setup

`setup.sh` will install requirements and set up the cronjob to run every 24 hours. 

1. Fork this repo.
2. Clone the repo on the server that will be running the script.
3. Run `sh ./setup.sh [github email]` on same server.
4. Profit

Security concerns (ssh keys, access controls, etc) are up to you.