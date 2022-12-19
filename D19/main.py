import re


class Blueprint:
    def __init__(self, build_costs):
        self.id = build_costs[0]
        self.costs = {
            "ore_bot": (build_costs[1], 0, 0),
            "clay_bot": (0, build_costs[2], 0),
            "obsidian_bot": (build_costs[3], build_costs[4], 0),
            "geode_bot": (build_costs[5], 0, build_costs[6]),
        }

        self.bots_of_type = {
            "ore_bot": [Ore_bot(self)],
            "clay_bot": [],
            "obsidian_bot": [],
            "geode_bot": [],
        }

        self.bot_types = {
            "ore_bot": Ore_bot,
            "clay_bot": Clay_bot,
            "obsidian_bot": Obsidian_bot,
            "geode_bot": Geode_bot
        }

        self.resources = Resources()

    def all_bots_produce(self):
        for bot_type, bots in self.bots_of_type.items():
            for bot in bots:
                bot.produce()

    def purchase_bots(self):
        pass



    def complete_turns(self, amt):
        for i in range(amt):
            self.all_bots_produce()

    def build_bot(self, bot_type_string):
        if self.resources.check_balance(self.costs[bot_type_string]):
            print(f"Building a {bot_type_string}")
            bot_type = self.bot_types[bot_type_string]
            bot = bot_type(self, self.costs[bot_type_string])
            self.bots_of_type[bot_type_string].append(bot)
            self.resources.pay_resource(self.costs[bot_type_string])
        else:
            print(f"Not enough resources to build a {bot_type_string}")


class Resources:
    def __init__(self):
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0

    def add_resource(self, res, amt):
        if res in ("ore", "clay", "obsidian", "geode"):
            setattr(self, res, getattr(self, res) + amt)

    def pay_resource(self, cost_tuple):
        self.ore -= cost_tuple[0]
        self.clay -= cost_tuple[1]
        self.obsidian -= cost_tuple[2]

    def check_balance(self, cost_tuple):
        if self.ore < cost_tuple[0] or self.clay < cost_tuple[1] or self.obsidian < cost_tuple[2]:
            return False
        else:
            return True

    def print_resources(self):
        print(self.ore, self.clay, self.obsidian, self.geode)


class Robot:
    def __init__(self, blueprint_parent, cost=(0, 0, 0)):
        self.ore_cost = cost[0]
        self.clay_cost = cost[1]
        self.obsidian_cost = cost[2]
        self.blueprint = blueprint_parent


class Ore_bot(Robot):
    def produce(self, res="ore", amt=1):
        self.blueprint.resources.add_resource(res, amt)


class Clay_bot(Robot):
    def produce(self, res="clay", amt=1):
        self.blueprint.resources.add_resource(res, amt)


class Obsidian_bot(Robot):
    def produce(self, res="obsidian", amt=1):
        self.blueprint.resources.add_resource(res, amt)


class Geode_bot(Robot):
    def produce(self, res="geode", amt=1):
        self.blueprint.resources.add_resource(res, amt)


with open('example.txt') as data:
    bp_data = [re.findall('\d+', i) for i in data.readlines()]
    bp_data = [[int(j) for j in i] for i in bp_data]
    print(bp_data)

resources = Resources()

blueprints = set()
for bp in bp_data:
    blueprints.add(Blueprint(bp))

for blueprint in blueprints:
    blueprint.complete_turns(24)
    blueprint.resources.print_resources()
