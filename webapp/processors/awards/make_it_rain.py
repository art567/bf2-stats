
from processors.awards import AwardProcessor,Column
from models.vehicles import ARTILLERY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using artillery.

    Implementation
	Whenever a kill event is received involving artillery, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Make It Rain', 'Most Kills with Artillery', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.vehicle.vehicle_type == ARTILLERY:
            self.results[e.attacker] += 1
