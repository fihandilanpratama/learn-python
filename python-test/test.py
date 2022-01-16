import math

def calculate(c, sd, m):
  result = (1 / (math.sqrt(2*math.pi) * sd)) * (math.pow(math.e, (-(c-m)**2) / (2*(sd)**2)))
  return "{:.4f}".format(result)

# result = (1 / (math.sqrt(2*math.pi) * 168.8787)) * (math.pow(math.e, (-(300-212)**2) / (2*(168.8787)**2)))
# format_float = "{:.4f}".format(result)
# print(calculate(300, 168.8787, 212))
# print(calculate(300, 261.9637, 435))
print(calculate(125, 5, 90))
print(calculate(125, 54.5436, 110))
