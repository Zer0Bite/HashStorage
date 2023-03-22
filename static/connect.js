if (typeof window.ethereum !== "undefined") {
  console.log("MetaMask is installed!'");
} else {
  console.log("MetaMask is NOT installed!");
}
function isEthereumAvailable() {
  return window.ethereum !== "undefined"
}

const connectInput = document.getElementById("connect");

async function getAccounts(){
    return window.ethereum.request({
         method: "eth_requestAccounts"
    });
}

function connect(){
    connectInput.textContent = "Loading...";
    return getAccounts().then(showAccount);
}

function showAccount(accounts){
    if(accounts.length > 0){
        connectInput.textContent = 'Connected';
        document.getElementById("userAddress").value = accounts[0];
    }
}

function init() {

  if (isEthereumAvailable()) {
    connectInput.textContent = "Connect Wallet";
    connectInput.removeAttribute("disabled");
    connectInput.addEventListener("click", connect);
  } else {
    connectInput.textContent = "Ethereum not available. Please install MetaMask!"
    connectInput.setAttribute("disabled", true);
  }
}

init()