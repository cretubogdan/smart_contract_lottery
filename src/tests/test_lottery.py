from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account}
    )
    assert lottery.getEntranceFee() > Web3.to_wei(0.010, "ether")
    assert lottery.getEntranceFee() < Web3.to_wei(0.015, "ether")
