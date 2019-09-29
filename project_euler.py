def euler_one():
  return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

def euler_two(n, lst=[1,2]):
  if n == 1:
    return [1]
  elif n == 2:
    return [1, 2]
  else:
    while lst[-1] < n:
      lst.append(lst[-1] + lst[-2])
      euler_two(n, lst)
    
    return sum([i for i in lst if i < n and i % 2 == 0])

def sieve_of_eratosthenes(n):
  dct = {d: 'unmarked' for d in range(2, n+1)}

  for i in dct:
    if dct[i] == 'unmarked':
      dct[i] = 'prime'
  
    for j in dct:
      if j % i == 0 and j != i:
        
        dct[j] = 'composite'
    
  return [i for i in dct if dct[i] == 'prime']

def euler_three():
  #miller-rabin primality test
  pass

def euler_four():
  return max((int(i * j) for i in range(100, 1000) for j in range(100, 1000) if str(i *j)[0:3] == str(i*j)[-3:]))

def euler_five(n):
  pass

    




