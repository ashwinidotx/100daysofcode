pragma solidity ^0.4.2;
// 0.4.11 - old
contract Election {
	//1.Model Candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    //2.Store Candidate
    //3.Fetch Candidate info
    mapping (uint => Candidate) public candidates;
    //4.Store Candidate count(votes)
    uint public candidateCount;
    
    function Election () public {
        addCandidate("Candidate 1");
        addCandidate("Batman");
    }

    function addCandidate(string _name) private {
        candidateCount++;
        candidates[candidateCount] = Candidate(candidateCount, _name, 0);
    }

}