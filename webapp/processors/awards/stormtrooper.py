
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the lowest accuracy.

    Implementation
    Get bullets fired and hit from player stats

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Stormtrooper', 'Lowest Weapon Accuracy',
                [PLAYER_COL, Column('Accuracy', Column.PERCENT, Column.ASC)])

    def on_accuracy(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        hits = player_stats.bullets_hit
        fired = player_stats.bullets_fired
        self.results[e.player] = [hits, fired]
