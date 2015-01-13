__author__ = 'victor'


class BacktrackingRec(object):
  @staticmethod
  def consistent(x):
    return not x[len(x) - 1] in x[:len(x) - 1] and list(x) == list(sorted(x))

  @staticmethod
  def output_solution(lst, x):
    sol = "["
    for i in x[:-1]:
      sol += str(lst[i]) + ", "
    sol += str(lst[-1]) + "]"
    print(sol)

  @staticmethod
  def is_solution(lst, x, n):
    suma = 0
    for i in x:
      suma += lst[i]
    return suma % n == 0

  def back_rec(self, x: list, n, lst):
    x.append(0)
    for i in range(0, len(lst)):
      x[-1] = i
      if self.consistent(x):
        if self.is_solution(lst, x, n):
          self.output_solution(lst, x)
        self.back_rec(x[:], n, lst)

  def backtracking(self, n, lst):
    self.back_rec([], n, lst)