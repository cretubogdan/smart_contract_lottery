python3 -m venv .venv_web3
source .venv_web3/bin/activate
python3 -m pip install -r requirements.txt
echo "export PRIVATE_KEY=<>" > .env
echo "export WEB3_INFURA_PROJECT_ID=<>" >> .env
echo "export ETHERSCAN_TOKEN=<>" >> .env
echo "Do replace <> with the actual values..."

