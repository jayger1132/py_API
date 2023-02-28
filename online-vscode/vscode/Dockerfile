FROM codercom/code-server:latest

ENV PATH="/home/coder/.local/bin/:${PATH}"

## https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server 但是為內嵌許多均不可連線
RUN code-server --install-extension ms-vscode.live-server
## 安裝顯示主題
RUN code-server --install-extension max-SS.Cyberpunk
## 支援Docker編寫輔助
RUN code-server --install-extension ms-azuretools.vscode-docker
## 支援系統即時資源顯示
## https://marketplace.visualstudio.com/items?itemName=mutantdino.resourcemonitor
RUN code-server --install-extension njzy.stats-bar
## 安裝中文字型
RUN sudo apt-get update && \
    sudo apt-get install -y fonts-arphic-ukai fonts-arphic-uming \
        fonts-ipafont-mincho fonts-ipafont-gothic fonts-unfonts-core

## 安裝Dcoker Cli，方便mount docker.socket後可使用指令
RUN sudo apt-get update && \
    sudo apt-get install -y docker.io docker-compose
