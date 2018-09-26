var scoreStore = artifacts.require("./scoreStore.sol");
module.exports = function (deployer) {
    deployer.deploy(scoreStore);
};
