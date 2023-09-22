/** @type import('hardhat/config').HardhatUserConfig */
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: "0.8.19",
  networks:{
    goerli:{
      url: "https://spring-fragrant-mansion.ethereum-goerli.discover.quiknode.pro/1c8b316fb572d0835d15c1378e109d41002c6e8f/",
      accounts: ["8a59fd8132cf494218b40e64654950d6a02d50c22833f03474cf6e43662be89c"]
    },
  },
    etherscan: {
      url: "https://goerli.etherscan.io/",
      apiKey: "9UDJK9QAU3J9N7VSWC41GAD1JZ9UMX3GPA"
    }
  
};
