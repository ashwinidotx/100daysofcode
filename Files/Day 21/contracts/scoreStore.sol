pragma solidity ^0.4.4;

contract scoreStore {

    mapping (string => int) PersonScore;

    function addPerson(string name, int startingScore) public {

        if(PersonScore[name]>0)
            revert();
        else
            PersonScore[name] = startingScore;
    }

    function getScore(string name) public view returns (int) {
        return PersonScore[name];
    }
}