var Election = artifacts.require("./Election.sol");

contract("Election", function(accounts){ 
    var electionInstance;

    it("Initializes with 2 candidates in total.", function() {
        return Election.deployed().then(function(instance){
            return instance.candidateCount();
        }).then(function(count){
            assert.equal(count,2);
        });
    });

    it("Initializes the candidates with the correct values.", function() {
        return Election.deployed().then(function(instance){
            electionInstance = instance;
            return electionInstance.candidates(1);
        }).then(function(candidate) {
            assert.equal(candidate[0],1,"Contains the Correct ID.");
            assert.equal(candidate[1],"Candidate 1","Contains the Correct Name.");
            assert.equal(candidate[2],0,"Contains the Correct votes.");
            return electionInstance.candidates(2);
        }).then(function(candidate) {
            assert.equal(candidate[0], 2, "Contains the Correct ID.");
            assert.equal(candidate[1], "Batman", "Contains the Correct Name.");
            assert.equal(candidate[2], 0, "Contains the Correct votes.");
        });
    });

});
