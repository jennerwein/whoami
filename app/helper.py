import math

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776
   #
   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.3f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.3f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.3f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.3f} TB'.format(B/TB)

##############################################################################
# Calculating the Perceived Brightness of a Color
# https://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx
def rgb_brightness(color):
   R = int(color[1:3], 16)
   G = int(color[3:5], 16)
   B = int(color[5:7], 16)
   return math.sqrt(0.241*R*R + 0.691*G*G + 0.068*B*B )
# Bessere Formel in:
# https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color


##############################################################################
if __name__ == '__main__':

   ##### Test humanbytes
   #  tests = [1, 1024, 500000, 1048576, 50000000, 1073741824, 5000000000, 1099511627776, 5000000000000]
   #  for t in tests:
   #      print('{0} == {1}'.format(t,humanbytes(t)))

   ##### Test rgb-brghtness
   print(rgb_brightness("#121314"))