__author__ = 'victor'


class BacktrackingRec(object):
  @staticmethod
  def consistent(x):
    return not x[-1] in x[:-1] and list(x) == list(sorted(x))

  @staticmethod
  def output_solution(x):
    sol = "["
    for i in x[:-1]:
      sol += str(i) + ", "
    sol += str(x[-1]) + "]"
    print(sol)

  @staticmethod
  def is_solution(x, n):
    return sum(x) % n == 0

  @staticmethod
  def next_elem(lst, i):
    if i < len(lst):
      return lst[i]
    return None

  def back_rec(self, x, n, lst):
    el = lst[0]
    x.append(el)
    i = 0
    while el is not None:
        i += 1
        x[-1] = el
        if self.consistent(x):
            if self.is_solution(x, n):
                self.output_solution(x)
            self.back_rec(x[:], n, lst)
        el = self.next_elem(lst, i)

  def backtracking(self, n, lst):
    self.back_rec([], n, lst)

