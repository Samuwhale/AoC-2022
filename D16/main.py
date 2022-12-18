from collections import deque


def parse_input(input):
    with open(input) as data:
        scan = [line.strip() for line in data.readlines()]

    flow_values = {}
    tunnel_connections = {}
    for valve in scan:
        flow_values[valve.split()[1]] = int(valve.split('=')[1].split(';')[0])
        tunnel_connections[valve.split()[1]] = [tunnel.strip(', ') for tunnel in valve.split()[9:]]

    return flow_values, tunnel_connections


def tick_minute(flow_rates):
    cum_flow = 0
    for flow in flow_rates:
        cum_flow += flow
    return cum_flow


def countdown(minutes: int):
    flow_rates = 0
    total_flow = 0
    for minute in range(1, minutes + 1):
        total_flow += tick_minute(flow_rates)
        print(f"{minute} minute(s) passed, total of {total_flow} pressure released.")



flows, tunnels = parse_input('example.txt')
print(f"Flows: {flows}")
print(f"Tunnels: {tunnels}")