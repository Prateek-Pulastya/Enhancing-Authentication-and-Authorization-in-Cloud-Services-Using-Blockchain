import random
import sys
import base64

import json

from web3 import Web3
from solcx import compile_standard
import solcx
solcx.install_solc()



compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "phb.sol": {
             "content": '''
                 pragma solidity >=0.4.0 <=0.8.17;
               

                contract PHB {

                     struct User
                    {
       
                        int user_id;
                        string username;
                        string password;
                        string mobile;
                        string p_address;
                    }

                    User []uss;

                    function addUser(int user_id,string memory username,string memory password,string memory mobile,string memory p_address) public
                    {
                        User memory e
                            =User(user_id,
                                    username,
                                    password,
                                    mobile,
                                    p_address);
                        uss.push(e);
                    }


                    function getUser(int user_id) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<uss.length;i++)
                        {
                            User memory e
                                =uss[i];
                                 
                            
                            if(e.user_id==user_id)
                            {
                                return(e.username,
                                    e.password,
                                    e.mobile,
                                    e.p_address
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }

                    function getUserCount() public view returns(uint256)
                    {
                        return(uss.length);
                    }

                    struct File
                    {                     
                        int id1;
                        string filename;
                        string username;
                        string date;
                        string time;
                        
                    }

                    File []files;

                    function addFile(int id1,string memory filename,string memory username,string memory date,string memory time) public
                    {
                        File memory e
                            =File(id1,filename,username,date,time
                                    );
                        files.push(e);
                    }

                    function getFile(int id1) public view returns(
                            
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<files.length;i++)
                        {
                            File memory e
                                =files[i];
                            
                            if(e.id1==id1)
                            {
                                return(e.filename,
                                        e.username,
                                        e.date,
                                        e.time
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found"
                               );
                    }

                     
                       
                }

               '''
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })







def create_contract():
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # get bytecode
    bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    f=open('contract_address.txt','w')
    f.write(tx_receipt.contractAddress)
    f.close()


def get_user(id1):
    id1=int(id1)
    p1=get_contract()
    print(id1,'============')
    store = p1.functions.getUser(id1).call()
    print(store)
    return store

def get_users():
    c=get_user_count()
    c_names=['username','password','mobile','p_address']
    dict1={}
    for i in range(1,c+1):
        d=get_user(i)
        dict2={}
        for j in range(len(c_names)):
            # if j==5:
            #     dict2[c_names[j]]=d[7]
            # else:
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1     


def get_user_count():
    p1=get_contract()
    store = p1.functions.getUserCount().call()
    print(store)
    return int(store)
    

def add_user1(user_id,username,password,mobile,p_address):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    # c=get_patient_count()+1
    tx_hash = p1.functions.addUser(user_id,username,password,mobile,p_address).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)



def add_file1(id1,file_name,username,date,time):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    
    tx_hash = p1.functions.addFile(id1,file_name,username,date,time).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    #print(tx_hash) 
    print(tx_receipt)
    

def get_file(id1):
    id1=int(id1)
    p1=get_contract()
    store = p1.functions.getFile(id1).call()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(store)
    return store
    

def get_contract():
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    return p1


def verify_adr(s):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(),"##########")
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    adrs = w3.eth.accounts
    print(adrs)

    if s in adrs:
        return True
    else:
        return False    


def bget_balance(adr):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())
    wei=w3.eth.getBalance(adr)
    print(wei)
    ethr=w3.fromWei(wei, 'ether')
    print(ethr)
    rs=ethr*100
    return rs

def verify_key(adr1,key,amount):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr1,
            'value': web3.toWei(1, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx,key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        return "Yes"
    except Exception as e:
        print(e)  
        return "No"  


def transfer(adr1,adr2,key,amount):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr2,
            'value': web3.toWei(1, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx,key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        return True
    except Exception as e:
        print(e)  
        return False


if __name__=="__main__":
    # pass
    
    create_contract()
    #get_file(7)