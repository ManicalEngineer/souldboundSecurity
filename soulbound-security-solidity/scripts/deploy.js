// Import the Hardhat library
const hre = require("hardhat");

// Define an async function to handle deployment
async function deploy() {
    // Obtain the Soulbound contract
    const Soulbound = await hre.ethers.getContractFactory("SoulBoundSecurity");
    // Deploy the Soulbound contract
    const soulbound = await Soulbound.deploy();
    await soulbound.deloyed;

    // Log the deployed contract's address
    console.log("Soulbound token deployed at:", soulbound.address);
}

deploy()
    .then(() => console.log("Deployment complete"))
    .catch((error) => console.error("Error deploying contract:", error));
