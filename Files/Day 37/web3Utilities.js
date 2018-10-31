const Web3 = require('web3')
const web3 = new Web3('https://mainnet.infura.io/v3/b71e22c7bbe44ee8bc23d9d51dfb99fb')

//-------------------Getting Average/Current Gas price-----------------------------
//web3.eth.getGasPrice().then(console.log)
web3.eth.getGasPrice().then((result) => {
    console.log(web3.utils.fromWei(result, 'ether'))
})
//--------------------Hasing Functions.--------------------------------------------

console.log("Name Hash(SHA3):   	" + web3.utils.soliditySha3('Ashwini Singh'))
console.log("Name Hash(KECCAK256):   " + web3.utils.keccak256('Ashwini Singh'))
console.log("Rog No Hash(SHA3): 	" + web3.utils.soliditySha3('3511055'))
console.log("Rog No Hash(KECCAK256): " + web3.utils.keccak256('3511055'))

const name = "Ashwini Singh"
const rollno = "3511055"
if (web3.utils.soliditySha3(name) == web3.utils.keccak256(name)) //&& web3.utils.soliditySha3(rollno) == web3.utils.keccak256(rollno) ) {
    console.log("Identical Hashes.")
// }

//-------------------Random Hex-----------------------------------------------------

console.log(web3.utils.randomHex(32))