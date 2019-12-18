def rectangular_prism_puzzle(maximum_range_of_integers_to_check):
 list_of_possibilities=[]
 for height in range(1, maximum_range_of_integers_to_check):
  if height % 100 == 0:
   print("Checking for possibilities with max side length: ",height)
  for width in range(1, height+1):
   for depth in range(1, width+1):
    volume=height*width*depth
    surface_area=2*height*width + 2*width*depth + 2*height*depth
    if volume == surface_area:
     print("\t\theight: ", height, ", width: ", width, ", depth:", depth, ", surface area = volume = ", surface_area)
     list_of_possibilities.append([height,width,depth])
 return list_of_possibilities

list_of_possibilities=rectangular_prism_puzzle(999)
