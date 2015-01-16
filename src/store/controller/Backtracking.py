__author__ = 'victor'


class Backtracking(object):
  @staticmethod
  def consistent(x):
    return not x[len(x) - 1] in x[:len(x) - 1] and list(x) == list(sorted(x))

  @staticmethod
  def output_solution(lst, x):
    sol = "["
    for i in x[:-1]:
      sol += str(lst[i]) + ", "
    sol += str(lst[x[-1]]) + "]"
    print(sol)

  @staticmethod
  def is_solution(lst, x, n):
    suma = 0
    for i in x:
      suma += lst[i]
    return suma % n == 0

  def back_iter(self, n, lst):
    x = [-1]
    while len(x) > 0:
      choose = False
      while not choose and x[-1] < len(lst) - 1:
        x[-1] += 1
        choose = self.consistent(x)
      if choose:
        if self.is_solution(lst, x, n):
          self.output_solution(lst, x)
        x.append(-1)
      else:
        x = x[:-1]

  def backtracking(self, n, lst):
    self.back_iter(n, lst)