const Web3 = require('web3')
const web3 = new Web3('https://mainnet.infura.io/v3/b71e22c7bbe44ee8bc23d9d51dfb99fb')

// latest block from block chain (etherscan.io)
web3.eth.getBlockNumber().then(console.log)

web3.eth.getBlock('latest').then(console.log)

web3.eth.getBlock('latest').then((block) => { // we can also specify block no or block address(hash) isntead of sayin 'latest'
	console.log({
		blockHash:block.hash, 
		blockNumber:block.number,
		})
})

// latest 10 block

web3.eth.getBlockNumber().then((latest) => {
 for(let i=0;i<10;i++)
 {
 	web3.eth.getBlock(latest-i).then((block) => {
 		console.log(block)
 	})
 }
})



web3.eth.getBlock('latest').then((b) => {console.log(b.hash)})
web3.eth.getBlockTransactionCount('latest').then(console.log)

//getting a Transaction from block
web3.eth.getTransactionFromBlock('latest', 2).then(console.log)

