# Bitcoin-Blockchain-Historical-Data
# About Dataset
A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data (generally represented as a Merkle tree, where data nodes are represented by leaves). Since each block contains information about the previous block, they effectively form a chain (compare linked list data structure), with each additional block linking to the ones before it. Consequently, blockchain transactions are irreversible in that, once they are recorded, the data in any given block cannot be altered retroactively without altering all subsequent blocks.

# Inspiration
Bitcoin's Blockchain is public. Anybody can run a node locally and get access to all the blocks, since genesis to the current height. However, this process can take some time as the current size exceeds 400 gigabytes and managing the data can be complex as most implementations require the data to be decoded.

The purpose of this dataset is to aid individual researches and developers to be able to analyze the blockchain deeply or even train machine learning models in just a few minutes, instead of several hours/days.
