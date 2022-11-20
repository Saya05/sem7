// SPDX-License-Identifier: MIT
pragma solidity^0.8.7;

contract banking{
    mapping(address => uint) public balances;

    function deposit(uint amount) public payable
    {
        balances[msg.sender] += amount;
    }

    function withdraw(uint amount) public payable returns (string memory){
        require(balances[msg.sender] >= amount, "not enough ether");
        balances[msg.sender] -= amount;
        return "Withdrawn Successfully";
    }


    function getBal() public view returns(uint){
        return balances[msg.sender];
    }
}