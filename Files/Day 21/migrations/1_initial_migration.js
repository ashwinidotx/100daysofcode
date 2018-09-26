var Migrations = artifacts.require("./Migrations.sol");
var scoreStore = artifacts.require("./scoreStore.sol");
module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(scoreStore);
};
