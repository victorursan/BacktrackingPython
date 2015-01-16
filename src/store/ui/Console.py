from store.controller.Backtracking import Backtracking
from store.controller.BacktrackingRec import BacktrackingRec

__author__ = 'victor'


class Console(object):
  @staticmethod
  def run():
    back_rec = BacktrackingRec()
    back = Backtracking()
    # back_rec.backtracking(5, [1, 2, 3, 4, 5, 6, 7])
    back.backtracking(5, [1, 2, 3, 4, 5, 6, 7])
