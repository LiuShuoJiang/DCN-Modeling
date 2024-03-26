# CSE 6730 Data Center Network Modeling Project

## Introduction

This project aims to explore, simulate, and analyze various data center network (DCN) topologies using the Fast Network Simulation Setup (FNSS) and Mininet. Our goal is to understand the performance implications of different network structures and contribute to the design of more efficient, scalable, and robust data center architectures.

## Project Overview

In the realm of cloud computing and large-scale internet services, the efficiency and scalability of data center networks play a pivotal role. This project focuses on modeling basic to advanced DCN topologies, simulating their behavior under different conditions, and analyzing their performance metrics such as throughput, bandwidth, and latency. Through our work, we aim to identify optimal network configurations that meet the ever-growing demands of modern data centers.

## Current Progress

- **Network Modeling and Simulation**: We have successfully modeled and simulated basic network structures like fat-tree architectures using FNSS and visualized these topologies with Mininet.
- **Visualization**: Leveraging NetworkX, we've achieved an intuitive understanding of network dynamics, enabling us to identify potential bottlenecks and inefficiencies within the simulated environments.

## Future Work

- **Custom Controller**: Implementing a custom controller for multi-path routing and load balancing to optimize network performance.
- **Advanced Structure Modeling**: Expanding our scope to include more sophisticated network topologies, aiming to compare their performance against basic models.
- **Custom Topology Development**: We plan to design and evaluate our own network topology, focusing on overcoming the limitations identified in traditional designs.

## Setup Instructions

- Set up a Ubuntu 20.04 Virtual Machine on your local machine or use a cloud-based service like Google Cloud Platform or Amazon Web Services. 
- Install Mininet following the instructions at [Mininet's official website](http://mininet.org/download/). 
  - Note: the installation of Mininet requires sudo privileges, and it is recommended to install it on a virtual machine to avoid crushing your local machine's network settings. 
- Install [FNSS](https://github.com/fnss/fnss):

```bash
pip install networkx
pip install scipy
pip install fnss
```
