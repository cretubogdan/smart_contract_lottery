# smart_contract_lottery
Smart Contract Lottery Description

Def:
1. users can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner

How do we want to test this?
1. mainnet-fork
2. development with mocks
3. testnet

Commands:
brownie init src
brownie compile
brownie networks delete mainnet-fork
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-sepolia.g.alchemy.com/v2/OptxRG0D0bqYhn-jnEVsEBfTe6hjPFBx accounts=10 mnemonic=brownie port=8545
brownie test --network mainnet-fork
