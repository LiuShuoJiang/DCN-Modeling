"""
File: Optimization.py
Brief: This file contains the main optimization logic for the data center network simulation.
"""

import random


def generate_mock_routing_info(network, active_user_indices):
    """
    This function is just for testing and needs to be replaced with a real routing algorithm!
    Generates mock routing information for the network.
    Each edge in the path from Data Center to Users through Hubs is assigned a random traffic intensity.
    :param network: the data center network object (NetworkX graph)
    :param active_user_indices: the list of active user indices
    """
    routing_info = {}
    for dc in network.data_centers:
        for hub in network.hubs:
            routing_info[(dc.name, hub.name)] = random.randint(0, 2)
            for user_index in active_user_indices:
                user_name = f"User_{user_index + 1}"
                if (hub.name, user_name) in network.graph.edges:
                    routing_info[(hub.name, user_name)] = random.randint(0, 3)
    return routing_info

# TODO: Optimization logic
